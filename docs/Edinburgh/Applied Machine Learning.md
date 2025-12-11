# Introduction
Probabilistic Machine Learning: An Introduction
https://probml.gthub.io/pml-book/book1.html
Pattern Recognition and Machine Learning

*Learning* from data
*Prediction* new data

![](../img/Pasted%20image%2020250918203215.png)
model `f`
input `x` : features or observations or measurements about the real-parameters $\color{#b293f6}\theta$: things going to learn from data
output `y`

*Manually defining exhaustive rules for a given task can be very challenging, as it is difficult to account for all possibilities.*

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

*Reinforcement learning*
Learn how to interact with its environment
Learn a **policy** which specifies the action to take in response to observation of the environment
Agents aims to maximise their reward

# Supervised Learning
goal is a function `f`, inputs `x` and output `y`
x and y are all given in the training data
![](../img/Pasted%20image%2020250918211650.png)
predicting some continuous quantity
## Classification
given an input feature vector x, predicting an output vector y

- binary classification: two possibilities
- multiclass classification: C possible options

### Generative Classification
**Making Predictions**
通过高斯分布确定特征
- Assumption: conditioned on the class, Data is Gaussian distributed\
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

#### Bernoulli Distribution
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

- **LDA (Linear Discriminant Analysis)**：假设所有类别共享同一个协方差矩阵$\Sigma$。 → 决策边界是线性的。
- **QDA (Quadratic Discriminant Analysis)**：每个类别都有自己的协方差矩阵 $\Sigma_c$。 → 决策边界是二次曲线。

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

*Logistic function*: sigmoid

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
Transform the original features `x` non-linearly into $\color{#bd93f9}𝜙(x)$ and **perform linear regression** on the transformed features, like a set of `M` basis functions
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
Define principal commponents
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

## Evaluation
### Classification
*Error*
Measure of how good a classifier is
![](../img/Pasted%20image%2020251026233000.png)

![](../img/Pasted%20image%2020251026233941.png)
*Recall*: 正类(应该为正) 中被正确识别的比例: 已找到的/该找到的
*Precision*: 预测为正的样本中，正确的比例 (真正为正) : 找对了/找到的

![](../img/Pasted%20image%2020251027000715.png)

*Cohen's Kappa*
$\color{#bd93f9}p_o$ Observed Agreement: Accuracy
$\color{#bd93f9}p_e$ Expected Agreement by Chance: 假设预测与真实独立时，随机一致的概率
$$p_e=\frac{(P_{true+}\cdot P_{pred+})+(P_{true-}\cdot P_{pred-})}{T^2}$$

如果一个模型预测与真实结果完全一致，κ = 1。  
如果模型表现与随机猜测差不多，κ = 0。  
如果模型比随机猜测还糟（系统性错误），κ < 0。

*Threshold*
Models typically compute "confidence" as $\color{#bd93f9}p(y|x)$
Decisions are made by *thresholding* of this confidence
![](../img/Pasted%20image%2020251027001036.png)
Thresholding $\color{#bd93f9}\tau$ determines error rates and confusion matrix, each provides a value for chosen measure
#### Precision-Recall Curve
![](../img/Pasted%20image%2020251027005722.png)
- 如果 **降低阈值 $\tau$**：模型更容易预测“正类”  
    → 正类召回更多 (**Recall ↑**)  
    → 但错误预测正类的概率也更高 (**Precision ↓**)
- 如果 **提高阈值 $\tau$**：模型更谨慎预测“正类”  
    → 错误的正例减少 (**Precision ↑**)  
    → 但漏掉一些真实正例 (**Recall ↓**)

#### ROC: Receiver Operating Characteristic
![](../img/Pasted%20image%2020251027005853.png)
*AUC: Area Under the ROC Curve*: Large Area ==> better model

#### Multi-Class Classification
*Cohen's Kappa*
*Matthews Correlation Coefficient (MCC)* $$MCC=\frac{p_0-p_e}{\sqrt{(1-p_y)(1-p_\hat{y})}}$$![](../img/Pasted%20image%2020251027010301.png)
Confusion Matrix *C*![](../img/Pasted%20image%2020251027010650.png)
衡量预测值与真实值之间的整体相关性

### Regression
Distance between predicted and actual values

![](../img/Pasted%20image%2020251027200327.png)

#### MSE: Mean Square Error
![](../img/Pasted%20image%2020251027200615.png)
Predict mean $\color{#b293f6}y$
- squaring: blow up error

- Sensitivity to outliers
- Sensitivity to scaling / transaction

#### MAE: Mean Absolute Error
![](../img/Pasted%20image%2020251027200718.png)
Median, not mean
Less sensitive to outliers: no squaring

**Variants**
![](../img/Pasted%20image%2020251027201326.png)

#### Correlation Coefficient
![](../img/Pasted%20image%2020251027201409.png)

![](../img/Pasted%20image%2020251027202410.png)
Insensitive to scaling and transaction
- for large $\color{#b293f6}y$, predict larger $\color{#b293f6}\hat{y}$
- for smaller $\color{#b293f6}y$, predict smaller $\color{#b293f6}\hat{y}$
衡量预测值与真实值的线性相关性: 上升或下降趋势
无量纲: 不受单位或尺度影响
方向相关性
非线性关系、异常值可能误判
**不反应偏移误差**

#### Coefficent of Determination $R^2$
![](../img/Pasted%20image%2020251027201923.png)![](../img/Pasted%20image%2020251027202118.png)Measures goodness of fit for model
Predict the mean label
![](../img/Pasted%20image%2020251027202029.png)

Convex optimality with scaling and translation, $\color{#b293f6}\rho^2=R^2$

## Model Selection
*Comparing Point Estimates*: can be susceptible to many kinds of reandom effects

*Comparison with tradeoff*: AUC of Precision-Recall
- Random effects can make comparison hard

Embracing Uncertanty

*Comparing Distributions*

### Statictical Tests
*Population*: all the elements from a set
*Sample*: observations drawn from population

*CLT: Central Limit Theorem*
For a set of samples $\color{#b293f6}x_1$, ..., $\color{#b293f6}x_N$, ... from a **population** with *expected mean* $\color{#b293f6}\mu$ and *finite variance* $\color{#b293f6}\sigma^2$
![](../img/Pasted%20image%2020251027222421.png)
样本均值的标准化分布会弱收敛 (weak convergence)于标准正态分布 (Gaussian)
- Independent
- Identically distribution
- large enough

*Student's-t Distribution*
For **smaller N**, not Gaussian
**Unknown population finate variance $\color{#b293f6}\sigma^2$**
estimate sample variance 样本方差 $\color{#b293f6}s^2=\frac{1}{N-1}\sum_{i=1}^{N}(x_i-\bar{x}_N)^2$
- `n-1`: Bessel's correction
![](../img/Pasted%20image%2020251027230547.png)
uses $\color{#b293f6}s=\sqrt{\frac{1}{N-1}\sum_{i=1}^{N}(x_i-\bar{x}_N)^2}$ , the precision changes along the sample size
`v` (df) = number of observations − number of parameters estimated ($\bar x$ in this case)
- larger N, larger v


![](../img/Pasted%20image%2020251027235552.png)

概率密度函数：每个自由度v下 t 分布的具体形状
![](../img/Pasted%20image%2020251027235814.png)

#### Hypothesis Testing
Formally examine two opposing conjectures (hypothesis): $H_0$ and $H_1$, Analyse data to determine which is True and which is False
![](../img/Pasted%20image%2020251028004126.png)

![](../img/Pasted%20image%2020251028004140.png)
二者命题应该完全相反, Null是可证明的, 对Null证伪以证明Alternative

单样本检验
- Null: 总体均值等于某固定值
- Alternative: 总体均值不等于某固定值
双样本检验
- 独立样本
	- Null: 两个样本均值相等
	- Alter：两个样本不相等 / 大于 / 小于
- 配对样本
	- Null: 差异等于0
	- Alter: 差异不等于0
方差分析检验
- Null: 所有总体均值相等
- Alter: 至少有两个, 总体的均值不相等

![](../img/Pasted%20image%2020251028004054.png)

$\alpha$: significance
临界值c: v=19, $\alpha$=0.05
Report confidence interval *CI* 置信区间
![](../img/Pasted%20image%2020251028005334.png)

![](../img/Pasted%20image%2020251028005637.png)

![](../img/Pasted%20image%2020251028005114.png)
![](../img/Pasted%20image%2020251028005048.png)

Rejecting $H_0\ne H_0$ is 100% false
Failing to reject $H_0\ne H_0$ is 100% true
but not how big or important the difference is

Simple cross-validation can violate that independence for CLT (overlap in $\mathcal{D}_{train}$)

## Recommender System
How to predict a user's rating for the items they have not yet seen

The rating data from other users, is likely to be very **sparse**: the average user only rates a very small number of items

*Explicit Feedback*: Users rate items directly
- hard to get information
*Implicit Feedback*: Extracted from user actions: clicking, watching until end...
- weaker form of supervision

Present user ratings as a matrix Y of sieze $|\mathcal{U}|\times|\mathcal{I}|$, can be very sparse
![](../img/Pasted%20image%2020251128220826.png)

### Predict missing ratings
*Average rating*: $\hat{Y}_{ui}$ 
![](../img/Pasted%20image%2020251128221503.png)
取所有已评分用户的平均评分
忽略了用户间的差异

### Collaboratve Filtering
Find similar users and make predictins for absent user of interest based their similarity to these existing users

> The underlaying assumption is that if user A and B rate items they have both seen similarly, then user A is more likely to rate items thay have not seen similar to how user B would.

Weight the rating score based on the similarity between the users
*Weighted average*
![](../img/Pasted%20image%2020251128224818.png)

### Matrix Factorisation
Recommenedation task => matrix completion
Predict all the missing entries of Y given the subset of user rating pairs $(u,y)\in S$
![](../img/Pasted%20image%2020251128225104.png)

Assume Y is a low rank matrix as $\hat{Y}=UV^{\top}\approx Y$, 
where $U$ is $|U| \times K$, $V$ is $|I| \times K$
![](../img/Pasted%20image%2020251128231750.png)
Each row $u_u$ of U represents a different user
Each row $v_i$ of V represents a different item
To predict a missing entry: $$\hat{Y}_{ui}=u_u^{\top}v_i$$
### Model Training With SGD
From subset of user rating pairs $(u,i)\in S$ where $Y_{ui}\ne ?$
Loss function $$\mathcal{L}(\theta)=\sum_{(u,i)\in S}(Y_{ui}-u_u^{\top}v_i)^2$$
![](../img/Pasted%20image%2020251128234630.png)

#### Regularisation
![](../img/Pasted%20image%2020251128234859.png)
![](../img/Pasted%20image%2020251128234908.png)

## Neural Networks
逻辑回归：线性决策边界， 表达力不足
- 切换非线性边界模型
- 非线性变换特征，在新空间线性可分

A linear method, can **learn the features** from the raw input data
![](../img/Pasted%20image%2020251129010449.png)

### Single Layer Network
$$\hat{y}=g2(w^\top_2g1(W_1x+b_1)+b_2)$$
![](../img/Pasted%20image%2020251129013833.png)

### Multilayer Neural Network
Multilayer perceptron (MLP)
Fully connected network with three input features, three hidden layers with four hidden units in each, and two output units
![](../img/Pasted%20image%2020251129014316.png)
Any sequence of linear layers can be equivalently represented with a single linear layer $$y=W3​(W2​(W1​x))=(W3​W2​W1​)x=W′x$$
Non-Linear Activation Functions
- *Sigmoid (Logistic)*:  $\sigma(z)=\frac{1}{1+exp(-z)}$ ，输出 \[0, 1\]
- *Hyperbolic tangent*: $tanh(z)=\frac{exp(2z)-1}{exp(2z)+1}$, 输出 \[-1,1\]
- *Rectified linear unit*: $ReLU(z) = max(z,0)$

*Universal function approximators*: 
具有非线性激活函数的前馈神经网络可以以任意精度近似任何函数

Deeper neural networks are more effective than shallow ones
In deeper networks, later layers can leverage teh features learned by earlier ones

#### Transforming Features
![](../img/Pasted%20image%2020251129020527.png)
![](../img/Pasted%20image%2020251129020915.png)
![](../img/Pasted%20image%2020251129021010.png)
increased the number of hidden units in the first layer
![](../img/Pasted%20image%2020251129021117.png)

### Training Neural Networks
For L-layer MLP with L weight matrix and bias vector, parameters $$\theta=(W_1,b_1,...,W_L,b_L)$$
*Loss function* $L(\theta)$ to measure the disagreement between the model prediction $f(x)$ and the ground truth target $y$
**Gradient of the loss + descent** $$\theta\leftarrow\theta-\eta\cdot\nabla_{\theta}\mathcal{L}$$
#### Backpropagation
A recursive calgorithm for computing the derivatives, uses the chain rule by stroing some intermediate terms
利用Chain Rule递归计算梯度
1. *Forward pass*: compute and store the values at all of the hidden units and the network output
2. *Backward pass*: calculate the derivatives of each weight, starting at the end of the network, and reusing the previous computation as we move towards the start
![](../img/Pasted%20image%2020251129023101.png)

![](../img/Pasted%20image%2020251129023810.png)

Multilayer neural networks are non-convex, gradient descent mau get stuck in local minima during training and never find the global optimum. In practice, it can still obtain good solutions for many proctical problems.

#### Hyperparamenters
Network Structure
- number of hidden layers
- number of units in each hidden layers
- the type of non-linear activation function

Training Schedule
- the learning rate
- the type of optimiser
- how the weights are initialised
- then to stop training

#### Automatic Differentation
Compute the gradient of a loss function applied to the output of the network wrt the parameters in each layer

*Autodiff*: automatic evaluate the derivative of a function

![](../img/Pasted%20image%2020251129025915.png)

### Convolutional Neural Network (CNN)
Constrain each hidden unit to extract features by sharing weights across the input, better for image

Image X with K\*K weight matrix W
![](../img/Pasted%20image%2020251129030334.png)
Multiple weight matrices can be used to produce multiple feature maps
![](../img/Pasted%20image%2020251129030455.png)

- **learnable** convolutional filters
- **non-learnable** pooling layers
	- reduce the spatial dimensionality of the feature maps
### Recurrent Neural Networks (RNN)
For sequence data (time series)
Each input is processed sequentially, one item at a time, past information is retained through past hidden states
![](../img/Pasted%20image%2020251129030732.png)

### Transformers
Process the entire input all at once
- training be performed in parallel
- less susceptible to foregetting information from the past, better in GPU

**Self-attention** unit, used to compute similarity scores between input in the input sequence

计算序列中任意两个位置之间的相似度，让模型能直接“看见”远处的词。


# Unsupervised Learning
have no label values
![](../img/Pasted%20image%2020250918211823.png)

## Clustering
### K-Means
让“离某些特殊点（簇心）最近”的样本分到同一簇；不断**交替**“分配→重算中心”。
Ensure points closest to some special point end up in the same cluster

Hard: a point belongs to just one cluster
Flat: **single level of clustering**
Polythetic: distance based similarity within clusters
![](../img/Pasted%20image%2020251104234137.png)

Converges to local minimum
repeat several random initialisations and pick one with smallest aggregate distance

choose K from a elbow plot

### Hierarchical
![](../img/Pasted%20image%2020251105004318.png)

#### HK-Means
Top-Down
Perform K-Means on data
For each resulting cluster $\color{#b293f6}c_i$, run K-Means within $\color{#b293f6}c_i$
once cluster has been determined at top level, cannot change

#### Agglomerative
Bottom-Up
Ensure "nearby" points end up in the same cluster

Hard: a point belongs to just one cluster
Hierachical: **multiple elvels of clustering**
Polythetic: distance-based similarity within clusters


![](../img/Pasted%20image%2020251105015445.png)

树状图的竖向高度代表合并时的距离；**水平切一刀**得到某个粒度下的若干簇；往上切→簇更少更粗，往下切→簇更多更细。
##### Cluster Distance Measures
*Single link*
两个cluster之间最近两点的距离
![](../img/Pasted%20image%2020251105015625.png)

*Complete link*
两个cluster之间最远两点的距离
![](../img/Pasted%20image%2020251105015637.png)

*Average link*
跨簇所有点对距离的平均
![](../img/Pasted%20image%2020251105015702.png)

*Ward's Method*
合并后类内方差（SSE）最小
![](../img/Pasted%20image%2020251105022001.png)

##### Unified Formulation
*Lance-Williams Algorithm*
合并$c_i,c_j$​ 得到$c_{i\cdot j}$后，与其他cluster $c_k$的新距离
![](../img/Pasted%20image%2020251105022606.png)

### Evaluation
#### Extrinsic
Solve downstream task 任务驱动
Quantisation: represent data with cluster features
- color quantisation: use centroid value
- feature extraction: use cluster index
Partition: train separate classifiers for each sub-group

#### Intrinsic
##### Unsupervised
Measure how well-separated clusters are
Compare intra-cluster distances to inter-cluster distance
![](../img/Pasted%20image%2020251105025325.png)
- a = 与**本簇**其余点的平均距离（簇内紧凑度）；
- b = 与**最近的其他簇**的平均距离（与他簇分离度）；

##### Supervised
Measure alignmetn of clusters to known labels
![](../img/Pasted%20image%2020251105025508.png)
把“样本对是否在同一簇/同一类”当二分类，计算 **Accuracy**

![](../img/Pasted%20image%2020251105025605.png)
在 RI 基础上**扣除随机期望**并做**归一化**，使“随机分区”的期望为 0；其计算基于簇–类交叉表 $N_{ij}=|r_i\cap c_j|$ 的组合项。
##### Human
Compare judgements to humans on exemplars

## Non-Linear Dimensionality Reduction
*Feature Transformation*: Transform inputs `x` using a feature map $\phi(x)$ to a higher dimension C > D, which data is linearly separable in C $$x\in \mathrm{R}^D,\phi(x)\in \mathrm{R}^C,C>D$$
![](../img/Pasted%20image%2020251127191150.png)

Choosing the right kernel: 
- to learn kernel matrices K directly from data

> Several non‑linear dimensionality reduction methods can be viewed as kernel PCA, with kernels learned from data

### Manifold Hypothesis
High-dimensional data in the real world really lies on low-dimensional manifolds within that high-dimensional space
- local measure of **closeness**
- project data `x` onto lower-dimensional manifold as `e`
![](../img/Pasted%20image%2020251127192045.png)

> 所有非线性可视化方法的共同目标：找到映射$f: X \to E$，让“重要的关系”（距离、邻居、概率分布、拓扑结构等）在 X 和 E 中尽量一致。

### Multi-Dimensional Scaling (MDS)
Project data from $\mathcal{X}$ to $\mathcal{E}$ while preserving the distance between **every pair** of samples in original data X
![](../img/Pasted%20image%2020251127192405.png)
Choosing L2, simpler optimisation

In swiss-roll, miss the manifold surface

### Isomap
Project data from X to E while preserving the distance between **points on the embedded manifold**, not arbitrary distance
![](../img/Pasted%20image%2020251127200311.png)

![](../img/Pasted%20image%2020251127195458.png)

拓扑形态，采样要求高
NN图可能不连通
FW是$O(N^3)$

### Locally Linear Embeddings (LLE)
Project data from X to E while preserving the **linear transform** that reconstructs points from the K nearest neighbours
![](../img/Pasted%20image%2020251127210450.png)

在高维空间中取每个点的K个邻居的线性重构，每个邻居的权重$w_{ik}$
在低维空间中希望用相同的权重重构嵌入点

对噪声敏感，流形结构无法保证

### t-distributed Stochastic Neighbour Embedding (t-SNE)
Project data from X to E while preserving the **probability distribution** over  
pairwise similarities between points in the space.
![](../img/Pasted%20image%2020251127212301.png)

### Uniform Manifold Approximation & Projection (UMAP)
*Leverage Riemannian geometry* and *topology* to construct a general framework for manifold learning and dimensionality reduction.
![](../img/Pasted%20image%2020251127223639.png)


# Ethics
形式化动作、后果、效用、意图，用于机器伦理推理

> Ethics is concerned with studying and/or building up a coherent set of rules or principles by which people ought to live

How human should act
- right, fair and just
- does not cause harm

*Virtue Theories*: Who is doing the action?
*Consequentialist Theories*: Are the consequences moral?
*Deontological Theories*: Is the action itself moral?
![](../img/Pasted%20image%2020251130003008.png)

## Machine Ethics
Can a computer operate ethically because it is internally ethical in some way?

**Top-down**: Start with an **ethical theory**, identify smaller problems and solve them
- not clear from the beginning if subproblems are solvable

**Bottom-up**: Start with **data**, learn ethical behaviour from data
- non-necessary subproblems may be dealt with

## The ART Principles
> We need to find an ethically acceptable way of designing technology that can benefit the society.

*Accountability*: The system explains and justifies its decision to users and relevant parties

*Responsibility*: The focus is on how the socio-tecnical systems operate

*Transparency*: It is about the data being used, methods being applied openness about choices and decisions

ART is essential to build social trust in Autonomous Systems
![](../img/Pasted%20image%2020251129032001.png)

### Transparency
- access to **justifications for decisions** when needed, how to contest and appeal
- addresses the right to know: participation information sheet in data lifecycle
- helps in understanding and managing risks

*Explanations*
- *Contrastive*: why P instead of Q
- *Selected*: weight factors explanations, influenced by cognitive biases
- **Driven by casual** rather than probabilities
- *Social/interactive*: audience knowledge/requirement background

many stakeholders, interested in something different

How to explain a "black box" model, avoiding system vulnerable to attacks
- use simpler models?

## Justice Fairness and Bias
Human dignity ==> discrimination, unjust treatment, stem of biases

Algorithmic fairness, since algorithms may amplify existing economic and societal bias

在 **数据收集、特征计算、建模、评估、部署** 等每一步都可能引入伤害。

> 有害后果往往不是“算法本身突然坏掉”，而是从整个机器学习流程中多个小偏差累积而成。

![](../img/Pasted%20image%2020251129213617.png)

### Representation Bias
Target population != Use population

Under-represented groups

*Sampling bias*: Target population is set to X, but the data available is only a small subset of X

![](../img/Pasted%20image%2020251129213516.png)

### Learning Bias
When modeling choices amplify performance disparities

Differential privacy 会在训练中加入噪声，换来隐私保证，但必然**降低模型准确度**

在DP中差距被进一步放大 ==> 保护隐私的机制本身也可能带来新的不公平效应

### Evaluation Bias
When the benchmark datasets **do not represent** the use population

The choice of metrices can also result in evaluation bias
- aggregate results
- reporting one type of metric

> 模型训练与评估时使用的基准数据没覆盖好这些群体 → 评估偏差；
> 模型参数与目标设计没有关注不同群体 → 学习偏差。

### De-biasing Algorithms
Aware different types of bias, in how to design an AI system

> We can talk about fairness when people are not discriminated against based on their membership to a specific group.

Arvind Narayanan

Fairness definition
- group fairness (statistical fairness)
- individual fairness

# Further Topics
## Semi-Supervised Learning
![](../img/Pasted%20image%2020251130010817.png)

![](../img/Pasted%20image%2020251130010853.png)

![](../img/Pasted%20image%2020251130010942.png)

![](../img/Pasted%20image%2020251130011105.png)
![](../img/Pasted%20image%2020251130011255.png)

![](../img/Pasted%20image%2020251130011203.png)

## Active learning
![](../img/Pasted%20image%2020251130010703.png)![](../img/Pasted%20image%2020251130010719.png)