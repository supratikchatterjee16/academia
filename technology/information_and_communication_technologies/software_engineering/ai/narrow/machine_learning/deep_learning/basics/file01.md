# Neural Networks

Neural networks are used classification problems.
To solve problems using Deep learning, the problem has to be turned into a classification problem.

Old classifier was the perceptron classifier. This yielded a 0 or 1, but over a discrete set.
Perceptrons made up what was called Multi-Layer Perceptron. This is a vanilla neural network.

## Shallow Learning - Tasks and Algorithms

Some of the tasks that can be grouped under shallow learning are:

1. Feature Extraction - Preprocessing
2. Mapping specific features into vector space - Kernel methods
3. Rule-based decision making - Decision Trees
4. Combining various estimates - Ensemble methods

Backpropagation has vanishing gradient problem.

For text processing tasks like sentiment analysis, parsing, and named entity recognition – use a Recurrent Net or a Recursive Neural Tensor Network, which we’ll refer to as an RNTN. For any language model that operates on the character level, use a Recurrent Net. For image recognition, use a Deep Belief Network or a Convolutional Net. For object recognition, use a Convolutional Net or an RNTN. Finally, for speech recognition, use a Recurrent Net. In general, Deep Belief Networks and Multilayer Perceptrons with rectified linear units – also known as RELU – are both good choices for classification. For time series analysis, it’s best to use a Recurrent Net. Deep Nets are the current state of the art in pattern recognition, but it’s worth noting that neural nets have been around for decades.

## Restricted Boltzmann Machine

Restricted Boltzmann Machine (RBM) was conceptualized by Geoffrey Hinton. It is used in

1. Dimension Reduction
2. Regression
3. Classification.

RBM has a very simple architecture.

RBMs have two layers:

1. Input
2. Hidden

Each input layer is linked to all the hidden layers. Each node in the input layer is not connected to one another.

Learning in RBM

1. RBMs learn by re-constructing the inputs.
2. They learn in an unsupervised fashion.
3. They re-construct the input in a backward manner and update the parameters accordingly.
