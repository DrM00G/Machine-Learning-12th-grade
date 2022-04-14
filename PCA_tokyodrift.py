# import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import random
import sklearn
from sklearn.decomposition import PCA

random.seed(1)

mnist = tf.keras.datasets.mnist
(x_train, y_train),(x_test, y_test) = mnist.load_data()

x_train = list(x_train)
# x_train.extend(list(x_test))

y_train = list(y_train)
# y_train.extend(list(y_test))

print("downloaded data")
random_ints = random.sample(range(0, len(x_train)-1),2000)
x_train = [x_train[i] for i in random_ints]

flattened_data = []

for x in x_train:
  x = np.array(x)
  x_flattened = list(x.flatten())
  x_flattened = [elem if elem != 0 else 0.01 for elem in x_flattened]
  flattened_data.append(list(x_flattened))


flattened_data = list(flattened_data)

print("data flattened")

X = np.array(flattened_data)
pca = PCA(n_components=2)
transformed_data = pca.fit_transform(X)

# pca = PrincinpalComponents()
# pca.fit(flattened_data, 2)
# transformed_data = pca.transformed_data

print("creating plot")

graph = plt.gca()

colors = ['red', 'green', 'blue','orange','purple','brown','yellow','black','lightblue','pink']
for i,point in enumerate(transformed_data):
    graph.scatter(point[0], point[1] ,marker=r"$ {} $".format(y_train[i]), c = colors[y_train[random_ints[i]]])

plt.savefig("my_version_mnist_pca_plot.png")
print("done")

