# %matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegressionCV

from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.utils import np_utils

iris = pd.read_csv('iris.csv')
print(iris.head())

sns.pairplot(iris, hue='species');

# We'll hold the petal and sepal data in an array X and the species labels in a corresponding array y.
X = iris.values[:, :4]
y = iris.values[:, 4]

## using scikit
# As is standard in supervised machine learning, we'll train with some of the data, and measure the performance of our model with the remainder.
train_X, test_X, train_y, test_y = train_test_split(X, y, train_size=0.5, random_state=0)

# We'll train a logistic regression classifier. Doing this, with built-in hyperparameter cross-validation, is one line in scikit-learn
# Like all scikit-learn estimator objects, a LogisticRegressionCV classifier has a .fit() method that takes care of the gory numerical details of learning model parameters that best fit the training data.
lr = LogisticRegressionCV()
lr.fit(train_X, train_y)

# Assess the Classifier Using Accuracy
print("Accuracy = {:.2f}".format(lr.score(test_X, test_y)))


## using keras

# First a bit of data munging: scikit-learn's classifiers accept string labels, e.g. "setosa". But Keras requires that labels be one-hot encoded.
# setosa
# versicolor
# setosa
# virginica

# to table that looks like

# setosa versicolor virginica
#      1          0         0
#      0          1         0
#      1          0         0
#      0          0         1


# alt. pandas.get_dummies(), and one-hot encoding is in scikit-learn
def one_hot_encode_object_array(arr):
    '''One hot encode a numpy array of objects (e.g. strings)'''
    uniques, ids = np.unique(arr, return_inverse=True)
    return np_utils.to_categorical(ids, len(uniques))

train_y_ohe = one_hot_encode_object_array(train_y)
test_y_ohe = one_hot_encode_object_array(test_y)

# Keras is a neural network library
model = Sequential()
#  define the size input layer
model.add(Dense(16, input_shape=(4,)))
model.add(Activation('sigmoid'))
#  define the size output layer
model.add(Dense(3))
model.add(Activation('softmax'))
# specify the optimization strategy and the loss function to optimize. We also instruct the model to calculate accuracy
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=["accuracy"])

# Use the Neural Network Classifier
model.fit(train_X, train_y_ohe, nb_epoch=100, batch_size=1, verbose=0);

# Keras's equivalent of the scikit-learn .score() method is called .evaluate().
loss, accuracy = model.evaluate(test_X, test_y_ohe, verbose=0)
print("Accuracy = {:.2f}".format(accuracy))

## 99% accuracy means NN is overfitting
## use dropout in NN or regularization in LR to reduce overfit
