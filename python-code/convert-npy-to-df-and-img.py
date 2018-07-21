import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# loading files
x_images = np.load('X.npy')
y_images = np.load('Y.npy')

# y_images file is just a series to show T/F, so simple csv conversion
df_y_images = pd.DataFrame(y_images)
df_y_images.to_csv('y.csv', sep=',')

# # checking image in python
# plt.figure(figsize=(5,5))
# plt.imshow(x_images[0])
# plt.show()

# # changing dimension from 4D to 2D in order to export as text (2d dataframe version)
# x_images.shape # (5547, 50, 50, 3) -> (5547, 50*50*3)
# x_images_2d = np.reshape(x_images, (5547,7500)) # when importing to r, need to reformat as 4d
# df_x_images_2d = pd.DataFrame(x_images_2d) # seems there are problems with np.savetxt func, using pd instead
# df_x_images_2d.to_csv('data/x.csv', sep=',')

# in case the the matrix -> image conversion doesnt work in r
for i in range(1,y_images.size):
    save_name = str(i) + '.png'
    img = Image.fromarray(x_images[i], 'RGB')
    img.save(save_name)
