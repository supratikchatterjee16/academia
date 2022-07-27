import numpy as np
import matplotlib.pyplot as plt
import h5py
import scipy

from PIL import Image
from scipy import ndimage
from lr_utils import load_dataset

train_set_x_orig, train_set_y, test_set_x_orig, test_set_y, classes = load_dataset()

plt.imshow(train_set_x_orig[2])
print(classes[np.squeeze(train_set_y[:, 25])].decode('utf-8'))

m_train = train_set_y.shape[1]  # number of training examples
m_test = test_set_y.shape[1]  # number of testing examples
num_px = train_set_x_orig.shape[1]  # height/width of each image

train_set_x_flatten = train_set_x_orig.reshape(train_set_x_orig.shape[0], -1).T
test_set_x_flatten = train_set_x_orig.reshape(test_set_x_orig.shape[0], -1).T

train_set_x = train_set_x_flatten / 255
test_set_x = test_set_x_flatten / 255


def sigmoid(z):
    '''Sigmoid function
    z is the weighted input
    z = w^T . x + b
    w is the weight matrix, here the image pixels
    b is bias, which we need to train
    '''
    return 1 / (1 + np.exp(-z))


def initialize_with_zeros(dim):
    '''
    The weights and biases need to be intialized with zeroes
    '''
    w = np.zeros(shape=(dim, 1))
    b = 0
    assert(w.shape == (dim, 1))
    assert(isinstance(b, float) or isinstance(b, int))
    return w, b


def propagate(w, b, X, Y):
    ''' This is a CNN, so forward and backward propagation will occur simultaneously
    '''
    m = X.shape[1]

    # forward propagation
    A = sigmoid(np.dot(w.T, X) + b)
    cost = (-1 / m) * np.sum(Y * np.log(A)) + (1 - Y) * (np.log(1 - A))

    # backward propagation
    dw = (1/m) * np.dot(X, (A - Y).T)
    db = (1/m) * np.sum(A - Y)

    assert(dw.shape == w.shape)
    assert(db.dtype == float)
    cost = np.squeeze(cost)
    assert(cost.shape == ())

    grads = {'dw': dw, 'db': db}

    return grads, cost


def optimize(w, b, X, Y, iter_count, learn_rate, print_cost=False):
    costs = []
    for i in range(iter_count):
        # cost and gradient calculation
        grads, cost = propagate(w, b, X, Y)

        # get derivatives
        dw = grads['dw']
        db = grads['db']

        # adjust
        w = w - learn_rate * dw
        b = b - learn_rate * db

        # record costs
        if i % 100 == 0:
            costs.append(cost)

        # Print cost
        if print_cost and i % 100 == 0:
            print('Cost at %i iterations : %f' % (i, cost))

        params = {'w': w, 'b': b}
        grads = {'dw': dw, 'db': db}
        return params, grads, costs


def predict(w, b, X):
    m = X.shape[1]
    Y_prediction = np.zeros((1, m))
    w = w.reshape(X.shape[0], 1)

    # compute probability vector
    A = sigmoid(np.dot(w.T, X) + b)

    for i in range(A.shape[1]):
        Y_prediction[0, i] = 1 if A[0, i] > 0.5 else 0  # activation
    assert(Y_prediction.shape == (1, m))
    return Y_prediction


def model(X_train, Y_train, X_test, Y_test, num_iterations=2000, learning_rate=0.5, print_cost=False):
    # Initialize parameters with 0s
    w, b = initialize_with_zeros(X_train.shape[0])

    # Gradient descent
    parameters, grads, costs = optimize(
        w, b, X_train, Y_train, num_iterations, learning_rate, print_cost)

    # Retrive parameters w, b from dictionary
    w = parameters['w']
    b = parameters['b']

    # Predict test/train set examples
    Y_prediction_test = predict(w, b, X_test)
    Y_prediction_train = predict(w, b, X_train)

    # Print test/train errors
    print("train accuracy: {} %".format(
        100 - np.mean(np.abs(Y_prediction_train - Y_train)) * 100))
    print("test accuracy: {} %".format(
        100 - np.mean(np.abs(Y_prediction_test - Y_test)) * 100))

    d = {'costs': costs,
         'Y_prediction_test': Y_prediction_test,
         'Y_prediction_train': Y_prediction_train,
         'w': w,
         'b': b,
         'learning_rate': learning_rate,
         'num_iterations': num_iterations}


d = model(train_set_x, train_set_y, test_set_x, test_set_y,
          num_iterations=2000, learning_rate=0.005, print_cost=True)

costs = np.squeeze(d['costs'])
plt.plot(costs)
plt.ylabel('cost')
plt.xlabel('iterations(per hundreds)')
plt.title('Learning rate = %f' % d['learning_rate'])
plt.show()
