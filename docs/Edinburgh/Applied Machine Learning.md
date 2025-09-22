Probabilistic Machine Learning: An Introduction
https://probml.gthub.io/pml-book/book1.html
Pattern Recognition and Machine Learning

*Learning* from data
*Prediction* new data

![](../img/Pasted%20image%2020250918203215.png)
model `f`
input `x` : features or oberservations or measurements about the real-parameters $\color{#b293f6}\theta$: things going to learn from data
output `y`

*Manually defining exhaustivev rules for a given task can be very challenging, as it is difficult to account for all possibilities.*

predefined rules
measure a given real y-value and prediction from model
![](../img/Pasted%20image%2020250918204821.png)
`l()` is a function that measures if the model's predictions are correct

choosing parameter
similar data as before

- What task am I trying to solve
- How should I **model the problem**
- How should I **represent** my data
- How can I **estimate the parameters** of my model
- How should I measure the **performance** of my model

### Classification
given an input feature vector x, predicting an output vector y

- binary classivication: two possibilities
- bulticlass classification: C possible options

#### Generative Classification:
通过高斯分布确定特征
- Assumption: conditined on the class, Data is Gaussian distributed\
![](../img/Pasted%20image%2020250918222504.png)

How likely it is that a test datapoint is from a given class
- evaluate the likelihood and divide by tatal
*Prior Knowledge*: Weighting factor
![](../img/Pasted%20image%2020250918224134.png)

*Bayes Classifier*
![](../img/Pasted%20image%2020250918224309.png)
Make prediction about new data that never seen before
![](../img/Pasted%20image%2020250918225018.png)

证据和结果的基于概率的决策关系
不确定性
证据 --> 认知
model fitting / model training
#### Maximum Likelihood Estimation MLE
*Likelihood function*
![](../img/Pasted%20image%2020250919190108.png)
*iid assumption*: independent and identically sampled from the same distribution

*Log Likelihood*
![](../img/Pasted%20image%2020250919190524.png)

*Negative Log Likelihood*
最小化损失函数
![](../img/Pasted%20image%2020250919191947.png)
- 对标签的NLL, $\color{#b293f6}\theta_b$​：控制标签分布（先验，Bernoulli 分布）
- 对特征的NLL, $\color{#b293f6}\theta_g$​：控制特征分布（条件分布，Gaussian 分布）

#### Mernoulli Distribution
![](../img/Pasted%20image%2020250919205721.png)
NLL
![](../img/Pasted%20image%2020250919225000.png)
MLE
![](../img/Pasted%20image%2020250919230310.png)

#### Gaussian Likelihood
![](../img/Pasted%20image%2020250920001300.png)

![](../img/Pasted%20image%2020250920004457.png)

![](../img/Pasted%20image%2020250920011930.png)

#### Multivariate Classification
Define model for multivariate data 多变量

Mean vector
![](../img/Pasted%20image%2020250920012818.png)
Convariance matrix
![](../img/Pasted%20image%2020250920012855.png)
- symmetric
- positive semi-definite x⊺ 𝚺x ≥ 0 and x⊺ 𝚺−1x ≥ 0
- full convariance matric has D(D+1)/2 free parameters

- **LDA (Linear Discriminant Analysis)**：假设所有类别共享同一个协方差矩阵 Σ\SigmaΣ。 → 决策边界是线性的。
- **QDA (Quadratic Discriminant Analysis)**：每个类别都有自己的协方差矩阵 Σc\Sigma_cΣc​。 → 决策边界是二次曲线。

### Supervised Learning
goal is a function `f`, inputs `x` and output `y`
x and y are all given in the training data
![](../img/Pasted%20image%2020250918211650.png)
predicting some continuous quantity



### Data Exploation and Evaluation

### Unsupervised Learning
have no y-values
![](../img/Pasted%20image%2020250918211823.png)

### Reinforcement Learning
Learn how to interact with its environment
Learn a **policy** which specifies the action to take in response to obeservation of the environment
Agents aims to maximise their reward

### Ethics

