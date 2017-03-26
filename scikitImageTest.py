import skimage
import matplotlib.pyplot as plt
# %matplotlib inline

import numpy as np
from matplotlib import pyplot as plt

from skimage import data

random_image = np.random.random([500, 500])
print(random_image)
plt.imshow(random_image, cmap='gray')
plt.colorbar()
plt.show()

coins = data.coins()
print(type(coins), coins.dtype, coins.shape)
plt.imshow(coins, cmap='gray')
plt.colorbar()
# plt.show()



