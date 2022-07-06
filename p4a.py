import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import cv2

pic_1 = np.array(Image.open('inputs/P4/kobytev_1941.png').convert('RGB'))[:,:771]
pic_2 = np.array(Image.open('inputs/P4/kobytev_1945.png').convert('RGB'))

intermediate_list= []

for i in np.linspace(0,1,100):
    intermediate_image = np.uint8((1-i)*pic_1 +i * pic_2)
    # plt.imshow(intermediate_image)
    # plt.show()

    intermediate_list.append(intermediate_image)

video_path = 'p4a' + '.avi'
size = intermediate_list[0].shape[1], intermediate_list[0].shape[0]
fourcc = cv2.VideoWriter_fourcc(*'avc1')
video = cv2.VideoWriter(video_path, fourcc, 20, size)

for i, img in enumerate(intermediate_list):

        video.write(img)

video.release()
