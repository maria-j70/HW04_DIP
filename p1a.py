
import numpy as np

from PIL import Image
import matplotlib.pyplot as plt


pic_1 = np.array(Image.open('inputs/P1/the_magnificent_eleven_1.png'))

class Spectrum:
    def __init__(self, image):
        self.image = image
        self.image_magnitude , self.image_phase= self.magnitude_phase_spectrum(self.image)
        self.filter()
        self.filtered_image = None

    def magnitude_phase_spectrum(self, image):
        f = np.fft.fft2(image)
        f_shift = np.fft.fftshift(f)

        magnitude_spectrum = np.abs(f_shift)
        phase_spectrum = np.angle(f_shift)

        # plt.imshow(20 * np.log(magnitude_spectrum), cmap='gray')
        # plt.show()
        #
        # plt.imshow(phase_spectrum, cmap='gray')
        # plt.show()

        return magnitude_spectrum, phase_spectrum

    def filter_vertical_remove_line(self,image,n, limit):
        rows, cols = image.shape
        crow, ccol = int(rows / 2)+1, int(cols / 2)+1
        # image[crow - n: crow +n, 0:ccol-limit] = 0
        # image[crow - n: crow +n, ccol+limit :] = 0
        image[241 , 0:ccol-limit] = 0
        image[241, ccol+limit :] = 0
        image[0:240 , ccol] = 0
        image[244: , ccol] = 0


        # image[:, 0: 100] = 0
        # image[:, 600: ] = 0



    def filter(self):
        filtered = np.copy(self.image_magnitude)
        self.filter_vertical_remove_line(filtered,0,2)
        plt.imshow(20 * np.log(filtered), cmap='gray')
        plt.show()
        filterd_fft = filtered * (np.cos(self.image_phase) + 1j * np.sin(self.image_phase))
        inverse_img = np.abs(np.fft.ifft2(filterd_fft))
        self.filtered_image = inverse_img
        plt.imshow(inverse_img, cmap='gray')
        plt.title('inverse Image')
        plt.show()


plt.imshow(pic_1, cmap='gray')
plt.show()
a= Spectrum(pic_1)
pass
pass