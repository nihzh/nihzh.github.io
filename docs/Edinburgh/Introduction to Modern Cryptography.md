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

## Secure Encryption
*Three principles of modern cryptography*
- Definitions: Precise, mathematical model and formal definition of what security means
- Assumptions: Clearly stated and unambiguous
- Proofs: Prove security and move away from design-break-patch

> Regardless of any prior information the attacker has about the plaintext, the ciphertext should leak no additional information obout the plaintext