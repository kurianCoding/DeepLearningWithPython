import numpy as np
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.utils import np_utils

#fix random seed for reproducibility
seed = 7
np.random.seed(seed)

#Load the MNIST dataset
(X_train, y_train), (X_test, y_test) = mnist.load_data()

#Flatten 28X28 images to 784 vector for each image
num_pixels = X_train.shape[1] * X_train.shape[2]
