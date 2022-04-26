import numpy as np
import cv2
import os

ori_photo = []

for filename in os.listdir('ori'):
    #with open(os.path.join('ori', filename), 'r') as f:
    #ext = f.read()
    print(filename)
    ori_photo.append(filename)

alpha = 0.55
print('Ori_photo named', ori_photo)

ori_photo.sort()

print('Len: ', len(ori_photo))

x = len(ori_photo)

for i in range(int(x)):
    print('i :', i)
    img1 = cv2.imread('sig/' + str(i) +'.jpg')
    s_img2 = cv2.imread('ori/'+ str(ori_photo[i]))

    gray_img = cv2.cvtColor(s_img2, cv2.COLOR_BGR2GRAY)

    gray_filename = 'gray/gray'+ str(i) +'.jpg'
    cv2.imwrite(gray_filename, gray_img)


    img2 = cv2.imread('gray/gray' + str(i) + '.jpg')
    #r,c,z = img1.shape
    

    out_img = np.zeros(img1.shape , dtype=img1.dtype)
    
    out_img[:,:,:] = (alpha * img1[:,:,:]) + ((1-alpha) * img2[:,:,:])
    

    filename = 'output/res'+ str(i) +'.jpg'
    #cv2.imshow('Output',out_img)
    cv2.imwrite(filename, out_img)

cv2.waitKey(0)