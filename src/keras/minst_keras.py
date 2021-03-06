# -*- coding: utf-8 -*-
"""minst_keras

Automatically generated by Colaboratory.

Recognizing MINST with Keras
"""

from __future__ import print_function

import numpy as np

import keras

print(keras.__version__)
keras.backend.backend()

from keras.datasets import mnist
from keras.models import Sequential
from keras.layers.core import Dense, Activation, Dropout
from keras.optimizers import SGD
from keras.utils import np_utils, plot_model

np.random.seed(1671)  # for reproducibility
NB_EPOCH = 100  # time the model is exposed to training set. Each time optimizer tries to adjust the weight so that the objective function is minimized
BATCH_SIZE = 128  # slice of input
VERBOSE = 1
NB_CLASSES = 10  # no. of outputs = digits 0-9
OPTIMIZER = SGD
N_HIDDEN = 128  # layers
VALIDATION_SPLIT = 0.2  # percentage of training set reserved for validation set
DROPOUT = 0.3  # helps prevent overfitting, by randomly setting some input units to 0

# data shuffled and split between training and test set
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# reshape X into 60000x784 rows
RESHAPED = 28 * 28
#
X_train = X_train.reshape(60000, RESHAPED)
X_test = X_test.reshape(10000, RESHAPED)
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')

# normalize input
# range normalize = 0 to 255.
X_train /= 255
X_test /= 255

print(X_train.shape[0], 'train samples')
print(X_test.shape[0], 'X_test samples')

# convert class vector to binary class matrices of output classes
Y_train = np_utils.to_categorical(y_train, NB_CLASSES)
Y_test = np_utils.to_categorical(y_test, NB_CLASSES)

# Define model with M_Hidden layers
# 10 layer output
# final stage is softmax
model = Sequential(
    [
        Dense(N_HIDDEN, input_shape=(RESHAPED,)),  # input_shape only on the first,
        Activation('relu'),
        Dropout(DROPOUT),  # Add Dropout - a form of regularization
        Dense(N_HIDDEN),
        Activation('relu'),
        Dropout(DROPOUT),
        Dense(NB_CLASSES),  # final layers should match the output categories
        Activation('softmax')
    ]
)
model.summary()

# execute the model a Adam optimizer
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

# train model
history = model.fit(X_train,
                    Y_train,
                    batch_size=BATCH_SIZE,
                    epochs=NB_EPOCH,
                    verbose=VERBOSE,
                    validation_split=VALIDATION_SPLIT)
# test model
score = model.evaluate(X_test, Y_test, verbose=VERBOSE)
print('Test score: ', score[0])
print('Test accuracy: ', score[1])
#
# # # viz
# # import pydot
# # plot_model(model)
#
