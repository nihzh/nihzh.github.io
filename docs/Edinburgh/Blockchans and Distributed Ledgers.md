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

##### Merkle Tree
- Binary, binary full and binary complete
- An authenticated binary tree;
- *BitTorrent*, to verify exchanged files
- *Bitcoin*, to store transactions

1. Split file into small chunks
2. Hash each chunk using a cryptographic hash function
3. combine them by two to create a binary tree, each node stores the **hash of the concat** of its children
![](../img/Pasted%20image%2020250924183843.png)

**Merkle tree-based file stroage (sets of keys) protocol**
Client sends file data `D` to server  
Client creates Merkle Tree root `MTR` from initial file data `D`  
Client deletes data `D`, but stores `MTR` (32 bytes)

Client requests chunk `x` from server
Server returns chunk `x` and short proof-of-inclusion `π`  
Client checks whether proof `π` of chunk `x` is correct w.r.t. stored `MTR`

**Proof-of-inclusion**
1. Prover sends chunk
2. Prover sends **siblings** along path connecting leaf to `MTR`
3. Verifier computes hashes along the path connecting leaf to `MTR`
4. Verifier checks that computed root is equal to `MTR`
![](../img/Pasted%20image%2020250924185712.png)

**Proof of non inclusion for x**
Show proof-of-inclusion for previous `H<` and next `H>` element in set
- proof-of-inclusion is correct
- they are adjacent in tree
- `H<` < `x` and `H>` > `x`
![](../img/Pasted%20image%2020250924192326.png)


##### Tries
(radix tree, prefix tree)
- ordered data structre
- store an associative array
- keys are usually strings

Initialize with empty root, two operations
- *add(key, value)*
- *query(key)* -> value

*Patricia trie*: An isolated path, with unmarked nodes which are *only children*, is merged into single edge, the label is teh concat of the labels merged
![](../img/Pasted%20image%2020250924192632.png)

*Merkle Patricia trie*
First implemented in Ethereum, for storage and transactions

Split nodes into three types
- *Leaf*: stores edge string leading to it, and **value**
- *Extension*: Stores **string** of a single node, **pointer** to next node, and **value** if node marked
- *Branch*: Stores one **pointer** to another node per alphabet symbol, and **value** if node marked

In Ethereum, 
- Encode keys as hex, alphabet size is 16
- Encode all chold edges in every node with some encoding like JSON

![](../img/Pasted%20image%2020250924191533.png)

### Blockchain
Each block references (hash to) a previous block
A list of transactions
**Arrows show authenticated inclusion**

#### Blocks
![](../img/Pasted%20image%2020250925000907.png)
- nonce (ctr): used to solve proof-of-work
- data (x)
	- in Bitcoin: financial data (`UTXO`-based)
	- in Ethereum: contract data (account-based)
- reference (s): pointer to the previous block by **hash**

Block validity: data valid (defined by application)

Proof-of-work equation, the value known as the **blockid**
![](../img/Pasted%20image%2020250925001319.png)
- `T`: protocol-parameter

![](../img/Pasted%20image%2020250925002908.png)

**Digital Signature Scheme**
- KeyGen(security_parameter) ==> <sk, vk>
	- signing/private key
	- verification/public key
- Sign<sk, m> ==> σ
	- m: message
	- σ: signature
- Verify<vk, m, σ> ==> {True, False}
#### Transactions
- Input: a proof of spending an existing UTxO
- Output: a varification procedure and a value
![](../img/Pasted%20image%2020250924195359.png)
Each block contains a coinbase, only have outputs
coinbase 的 outputs 定义了谁能拿到矿工奖励以及如何花这笔钱

![](../img/Pasted%20image%2020250924195441.png)

#### Bitcoin network
Each node connected to a common p2p network to its (network) neighbours, runs the Bitcoin protocol (open source code)

Each node can freely enter the network, no permission needed

***So, there is no trust placed on any specific node or participant, anyone individually mayulie***

**Peers**
Each node stores a list of peers (IP), when Alice connects to Bob, Bob sends Alice his own known peers, Alice can learn about new peers

"Known peers" can be extra specified when running a node

*gossip protocol*: peer to peer diffusion, when recieves some unfamiliar data, **broadcast** it, until whole network learns it

*Eclipse attacks*
Isolate some **hosest nodes** in the network, effectively causing a network split in two partitions A and B. If peers in A and peers in B are disjoint and don't know about each other, the ntworks will remain isolated
- ***liveness favoring operation***
被孤立的节点只能看到攻击者转发/伪造的消息，从而被驱动做出对攻击者有利的行为如：接收伪造的区块、丢失真实交易、执行双花等

*The connectivity assumption*
- There is a path between two nodes on the network
- If a node broadcasts a message, every other node **will** learn it

## Smart contract
A contract is a legally binding agreement that defines and governs the rights and duties between or among its parties

*Bitcoin Script*
- stack-based
- Notation: <>, data in the script
- Opcodes: commands for functions

![](../img/Pasted%20image%2020251001181934.png)


## Ethereum
Global state: accounts
- personal accounts
- contract accounts
![](../img/Pasted%20image%2020251001184221.png)

![](../img/Pasted%20image%2020251001184324.png)
Signature: sender's private key

Extra block of data about the contract

Create -> Interact -> Destroy

Can only send transactions when other transactions received

*Message*: a transaction except it is produces by a contract

Ethereum Virtual Machine
- A quashi Turing complete machine

*Gas*: Every computationn step has a fee, unit in gas
![](../img/Pasted%20image%2020251001193138.png)
startgas & gasprice block
- all unused gas is refunded
- gas (price) raised determines how quickly a transaction will be included in a block

### Solidity
A high level programming language for writeing smart contracts on Ethereum, compile code for the *Ethereum Virtual Machine*
- look like classes
- Statically typed language

`pragma solidity ^0.8.1`enable certain compiler (version) features or checks

```solidity
contract <ContractName> {
	constructor (uint x, ...) { ... }
	
	address owner;
	address payable anotherAddress;
	
	enum State {Created, Locked, Inactive}
	
	mapping(address => uint256) balances;
	
	struct Voter {
		bool voted;
		...
	}
}
```

State variables
Local variables

##### Types

- 2 Category
	- Value types
	- Reference types
- Undefined or NULL not exist
- Uninitialised variables always have a default value (zero-state)
- C99


address
static and dynamic arrays
mappings: key => value

##### Visibility
public
external
internal
*private*: can be called only by the contract in which they are defined and not by a derived contract

##### Functions

##### Inheritance
interface
```solidity
interface Regulator {  
	... 
}  
contract Bank is Regulator {}
```

##### Data location
**Reference type**: storage and memory

##### Events, Modifiers and Global variables

EVM logging machanism, stored arguments
listeners