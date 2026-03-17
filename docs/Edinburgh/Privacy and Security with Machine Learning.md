> Machine Learning is the study of algorithms that improve their **performance P** at a **task T** with **experience E**

## Introduction
Focus on Algorithms
![](../img/Pasted%20image%2020260113182910.png)

Data acquisition -> Data preparation -> Model training -> Model testing -> Model deployment

Adversaries with ML:
- Automation: lower cost and larger scale
- Synthesis
- Pattern extraction
- Network traffic analysis, Data deanonymisation, Hardware side-channels

Classification of samples ==> threat model extraction
"urgency"

## Basics
### Machine Learning
*Supervised -- Classification*
Given a set of observation with labeled, assign labels to new instances
- measure ***characteristics*** and **features**
- Decision threshold `f(x)`, a hyperplane in linear models
- Give an algorithm to fix the task

#### Non-linear models
Non-linear, introduce new dimension
Non-linear models: Neural networks
- activation function
- loss function: find best `w` which minimise the lost
- gradient descent
- backward propagation

#### Evaluation
- generalisation: bias-variance trade-off
- separate dataset
- confusion matrix & predictive performance metrics
- ROC curve

**Class imbalance**
misleading result for classifying result
the accuracy high, but precision is very low

**IID assumption**
new samples are independent and follow the same underlying distribution 
mapping from inputs (feature vectors) to outputs (classes)
high dimensional spaces, lost useful of distances, common in su

### Computer Security
Policy -- Threat model -- Mechanism
Try to figure out all possible actions attackers can do
**You can never achieve perfect security**

- *Confidentiality*: only *authorized* entities can access the information
- *Integrity*: the data is **untampered** and **uncorrupted**
- *Availability*: both the data and the system that provides access to it are there **when you need** them

Cryptography:
- ensures confidentiality -- only accessible by keys
- authenticating users -- digital signatures
- ensures integrity

Threat modelling in communication systems
- Passive (read) - Active (add, remove or modify)
- Internal (control one or several system components) - External (only control communication links)
- Local (only sees part of the system) - Global (access to the entire system)
- Targeted (compromise a specific set of users) - Untargeted (attempts to compromise any user)

Specification -> Design -> Implementation -> Assurance
- Designed to achieve a security goal
- Defense embedded
- New defensive system alongside an existing, unmodified system

*Trust*
- *Assurance*: the means to know that the system is secure
- *Reliability/Resilience*: they are robust and continue operating intact or gracefully degrade
- *Accountability*: the means to verify that the system is operating as intended

*Privacy*: Concerns individuals and their expectations on how their data, behaviours, and interactions are recorded, utilized, and spread

*Anonymity*: set of individuals that share the same attributes

## Application of ML to Traffic Analysis
Traffic analysis: Passively analyze communication metadata to extract information

*Tor* 
Website / Protocol Fingerprinting (WF)
- attacks can be deployed by a low-resource adversary
- some Tor users are especially vulnerable

Training a model by datasets of fingerprinting, for predict content and routs, driven by ML innovation
![](../img/Pasted%20image%2020260130204141.png)

Closed world/ Open world
![](../img/Pasted%20image%2020260207054832.png)
现实世界很多unmonitored，模型需要先判断是否monitored

The base rate fallacy
![](../img/Pasted%20image%2020260130203423.png)

Defences:
- generate some dummy random package, encrypt and send as normal
- delay the sending
- escape from the pattern

![](../img/Pasted%20image%2020260130204455.png)

## Malware
Intrusive programs, for gaining profit
- cause damage
- steal information
- ransom
- take control of devices

Extract the signature and do blocking: hash, specific bytes...
- Can be overpass by just modify the malware program a little bit

ML classifier: selecting appropriate features
Find efficient representations automatically

Characteristics of the malware
- Static analysis: source code without execute
- Dynamic analysis: program while running
- Hybrid

### Static Analysis
**Drebin**: xml file, disassembled code
Access to hardware components
Permissions
App components: interfaces, activities, services, content providers and broadcast receivers
- suspicious API calls
- used permissions
Network address
Intent filters

Embedding binary features in vector space
- Linear SVM: test is the inner product between point and hyper-plane

### Dynamic malware detection
- **Traces of execution**: malicious behaviour
- **Features to extract**: APIs, IP address connecting, services interacting
- **End-to-end learning**: action sequence -> list of tokens to apply NLP

*Gradient Descent* to find an approximate solution
Find perturbation 𝜹 s.t. perturbed input 𝒙𝟎 + 𝜹 is misclassified
![](../img/Pasted%20image%2020260207061245.png)

*Evasion*: modify input such that it preserves malicious intent but is detected as benign
- The 𝜹 is 'noise' added to the input, but not random
- crafted to maximize the error of the classifier $$\delta^*=\arg\underset{\delta\in\mathcal{C}}{\min}s_{mal}(x+\delta)$$
![](../img/Pasted%20image%2020260207064340.png)

### Modeling assumptions
#### Access to model parameters (unrealistic)
Threat model in ML security/privacy
![](../img/Pasted%20image%2020260207063807.png)

#### Feature mapping is invertible (semantic gap)
*Features space representation*: the abstract representation of software applications as vectors of descriptive features used to train and test machine learning based malware classifiers

*Problem space representation*: the original, unprocessed form of the software application from which features are extracted

Semantic gap: Problem imposes constraints on possible perturbations
在feature space找到$\delta$不代表能在problem space实现
- legit?
- which semantics?
- how to verify automatically
- preprocessing?

#### IID assumption (adversarial drift)
dataset shift, distribution shift, concept drift...
  
The noise is not stochastic but adversarial: The adversary adapts to stay under the radar -- shifting the concept of malware over time
![](../img/Pasted%20image%2020260207070251.png)

![](../img/Pasted%20image%2020260207070440.png)

**Experimental bias**
Temporal Inconsistency in Train/Test Sets

## Privacy and Anonymization
Sharing data & protect privacy

After anonymized, the interception of multiple datasets acts as a *quasi-identifier* 准识别符，组合后高度可识别

*Personality Identifiable Information (PII)*: any information that can uniquely identify a specific person

Bigdata analysis
Data protection regulation does not apply to anonymized data

> There is no perfect mechanism to fully protect privacy of data

Third parties / public can always have auxiliary information
![](../img/Pasted%20image%2020260207011426.png)

### K-anonymity (Sweeny)
A dataset satisfies k-anonymity of the records associated with each individual in the dataset cannot be distinguished from at least k-1 other individuals in the dataset
- suppression and generalization such that quasi-identifiers map to k or more people 一个准标识符映射到至少k个个体
- enables a **trade-off** between utility and privacy
![](../img/Pasted%20image%2020260207011926.png)
- assumes that auxiliary knowledge is bounded (fixed)
- *l-diversity*, *t-closeness*

> It is unreasonable to expect that a privacy mechanism will provide **utility** and at the same time **prevent all individual inference** for **arbitrary auxiliary knowledge**

**Homogeneity attack**: all k-records have the same sensitive value
**Background knowledge attack**: e.g., low incidence of disease for a demographic

Sparse data: sparsity means that rows are more likely to be unique

> In general, we cannot know the adversary's background knowledge: we cannot bound it!

### Statistical Disclosure Control (SDC)
> nothing about an individual should be learnable from the database that cannot be learned without access to the database

Aux. info: “Alice is 8cm shorter than average”

## Differential Privacy
A randomized algorithm $\mathcal{M}$ is $\varepsilon$-differentially private if for all adjacent datasets $D,D'$ and for all $S\subseteq Range(\mathcal{M})$
$$\Pr[\mathcal{M}(D)\in\mathcal{S}]\le e^\varepsilon \Pr[\mathcal{M}(D')\in\mathcal{S}]$$
where $\varepsilon$ is a parameter called the *'privacy budget'*

"Distance between output distributions is at most $\varepsilon$"
个体层面被随机化（噪声）保护，但总体统计仍可恢复

*Local DP: Randomized Response*
Parameter `p` (randomizing) adjusts privacy-utility trade-off
以p概率说真话：
- 1: no privacy
- 1/2: perfect privacy

以概率 p 说真话，以概率 1-p 说假话
观测到“回答 Yes 的比例” γ，可反推总体真实比例 x $$\gamma=px+(1-p)(1-x)\Rightarrow x=\frac{\gamma+p-1}{2p-1}$$

**Continuous values f(x)**: add noise sampled from a probability distribution cantered around 0 $$f(x)+Y~where~Y\sim Lap(0,\sigma)$$

**Sensitivity**: 换掉一个人的数据，统计量最多能变多少
$$\Delta f=\underset{D\sim D'}{\max}|f(D)-f(D')|$$

*Local DP*: 数据提供者发送前加噪 (1 query)
*Global DP*: 可信数据库管理者提供查询接口 (n queries)
- n的数量受限于privacy budget

$(\varepsilon,\delta)$-DP
$$Pr[\mathcal{M}(D)\in\mathcal{S}]\le e^\varepsilon Pr[\mathcal{M}(D')\in\mathcal{S}]+\delta$$
where $\delta$ is Failure probability, $M$ is $\varepsilon$-DP with probability $1-\delta$

Mechanisms
- **Robustness to post-processing**: it is safe to apply arbitrary functions on output
- **Composition**: if we run a $(\varepsilon,\delta)$-DP mechanism $k$ times, the resulting mechanism is $(k\varepsilon,k\delta)$-DP
- **Advanced composition**: if $k\lt\frac{1}{\varepsilon^2}$, the resulting mechanism is $(\mathcal{O}(\sqrt{k~log(\frac{1}{\delta'})})\varepsilon,k\delta+\delta')$-DP for all $\delta'\gt0$ 
- **Amplification**: if we sample a fraction $q$ of the data, our mechanism becomes $(q\varepsilon,q\delta)$-DP

A rigorous "worst-case" mathematical definition of privacy, independent of background knowledge of auxiliary data

Hard to interpret, hard to pick Epsilon, privacy budget

*DP-ERM*
- Output perturbation: minimize then perturb
- Objective perturbation: perturb then minimize

*DP-SGD*: calculate gradient over sample iteratively, apply DP at that level
### Private Learning
DP mechanism sits within the learning algorithm, Once the model has been trained, it can be safely released
![](../img/Pasted%20image%2020260224225939.png)

## ML for Intrusion Detection Systems
*Intrusion Detection*: sensing and analysing system events for the purpose of noticing attempts to access system resources in an unauthorized manner

*Intrusion Detection System*: a service implemented in software or hardware, that automates the task of intrusion detection

Servers, Endpoints, Network Infrastructure, authentication and backup systems, the IDS

**Host-based IDS**: run directly on the hosts
- An agent runs on each host
- deep but narrow
**Network-based IDS (NIDS)**: sensors are placed on subnetwork components, and analysis components run either on those components or hosts
- Analyze the correct execution of protocols
- Traffic analysis: capture more complex network behaviors
- broad but shallow

Should rely on both approaches

### Signature detection
look for patterns (signatures of intrusion)
**Rule-based**: 
- network (headers, payloads)
- host (events)
Limitation: Low detection rate for unknown attacks

### Anomaly detection
Intrusion behavior will look different from benign behaviour
Anomaly: Data point or pattern that does not conform to normal behaviour
- outliers
- abnormalities
- deviations

Model "normal" behavior and raise alarms for behaviors that significantly deviate from it

Limitation: Base rate fallacy 

Classification discriminative (supervised): use labeled data to train a model for the positive/negative classes
- Positive unlabeled: models the malign class
- may limit the discovery of new threats

**One-class SVM** (Semi-supervised): model only the benign class, more robust to new attacks, can be improved by giving negative examples to model the positive class boundary 
- intrusions are positive

![](../img/Pasted%20image%2020260225031948.png)

![](../img/Pasted%20image%2020260224184057.png)

LUCID
- features: 10 features from the first n packets of a flow
- model: CNN

Spurious correlations
lab-only evaluation
- baseline not reflect real-world settings
- biased parameter selection
label inaccuracy
- noise exists
- labelling errors common in IDS, unreliable
- mitigate: verify labels, actively model label noise
Base rate fallacy
- A: alarm event
- I: intrusion event
![](../img/Pasted%20image%2020260225040113.png)
$$\thickapprox\frac{TPR}{FPR}BR$$
Denominator is dominated by the factor governing FPR
当基率极低时，Precision 主要靠把 FPR 压到极低来救
NOT FEASIBLE IN PRACTICE!

## Evasion attacks
Undermining integrity, models failed to detect/classify
![](../img/Pasted%20image%2020260227212120.png)

![](../img/Pasted%20image%2020260227215217.png)
$L_\infty$ norm = $\underset{i}{\max}|x_i|$

![](../img/Pasted%20image%2020260303183411.png)

Continuous domain and white box inference model, knows architecture and parameters

**Gradient-based**
![](../img/Pasted%20image%2020260227203403.png)

*Targeted*: Objective is to maximize misclassification confidence
*Untargeted*: Objective is to minimize and distance of evasion

### Iterative attacks
#### Evasion attacks against machine learning at test time (Biggio et al.)
Attacker scenarios:
- Perfect knowledge (PK): knows model and training data
- Limited knowledge (LK): unknown model but can sample training data distribution

Attacker capabilities
- Modification of features (at test time)
- Some constrains on problem space
	- PDF documents: only add, no remove content

$g(x)$ is the model prediction on $x$
- $g(x)\lt0$, ~ -1 == Benign
- $g(x)\gt0$, ~1 == Malicious
- Pr\[y = Malicious | x\] (confidence score)

Add a second term to maximize the probability density around benign training samples
- Pr\[x | y = Benign\] ==> KDE
- $\frac{1}{n}\sum^n_{i=1}k(\frac{x-x_i}{h})$ k: kernel function; h: smoothing parameter bandwidth

**Gradient descent attack**
- gradient of classifier
- gradient of density

现实约束下（problem space + 特征约束），evasion 依然可行

#### Szedegy: Intriguing properties of neural network
对抗样本 ==> 最小扰动
- 分类器 $f:[0,1]^m\to\{1,\dots,k\}$
- 有连续损失$\ell_f(x,l)$
- 给定原始 x 和目标标签 l，找扰动 r
分类约束作为损失项
$$\min_r \; c\|r\| + \ell_f(x+r,l)\quad \text{s.t.}\; x+r\in[0,1]^m$$

### One-step attack
**Fast gradient sign method (FGSM)**
$$x_{\text{adv}} = x + \epsilon\cdot \text{sign}\big(\nabla_x \ell(\theta,x,y_{\text{true}})\big)$$
对输入求梯度，每个维度都向“最增加损失”移动相同步长
这样天然保证 $\|x-x_{\text{adv}}\|_\infty \le \epsilon$

### Reasons adv examples happen
**Overfitting**: complex decision boundary, easy to find inputs that result in unexpected outputs

Different models to have very different adversarial examples, can transfer across different models and architectures and obtained with different learning algorithms

**Linearity**: neural networks tend to be **local linear**, tend to be over-confident on points far from the decision boundary

"**High-dimensionality in inputs**", can be somewhat counterintuitive ways when moving away from the data
![](../img/Pasted%20image%2020260303182257.png)

### Black-box evasion attacks
Query very lot of times, incur significant cost on both time and money

![](../img/Pasted%20image%2020260303183700.png)
Perturb inputs and observe changes in output
- label, conditional prob., distribution over classes
- find decision boundary

for each training example, provide an adversarial example to increase the probability of the right label

## Evasion defenses
### Defensive primitives
**Adversarial example detection**: distinguish between adversarial and genuine
- dimensionality reduction: feature squeezing, PCA, etc.
- 只要检测器本身可微、可模拟、可近似，攻击者就可以把“骗过分类器”和“骗过检测器”一起作为优化目标。

**Reduce model sensitivity**: model outputs shouldn't change much on small input perturbations
- data augmentation: add random perturbations to training examples
- 普通随机增强不一定覆盖到**最坏方向**的扰动，最致命的方向

**Limit information** to attacker
- gradient smoothing / hiding / masking: reduce information provided by the gradients
- 让梯度“看起来没用”不等于模型真的鲁棒。

**Reduce overfitting and model complexity**: early attempts were focused on reducing the model complexity although Goodfellow show evidence that these are not sufficient 模型复杂或过拟合导致对抗样本脆弱
- regularization: smoothness penalty
- 高维空间里，小扰动沿着很多维度积累，最终能带来很大 logit 变化

**Reduce the size of the input space**
- Low-pass filters
- Feature squeezing

**Blocking transferability**
- defences often defeated by training a surrogate model that implements the defense and exploiting the transferability of adversarial examples across models

When designing and evaluating a defense, we should not underestimate the attacker  
Defense design should consider **adaptive attacks**
### Adversarial training
For each training example, provide an adversarial example to increase the probability of the right label
同时使用对抗样本训练模型，专门使用让模型出错的扰动，并要求它仍然输出正确标签，最成功的防御手段之一
![](../img/Pasted%20image%2020260308030447.png)

*Min-max optimization* problem  直接选择最大化损失的攻击
![](../img/Pasted%20image%2020260308030633.png)
Not depend on a specific attack, but **maximizes the model's loss** instead,, regardless of the attack or adversary's strategy
内层max：在每个训练样本上在半径$\epsilon$内找到最坏的扰动$\delta$
外层min：找到模型参数$\theta$使总体损失尽可能小
复杂且昂贵：对于每个训练样本，都要先攻击一次模型，且会牺牲accuracy
会过拟合某类攻击

### Adversarial example detection
真实样本和对抗样本在模型内部表示或某些统计量上可能有规律可抓
新增一个第N+1类，专门代表adversarial examples
**training time**: validation set error

**statistics**
“The odds are odd”
Hypothesis: Robustness to noise statistics are different between adversarial and legitimate examples
- difference noise of input, the models are varied
- some adversarial model may less robust to perturbation: **use random noise as probing instrument**

![](../img/Pasted%20image%2020260308040233.png)
![](../img/Pasted%20image%2020260308040344.png)
可以被adaptive attakcs绕过，或针对softmax分布设计攻击
“只要你的检测依据是某种可观测统计量，攻击者就可以把“伪装出正常统计量”也纳入目标。”

#### feature squeezing
同时对输入做一个或多个squeezing变换，分别进模型得到多个prediction，比较差异，差异太大则为adversarial
![](../img/Pasted%20image%2020260306204324.png)
squeezers are correlated: achieve independent robustness
正常样本经过轻微简化后，模型预测不该变太多；对抗样本可能很依赖那些细微脆弱特征，一压缩就露馅。
- 压缩颜色精度 / 彩色=> 灰度
- 梯度平滑/增加噪声： **obfuscated/masked  gradients** 通过让通向对抗样本的方向变得不清楚，从而误导攻击者。
- JPEG compression

![](../img/Pasted%20image%2020260308041233.png)
![](../img/Pasted%20image%2020260308041246.png)
梯度可以被恢复

#### Stochastic Activation Pruning (SAP)
按照单元激活绝对值加权的概率去丢弃神经元。
推理时网络的某些激活会随机被裁剪掉。
drop out units randomly for classification
add noise in weight
平均重复采样可以估计真实梯度
- LFGS attack

#### Distillation
student model gives **smooth gradients**, act as **surrogate**
find adversarial examples in student model
check that adversarial examples are also adversarial in the target model
- soft probabilities gives information about class boundaries

**soft probabilities** 指的是模型输出的那一整组**“软”的类别概率分布**，而不是只给一个最终类别。

![](../img/Pasted%20image%2020260308041735.png)

![](../img/Pasted%20image%2020260308042224.png)
- adaptive attacker 威胁模型必须假设攻击者知道防御存在
- all approaches
- “Anyone, from the most clueless amateur to the best cryptographer, can create an algorithm that she herself can’t break”
- We need to know how to break defenses before building new ones

#### Certified Defenses
Randomized smoothing：分类器在某点 x 周围某个集合内的预测是可验证地不变的。
Given a soft classifier $f$, smoothed prediction $g(x)$is the class that 𝑓 is most likely to assign to the random variable
$$X \sim \mathcal{N}(x,\sigma^2 I)$$
$g(x)$是给 x 加高斯噪声后，f 最可能输出的类别。
![](../img/Pasted%20image%2020260308042608.png)

![](../img/Pasted%20image%2020260308042737.png)

## Poisoning attack
Inject malicious data in training samples
攻击者不直接改模型参数，也不一定在测试时改输入，而是在训练数据或训练流程中“下毒”

Transfer learning 迁移学习
外部(不可信数据来源 Collaborative (federated) learning: to train the larger model, share data across models ==> malicious co-worker

Evasion 在测试和部署时定制输入样本绕过模型检查
Poisoning 在训练阶段对数据投毒, 破坏模型
![](../img/Pasted%20image%2020260310180622.png)
*Availability poisoning*: attacker not for specific inputs of class, untargeted, just lower the performance and generalization ability
*Integrity poisoning*: targeted, making some specific inputs fail

malware/intrusion detection


![](../img/Pasted%20image%2020260310183906.png)
双层优化问题，共同使用$\hat{w}$变量
- 外层：使攻击效果最大
	- $\theta\in\Theta$ 攻击者知识: 训练数据结构, 模型结构, 学习算法, 超参等
	- $\mathcal{D}_c$ 攻击者可操作的基础样本集合
	- $\mathcal{D}_c'\in\Phi(\mathcal{D}_c)$ 被修改后的投毒样本集合
	- $\mathcal{A(D_c',\theta)}\in\mathbb{R}$ 攻击目标函数, 攻击效果=模型在验证集上的损失
- 内层：优化模型参数，最小化损失
	- 防御者（或者学习算法）会在“干净代理训练集 + 投毒样本”上训练模型，找到使训练损失最小的参数 $\hat{w}$

### Threat model: clean-label attack
Not modifying the labels
The dataset is audited or created manually
Transfer learning and end-to-end retraining

Misclassification of a single target sample as a target class, while keeping the same performance on untargeted points

**Feature collision** to crafting poison data
Given a target 𝒕 and a base 𝒃, generate a point 𝒑 such that is close to 𝒕 in the model 𝑓’s output, but close to 𝒃 in its input
![](../img/Pasted%20image%2020260310225706.png)
- 用梯度下降最小化与 target 的 L2 距离（在输出 / 特征空间）；
- 用 proximal update 最小化与 base 的 Frobenius 距离（在输入空间）

**Evaluation**
![](../img/Pasted%20image%2020260310225856.png)

- One-shot attack, only good at transferred
- multi-shot attack, good at both

### Backdoor attacks: conceptual model
![](../img/Pasted%20image%2020260310230115.png)
Adversaries also inject perturbations to inputs

Poisoning the training data: adding samples with a trigger feature
Manipulating model parameters
Neural Trojans: modifying the model architecture, **only activates in the presence of a trigger**

Malicious behavior is only activated by inputs stamped within "torjan" trigger
1. **Poison the training dataset** with backdoor trigger-stamped inputs
2. Retain the target model to compute new weights ==> BadNet

Triggers can seems natural

MNIST: Single-pixel backdoor, Pattern backdoor

*Invisible Sample-Specific Backdoor Attack (ISSBA)*: trigger specifically **designed for each image**, more effective

**Triggers**：
- blended image with the trigger
- distributed/spread trigger: yellow square, image of flower...
- accessory: glasses...
- facial characteristic: arched eyebrows, narrowed eyes
	- natural demographic: skin color, face feature, disability aid

Invisible trigger & clean-label backdoors: very small perturbation

100 success with 10% of poisoning

![](../img/Pasted%20image%2020260313203009.png)

![](../img/Pasted%20image%2020260313203247.png)
attacker cannot perturb more than certain fraction of dataset

## Privacy and Confidentiality risks in ML
*Confidentiality*: preventing unauthorized access to data
- architecture
- model parameters

*Privacy*: individuals

Membership's personal data involved into the dataset training, lot of sensitive info
- Membership inference

### Black-box & White-box MIA
Adversary can query the target model, return the model's output (prediction, vector probability)
- Oracle access: **black-box**
- Full access: **white-box**, learning algorithm, architecture

**Black-box**
May have some **auxiliary knowledge** about the population
- The learning algorithm (𝐴) and the distribution of the training dataset (𝒟) from which training dataset S was drawn.

**Goal**: determine whether a data point $z$ is a part of the training set $S$ of a model $h_S=A(S)$, by querying the model (knowing algorithm 𝐴 and distribution 𝐷)

**White-box**: 
在overfitting白盒下，用一个z很容易得到它是否在S内
The attack can be implemented with a meta-classifier (shadow models)
- sample from the training dataset 模拟目标模型的行为模式
- training model k with target's learning algorithm 观察in/out行为差异
- repeats for many samples, average behaviour will closer to the target model 训练attack model
overfit => better on more classes
memorizing all data in the dataset
![](../img/Pasted%20image%2020260314033631.png)
攻击者在学习“目标模型对见过的数据和没见过（在不在训练集中）的数据，输出行为有什么统计差异”。
拥有更多类别的模型，攻击精度更高：模型为了区别类型，需要学习更细力度，学习到尖锐的特征

Adversary relax the assumption of having access to D
- Model-based synthesis: No assumption of access to any data or any statistics
	- we try to find record, assuming model overfitted and close to the target
- Statistics-based synthesis
- Noisy real data

![](../img/Pasted%20image%2020260317182128.png)

Model inversion: auxiliary information
- Warfarin dosage
![](../img/Pasted%20image%2020260317183050.png)

1. duplicate values that agree with to create hypothesis on unknown feature
2. compute and compare the attributes with "dosage" value
3. incorporation error information and marker

Learning from the population is not a privacy issue
Lear certain attribute in the certain dataset
DP: change the framing, make hard to mining statistics

If model is a polynomial of degree $n$, attacker needs $n+1$ queries!

Equation solving attacks
- Logistic regression
- Multiplayer perceptron
![](../img/Pasted%20image%2020260317185726.png)