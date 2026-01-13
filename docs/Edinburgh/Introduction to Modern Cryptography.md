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