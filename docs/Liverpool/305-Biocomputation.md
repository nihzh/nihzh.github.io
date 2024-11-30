- Biomolecular Computation
- Computational Biology
- Bioinformatics
- Biological Computation
![](../img/IMG_1327.PNG)


## Perceptron
A neuron network that changes with "experience" using an error-correction rule.

Weight of a neuron changes when it makes **error response** to the input presented to the network

![](../img/Pasted%20image%2020241201001440.png)

- One layer of inputs
- One layer of outputs
The two layers are fully interconnected.

Semantically, a *perceptron* can be considered as a vector-valued function that maps the input `a = {a0, a1,..., an}` to the output `X = {X1, X2, ..., Xm}`, allows **real inputs**

Each output neuron has the same inputs, which the total input layer, while each individual outputs are with **individual connections** and therefore have **different weights** of connections

### Perceptron Training
The *weighted input* to the j-th output neuron
$$S_{j} = w_{j0} a_{0} + \sum_{i=1}^{n} w_{ji} a_{i}$$
- $\color{aqua}{a_{0}}$ is a special input neuron with **fixed** input value of +1
- $\color{aqua}{w_{j0}}$ rename as $\color{aqua}{-\theta_{j}}$
$$S_{j} = -\theta_{j} + \sum_{i=1}^{n} w_{ji} a_{i}$$
Thus, no need to set threshold manually, threshold train like weights

The value $X_{j}$ depends on whether the weighted input in greater than 0
![](../img/Pasted%20image%2020241201004603.png)
`f`: *activation function*
Predict the "desired output" ==> *perceptron "learning" or "training"*

The perceptron is trained by using a *training set* with *target outputs (labels)*
- 多样本训练集:  a set of input pattern **repeatedly (multiple times)** presented to the network during training
	- Input pattern in the set is **n-dimensional**. `a0 = 1`
- 目标输出 (标签): pre-defined correct output of an input pattern in the training set. 标签是supervised learning的标志

The output neuron first compute an output `Xj`
then compared to the desired outputs specified in the trainingg set and abtain the *error* ==> the difference between the target output and the instant one.
![](../img/Pasted%20image%2020241201012852.png)

The **goal of the training** is to arrive at a singleset of wights that allow each input in the training set to be mapped to the correct output by the network.

### Weight Update
1. Compute "error" of every connection for every ouput neuron
$$e_{j}^{k} = \{t_{j}^{k} - X_{j}^{k}\}$$
2. Update the weights:
$$w_{ji}^{k} = w_{ji}^{k} + \Delta w_{ji}^{k}$$
	where *Perceptron Learning Rule*
$$\Delta w_{ji}^{k} = Ce_{j}^{k}a_{i}^{k}$$
	A weight changes iff both the *input value* and the *error of the output* are **not** equal to 0
	
	The *"learning rate"* `C` is usually below 1 and determines the amout of correction made in a **single iteration**
	
	The **overall learning time of the network** is affected by the value of the "learning rate" C: *slower for small values* and *faster for larger*

3. When RMS is closed to zero, stop the training
	![](../img/Pasted%20image%2020241201021114.png)
	The network performance during training session is measured by root-mean-square error value
	
	The **first sum** is overall patterns; the **second sum** is all output neurons
	
	Once t, r, m and a are constants, $X_{j}^{k}$ is the only variation in the RMS function only, and the weights $w_{ji}^{k}$ is the only variation of X
	$$X_{j}^{k} = f(\sum_{i=0}^{n}w_{ji}^{k}a_{i}^{k}) = \overline f_{a}\tiny k(w_{ji}^{k})$$
	Thus, RMS error: `RMS` = $F_{D}(w)$, where `w` is network weight, `D` is data set
	
	The **best performance of the network** over a given data set `D` corresponds to the minimum of the `RMS error`, and we adjust the weight of connections `w` in order to reach the minimum
	
	The initially weights are all set to **small random values**, the error close to zero during training, the network has **converged**

## Multilayer Perceptron
![](../img/Pasted%20image%2020241201035500.png)
- All the neurons are divided into `l` subsets, each set is called alayer
- adjacent layers are **fully connected**
- each connection is associated with a *real weight*
- each neuron is associated with a *real bias* (assumed 0)
- inputs and outputs are all **real**

### Forward Propagation
The *first hidden layer*, the output of the j-th neuron in the first layer
$$X_{j}^{1} = f_{j}^{1}(S_{j}^{1})=f_{j}^{1}(\sum_{i=0}^{n^{0}}w_{ji}^{1}X_{j}^{0}+b_{j}^{1})=F_{j}^{1}(w_{j}^{1},X^{0}),j=1,...,n^{1}$$
Thus, *output of layer1* is the *output of layer0* combined with *weight layer1*$$X^{1} = F^{1}(w^{1},X^{0})$$
Can be derived for the following layers, called *forward propagation*

### Gradient Descent
Define the *performance of multilayer perceptron* over a dataset `D` as a half of the total squared error (`r`: data set number; `m`: output neurons), 1/2: simplified coefficient of gradient
$$E = \sum_{k=1}^{r}E^{k} = \frac 12\sum_{k=1}^{r}\sum_{j=1}^{m}(e_{j}^{k})^{2} = \frac 12\sum_{k=1}^{r}\sum_{j=1}^{m}(t_{j}^{k}-X_{j}^{k})^{2}$$
Substitute with the k-th input pattern $a^{k}$, and j-th neuron output layer $F_{j}$: $$=\frac 12\sum_{k=1}^{r}\sum_{j=1}^{m}(t_{j}^{k}-F_{j}(w^{l}, w^{l-1}, ..., w^{1}, a^{k}))^{2} = E(W)$$
Therefore, the *MLP error function* `E` is a function of the weights of connections only

The better the MLP performs, the smaller the MLP error function `E` is
The optimization problem: $min_{w}E(w)$, which the ***Gradient Descent***, addresses the issuue of how to update weights

#### Error Backpropagation Algorithm
One of the most popular techniques, it looks for the minimum of teh error function `E`  in the space of weights of connections `w` using the method of gradient descent
![](../img/Pasted%20image%2020241201051845.png)

$\frac {\partial E}{\partial w_{ji}^{h}}$: partial derivative of the error function `E` w.r.t. the weight of connection between `j-th` neuron in the layer `h` and `i-th` neuron in the previous layer `h-1`

***Update rule*** including the hidden layer (`C`: learning rate):
$$w_{ji}^{h}=w_{ji}^{h}+\Delta w_{ji}^{h},\space\space where\space\Delta w_{ji}^{h}=-C\frac {\partial E}{\partial w_{ji}^{h}}$$
Using a continuous and differentiable activation function $f$ ==> *Generic sigmoidal activation function* associated with a hidden or output neuron
$$f(S)=\frac {\alpha}{1+e^{-\beta S+ \gamma}}+\lambda$$
- The product `𝛼𝛽` defines the steepness of the curve
- The parameter `𝜸` causes a shifting along the horizontal axis and is usually equal to zero
- The parameters `𝛼` and `𝜆` define the range limits for scaling purposes

$$f'(S)=\frac {df}{dS} = \frac {\beta}{\alpha}\cdot(f(S)+\lambda)(\alpha+\lambda-f(S))$$
If the value of activation function itself is known for that value of S, it is straight foreard to compute the derivative at any perticular value of variable S without actual differntation

If all actication functions $f(S)$ in the network are differntiable, then we can use the *chain rule* to calculate the partial derivative of the error function `E` w.r.t. the weight of a specific connection