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

#### Decision Trees
Nonlinear Data: classification and regression
Nodes:
- Root
- Internal
- Leaves

At each node, split data based on *feature dimension* and *threshold 𝜃*

1. All the data at the root node of the tree
2. Grow the tree by recursively splitting the data at each node
3. Until reach a specified condition
	- predefined maximum depth
	- impossible to split the data further

**Favour splits that result in child nodes that have high 'purity' i.e. 'impurity' `I(S)`** 

Measure the *entropy* at each node, using the distribution of datapoints
![](../img/Pasted%20image%2020251007224521.png)
Also notated as `H(S)`

*Gini Impurity*
![](../img/Pasted%20image%2020251007224807.png)

Measure the *Information Gain* of a split for each feature dimension and threshold pair, choose the **largest gain**
![](../img/Pasted%20image%2020251007225533.png)

"Singleton nodes" will be 100% purity ==> **overfitting**
Additional *hyperparameter* to prune it
- Maximum tree depth
- Minimum number of datapoints per node
- Minimum information gain

##### Regression trees
Ground truth targets are continuous values, *Node purity*: variance
![](../img/Pasted%20image%2020251007232448.png)
At each leaf we store the **mean** of all the datapoints that arrived at the node
![](../img/Pasted%20image%2020251007232534.png)

##### Ensembles of Trees
> 训练多棵稍有差异的决策树，然后**让它们共同投票或平均预测结果**。
> 这样单个树的“噪声”会被平均掉，整体模型更稳、更准确。

Grow an ensemble of `K` different decision trees
1. Pick a random subset of the data
2. Train a decision tree on this data, when splitting, choose a random subset of features
3. Repeat this `K` different times

Given a new datapoint `x` at test time: **classify `x` separately using each tree**
- Classification: majority vote
- Regression: mean prediction

## Optimisation
"Learning" --> continuous optimisation
descending error surface, minimise *error function* $\color{#bd93f9}\mathcal{L}(w)$
When data is i.i.d. (Independent and Identically Distributed)
![](../img/Pasted%20image%2020251018175302.png)

*Smoothness*
Constrained/continuous data, $\color{#bd93f9}\mathcal{L}(w)$ provides information about $\mathcal{L}$ and nearby values

*Derivatives*
For differentiable $\color{#bd93f9}\mathcal{L}(w)$, partial derivatives $\frac{\partial \mathcal{L}}{\partial w_i}$
vector of partial derivatives = gradient of the error: steepest error ascent 误差上升最快的方向 $$\nabla_w \mathcal{L} = \left( \frac{\partial \mathcal{L}}{\partial w_1}, \frac{\partial \mathcal{L}}{\partial w_2}, \dots, \frac{\partial \mathcal{L}}{\partial w_N} \right)$$
for descent 最小化误差: $$-\nabla_w \mathcal{L}$$

*Optimisation algorithm* $$\underset{w}{min}\space\mathcal{L}(w)$$
![](../img/Pasted%20image%2020251018212110.png)
> 不断计算梯度 → 确定下降方向 → 沿负梯度方向更新参数 → 直到误差足够小为止

$\color{#bd93f9}\eta$: step size

![](../img/Pasted%20image%2020251019002906.png)
> “Taking a step along δ cannot increase value locally”
> 只要步长足够小，沿着负梯度方向（δ方向）前进，不会让损失上升。

![](../img/Pasted%20image%2020251019010019.png)

### Gradient Descent
`compute directiono d=g`
![](../img/Pasted%20image%2020251019010231.png)

Computation
![](../img/Pasted%20image%2020251019013925.png)
- Estimation requires evaluating gradients at all N data points

*Stochastic Gradient Descent*
Compute update for parameter with just a single instance
![](../img/Pasted%20image%2020251019014754.png)
- Choose randomly for $\color{#bd93f9}i\in{1,...,N}$
- $\mathrm{E}[\nabla_w\mathcal{L}^i(w)] = \nabla_w\mathcal{L}(w)$
Provides an unbiased estimate of the gradient at each step

Struggle close to optimum

*Mini-batches Stochastic Gradient Descent*
![](../img/Pasted%20image%2020251019021044.png)
reduces the variance of the gradient estimator by `1/B`, also `B` times more expensive to compute `O(B * D)`

## Generalisation
Overfitting & Underfitting

*Qualitative*: Traning Data, Model Parameters
*Goldkocks Zone*: sufficient capacity to lean true regularities, but not enough to memorise or expoit accedential regularities

Control capacity: **model hyper-parameters**, to minisise generalisation error
- Regression: polynominal order
- Naive Bayes: # attributes, bounds on $\color{#b293f6}/sigma^2$
- Decision Trees # nodes

### Measuring Generalisation
Generalise to **novel** and **unseed** instances
Estimate error on test data without training on test data

#### Cross Validation
Partition data into train/test in different ways $$\{\mathcal{D}_{train_1};\mathcal{D}_{test_1}\},...,\{\mathcal{D}_{train_K};\mathcal{D}_{test_K}\}$$
For each partition: train model on training data -> test error on test data
**Find model from partition with lowest test error**
**Typically for small data**

#### Train-Val-Test
Hyper-parameters $$\mathcal{D}=\{\mathcal{D}_{train};\mathcal{D}_{val};\mathcal{D}_{test}\}$$
Tuning typer-parameters on $\mathcal{D}_{val}$
- for every candidate set of hyper-parameters, train on $\mathcal{D}_{train}$
- evaluate error on $\mathcal{D}_{val}$
- Find the hyper-parameters that lowest error on $\mathcal{D}_{val}$
Test error on $\mathcal{D}_{test}$
**Typically for big data that hard to 'cross validate'**

*Modelling Generalisation Error*
![](../img/Pasted%20image%2020251020214149.png)

#### Bias and Variance
![](../img/Pasted%20image%2020251020215742.png)
Bayes Error: 即使知道x也无法消除的目标随机性

![](../img/Pasted%20image%2020251020220044.png)
> 模型预测的**平均值**与真实均值差距（$423K vs $420K）就是 **bias（偏差）**；
> 不同训练得到的预测值之间的波动是 **variance（方差）**；
> 同样房子的真实售价自身的波动（$410K~$430K）就是 **Bayes error（噪声）**。

![](../img/Pasted%20image%2020251020223339.png)

### Improving Generalisation
Reducting overfitting
- Reducing capacity: tune on a validation set
- Early stopping: stop training when generalisation error starts to increase
- Ensembles: train different models on random subsets of training data and **averaging predictions** from multiple models reduces variance
- Regularisation

#### Regularisation
Penalise parameters that may be pathological and unlikely to generalise well
Complexity cost
![](../img/Pasted%20image%2020251020223543.png)

Linear regression    Ridge
![](../img/Pasted%20image%2020251020224049.png)

![](../img/Pasted%20image%2020251020230903.png)


# Data Exploration and Evaluation
## Representing Data

*Core Questions*
- What task am I trying to solve?  
- How should I model the problem?  
- How should I represent my data?  
- How can I estimate the parameters of my model?  
- How should I measure the performance of my model?

![](../img/Pasted%20image%2020251011213935.png)
Present data mathematically (feature representation)

**Feature-Value Pairs**

*Categorical Features*
- Each instance falls into one of a set
- Mutually exclusive
- Typically encoded as numbers that index into the set
- No natural 'ordering', 'closeness', only equality

*Ordinal Features*
- Each instance falls into one of a set
- Natural ordering to the categories (increasing/decreasing)
- Compare (<, >, =) only

*Numeric Features*
- Integers or real numbers
- comparison, closeness, functions(mean, variance)
- Extendable to higher order features

![](../img/Pasted%20image%2020251012015954.png)

### Modern representation
Learn what values for features helps with doing the task well
> 学习获得有效特征而不是手工设计特征

Choose a basic set of attributes, say image “patches”
![](../img/Pasted%20image%2020251012020205.png)

> Consider both data and task
> Consider what kind of model you want
> 	nuanced, interpretable
> 	scalable, performant
> Opaque decision making over learnt task‑specific features

### Plotting Data
Features
- title
- labelled axes
- axes ranges and ticks
- clarity (colour / thickness)
- legend

Informative: Convey as much as necessary
Clean: avoid overfilling & redundancy

#### Dimensionality Reduction
> *Manifold Hypothesis*: High-dimensional data in the real world really lies on low-dimensional manifolds within that high-dimensional space

**High dimensionality**
- **Counting** problem: As dimensionality grows, fewer abservations per region
- Mitigation
	- domain knowledge
	- feature engineering
	- modelling assumptions about features independence smoothness symmetry
	- reduce data dimensionality, struct a new set

*Dimensionality Reduction*
Represent data using a "few" variables
- *compression*: preserve as much information / structure as possible
- *discrimination*: only keep information that enables task
	- classification

*Feature selection*
- subset all features
- relevant to task

*Featrue Transformation*
- construct a new set of dimensions
![](../img/Pasted%20image%2020251013194650.png)
- transformation of original: linear F =⇒ e = Fx

##### Principal Components Analysis
Define printcipal commponents
- 1st PC: direction of **greatest** variation in the data
- 2nd PC: ⊥ 1st PC; **greatest remaining** variation
- ... until D, for $\color{#b293f6}x\in\mathrm{R}^D$

First $M << D$ components become new basis dimensions
Transform coordinates of each data point to new basis

Variation along direction = information
Transform basis --> fit maximum informaiton into M dimensions

![](../img/Pasted%20image%2020251013210933.png)
**不断乘以 S 会把任意非零向量的方向推向 S 的*主特征向量***（对应最大特征值的那个向量)

![](../img/Pasted%20image%2020251013214241.png)
任意单位向量 $v$ 上的投影方差是 $v^TSv$, 而 PCA 正是寻找让这个方差最大的方向$v$
- 方向 $v$ 是 $S$ 的特征向量;
- 方差大小（投影后信息量）= 对应的特征值 $\lambda$。

![](../img/Pasted%20image%2020251013221556.png)

![](../img/Pasted%20image%2020251013222654.png)

*Explained Variance*: Find minimum $M$, such![](../img/Pasted%20image%2020251013222810.png)
累计方差比例 / 特征值下降趋势

![](../img/Pasted%20image%2020251013223835.png)
降维：“把高维数据在主成分方向上投影”。
原来的 D 维向量现在用 M 个主成分坐标 $e_i$​ 来表示。

重构：“从低维空间近似地恢复原始数据”
M 越大，重构越接近原数据

##### Limitations
Sensitivity: **outliers** changes variance and pricipal components
- normalise: zero mean unit variance![](../img/Pasted%20image%2020251013233209.png)
- find outliers using interquartile range (IQR)
	- median(upper quartile 25%) ‑ median(lower quartile 75%)
	- define 'outlier' as values > 1.5\*IQR

Transform to handle non-linearity
LDA supervised

# Unsupervised Learning
have no label values
![](../img/Pasted%20image%2020250918211823.png)

# Reinforcement Learning
Learn how to interact with its environment
Learn a **policy** which specifies the action to take in response to observation of the environment
Agents aims to maximise their reward

# Ethics

