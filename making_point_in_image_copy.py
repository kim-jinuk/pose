import numpy as np
import cv2
import json

datalist = '000545'
img = cv2.imread('LINEMOD/can/JPEGImages/' + datalist + '.jpg')
f = open('LINEMOD/can/labels/'+ datalist + '.txt', 'r')
line = f.readline()
line = line.split(' ')


img = cv2.line(img, (int(float(line[1])*640),int(float(line[2])*480)), (int(float(line[1])*640),int(float(line[2])*480)), (0,255,0), 5)
img = cv2.line(img, (int(float(line[3])*640),int(float(line[4])*480)), (int(float(line[3])*640),int(float(line[4])*480)), (0,255,0), 5)
img = cv2.line(img, (int(float(line[5])*640),int(float(line[6])*480)), (int(float(line[5])*640),int(float(line[6])*480)), (0,255,0), 5)
img = cv2.line(img, (int(float(line[7])*640),int(float(line[8])*480)), (int(float(line[7])*640),int(float(line[8])*480)), (0,255,0), 5)
img = cv2.line(img, (int(float(line[9])*640),int(float(line[10])*480)), (int(float(line[9])*640),int(float(line[10])*480)), (0,255,0), 5)
img = cv2.line(img, (int(float(line[11])*640),int(float(line[12])*480)), (int(float(line[11])*640),int(float(line[12])*480)), (0,255,0), 5)
#img = cv2.line(img, (int(float(line[13])*640),int(float(line[14])*480)), (int(float(line[13])*640),int(float(line[14])*480)), (0,255,0), 5)
#img = cv2.line(img, (int(float(line[15])*640),int(float(line[16])*480)), (int(float(line[15])*640),int(float(line[16])*480)), (0,255,0), 5)
#img = cv2.line(img, (int(float(line[17])*640),int(float(line[18])*480)), (int(float(line[17])*640),int(float(line[18])*480)), (0,255,0), 5)
cv2.imwrite('image_' + datalist + '.png', img)
