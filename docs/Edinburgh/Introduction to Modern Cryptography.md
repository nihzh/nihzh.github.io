Proof something is secure
> The art of making and breaking secret codes

## Introduction
*Private-key (SK)*: Message authentication codes
*Public-key (PK)*: Digital signatures

**Private-key (symmetric-key) encryption**
![](../img/Pasted%20image%2020260113233346.png)

*Kerckhoffs's principle*: The encryption scheme is not secret
- The attacker knows the encryption scheme
- The only secret is the key
- The key must be chosen at random; to kept secret

*Modular arithmetic*  同余&取模运算
![](../img/Pasted%20image%2020260113234130.png)

*Byte-wise Shift Cipher*
- Alphabet of bytes rather than English letters
- Use XOR instead of modular addition (reversible)
![](../img/Pasted%20image%2020260113235129.png)

The key space must be large enough to make brute-force attacks impractical

Shift Cipher
### Vigenere Cipher
**Index of Coincidence**
![](../img/Pasted%20image%2020260116232932.png)
![](../img/Pasted%20image%2020260116233042.png)

**Finding the key length**
![](../img/Pasted%20image%2020260116233716.png)
Natural English Language IC: 0.065
Random IC: 0.038

![](../img/Pasted%20image%2020260117002840.png)
$$26L+26^2L\approx26^2L\ll26^L$$

## Secure Encryption
*Three principles of modern cryptography*
- Definitions: Precise, mathematical model and formal definition of what security means
- Assumptions: Clearly stated and unambiguous
- Proofs: Prove security and move away from design-break-patch

**Goal**: What we want to prevent the attacker from achieving
**Threat model**: What capabilities the attacker is assumed to have

> Regardless of any prior information the attacker has about the plaintext, the ciphertext should leak no additional information about the plaintext
> **加密后的密文不应该让攻击者在这些知识基础上得到任何新增优势**。

### Perfect Secrecy
*Random variable (RV)*: variable that takes on discrete values with certain probabilities

*Probability distribution (PD)*: A PD for a RV specifies the probabilities with which the variable takes on each possible value
- Each between 0 and 1
- Probabilities sum to 1

![](../img/Pasted%20image%2020260120231622.png)
![](../img/Pasted%20image%2020260120231644.png)

$$\sum_iP[A|E_i]\cdot P[E_i]=P[A]=\sum_i[E_i\land a]$$
$$P[A|B]=\frac{P[A\land B]}{P[B]}$$

Shift cipher 拥有固定的密文模式，从Chosen Ciphertext攻击中反推明文

*Perfect Secrecy*
![](../img/Pasted%20image%2020260120233941.png)
每个加密后字符拥有同样的概率对应明文的每个字符

*Bayes's theorem*
$$Pr[A|B]=\frac{Pr[B|A]Pr[A]}{Pr[B]}$$
![](../img/Pasted%20image%2020260120234546.png)

### One-time Pad
![](../img/Pasted%20image%2020260120234752.png)
**The One-time Pad satisfies perfect secrecy**
- Any observed ciphertext can correspond to any message
- Having observed a ciphertext, the attacker cannot conclude for certain which message was sent
