import json

k = [15,16,24,31,32,40,41,42,46,47,48,56,64,72,73,79,80,88,89,96]

for l in k:
    i = '070608_0004' + str(l) + '.json'
    with open('new_dataset/tissue/labels/3D_json/'+ i,'r') as f:
        data = json.load(f)
        for w in range(10):
            if str(data['labelingInfo'])[3] == "'" :
                if str(data['labelingInfo'])[2] == str(w):
                    k = open('new_dataset/tissue/labels/using_data_sample/' + i[-18:-5] + '.txt','w')
                    k.write('2 ')
                    k.write(str(float(data['labelingInfo'][str(w)]['location'][0]['x9'])/1280))
                    k.write(' ')
                    k.write(str(float(data['labelingInfo'][str(w)]['location'][0]['y9'])/720))
                    k.write(' ')
                    k.write(str(float(data['labelingInfo'][str(w)]['location'][0]['x8'])/1280))
                    k.write(' ')
                    k.write(str(float(data['labelingInfo'][str(w)]['location'][0]['y8'])/720))
                    k.write(' ')
                    k.write(str(float(data['labelingInfo'][str(w)]['location'][0]['x5'])/1280))
                    k.write(' ')
                    k.write(str(float(data['labelingInfo'][str(w)]['location'][0]['y5'])/720))
                    k.write(' ')
                    k.write(str(float(data['labelingInfo'][str(w)]['location'][0]['x7'])/1280))
                    k.write(' ')
                    k.write(str(float(data['labelingInfo'][str(w)]['location'][0]['y7'])/720))
                    k.write(' ')
                    k.write(str(float(data['labelingInfo'][str(w)]['location'][0]['x6'])/1280))
                    k.write(' ')
                    k.write(str(float(data['labelingInfo'][str(w)]['location'][0]['y6'])/720))
                    k.write(' ')
                    k.write(str(float(data['labelingInfo'][str(w)]['location'][0]['x4'])/1280))
                    k.write(' ')
                    k.write(str(float(data['labelingInfo'][str(w)]['location'][0]['y4'])/720))
                    k.write(' ')
                    k.write(str(float(data['labelingInfo'][str(w)]['location'][0]['x1'])/1280))
                    k.write(' ')
                    k.write(str(float(data['labelingInfo'][str(w)]['location'][0]['y1'])/720))
                    k.write(' ')
                    k.write(str(float(data['labelingInfo'][str(w)]['location'][0]['x3'])/1280))
                    k.write(' ')
                    k.write(str(float(data['labelingInfo'][str(w)]['location'][0]['y3'])/720))
                    k.write(' ')
                    k.write(str(float(data['labelingInfo'][str(w)]['location'][0]['x2'])/1280))
                    k.write(' ')
                    k.write(str(float(data['labelingInfo'][str(w)]['location'][0]['y2'])/720))
                    k.write(' ')
                    k.write(str(float(data['labelingInfo'][str(w)]['location'][0]['x-range'])/1280))
                    k.write(' ')
                    k.write(str(float(data['labelingInfo'][str(w)]['location'][0]['y-range'])/720))
                    k.write(' ')
                    


            