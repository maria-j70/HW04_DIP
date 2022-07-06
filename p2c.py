import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

class NearestNeighborValueInterpolation:
    def __init__(self, image, resize_factor ):
        self.image= image
        self.resize_factor = resize_factor
        self.row, self.column = self.image.shape
        self.x_data = np.linspace(0, self.row - 1, self.row)
        self.y_data = np.linspace(0, self.column - 1, self.column)
        self.x_new = np.linspace(0, self.row * self.resize_factor - 1, self.row * self.resize_factor)
        self.y_new = np.linspace(0, self.column * self.resize_factor - 1, self.column * self.resize_factor)
        self.resized_image = np.zeros((self.row * self.resize_factor, self.column * self.resize_factor))

    def lookupNearest(self,x0, y0):
        xi = np.abs(self.x_data - x0).argmin()
        yi = np.abs(self.y_data - y0).argmin()

        return self.image[xi, yi]

    def interpolate_value(self,x0, y0):
        if int(x0)==x0 and int(y0)==y0:
            return self.image[int(x0), int(y0)]
        x0 = int(x0)
        y0 = int(y0)
        x1= min(x0 +1, self.row-1)
        y1= min(y0 +1, self.column-1)

        nearest_points_list = [self.image[x0, y0], self.image[x1, y0], self.image[x0, y1],self.image[x1, y1]]
        mean= sum(nearest_points_list)/4
        result= nearest_points_list[np.abs(np.array(nearest_points_list,dtype=float) - mean).argmin()]
        return result


    def resize(self):
        for row in self.x_new:
            for column in self.y_new:

                self.resized_image[int(row),int(column)] = self.interpolate_value(row/2,column/2)



pic_1 = np.array(Image.open('inputs/P2/wait_for_me_daddy_lr.png'))
pic_gt = np.array(Image.open('inputs/P2/wait_for_me_daddy_gt.png'))

plt.imshow(pic_1, cmap='gray')
plt.show()
x = NearestNeighborValueInterpolation(pic_1,2)
x.resize()

plt.imshow(x.resized_image, cmap='gray')
plt.show()
pass
