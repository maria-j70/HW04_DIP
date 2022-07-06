import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

pic_1 = np.array(Image.open('inputs/P2/wait_for_me_daddy_[+0.1,-0.5].png'))
pic_2 = np.array(Image.open('inputs/P2/wait_for_me_daddy_[+0.6,+0.2].png'))
# pic_3 = np.array(Image.open('inputs/P2/wait_for_me_daddy_[+0.6,+0.2].png'))
# pic_4 = np.array(Image.open('inputs/P2/wait_for_me_daddy_[+0.6,+0.2].png'))

plt.imshow(pic_1, cmap='gray')
plt.show()
# x = NearestNeighborValueInterpolation(pic_1,2)
# x.resize()

# plt.imshow(x.resized_image, cmap='gray')
# plt.show()
pass