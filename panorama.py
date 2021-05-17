
import cv2
import os

stitcher = cv2.Stitcher_create()

path = 'cv2/panorama'

images = []

for i in os.listdir(path):
    a = cv2.imread(f'{path}/{i}')
    images.append(a)

_, Panorama = stitcher.stitch(images)

if _ == 0:
    print('Panorama Operation Successful')
    cv2.imwrite(f'{path}/Panorama.jpg', Panorama)
else:
    print('Panorama Operation Unsuccessful')




