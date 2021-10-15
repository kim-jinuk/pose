import numpy as np
import cv2
import json

datalist = '070205_000817'
img = cv2.imread('new_dataset/watercup/origin/Images/' + datalist + '.png')
with open('new_dataset/watercup/labels/3D_json/' + datalist + '.json') as f:
    data = json.load(f)
    location = data['labelingInfo'][0]['3DBox']['location'][0]
    img = cv2.line(img, (int(location['x1']),int(location['y1'])), (int(location['x1']),int(location['y1'])), (0,255,0), 5)
    img = cv2.line(img, (int(location['x2']),int(location['y2'])), (int(location['x2']),int(location['y2'])), (0,255,0), 5)
    img = cv2.line(img, (int(location['x3']),int(location['y3'])), (int(location['x3']),int(location['y3'])), (0,255,0), 5)
    img = cv2.line(img, (int(location['x4']),int(location['y4'])), (int(location['x4']),int(location['y4'])), (0,255,0), 5)
    img = cv2.line(img, (int(location['x5']),int(location['y5'])), (int(location['x5']),int(location['y5'])), (0,255,0), 5)
    img = cv2.line(img, (int(location['x6']),int(location['y6'])), (int(location['x6']),int(location['y6'])), (0,255,0), 5)
    img = cv2.line(img, (int(location['x7']),int(location['y7'])), (int(location['x7']),int(location['y7'])), (0,255,0), 5)
    img = cv2.line(img, (int(location['x8']),int(location['y8'])), (int(location['x8']),int(location['y8'])), (0,255,0), 5)
    img = cv2.line(img, (int(location['x9']),int(location['y9'])), (int(location['x9']),int(location['y9'])), (0,255,0), 5)
    cv2.imwrite('image_' + datalist + '.png', img)