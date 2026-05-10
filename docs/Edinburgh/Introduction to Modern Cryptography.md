Proof something is secure
> The art of making and breaking secret codes

> Design, analysis, and implementation of mathematical techniques for securing information, systems, and distributed computations against adversarial attack

Data integrity & authentication
## Introduction
![](../img/Pasted%20image%2020260505231624.png)

**Private-key (symmetric-key) encryption**: single user / multiple parties
![](../img/Pasted%20image%2020260113233346.png)

*Kerckhoffs's principle*: The encryption scheme is not secret
- The attacker knows the encryption scheme
- The only secret is the key
- The key must be chosen at random; to kept secret

- easier to keep key secret than algorithm
- easier to change key than to change algorithm
- standardisation: ease of deployment, public scrutiny

### Shift Cipher
*Modular arithmetic*  同余&取模运算
![](../img/Pasted%20image%2020260113234130.png)
$c_i=[m_i+k\mod 26]$;  $m_i=[c_i-k\mod 26]$
26 possible keys => easy brute-force

*Byte-wise Shift Cipher*
- Alphabet of bytes rather than English letters 用一字节编码
	- $k\in\mathcal{K}=\{\text{0x00}\dots\text{0xFF}\}$, 256 possible keys
	- printable? 
- Use XOR instead of modular addition (reversible) 用可逆XOR
	- $c_i=m_i\oplus k$;  $m_i=c_i\oplus k$

> The key space must be large enough to make brute-force attacks impractical
### Vigenere Cipher
分片成n个stream，统计字符频率，尝试最常见字符为e
**Index of Coincidence** 算总体符合概率
![](../img/Pasted%20image%2020260116232932.png)
![](../img/Pasted%20image%2020260116233042.png)

**Finding the key length**
用正确的key长度解密的文本应该拥有合理的$\sum_i {q_i}^2=0.065$, 即无论密钥都拥有相同的分布, 但长度猜测错误时内容完全混乱趋近于$\sum_i {q_i}^2=0.038$
- 对每个候选长度N的每个stream (通常一个stream确定) 计算$\sum_i {q_i}^2$, 并选取最大的N
- Natural English Language IC: 0.065
- Random distribution IC: 0.038
- 总体时间

**Attack Time**
1. 确认key length: 对于最长L的密钥, 分别计算26个字母的频率
	- $L\cdot\sum_{i=0}^{25}{q_i}^2$
2. 确认key: 
	1. 对于第i个stream (第i位密钥): 对于26个候选值B(a-z), 分别计算频率$q_i$, 取值最接近0.065 ==> $26^2$
	2. 总用时$\le26^2L$
Brute-force: $26^L$
$$26L+26^2L\approx26^2L\ll26^L$$

> Large key space is a necessary, but not efficient condition for a secure encryption scheme

### Modern Cryptography
- Formal **definition**: evaluation & modularity
- Precise **Assumptions**: explicit, mathematically precise
- Proof of security, under two principles above

> A proof of security is always relative to the definition being considered and the assumption(s) being used.

The proof is irrelevant
- If the security guarantee does not match what is needed 安全保证不符合需求
- If the threat model does not capture the adversary's true abilities 威胁模型不符合真实能力
- If the assumption that is relied upon turns out to be false 所依赖的假设是错误的

> Provable security of a scheme does not necessarily imply security of that scheme in the real world
> 可证明安全不必然等价于现实安全

要攻击一个“可证明安全”的方案，现实攻击者通常只能从两条路入手：
1. 针对**定义与现实环境的差距**（理想化模型遗漏了什么现实因素）
2. 针对**底层假设是否真的成立**（假设在实践中是否被打破或被削弱）

# Symmetric Cryptography
## Secure Encryption
*Three principles of modern cryptography*
- Definitions: Precise, mathematical model and formal definition of what security means
- Assumptions: Clearly stated and unambiguous
- Proofs: Prove security and move away from design-break-patch

**Goal (Security guarantee)**: What we want to prevent the attacker from achieving
**Threat model**: What capabilities the attacker is assumed to have
- Ciphertext-only attack (COA), 仅密文攻击
- Known-plaintext attack (KPA), 已知明文攻击
- Chosen-plaintext attack (CPA), 选择明文攻击
	- API接口
- Chosen-ciphertext attack (CCA), 选择密文攻击
**Secure Encryption**: How would you define what it means for encryption scheme $\mathsf{(Gen,Enc,Dec)}$ over message space $\mathcal M$ to be **secure**

> Regardless of any prior information the attacker has about the plaintext, the ciphertext should leak no additional information about the plaintext
> **加密后的密文不应该让攻击者在这些知识基础上得到任何新增优势**。

## Perfect Secrecy
*Random variable (RV)*: variable that takes on discrete values with certain probabilities 以特定概率取离散值

*Probability distribution (PD)*: A PD for a RV specifies the probabilities with which the variable takes on each possible value 取值的概率分布
- Each probability between 0 and 1
- Probabilities sum to 1

*Event*: a particular occurrence of event E in some experiment => $\Pr[E]$
*Conditional probability*: one event occurs, given that some other event occurred: $\Pr[A|B]=\frac{\Pr[A\land B]}{\Pr[B]}\equiv\frac{\Pr[AB]}{\Pr[B]}$
*Independence*: Two RV X, Y are independent if: $\forall x,y:\Pr[X=x|Y=y]=\Pr[X=x]$  y是否加入的概率相同

*Law of total probability*: Let $E_1\dots E_n$ are a partition of all possibilities, then $\forall A$: $$Pr[A]=\sum_i\Pr[A\land E_i]=\sum_i\Pr[A|E_i]\Pr[E_i]$$
事件A发生时必定伴随着一个$E_i$发生
$$\Pr[A|B]=\Pr[A\land B]/\Pr[B]\Longrightarrow\Pr[A\land B]=\Pr[A|B]\Pr[B]$$


Shift cipher 拥有固定的密文模式，从Chosen Ciphertext攻击中反推明文

RV M and K are independent
Pr\[M = attack today\] = 0.7     Pr\[M = don′t attack\] = 0.3
Pr\[K = k\] = Pr\[Gen outputs key k\]
C be a RV denoting the value of the ciphertext in this experiment

*Perfect Secrecy*
![](../img/Pasted%20image%2020260120233941.png)
每个加密后字符拥有同样的概率对应明文的每个字符, 即对密文的观察不会泄露任何关于明文的信息，在看到密文 c 的条件下，每个消息 m 都是可能的

*Bayes's theorem*
$$Pr[A|B]=\frac{Pr[B|A]Pr[A]}{Pr[B]}$$
![](../img/Pasted%20image%2020260120234546.png)

### One-time Pad
![](../img/Pasted%20image%2020260120234752.png)
**The One-time Pad satisfies perfect secrecy**   掩码
- Any observed ciphertext can correspond to any message
- Having observed a ciphertext, the attacker cannot conclude for certain which message was sent

![](../img/Pasted%20image%2020260123234002.png)
![](../img/Pasted%20image%2020260123234016.png)
![](../img/Pasted%20image%2020260123234030.png)

#### Brute-force Attack Resisting
![](../img/Pasted%20image%2020260124035425.png)

#### Limitations of OTP (all schemes for PS)
1. **The key is as long as the message**: parties must share keys of (total) length equal to the (total) length of all the message they might ever send  需要与消息等长的密钥
2. **A key must be used only once**: only secure if each key is used to encrypt a single message, such that 密钥仅限一次性使用$$c_1\oplus c_2=(k\oplus m_1)\oplus(k\oplus m_2)=m_1\oplus m_2$$leaks information about m1, m2 (differ between) 泄露二者差异
	- XOR with a letter(01...) and a space(00...), results 01..., whereas 00... if they are both letters
3. Trivially broken by a known-plaintext attack

#### Optimality of the One-time Pad
> If `(Gen, Enc, Dec)` with message space M is perfectly secret, then $|\mathrm{K}|\ge\mathrm|M|$ 
> 
> 对于指定的密文c, 令集合$S_c=\{Dec_k(c)\},k\in\mathcal{K}$ (key space) ，其必须与$\mathcal{M}$相等，即令每一条可能的密文都对应所有可能的明文。如$|\mathcal{K}|<|\mathcal{M}|$，则可以通过穷举$\mathcal{K}$得到$|S_c|=|\mathcal{K}|$的完整消息空间，找到$\mathcal{M}$中没有对应的消息m\*，以排除指定消息。这不符合无多余信息泄露的标准。

![](../img/Pasted%20image%2020260124021245.png)
![](../img/Pasted%20image%2020260124021218.png)
## Perfect Indistinguishability
*Perfect Indistinguishability (PI)*: Randomized experiment, equivalent with PS
![](../img/Pasted%20image%2020260127231738.png)
$D_m$: 固定明文m和密钥空间中$k\in\mathcal K$对应的 密文空间概率分布, 即**两个不同明文输出的密文空间概率分布相等**

![](../img/Pasted%20image%2020260127232012.png)
![](../img/Pasted%20image%2020260127232028.png)
![](../img/Pasted%20image%2020260127232443.png)
对手通过观察加密后的内容得到的信息与没加密前一致
For all attacker a, no matter what he does, he have fixed 1/2 for winning this game

### Computational Secrecy
**Relax perfect indistinguishability**, allowing "fail" with tiny probability
Little weaker
#### Computational Indistinguishability (Concrete security)
Security may fail with probability $\le\varepsilon$
Restrict attention to attackers running in time/CPU cycles $\le$ t
在攻击者能力t下, 存在失败率小于$\varepsilon$ 
**$(t,\varepsilon)$-indistinguishable** $$Pr[\textsf{Priv}K_{A,\pi}=1]\le \frac{1}{2}+\varepsilon$$
#### Asymptotic security
Security parameter $\color{#b293f6}n$ (key length)
- chosen by honest parties when they generate/share keys
- **known by adversary**

Security may fail with probability **negligible** in n
Restrict attention to attackers running in time **polynomial** in n

*Polynomial function*
![](../img/Pasted%20image%2020260128025903.png)

*Negligible function*
![](../img/Pasted%20image%2020260128025918.png)
当n大过一个阈值之后，$f(n)$小于任何多项式$p(n)$
$2^{-n}$, $2^{-\sqrt n}$, $n^{-\log n}$, 

![](../img/Pasted%20image%2020260128032305.png)

efficient = *probabilistic polynomial-time (PPT)*
poly · negl = negl

![](../img/Pasted%20image%2020260128032819.png)
$1^n=\underbrace{11\cdots1}_{\text{n times}}$, denotes the algorithm is polynomial in n

When computer get faster, a tiny increase of n could compensate the gap, the scheme still remain secure

![](../img/Pasted%20image%2020260128033155.png)

![](../img/Pasted%20image%2020260228062334.png)
## Pseudorandomness
*Random*: sample a random element according to **some distribution**

*Uniform*: sample an element uniformly at random means to sample according to the uniform distribution
- If we generate a uniform 16-bit string, each of the above occurs with probability $2^{-16}$

*Uniformity*: a property of a distribution
- $D: \{0,1\}^n\rightarrow[0,1]$ such that $\sum_xD(x)=1$
*Uniform distribution*: 一个分布函数$U_n$, 每个$x\in\{0,1\}^n$ 分配概率$2^{-n}$

*Pseudorandom*: cannot be distinguished from uniform (random)
- Pseudorandomness is a property of a **distribution**
- looks like random

> $D$ is pseudorandom if it passes all efficient statistical tests

![](../img/Pasted%20image%2020260131012622.png)
任何“算力不超过t” 的攻击者 A，都几乎分不清样本来自 D 还是来自真正均匀随机$U_p$，概率差最多$\epsilon$

### Asymptotic Pseudorandomness
- parameter $n$, polynomial $p$
- Let $D_n$ be a distribution over $p(n)$-bit strings
- Pseudorandomness is a property of a sequence of distributions $${D_n}=\{D_1,D_2,\cdots\}$$
![](../img/Pasted%20image%2020260131014747.png)

### Pseudorandom Generators (PRG)
> $G$ is a deterministic, poly-time algorithm that is **expanding** $$|G(x)|=p(|x|)>|x|$$输出长度由某个固定多项式p决定, 只依赖于输入长度; 一定比输入长度长

![](../img/Pasted%20image%2020260130235807.png)
G能产生的串只占整个输出空间的$2^{-n}$, 其余在$D_n$中出现的概率严格为0
![](../img/Pasted%20image%2020260130233914.png)
对于所有PPT adversary不可区分, 除非枚举所有可能种子, 消耗$2^n$不是PPT
![](../img/Pasted%20image%2020260203232337.png)

The PRGs exist requires the unproven assumption $\mathcal{P}\ne\mathcal{NP}$ 
**We assume certain algorithms are PRGs**

## Pseudo One-Time Pad (POTP)
![](../img/Pasted%20image%2020260203231531.png)

Secure: prove under definition of indistinguishability

### Proof by Reduction
**Modern Crypto = Definitions + Proofs + Assumptions**

> If G is a pseudorandom generator, then the pseudo one-time pad $\Pi$ is EAV-secure (computationally indistinguishable)

Assume G is a pseudorandom generator
Assume toward a contradiction that there is an efficient *attacker A* who breaks POTP, use A as a subroutine to build an efficient *distinguisher D* that breaks pseudorandomness of G   用D模拟PrivK给A
- If A runs in polynomial time, then so does D
- By assumption, not such D exists ==> No such A can exists
![](../img/Pasted%20image%2020260508032908.png)
Relate the *distinguishing gap of D* to the *success probability of A*
- By assumption, the distinguishing gap of D must be negligible ==> bound the success probability of A

> If G is a pseudorandom generator, then pseudo one-time pad $\Pi$ is EAV-secure (computationally indistinguishable)
![](../img/Pasted%20image%2020260204011447.png)

Reduce the security of the POTP to the security of the underlying G

![](../img/Pasted%20image%2020260204021402.png)
![](../img/Pasted%20image%2020260204014303.png)

![](../img/Pasted%20image%2020260204014426.png)
POTP 的破解优势不会比你能破解 PRG 的优势更大

The POTP has a key shorter than the message:
- n bit vs p(n) bits

![](../img/IMG_20260203_155548_edit_1510111022340134.jpg)
![](../img/IMG_20260203_155215.jpg)

More problem: smaller key, same key multiple encryption problem

## Security Against Chosen-Plaintext Attacks (CPA)
### Multiple-message Secrecy (MMS)
Parties share $k$; multiple $m_i$; encrypted under $k$
- Threat model: attacker observes multiple ciphertexts $c_i$
- Security goal: given $c_i$ attacker can not derive any information on any $m_i$

![](../img/Pasted%20image%2020260207005753.png)
在多条内容上使用相同的k加密
![](../img/Pasted%20image%2020260207005828.png)

构建vector0 两条相同的内容, vector1 两条不同的内容, 根据结果是否相同决定
![](../img/Pasted%20image%2020260207010842.png)
No **deterministic** encryption scheme is multiple-message indistinguishable

### CPA-security
> CPA is the minimal notion of security an encryption scheme should satisfy
> If $\Pi$ is CPA-secure ==> $\Pi$ is multiple-message indistinguishability

**Threat model**: attacker A can request encryption of any $m_i$ of his choice
- A is given access to an encryption oracle $E_k$
- A submits $m_i$ ==> obtains $c_i=E_k(m_i):i=1,2,\dots$
**Security goal**: given $c_i$ attacker cannot derive any information on $m_i$

![](../img/Pasted%20image%2020260207012425.png)
![](../img/Pasted%20image%2020260206232303.png)
A直接询问oracle m0和m1
> No deterministic encryption scheme can be CPA-secure
> Consider randomized scheme

### Pseudorandom functions (PRF)
Choosing $f$ uniformly at random **or** interacting with oracle $f$

For each $x\in\{0,1\}^n$, choose $f(x)$ uniformly in $\{0,1\}^n$
为每个需要的x: 
- 如果x已存在在表T中, 返回表T中对应的值$y$
- 如果x不存在, 返回一个均匀采样的$y\leftarrow\{0,1\}^n$并记录到T
- $|\mathcal F_n|=2^{n2^n}$

*Keyed functions*
![](../img/Pasted%20image%2020260207021258.png)
**Length-preserving**: $|k|=|x|=|F(k,x)|$, inputs and output of equal size

Choosing a uniform $k\in\{0,1\}^n$ is equivalent to choosing the function $F_k:\{0,1\}^n\rightarrow\{0,1\}^n$, naturally induces a distribution on functions from $\mathcal{F_n}$
![](../img/Pasted%20image%2020260207030405.png)
F是一族函数$\{F_k\}_{k \in \{0,1\}^n}​$, 每个k指向一个具体函数, 所以在完整的$\mathcal{F_n}$($2^{n2^n}$个)中选中k(至多$2^n$个, 取决于k长度)中函数的概率只有$2^{-n}$, only a tiny fraction

定义n长度uniform key的函数F，与从函数群选择一个uniform函数，产生的结果概率相等

![](../img/Pasted%20image%2020260207031654.png)
D can query $f$ and $F_k$ respectively on any input $x$ at most poly times
**The k must be unknown by D**

PRF is a PRG with random access to exponentially long output
- the function $F_k$ can be viewed as the $n2^n$-bit string
### Pseudorandom permutations (PRP)
![](../img/Pasted%20image%2020260207034423.png)

*Keyed Permutations*
![](../img/Pasted%20image%2020260207035758.png)

*Pseudorandom Permutation*
![](../img/Pasted%20image%2020260207035914.png)

> A random permutation is indistinguishable from a random function for large enough n
- In practice PRPs are also good PRFs

### CPA-secure encryption using PRF/PRP
![](../img/Pasted%20image%2020260210231858.png)
将随机数r引入，使掩码每次都不同，又使用相同的$F_k$使其可复原
r被同样发送，只有正确的k可以复原，解决重复加密问题
PRG生成的均匀随机

i.e. If encrypt multiple messages with same key, output
$$\forall m, m'\space\space Enc(k,m)\ne Enc(k,m')$$

> If $F$ is a pseudorandom function then $\Pi$ is CPA-secure

**Proof**
*Distinguisher D* that uses *attacker A* (towards $\Pi$) as a subroutine to attack the PRF $F$: 
- D tries to distinguish F from a random function
- D simulates to A the steps in the $PrivK^{cpa}_{A,\Pi}(n)$ experiment **for $\color{#f6fa99}\mathbf F$** and **for a RF**

![](../img/Pasted%20image%2020260210234250.png)
$A$ succeeds ==> $D$ succeeds ==> $F\ne$ PRF
$$\Pr_{k\leftarrow\{0,1\}}[D^{F_k(\cdot)}=1]=\Pr[PrivK_{A,\Pi}^{CPA}(1^n)=1]$$
Contradicts $F$ PRF ==> A can not succeed ==> $\Pi$ CPA-secure

**World 0: Truly Random Function $f$**
Security assuming $f$ (a random function) is never evaluated on the same input twice, except with negligible probability
- Clarification PDF: cpa-secure-encryption.pdf

重用r问题: the encryption is deterministic
![](../img/Pasted%20image%2020260508101735.png)
![](../img/Pasted%20image%2020260508101759.png)
A is PPT: can make at most $q(n)$ polynomial number or queries
As $r_c$ is chosen uniformly, it follows
在uniform随机下出现重复r的几率
$$Pr[\mathtt{Repeat}]=\frac{q(n)}{2^n}$$
$$Pr[\mathtt{\lnot Repeat}]=1-\frac{q(n)}{2^n}=1-negl\approx1$$
![](../img/Pasted%20image%2020260508102149.png)

**World 1: Pseudorandom Function**
![](../img/Pasted%20image%2020260508102651.png)

![](../img/Pasted%20image%2020260211025447.png)
![](../img/Pasted%20image%2020260211025459.png)

When $r$ is a uniform, n-bit string, the probability of a repeat is negligible

**Attacks**
- Nonce $r$ not used correctly
	- repeats, same with OTP multiple encryptions
	- too short
	- chosen from another distribution, repeats may happen
- $F$ not used correctly
	- plaintext leaked in ciphertext $\langle m,F_k(m)\rangle$
	- not used with a random, unknown key $\langle r,F_r(m)\rangle$

**Problems**
- 1-block plaintext ==> 2-block ciphertext
- OTP limitation 1: same length of encryption

![](../img/Pasted%20image%2020260211025557.png)

#### Block Ciphers and Stream Ciphers
Problem of encrypting long messages: ciphertext expansion by a factor of 2

*Mode of Operation (MO)*: Efficient mechanisms for encrypting arbitrary length messages
PRP/PRF ==> block cipher
PRG ==> stream cipher
##### Block Cipher MO
![](../img/Pasted%20image%2020260225004753.png)
AES: 128，192，256 bits key length and 128 bits block length
密钥不等长的加密: 实际部署中没有渐进的概念
$\mathcal{P}_m$空间里的随机置换(permutation)模式 $\{0,1\}^m\rightarrow\{0,1\}^m$, 双射可逆
能力十分接近$2^n$的对手(差$2^c$), 区分$F_k$和真随机置换的优势negligible

*ECB Mode*
![](../img/Pasted%20image%2020260224232519.png)
Deterministic ==> not CPA-secure, can tell whether $m_i=m_j$
仅改变了原本的值, 没有隐藏关系等side channel

*CTR Mode*
![](../img/Pasted%20image%2020260224232741.png)
If $F$ is a PRF, then CTR mode is CPA-secure
Ciphertext expansion: 1 block, the $ctr$ value 密文膨胀
![](../img/Pasted%20image%2020260508105333.png)

*CBC Mode*
![](../img/Pasted%20image%2020260224233443.png)
If $F$ is a PRP, then CBC mode is a CPA-secure
难以Dec，需要$F^{-1}(c_3)$逆运算
密文膨胀1 block, the IV value

*OFB Mode*
![](../img/Pasted%20image%2020260224233551.png)
![](../img/Pasted%20image%2020260225013133.png)
If $\mathbf F$ is a PRF, then OFB mode is CPA-secure
##### Stream Cipher MO
Practical realization of PRGs: expand $n$ to $p(n)$, produce all output at once
Producing an infinite stream of pseudorandom bits
![](../img/Pasted%20image%2020260224233730.png)
A5/3, Aslsa20 http://www.ecrypt.eu.org/stream/

## Security Against Chosen-Ciphertext Attacks (CCA)
Active attackers: interfering, modifying, injecting traffic on the channel
No more assume that the ciphertext can reach the receiver **unchanged**
- Receiver decrypts c' to m'$\ne$m and has no way of detecting the modification

*Malleability*: A scheme is malleable if it is possible modify a ciphertext cause **a predictable change to the plaintext** 在修改密文c后可以预测解密后的m如何变化, 修改成另一个"有意义"的密文
- a perfectly secret scheme may still be malleable: OTP flip last bit

*Injecting*: A impersonates the sender and injects its own ciphertext c', by forcing the receiver to decrypt c', A may learn something about m'

*Chosen-ciphertext Attacks (CCA)*
Models settings in which the attacker can influence what gets decrypted, and observe the effects

A is allowed to interfering and **modify** c to c', and forward c' to the receiver
- has access to both encryption and decryption oracle (sender and receiver)
- obtain the decryption of **any ciphertext of its choice**, beside the challenge ciphertext

![](../img/Pasted%20image%2020260225022146.png)
![](../img/Pasted%20image%2020260225022335.png)

CCA-security implies non-malleability: 对于目标密文c, 提交可预测的修改c'获得修改版明文m', 对m'反向应用修改获得c对应的m
![](../img/Pasted%20image%2020260508233236.png)

Scenario: one bit about decrypted ciphertexts is leaked, can be exploited to learn the entire plaintext

Padding oracle attack: 利用服务器返回的padding正确性报错, 

### Message Integrity
*Integrity*: ensures that a received message 来源&完整
- originated from the intended sender and
- was not modified
Security and integrity are orthogonal concerns

**Not concerned with secrecy, message m transmitted in the clear**
在Integrity条件下可以用明文传输
Passive Attacks (eavesdropping) ==> Active Attacks: attacker has full control over the channel

### Message Authentication Code (MAC)
![](../img/Pasted%20image%2020260227232051.png)
**Threat model**: *adaptive chosen-message attack*: assume the attacker can induce the sender to authenticate messages of the attacker's choice 攻击者可以使发送方认证任意消息, 除了挑战消息
**Security goal**: *existential unforgeability*: attacker should not be able to forge a valid tag on any message not previously authenticated by the sender 攻击者不能伪造任何发送方没有认证的消息认证

![](../img/Pasted%20image%2020260227232620.png)
![](../img/Pasted%20image%2020260227232706.png)
Secure MAC ==> infeasible to forage even a single message

*Replay attack*: A message from previous communication is captured and re-transmitted (replayed) at a later point in time 重新发送相同的内容
- MACs **do not prevent replay attacks**
- No stateless mechanism can prevent replay attacks
- application-dependent

#### Fixed-length MAC
![](../img/Pasted%20image%2020260228022020.png)
**Let Mac be a PRF**, set $Mac_k\equiv F_k$

> F is a PRF ==> $\Pi$ is a secure MAC

**Proof by Reduction**: Design distinguisher D, simulates to A the steps in the $\mathsf{Forge}_{A,\Pi}(n)$ experiment for F and for a RF
- relate the success Pr of A to the success Pr of D
- Contradicts F PRF ==> A cannot succeed ==> $\Pi$ is a secure MAC
![](../img/Pasted%20image%2020260227234028.png)

![](../img/Pasted%20image%2020260228024344.png)

![](../img/Pasted%20image%2020260228024752.png)
![](../img/Pasted%20image%2020260228024608.png)
![](../img/Pasted%20image%2020260228024738.png)

#### Variable-length MAC
Break a long message into multiple fixed length string and do fixed-length MAC respectively

Prevent: 
- Block reordering
- Truncation
- Mixing-and-matching blocks from multiple messages

*Basic CBC-MAC*
![](../img/Pasted%20image%2020260228025313.png)
No IV (no need randomized to be secured), 不需要逆运算, Deterministic, verification done by re-computing the result (only output)

> If F is a length-preserving PRF with input length $n$, then for any fixed $l$ basic CBC-MAC is a secure MAC for messages of length $ln$

The sender and receiver must agree on the length parameter $l$ in advance, **Basic CBC-MAC is not secure if this is not done**! 需要提前确定分组数$l$
分组数不符会导致长度扩展攻击，构造一个相同tag的内容

Adversary query $T_A=E_k(A)$ and $T_B=E_k(B)$ then **forge** $M_{forge}=A|(B\oplus T_A)$
![](../img/Pasted%20image%2020260509022936.png)

![](../img/Pasted%20image%2020260228032147.png)

### Hash Functions
> Deterministic function mapping arbitrary length inputs to a short, fixed-length output (a digest)

*Collision-resistance*
![](../img/Pasted%20image%2020260303233128.png)

**Collisions are guaranteed to exist**
Best **Generic collision attack** on a hash function $H:\{0,1\}^*\rightarrow\{0,1\}^l$ ==> brute force

*Birthday attack*: compute $H(x_1)\dots H(x_k)$, what is the probability of a collision (function of k)
The collision probability is $\mathcal{O}(k^2/N)$
- N is the enumeration space
- take k samples (k time hashes)
When $k\approx \sqrt{N}$, probability of a collision is $\approx 50\%$
**$k\approx\sqrt{2^l}$ hash-function evaluations**

> 攻击者通常只需要找到**任意两个**能产生相同哈希值的输入即可伪造签名或破坏完整性。
> To protect against attackers running in time $2^n$ we need the output of our hash function to be l = 2n  需要两倍密钥长度来保证安全
- To ensure 128 bit security we need a block cipher with 128 bit key and a hash function with 256 bit output

**The birthday bound $k\approx2^{n/2}$**  $2^n$密钥空间下理论最多支持k次查询满足collision-resistance
- CTR-mode IV reuse

#### Hash function building
Fixed-length inputs hash $h$, a *compression function* 定长哈希函数h
Hash function $H$, arbitrary length inputs based on $h$ 基于h的变长哈希函数H

> If $h$ is collision-resistance, then so is $H$

*Merkle-Damg ̊ard Transform*
![](../img/Pasted%20image%2020260304071835.png)
当$H$中发生碰撞时$H(m_1\dots m_B)=H(m_1'\dots m_B')$
- 两条消息长度不同, 则最后一个块$m_{B+1}=|M|$绝对不相等, 则在最后一个在$h$是collision-resistance情况下, 最后一个$h$的输入不相等而输出相等是不存在的
- 两条消息长度相同, 则寻找最大的索引$i$位置的$h$, 满足输入不同$(z_{i-1},m_i)\ne(z_{i-1}',m_i')$但输出相同, 在$h$ is collision-resistance的情况下同样不存在

（长度扩展攻击问题）

*Compression function*
![](../img/Pasted%20image%2020260303234852.png)
用消息块作为密钥, 内部状态作为被加密的明文
使用feedforward来完成哈希函数**单向不可逆**的特性, (分组密码是可逆的), 就算明文是已知的也uninvertable 

SHA-256: Merkle-Damgard + Davis-Meyer + Block cipher (SHACAL-2)
- $H_i$:256 bits; $M_i$: 512 bits
SHA-1, MD5: broken
SHA-2 (use M-D transform), SHA-3/Keccak (not use M-D transform)
- 224, 256, 384, 512-bit outputs

### Hash-and-MAC
Use hash functions to construct a secure MAC for arbitrary-length messages
- MAC: a reliable short messages channel
- 通过MAC传输hash value, 是可信的且长度固定的
![](../img/Pasted%20image%2020260509064735.png)

![](../img/Pasted%20image%2020260304074116.png)

*HMAC*
For matching block-length, need to implement two crypto primitives
- block cipher and hash function

A practical instantiation of the Hash-and-MAC paradigm, with (part of) the hash function being used as a PRF

![](../img/Pasted%20image%2020260304074555.png)
$$HMAC_K(M) = H((K \oplus \text{opad}) \parallel H((K \oplus \text{ipad}) \parallel M))$$
**randomness should never be reused or correlated**

## Authenticated Encryption
**Combined secrecy and integrity**
- Secrecy: PRF/block cipher in a mode of operation
- Integrity: MAC

### Encrypt-and-Authenticate (E-and-A)
![](../img/Pasted%20image%2020260307010900.png)
- 使用的MAC是deterministic，则**不CPA-secure**，相同的明文生成的tag会完全相同，与加密算法无关
- MAC使用直接暴露明文的scheme，则**不EVA-secure**
	- $MAC’_k(m)=(m,MAC(m))$ 依然是安全MAC

### Authenticate-then-Encrypt (A-then-E)
![](../img/Pasted%20image%2020260307011359.png)
没有指定使用的MAC和Enc scheme
受到*Oracle Padding Attack*，则**不CCA-secure**
![](../img/Pasted%20image%2020260307012325.png)
![](../img/Pasted%20image%2020260307012344.png)
![](../img/Pasted%20image%2020260307024250.png)
流式密码允许攻击者通过翻转密文位来精准改变解密后的结果 (malleable), 打破了authenticate带来的integrity属性. Oracle需要先解密再验证MAC，在解密时攻击方通过服务器的Padding错误返回信息, 获得有利消息，**直接获取明文**
padding：有冗余位，多携带了信息，将其利用作为错误返回的指示
authenticate没有起作用，直接获取了明文

### Encrypt-then-Authenticate (E-then-A)
![](../img/Pasted%20image%2020260307014536.png)
*CCA-secure Scheme*: E和A二者相互独立，互不影响 ($k_1$ and $k_2$ must be independent)
- CPA-secure encryption scheme to encrypt the message
- MAC to prevent the ciphertext from being modified

Stronger notion than CCA
- The MAC is applied on the ciphertext produced by the sender: the adversary is not able to obtain any valid ciphertext that was not generated by the legitimate parties
- CCA-security中adversary可以使用chosen ciphertexts访问decryption oracle的特性失去作用，因为**接收方会先验证MAC**，一切修改c为c'再询问oracle的操作无法通过authentication，无法返回有效的结果
- 直接隔离oracle padding attack的可能性

**Authenticated Encryption (AE) scheme**
Given ciphertexts $(c_1,t_1),(c_2,t_2),\dots$ corresponding to (chosen) plaintexts $m_1,m_2,\dots$, it is infeasible for an attacker to generate any new valid ciphertext $(c,t)$.
- The decryption oracle will output an error


> If the underlying encryption scheme is CPA-secure and the MAC is secure (i.e. existentially unforgeable) then the E-then-A combination is an AE  scheme

Using any CPA-secure scheme + any secure MAC to construct an AE scheme
OCB, CCM, GCM

![](../img/Pasted%20image%2020260307031008.png)
![](../img/Pasted%20image%2020260307031018.png)

# Public Key Cryptography
## Number Theory and Cryptographic Hardness Assumptions
### Modular Arithmetic
![](../img/Pasted%20image%2020260307042736.png)
模空间下的加法和乘法一样

If for a given integer `b` there exists an integer `c` such that $\color{#b293f6}bc = 1~mod~N$, we say that `b` is *invertible modulo* `N` and call `c` a *multiplicative inverse* of `b` modulo `N`.  b是在模N空间下可逆的, c是b在模N空间下的乘法逆元(逆运算)

`c mod N` is *unique multiplicative inverse* of `b` that lies in the range $\{1,\dots,N-1\}$ and denoted $\color{#b293f6}b^{-1}$   c mod N是b在模N空间下的唯一逆元

If $ab = cb$ mod N and b is invertible, then we have that 可逆可消
$$(ab) \cdot b^{−1} = (cb) \cdot b^{−1}\bmod N ⇒ a = c\bmod N$$

> Let b, N integers with $b \ge 1$ and $N \gt 1$. Then b is invertible module N if and only if $gcd(b, N)=1$  充要条件: b和N互质

![](../img/Pasted%20image%2020260509170136.png)

### Groups
A group is a set $\mathbb{G}$ along with a binary operation $\circ$ for which the following conditions hold:
- *Closure*: For all $g, h \in \mathbb{G}$, $g\circ h\in \mathbb{G}$
- *Existence of identity*: There exists an **identity** element $e\in\mathbb{G}$ such that for all $g\in\mathbb{G}$, $e\circ g=g=g\circ e$   存在单位元 1 运算后保持原样
- *Existence of inverse*: For all $g\in\mathbb{G}$ there exists an element $h\in\mathbb{G}$ such that $g\circ h=e=h\circ g$. Such an $h$ is called an **inverse** of $g$  存在唯一逆元
	- the inverse $h$ of $g\in\mathbb{G}$ is unique
- *Associativity*: For all $g_1, g_2, g_3 \in\mathbb{G}$, $(g_1\circ g_2)\circ g_3=g_1\circ(g_2\circ g_3)$  结合律

A group $\mathbb{G}$ with operation $\circ$ is *abelian* if the following holds:
- *Commutativity*: For all $g, h\in\mathbb{G}$, $g\circ h=h\circ g$ 交换律

A set $\mathrm{H}\subseteq\mathbb{G}$ is a **subgroup** of $\mathbb{G}$ if itself forms a group under the same operation associated with $\mathbb{G}$  子群拥有相同的特性

If $\mathbb{G}$ is **finite** if it has finite number of elements.
The number of elements is the **order** of $\mathbb{G}$, denoted by $|\mathbb{G}|$

#### Examples
The set {0, . . . , N − 1} with respect to addition modulo N is an abelian group of order N with identity 0. The inverse of k is $(N − k)\bmod N$. We denote this group by $\mathbb{Z}_N.$

The set of **invertible elements** modulo N is an abelian group under multiplication with identity 1. Namely, $$\mathbb{Z}_n^*\overset{def}{=}\{b\in\{1,\dots,N-1\}|gcd(b,N)=1\}$$模N下所有**可逆元素**组成的集合
- Inverse of $b$: use **extended Euclidean algorithm** to find $x,y$ such that $bx+Ny=gcd(b,N)=1$. Then $x\bmod N$ is the inverse of b modulo N.
- Closure: let $a,b\in\mathrm{Z}_N^*$. Then $(ab)\bmod N$ has inverse $(b^{-1},a{-1})\bmod N$ so $ab\in\mathbb{Z}_N^*$

Special case: for prime p, it holds that 质数p与所有元素都互质$$\mathbb{Z}_p^*=\{1,2,\dots,p-1\}$$
If $\mathbb G$ is abelian, then $g^m\cdot h^m=(g\cdot h)^m$
Let $\mathbb{G}$ be a finite group with $m=|\mathbb{G}|$. Then for every element $g\in\mathbb{G}, g^m=1$
![](../img/Pasted%20image%2020260307163031.png)

Let $\mathbb{G}$ be a finite group with $m=|\mathbb{G}|\gt1$. Then for every element $g\in\mathbb{G}$ and every integer $x$, we have $g^x = g^{x \bmod m}$
在指数运算中，指数是可以用群的阶 $m$ 来取模的，即 $g^x = g^{x \bmod m}$
![](../img/Pasted%20image%2020260307074637.png)

![](../img/Pasted%20image%2020260307074337.png)

The *order of element* ==> subgroup of $\mathbb{G}$
元素$g\in\mathbb G$的order: 以g的次方在$\mathbb G$下的遍历 => 子群的order
Must divisible to $|\mathbb{G}|$  拉格朗日定理: 元素的阶必然能整除群的阶
![](../img/Pasted%20image%2020260307074656.png)

$\mathbb{G}$ is *cyclic* if it has *generator* that generates all elements of $\mathbb{G}$
$g^x\in\mathbb{G}$
生成的子群等于整个群, 生成元的order=$\mathbb G$的order 
![](../img/Pasted%20image%2020260307163647.png)

Group with prime order $p$ is cyclic group, all elements are generators
素数阶群一定是循环群, 且除了单位元以外的所有元素都是生成元
![](../img/Pasted%20image%2020260307174643.png)

### The discrete logarithm problem
Let $\mathcal{G}$ denote a generic PPT group generation algorithm
- input $1^n$ outputs a description of a cyclic group $\mathbb{G}$
- order $q$
- generator $g\in\mathbb{G}$
For every $h\in\mathbb{G}$ there is a **unique** $x\in\mathbb{Z}_q$ such that $g^x=h$, we call $x$ the *discrete logarithm* of $h$ with respect to $g$ 离散对数
- $g^x=h$ ==> $log_g~h$

![](../img/Pasted%20image%2020260311011625.png)

> We say that discrete logarithm problem is hard relative to $\mathcal{G}$, if for all PPT adversaries $\mathcal{A}$, it holds that $$Pr[\mathsf{DLog}_{\mathcal{A,G}}(n)=1]\le negl(n)$$

### The computational Diffie-Hellman problem
![](../img/Pasted%20image%2020260311011640.png)

> We say that the CDH problem is hard relative to $\mathcal{G}$, if for all PPT adversaries $\mathcal{A}$, it holds that $$Pr[\mathsf{CDH}_\mathcal{A,G}(n)=1]\le negl(n)$$

### The decisional Diffie-Hellman problem
![](../img/Pasted%20image%2020260311012418.png)

> We say that the DDH problem is hard relative to $\mathcal{G}$ if for every PPT adversary $mathcal{A}$, it holds that $$|\Pr[\mathcal{A}(\mathbb{G},q,g,g^x,g^y,g^z)=1]-\Pr[\mathcal{A}(\mathbb{G},q,g,g^x,g^y,g^{xy})=1]|\le negl(n)$$, where in each case the probabilities are taken over the experiment $\mathsf{DDH}_\mathcal{A,G}(n)$

> ***Large prime order subgroups of $\mathbb Z_p^*$, where $p$ prime, are believed to be safe.

![](../img/Pasted%20image%2020260311013918.png)
选$\mathbb Z_p^*$里的**大素数阶子群**。
![](../img/Pasted%20image%2020260311035134.png)
$r$ 必须是 $p-1$ 的因数
当$p=2q+1$ (r=2)时, 会得到一个阶正好为q的子群
![](../img/Pasted%20image%2020260311060215.png)
## Key Exchange and the Diffie-Hellman Protocol
**An interactive protocol**: $k_A=k_B=k$
![](../img/Pasted%20image%2020260311070248.png)

> A key-exchange protocol $\Pi$ is secure in the presence of an **eavesdropper** if for every PPT adversary $\mathcal A$, it holds that $$Pr[\mathsf{KE}_{\mathcal A,\Pi}^{\mathsf{eav}}(n)=1]\le\frac{1}{2}+negl(n)$$

### The Diffie-Hellman key-exchange protocol
![](../img/Pasted%20image%2020260311071025.png)

![](../img/Pasted%20image%2020260311071039.png)

**Proof**
Considering the experiment $\widehat{\mathsf{KE}}_{\mathcal A,\Pi}^{\mathsf{eav}}$, the adversary $\mathcal A$ is given $(\mathbb G,q,g,h_A=g^x,h_B=g^y,\hat k)$, where $\hat k$  is either the actual key $k^{xy}$ (b=0) or a uniform group element (b=1)
A需要区分$\hat k$是key $g^{xy}$而不是随机群元素

> If the DDH problem is hard relative to $\mathcal G$, then the Diffie-Hellman key-exchange protocol is secure in the presence of an eavesdropper

![](../img/Pasted%20image%2020260311073351.png)

Active attacks: man-in-the-middle attack
- able to modifying messages

## Hybrid proof
![](../img/Pasted%20image%2020260312031514.png)
![](../img/Pasted%20image%2020260312031657.png)

## Public-key Encryption
![](../img/Pasted%20image%2020260510035357.png)
*Correctness*: For any message M, we have that $\mathsf{Dec}_{sk}(\mathsf{Enc}_{pk}(M))=M$ except with negligible probability over $(pk,sk)$ output by $\mathsf{Gen}(1^n)$

Parties can communicate securely without having agreed on any secret information in advance
- only the secrecy of the private key $sk$ is required
- every one who know the $sk$ public key can encrypt

Against CPA attacks: 在公钥密码体系中, EAV和CPA在能力上完全等价
- 公钥pk是完全公开的 (当然算法也是), 其本身就是一个encryption oracle
![](../img/Pasted%20image%2020260313234146.png)
![](../img/Pasted%20image%2020260313234231.png)

## El Gamal encryption
![](../img/Pasted%20image%2020260313234747.png)
![](../img/Pasted%20image%2020260313234757.png)

![](../img/Pasted%20image%2020260314014557.png)
虽然 $M$ 是固定的，但因为 $k$ 是完全随机的，所以乘出来的结果 **$k'$ 也会在整个群 $\mathbb{G}$ 中呈现绝对的均匀随机分布**
![](../img/Pasted%20image%2020260314014853.png)
在群中，随机选一个k等于一个固定值的概率就是$\frac{1}{|\mathbb G|}$
群论one-time pad

在Enc中使用$<g^y,g^z\cdot m>$, 则结果m是完全随机的内容 $$\Pr[\mathsf{PubK}_{\mathcal A,\tilde\Pi}^{\mathsf{eav}}(n)=1]=\frac{1}{2}$$又, 正常Enc$<g^y,g^{xy}\cdot m>$ $$\Pr[\mathsf{PubK}_{\mathcal A,\Pi}^{\mathsf{eav}}(n)=1]=\Pr[\mathcal{A}(\mathbb{G},q,g,g^x,g^y,g^{xy})=1]$$所以 $$\Pr[\mathsf{PubK}_{\mathcal A,\Pi}^{\mathsf{eav}}(n)=1]\le\frac{1}{2}+\mathsf{negl}(n)$$

![](../img/Pasted%20image%2020260510143642.png)
![](../img/Pasted%20image%2020260510143650.png)
![](../img/Pasted%20image%2020260510143700.png)
![](../img/Pasted%20image%2020260510143708.png)
![](../img/Pasted%20image%2020260510143718.png)
![](../img/Pasted%20image%2020260510143746.png)

#### CCA
![](../img/Pasted%20image%2020260510143823.png)

**Malleability of El Gamal**
you can do operation with different calculation
![](../img/Pasted%20image%2020260318023701.png)
When the adversary is able to access the decryption oracle
**Not CCA-secure**
### RSA
![](../img/Pasted%20image%2020260318024825.png)

![](../img/Pasted%20image%2020260318025530.png)
找到与$\phi(N)$互质的元素e
- 对于$x\in\mathbb Z_N^*$, $x^e$是随机的元素permutation
- 一定存在逆元$d=e^{-1}\bmod \phi(N)$, 可以用于恢复密文

*Euler's Theorem*: if $M$ and $N$ are coprime, then $$M^{\phi(N)}=1\bmod N$$
N是质数, 其空间$\mathbb Z_N^*$下所有数即都和它互质, 包括信息$M$
RSA is deterministic, therefore it **not CPA-secure**

## Digital Signatures
### Random Oracles
Take some input, it outputs looking random
$$H:\{0,1\}^*\rightarrow Y$$
*Consistent*: if a question is repeated, the random oracle must return the same answer
> If a scheme is secure assuming the adversary views some hash function as a random oracle, it is said to be secure in the **Random Oracle Model**

$(M,t)\in\mathsf{History}$ for $t\xleftarrow{\$} Y$

Not available in the real world
![](../img/Pasted%20image%2020260321013701.png)


Oracle: Adversary cannot really access except input and output

Reduction can observe the scheme, and fully control its distribution of output

Better in formal justification than no proof

### Digital signature
- A *signer* S has a unique private signing key and publishes the corresponding public verification key
- S signs a message M and everyone who knows the public key can verify that M originated form the signer S

$\mathsf{Gen}(1^n)\gets(sk, vk)$ 
$\mathsf{Sign}(sk,M)=\sigma$
$\mathsf{Verify}(vk,M,\sigma) = 1$ if signature is valid, 0 otherwise

![](../img/Pasted%20image%2020260321015052.png)
![](../img/Pasted%20image%2020260321015038.png)
The digital signature scheme(Gen,Sign,Verify) has **existential unforgeability under adaptive chosen message attacks** (EUF-CMA) if for every PPT adversary0 $\mathcal A$, it holds $$\Pr[\text{Game}_{EUF-CMA}^{\mathcal A^{\mathsf{Sign}}}(1^n)=1]\le\mathsf{negl}(n)$$
A无法得知oracle内部的工作方式

**Trapdoor One-way Function (TOWF)**
- Easy to compute
- Hard to invert
- Easy to invert *with trapdoor*
Only success if having trapdoor $z$
![](../img/Pasted%20image%2020260321015705.png)

![](../img/Pasted%20image%2020260321020619.png)

**Correctness**
![](../img/Pasted%20image%2020260321021130.png)

**Unforgeability**
![](../img/Pasted%20image%2020260321021847.png)
> 任何“会伪造签名的人”，都能被改造成“会求 $f_e$​ 原像的人”。所以如果 $f_e$​ 真的是 one-way function，那么伪造签名的人就不该存在。

![](../img/Pasted%20image%2020260325002721.png)
B 来对A伪装Sign和H

![](../img/Pasted%20image%2020260321024041.png)
> 伪造签名，本质上就是给某个哈希值找原像；而 random oracle 允许 reduction 把这个哈希值编程成 one-way challenge，因此签名伪造者就能被转化成 one-way inverter。

creates a forgery
A: adversary of signature scheme
B: forgery of OWF scheme

**Conditional Independency**
$$\Pr[A\land B|C]=\Pr[A|C]\Pr[B|C]$$

adversary is success and B guess the index correctly
adversary never query the signing oracle
$$f_e(\sigma')=H(m')$$
whenever adversary query the G

![](../img/Pasted%20image%2020260325005506.png)

B有一个来自挑战者的y
B用random oracle模拟A对H的查询
B选中一个j来将A的查询模拟成$H(M^*)=y$
如果A最终问了Sign(M, y)，则模拟失败，因为A不能问正确的y
通过猜中A最终伪造消息对应的那次哈希查询，把伪造签名转化为y的preimage
![](../img/Pasted%20image%2020260325010515.png)

## Zero-Knowledge Interactive Proofs
**Two parties proof**
- *prover* (Merlin): has unbounded resources
- *verifier* (Arthur): has limited resources
![](../img/Pasted%20image%2020260327231407.png)
$x$ is an NP statement and $\pi$ is its certificate/witness/proof

*Graph Isomorphism*
![](../img/Pasted%20image%2020260328021149.png)

*Interactive Prove*: 
A proof is described as as a game between a *prover* and a *verifier*
- the theorem is true if and only if the prover wins the game always
- if the theorem is false then the prover loses the game with 50% probability

两支笔的颜色不相同：prover回答verifier的是否交换（做随机挑战） == > 如果颜色相同则prover获胜的概率一定小于50%

*Graph Non-Isomorphism*
![](../img/Pasted%20image%2020260328024022.png)
![](../img/Pasted%20image%2020260328023841.png)
![](../img/Pasted%20image%2020260328025720.png)
![](../img/Pasted%20image%2020260328025733.png)

*Zero-Knowledge*: leakage only one bit ==> 1 if the theorem is true and 0 otherwise, **not disclose the witness**

**ZK Graph Isomorphism** 证明同构的同时不泄漏映射
![](../img/Pasted%20image%2020260328041221.png)
verifier只看到C，一个随机同构副本，不是G也不是H
挑战只让prover证明，其中之一
- C和G同构
- C和H同构

*Simulator* 在没有witness的情况下，为造出看起来像真实交互的transcript
$P(x,w)\rightarrow S(x)$ with no leakage of $w$
- knows only that theorem x is true
- is efficient
- generates a transcript that is distributed similarly to the real one (when the verifier is honest), simulator & process ideally same
- has black-box access to the adversary

**Honest-Verifier Zero-Knowledge (HVZK)** 诚实验证者零知识
- 不考虑恶意偏离协议的verifier
- verifier看到的东西，可被模拟
- 真实执行和模拟执行都只围绕 C which a random permutation of G

### Sigma protocols
1. prover发送commitment/首消息 $a$
2. verifier发送random challenge $c$
3. prover发送response $z$

**Completeness**: 如果prover确实知道witness $w$, 那它总能生成让verifier 接受的$(a,c,z)$
**HVZK**: 存在simulator $HVZK_{Sim}(x)$ 或更强的 $SHVZK_{Sim}(x,c)$ (special), 能在不知道witness 的情况下, 生成与真实transcript 相似的三元组
**Special Soundness**: 

CCA-encryption scheme
Multi-party computation
Identification schemes
Privacy-preserving blockchains