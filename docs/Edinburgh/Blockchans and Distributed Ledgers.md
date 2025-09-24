Distributed database that satisfies a unique set of safety and liveness properties

![](../img/Pasted%20image%2020250917185342.png)
Hash Functions: Produce a fingerprint of a file
- SHA-256 for bitcoin
Collision resistance: find a `y` for given `x` that **H(x) = H(y)**

Pre-image attack 
One-way functions: P != NP

Digital Signatures, producesd by one specified entity
- depend on the file signing
Algos
- KeyGen: input security parameter --> signing-key, verificatoin-key
- Sign: sign the message with signing-key
- Verify: message and signature, varification-key

global matching
![](../img/Pasted%20image%2020250917195126.png)

#### Verifications
File transfer and cloud storage: Authenticated protocols
- Don't trust, verify!

Hash-based vs Digital signature-based

*Merkle Trees*
- Binary, binary full and binary complete
- An authenticated binary tree

1. Split file into small chunks
2. Hash each chunk using a cryptographic hash function
3. combine them by two to create a binary tree, each node stores the **hash of the concat** of its children
![](../img/Pasted%20image%2020250924183843.png)

Client sends file data D to server  
Client creates Merkle Tree root MTR from initial file data D  
Client deletes data D, but stores MTR (32 bytes)
Client requests chunk x from server  
Server returns chunk x and short proof-of-inclusion π  
Client checks whether proof π of chunk x is correct w.r.t. stored MTR
![](../img/Pasted%20image%2020250924185712.png)

*Tries* (radix tree, prefix tree)
- ordered data structre
- store an associative array
- keys are usually strings
- two operations: *add(key, value)*, *query(key)* -> value

*Patricia* tree: An isolated path, with unmarked nodes which are *only children*, is merged into single edge, the label is teh concat of the labels merged

*Merkle Patricia trie*: authenticated  Ethereum
![](../img/Pasted%20image%2020250924191533.png)

#### Transactions
![](../img/Pasted%20image%2020250924195359.png)

![](../img/Pasted%20image%2020250924195441.png)

Each block contains a coinbase, only have outputs

*gossip* protocol: peer to peer diffusion

Eclipse attacks: isolate some hosest nodes in the network, effectively causing a network aplit in two partitions A and B