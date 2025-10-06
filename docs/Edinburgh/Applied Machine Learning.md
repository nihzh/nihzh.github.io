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

# Supervised Learning
goal is a function `f`, inputs `x` and output `y`
x and y are all given in the training data
![](../img/Pasted%20image%2020250918211650.png)
predicting some continuous quantity
## Classification
given an input feature vector x, predicting an output vector y

- binary classivication: two possibilities
- bulticlass classification: C possible options

### Generative Classification
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

*Log Likelihood* : preserve the ordering
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

##### Convariance matrix
![](../img/Pasted%20image%2020250920012855.png)
The main diagnal contains *variances*, i.e. the *covariance* of each dimension with itself, for a given random vector $\color{#bd93f9}x=[x1​,x2​]^⊤$
![](../img/Pasted%20image%2020250923193913.png)
- symmetric
- Generalises the notion of variance to **multiple dimensions**
- positive semi-definite x⊺ 𝚺x ≥ 0 and x⊺ 𝚺−1x ≥ 0
- full convariance matric has D(D+1)/2 free parameters

![](../img/Pasted%20image%2020250923234808.png)

- **LDA (Linear Discriminant Analysis)**：假设所有类别共享同一个协方差矩阵 Σ\SigmaΣ。 → 决策边界是线性的。
- **QDA (Quadratic Discriminant Analysis)**：每个类别都有自己的协方差矩阵 Σc\Sigma_cΣc​。 → 决策边界是二次曲线。

![](../img/Pasted%20image%2020250923194233.png)

y ∈ {1, ..., C} and C > 2, by simply defining a class conditional model p(x|y = c) for each class

#### Naive Bayes
*Probabilisitc model* for conditional density $\color{#bd93f9}p(x|y)$, assume that **features are conditionally independent given the class label**
![](../img/Pasted%20image%2020251002165008.png)

*independent*: one variable does not affect another, `A` is (marginally) independent of `B` if $$p(A|B)=P(A)$$, which in conditional probability, $$p(A, B)=P(A)P(B)$$

`A` is *Conditionally independent* of `C` given `B` if $$p(A|C, B)=p(A|B)$$ i.e. once we know `B`, knowing `C` does not provide additional information about `A`

![](../img/Pasted%20image%2020251002180731.png)

![](../img/Pasted%20image%2020251002184116.png)
![](../img/Pasted%20image%2020251002184812.png)
![](../img/Pasted%20image%2020251002184846.png)

![](../img/Pasted%20image%2020251002184920.png)

*Laplace smoothing*: add a small positive number to all counts
![](../img/Pasted%20image%2020251002192253.png)

Missing Data: simply **ignore** the feature in any instance where the value is missing

##### Continuous Data
![](../img/Pasted%20image%2020251002203405.png)

![](../img/Pasted%20image%2020251002203904.png)

The conditional independence assumption used by Naive Bayes can fail to capture relationships that may be present in some datasets

### Discriminative Classifiers
Unlike Generative classifiers, the *discriminative classifiers* do not modelling the generative process

Discriminative approaches directly model the posterior $\color{#bd93f9}p(y|x)$
![](../img/Pasted%20image%2020251002232234.png)

#### Binary Linear Classification
Given some input features `x`, with associated class labels `y`, the goal is to estimate the parameters `w` of a *hyperplane* that can separate the data into the two classes

The *decision boundary* is where teh two classes are tied
- In 2D, **line**
- In 3D, **plane**
- In higher dimensions, **hyperplane**

![](../img/Pasted%20image%2020251002232909.png)

Decision boundary: $\color{#bd93f9}w^⊤ϕ(x)=0$
![](../img/Pasted%20image%2020251002235103.png)

If we can find a hyperplane to separate the data based on the class labels, the problem is said to be *linearly separable*

#### Logistic Regression
Model predictionos need be in range `[0, 1]`

*Logistic function*

![](../img/Pasted%20image%2020251003000434.png)
As `z` goes from $\color{#bd93f9}-\infty$ to $\color{#bd93f9}\infty$, $\color{#bd93f9}\sigma(z)$ goes from 0 to 1, has a **sigmoid** shape

![](../img/Pasted%20image%2020251003000916.png)
Modifying the input to the logistic function changes the shape of the function

Logistic regression = **linear weights + logistic squashing function**
![](../img/Pasted%20image%2020251003001443.png)

Has a linear decision boundary $\color{#bd93f9}p(y=1|x;w)=p(y=0|x)=0.5$, which equivalent to $\color{#bd93f9}w^⊤ϕ(x)=0$
![](../img/Pasted%20image%2020251003002549.png)

![](../img/Pasted%20image%2020251004014446.png)

- `w0` bias term
- `w1` weight for feature 1
	- 如果 $w_1 > 0$，说明 $x_1$​ 越大，越倾向于预测为正类（y=1）。
	- 如果 $w_1 < 0$，说明 $x_1​$ 越大，越倾向于预测为负类（y=0）。
- `w2` weight for feature 2

![](../img/Pasted%20image%2020251004234038.png)
![](../img/Pasted%20image%2020251004234109.png)
在参数 `w` 下，所有样本的标签刚好等于观测到的 `y` 的概率
最大似然估计MLE就是 **找到最优的 `w`，让观测数据的概率最大**
![](../img/Pasted%20image%2020251004234344.png)
$\color{#bd93f9}x_{nd}$​：将误差按每个特征维度的贡献进行加权

*One-vs-Rest* classification
- train an separate classifier, with an associated weight vector $\color{#bd93f9}w_c$, for each class
![](../img/Pasted%20image%2020251004235857.png)
- We select the maximum of the different classifiers as the predicted class
![](../img/Pasted%20image%2020251005000556.png)


*Softmax* function
![](../img/Pasted%20image%2020251005002811.png)
where![](../img/Pasted%20image%2020251005002832.png)![](../img/Pasted%20image%2020251005002927.png)
#### Linear Regression
The relationship between the features `x` and the target `y` is linear

![](../img/Pasted%20image%2020251005192519.png)
![](../img/Pasted%20image%2020251005192440.png)

The solved weights tell us the contribution of each feature to the final prediction
- Weight that close to 0 --> feature does not influence the output
- Large positive value --> strong positive relationship
- Large negative value --> string negative relationship

Standardise the data: interpret the relative model weights across the different dimensions, for each feature dimension from the training set:
- Mean
- Standard deviation

![](../img/Pasted%20image%2020251005231305.png)
*Sum of Squared Errors (SSE)*
![](../img/Pasted%20image%2020251005231359.png)
![](../img/Pasted%20image%2020251005235144.png)

![](../img/Pasted%20image%2020251006000538.png)

![](../img/Pasted%20image%2020251006001329.png)

Sensitive to *outliers*:
- Is the relationship obviously nonlinear
- Are there obvious outliers?

#### Non-linear Regression
*Polynomial regression*, the dimensionality of weights `w` will be the same as $\color{#bd93f9}𝜙(x)$
![](../img/Pasted%20image%2020251006005057.png)

##### Basis Expansion
Transform the original features `x` non-linearly into $\color{#bd93f9}𝜙(x)$ and *perform linear regression* on the transformed features, like a set of `M` basis functions
![](../img/Pasted%20image%2020251006005109.png)

So, the model becomes
![](../img/Pasted%20image%2020251006005133.png)

##### Radial Basis Functions (RBFs)
Each RBF $\color{#bd93f9}𝜓 ()_m$ has two parameters, a bell-shaped curve
- A centre location $\color{#bd93f9}c_m$
- A width $\color{#bd93f9}𝜎^2_m$
- outputs a single scalar
![](../img/Pasted%20image%2020251006005507.png)
Choosing a subset of the datapoints as centres




# Data Exploration and Evaluation

# Unsupervised Learning
have no y-values
![](../img/Pasted%20image%2020250918211823.png)

# Reinforcement Learning
Learn how to interact with its environment
Learn a **policy** which specifies the action to take in response to obeservation of the environment
Agents aims to maximise their reward

# Ethics

