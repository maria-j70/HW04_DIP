import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import cv2
from cpselect.cpselect import cpselect
import correlateim
pic_1 = np.array(Image.open('inputs/P4/kobytev_1941.png').convert('RGB'))[:,:771]
pic_2 = np.array(Image.open('inputs/P4/kobytev_1945.png').convert('RGB'))
reference_points = np.arrayImage.open('inputs/P4/reference_keypoints.png.png').convert('RGB')()

