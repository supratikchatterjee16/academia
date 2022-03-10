# Topics an Papers of interest

## Aim

Primary topic of interest is creativity in computers.

The topic is a mix of concepts spreading over the topics of
fuzzy logic, neural networks, knowledge management, data wrangling.

Application for these will invove topics in Human Computer Interface,
which will include specializations in the area of sonography, computer vision,
natural language processing and quite possibly elements of automation.

## Neural Networks

### Artificial Neural Networks

#### Neocognitron

The neocognitron is a hierarchical, multilayered artificial neural network proposed by Kunihiko Fukushima in 1979.
It has been used for Japanese handwritten character recognition and other pattern recognition tasks, and served as the inspiration for convolutional neural networks.


The neocognitron was inspired by the model proposed by Hubel & Wiesel in 1959. They found two types of cells in the visual primary cortex called simple cell and complex cell, and also proposed a cascading model of these two types of cells for use in pattern recognition tasks.

#### Spiking Neuron Model

A neural network model that incorporates time additionally to neuronal and synaptic states, in their operating models.
The idea is that neurons in the SNN do not transmit information at each propagation cycle (as it happens with typical multi-layer perceptron networks), but rather transmit information only when a membrane potential – an intrinsic quality of the neuron related to its membrane electrical charge – reaches a specific value, called the threshold. When the membrane potential reaches the threshold, the neuron fires, and generates a signal that travels to other neurons which, in turn, increase or decrease their potentials in response to this signal. A neuron model that fires at the moment of threshold crossing is also called a spiking neuron model.

Further models : 
1. Leaky integrate and fire models(Louis Lapicque)

Research materials : 

1. Maass, Wolfgang (1997). "Networks of spiking neurons: The third generation of neural network models". Neural Networks. 10 (9): 1659–1671
2. Gerstner, Wulfram. (2002). Spiking neuron models : single neurons, populations, plasticity. Kistler, Werner M., 1969-. Cambridge, U.K.: Cambridge University Press
3. Lee, Dayeol; Lee, Gwangmu; Kwon, Dongup; Lee, Sunghwa; Kim, Youngsok; Kim, Jangwoo (June 2018). "Flexon: A Flexible Digital Neuron for Efficient Spiking Neural Network Simulations". 2018 ACM/IEEE 45th Annual International Symposium on Computer Architecture (ISCA): 275–288

DYNAP(Dynamic Neuromorphic Asynchronous Processor)


#### Biological neuron model 

This is a topic for further discussions. The link for the topic : https://en.wikipedia.org/wiki/Biological_neuron_model#Leaky_integrate-and-fire

#### Quantum Neural Networks

## Recurrent Neural Networks

A recurrent neural network (RNN) is a class of artificial neural networks where connections between nodes form a directed or undirected graph along a temporal sequence. This allows it to exhibit temporal dynamic behavior. Derived from feedforward neural networks, RNNs can use their internal state (memory) to process variable length sequences of inputs. his makes them applicable to tasks such as unsegmented, connected handwriting recognition or speech recognition. Recurrent neural networks are theoretically Turing complete and can run arbitrary programs to process arbitrary sequences of inputs.

The term "recurrent neural network" is used to refer to the class of networks with an infinite impulse response, whereas "convolutional neural network" refers to the class of finite impulse response. Both classes of networks exhibit temporal dynamic behavior. A finite impulse recurrent network is a directed acyclic graph that can be unrolled and replaced with a strictly feedforward neural network, while an infinite impulse recurrent network is a directed cyclic graph that can not be unrolled. Both finite impulse and infinite impulse recurrent networks can have additional stored states, and the storage can be under direct control by the neural network. The storage can also be replaced by another network or graph if that incorporates time delays or has feedback loops. Such controlled states are referred to as gated state or gated memory, and are part of long short-term memory networks (LSTMs) and gated recurrent units. This is also called Feedback Neural Network (FNN).

**Dynamic Systems Theory** is important for complex dynamic systems which RNN and CNN tend to become.

### Reservior computing

Reservoir computing is a framework for computation derived from recurrent neural network theory that maps input signals into higher dimensional computational spaces through the dynamics of a fixed, non-linear system called a reservoir. After the input signal is fed into the reservoir, which is treated as a "black box," a simple readout mechanism is trained to read the state of the reservoir and map it to the desired output. The first key benefit of this framework is that training is performed only at the readout stage, as the reservoir dynamics are fixed.[1] The second is that the computational power of naturally available systems, both classical and quantum mechanical, can be used to reduce the effective computational cost.

#### Liquid State Machines

A liquid state machine (LSM) is a type of reservoir computer that uses a spiking neural network. An LSM consists of a large collection of units (called nodes, or neurons). Each node receives time varying input from external sources (the inputs) as well as from other nodes. Nodes are randomly connected to each other. The recurrent nature of the connections turns the time varying input into a spatio-temporal pattern of activations in the network nodes. The spatio-temporal patterns of activation are read out by linear discriminant units.

The soup of recurrently connected nodes will end up computing a large variety of nonlinear functions on the input. Given a large enough variety of such nonlinear functions, it is theoretically possible to obtain linear combinations (using the read out units) to perform whatever mathematical operation is needed to perform a certain task, such as speech recognition or computer vision.

**Universal function approximation** : If a reservoir has fading memory and input separability, with help of a readout, it can be proven the liquid state machine is a universal function approximator using Stone–Weierstrass theorem.

##### Stone-Weierstrass theorem

In mathematical analysis, the Weierstrass approximation theorem states that every continuous function defined on a closed interval [a, b] can be uniformly approximated as closely as desired by a polynomial function. Because polynomials are among the simplest functions, and because computers can directly evaluate polynomials, this theorem has both practical and theoretical relevance, especially in polynomial interpolation. The original version of this result was established by Karl Weierstrass in 1885 using the Weierstrass transform.

Marshall H. Stone considerably generalized the theorem (Stone 1937) and simplified the proof (Stone 1948). His result is known as the Stone–Weierstrass theorem. The Stone–Weierstrass theorem generalizes the Weierstrass approximation theorem in two directions: instead of the real interval [a, b], an arbitrary compact Hausdorff space X is considered, and instead of the algebra of polynomial functions, a variety of other families of continuous functions on X {\displaystyle X} X are shown to suffice, as is detailed below. The Stone–Weierstrass theorem is a vital result in the study of the algebra of continuous functions on a compact Hausdorff space.

Further, there is a generalization of the Stone–Weierstrass theorem to noncompact Tychonoff spaces, namely, any continuous function on a Tychonoff space is approximated uniformly on compact sets by algebras of the type appearing in the Stone–Weierstrass theorem and described below.

A different generalization of Weierstrass' original theorem is Mergelyan's theorem, which generalizes it to functions defined on certain subsets of the complex plane. 

**Weierstrass Approximation theorem** :      Suppose |f| is a continuous real-valued function defined on the real interval [a, b]. For every ε > 0, there exists a polynomial p such that for all x in [a, b], we have |f(x) − p(x)| < ε, or equivalently, the supremum norm ||f − p|| < ε.

A constructive proof of this theorem using Bernstein polynomials is outlined on that page.



## Self Organizing Maps

### Hybrid Kohonen self-organizing map

In artificial neural networks, a hybrid Kohonen self-organizing map is a type of self-organizing map (SOM) named for the Finnish professor Teuvo Kohonen, where the network architecture consists of an input layer fully connected to a 2–D SOM or Kohonen layer. 

The output from the Kohonen layer, which is the winning neuron, feeds into a hidden layer and finally into an output layer. In other words, the Kohonen SOM is the front–end, while the hidden and output layer of a multilayer perceptron is the back–end of the hybrid Kohonen SOM. The hybrid Kohonen SOM was first applied to machine vision systems for image classification and recognition.

References : 

1. F. Nabhani and T. Shaw. Performance analysis and optimisation of shape recognition and classification using ANN. Robotics and Computer Integrated Manufacturing, 18:177–185, 2002.
2. Mark O. Afolabi and Olatoyosi Olude (2007), Predicting Stock Prices Using a Hybrid Kohonen Self Organizing Map (SOM), in 40th Annual Hawaii International Conference On System Sciences’, 2007, IEEE, pp. 48–56.


