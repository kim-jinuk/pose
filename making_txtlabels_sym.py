import json
import os
import numpy as np
from numpy.lib.polynomial import poly
from utils import *
from MeshPly import MeshPly
import math
import cv2

name_list = os.listdir('new_dataset/bowl9/labels/3D_json')
meshname = 'new_dataset/bowl9/origin/3D_Shape/020309.ply'
mesh = MeshPly(meshname)
vertices = np.c_[np.array(mesh.vertices), np.ones((len(mesh.vertices), 1))].transpose()
corners3D = get_3D_corners(vertices)

for i in name_list:
    with open('new_dataset/bowl9/labels/3D_json/'+ i,'r') as f:
        data = json.load(f)
        fx = float(data['metaData']['Fx'])
        fy = float(data['metaData']['Fy'])
        u0 = float(data['metaData']['PPx'])
        v0 = float(data['metaData']['PPy'])
        intrinsic_calibration = get_camera_intrinsic(fx,fy,u0,v0)

        location = data['labelingInfo'][0]['3DBox']['location'][0]
        box_gt = list()
        box_gt.append(float(location['x9']))
        box_gt.append(float(location['y9']))
        box_gt.append(float(location['x4']))
        box_gt.append(float(location['y4']))
        box_gt.append(float(location['x1']))
        box_gt.append(float(location['y1']))
        box_gt.append(float(location['x8']))
        box_gt.append(float(location['y8']))
        box_gt.append(float(location['x5']))
        box_gt.append(float(location['y5']))
        box_gt.append(float(location['x3']))
        box_gt.append(float(location['y3']))
        box_gt.append(float(location['x2']))
        box_gt.append(float(location['y2']))
        box_gt.append(float(location['x7']))
        box_gt.append(float(location['y7']))
        box_gt.append(float(location['x6']))
        box_gt.append(float(location['y6']))
        box_gt = np.array(np.reshape(box_gt,[9,2]), dtype='float32')

        R_gt, t_gt = pnp(np.array(np.transpose(np.concatenate((np.zeros((3, 1)), corners3D[:3, :]), axis=1)),
                                          dtype='float32'), box_gt,
                                 np.array(intrinsic_calibration, dtype='float32'))
        
        theta = math.atan2(R_gt[1][0],R_gt[0][0])
        beta = math.atan2(-R_gt[2][0],math.sqrt(((R_gt[2][1])**2)+((R_gt[2][2])**2)))
        alpha = math.atan2(R_gt[2][1],R_gt[2][2])
        alpha = alpha*180/math.pi
        if alpha>90 and alpha<180:
            alpha = alpha-90
        elif alpha<0 and alpha>-90:
            alpha = alpha+90
        elif alpha<-90 and alpha>-180:
            alpha = alpha+180    
        theta = theta*math.pi/180
        R_gt[0][0] = math.cos(theta)*math.cos(beta)
        R_gt[0][1] = (math.cos(theta)*math.sin(beta)*math.sin(alpha))-(math.sin(theta)*math.cos(alpha))
        R_gt[0][2] = (math.cos(theta)*math.sin(beta)*math.cos(alpha))+(math.sin(theta)*math.sin(alpha))
        R_gt[1][0] = math.sin(theta)*math.cos(beta)
        R_gt[1][1] = (math.sin(theta)*math.sin(beta)*math.sin(alpha))+(math.cos(theta)*math.cos(alpha))
        R_gt[1][2] = (math.sin(theta)*math.sin(beta)*math.cos(alpha))-(math.cos(theta)*math.sin(alpha))
        R_gt[2][0] = -math.sin(beta)
        R_gt[2][1] = math.cos(beta)*math.sin(alpha)
        R_gt[2][2] = math.cos(beta)*math.cos(alpha)

        Rt_gt = np.concatenate((R_gt, t_gt), axis=1)
        proj_corners_gt = np.transpose(compute_projection(corners3D, Rt_gt, intrinsic_calibration))
        k = open('new_dataset/bowl9/labels/using_data/' + i[-21:-5] + '.txt','w')
        k.write('3 ')
        k.write(str(float(location['x9'])/1280))
        k.write(' ')
        k.write(str(float(location['y9'])/720))
        for j in range(8):
            k.write(' ')
            k.write(str(proj_corners_gt[j,0]/1280))
            k.write(' ')
            k.write(str(proj_corners_gt[j,1]/720))
        k.write(' ')
        k.write(str(float(location['x-range'])/1280))
        k.write(' ')
        k.write(str(float(location['y-range'])/720))
        
        img = cv2.imread('new_dataset/bowl9/origin/Images/' + i.replace('.json','.png'))
        for k in range(8):
            img = cv2.line(img, (int(proj_corners_gt[k,0]), int(proj_corners_gt[k,1])), (int(proj_corners_gt[k,0]), int(proj_corners_gt[k,1])), (0,255,0), 5)
            cv2.imwrite('image_' + i.replace('.json','.png'), img)