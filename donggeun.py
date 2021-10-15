import cv2 as cv
import json
import matplotlib
import numpy as np
import os

root = 'new_dataset/sause_container13'
k=1

for i in range(k, 416):
    name = '010305_000' + '{:03}'.format(i) + '_TR'
    # loading label
    with open(os.path.join(root, 'labels', '3D_json', name + '.json')) as f:
        data = json.load(f)
    
    location = data['labelingInfo'][0]['3DBox']['location'][0]
    points = [(int(location['x1']), int(location['y1'])), (int(location['x2']), int(location['y2'])), (int(location['x3']), int(location['y3'])),
              (int(location['x4']), int(location['y4'])), (int(location['x5']), int(location['y5'])), (int(location['x6']), int(location['y6'])),
              (int(location['x7']), int(location['y7'])), (int(location['x8']), int(location['y8'])), (int(location['x9']), int(location['y9']))]
    # loading images
    print(name[:-3] + '_NT.png')
    img_ori = cv.imread(os.path.join(root, 'origin', 'Images', name + '.png'))
    
    for i in range(9):
        point = points[i]
        img = img_ori
        img = cv.line(img, point, point, (0, 255, 0), 8)
        
        cv.imwrite('new_dataset/sause_container13/origin/sampling/test{}_{}.png'.format(k,i), img)

    '''       
    img = img_ori
    center = ((points[0][0]+points[1][0]+points[4][0]+points[5][0])//4, (points[0][1]+points[1][1]+points[4][1]+points[5][1])//4)
    
    #img = cv.line(img, center, center, (255,0,0), 8)
    img = cv.line(img, points[0], points[1], (0, 255, 0), 5)
    img = cv.line(img, points[5], points[1], (0, 255, 0), 5)
    img = cv.line(img, points[5], points[4], (0, 255, 0), 5)
    img = cv.line(img, points[0], points[4], (0, 255, 0), 5)
    
    img = cv.line(img, points[2], points[3], (0, 255, 0), 5)
    img = cv.line(img, points[7], points[3], (0, 255, 0), 5)
    img = cv.line(img, points[7], points[6], (0, 255, 0), 5)
    img = cv.line(img, points[2], points[6], (0, 255, 0), 5)
    cv.imwrite('new_dataset/sause_container13/origin/sampling/test_{}.png'.format(k), img)
    '''   
    k = k + 1
    
    print('done')