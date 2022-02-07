import tensorflow.keras.datasets.mnist as mnist
import matplotlib.pyplot as plt
import numpy as np
import random
import sys
import subprocess
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'sklearn'])
from sklearn.decomposition import PCA
# import tensorflow_datasets as tfds
# from PCA import PCA 

print('Beginning to download dataset')
# mnist = tf.keras.datasets.mnist # Object of the MNIST dataset
(x_train, y_train),(x_test, y_test) = mnist.load_data() # Load data

print('Finished downloading dataset')
images=[[] for n in range(10)]
for n in range(10):
  print(n)
  for row in x_train[n]:
    for digit in row:
      if digit==0:
        images[n].append(0.01)
      else:
        images[n].append(digit)
print(len(images))
ImageProcessor=PCA(n_components = 2)
print("start fit")
adjusted_coords = PCA.fit_transform(np.array(images))
print("Complete")

# adjusted_coords=[[] for n in range(10)]

# for n in range(10):
#   for digit in range(2):
#     print(ImageProcessor.eigens[1][n])
    



# for n in range(10):
#   print(n)
#   for digit in range(2):
#     adjusted_coords.append(images[n][digit]*ImageProcessor.eigens[1][n][digit])

print(adjusted_coords)



# print(ImageProcessor.eigens)