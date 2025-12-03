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
Transaction-based deterministic state machine
- global state
- decentralized applications/computing infrastructure
- stack-based
- turing-completeness

**Global state of Ethereum**: *accounts* which interact to each other through *transactions* (or *messages*)

### Ethereum Accounts
- *personal account*
![](../img/Pasted%20image%2020251002104723.png)
- *contract account*
![](../img/Pasted%20image%2020251002104754.png)

![](../img/Pasted%20image%2020251001184221.png)
nonce: total transactions

### Ethereum Transactions
*Smart Contract*
Create -> Interact -> Destroy

![](../img/Pasted%20image%2020251002110018.png)
*Signature*: sender's private key
*Data*:
- Create: *Smart contract code* + *initial arguments*
- Interaction: Which method to call + arguments

When contract account is activated:
- **Contract code** runs
- Read/write to internal storage
- Send other transactions or call other contracts

Can only send transactions when other transactions received

*Message*: a transaction except it is **produces by a contract**
- Exist only in the Ethereum execution environment
- Leads to the recipient account running its code
- Relationship with other contracts

Ethereum Virtual Machine
- A quashi Turing complete machine

Types of transactions
![](../img/Pasted%20image%2020251002111704.png)


*Gas*: Every computationn step has a fee, unit in gas

`gasLimit`: 用户愿意为这笔交易最多提供多少gas
`gasUsed`: 实际执行过程中消耗的gas
- `maxFeePerGas` / `maxPriorityFeePerGas`
	- `maxFeePerGas`: 用户愿意支付的最高费用
	- `maxPriorityFeePerGas`: tips给区块提议者
	- `baseFee`: 由协议自动调整的底价, 随网络拥堵程度波动
$$gasUsed*(baseFee+priorityFee)$$

![](../img/Pasted%20image%2020251001193138.png)
startgas & gasprice block
- all unused gas is refunded
- gas (price) raised determines how quickly a transaction will be included in a block

### Ethereum Block
Contain: transaction list and most recent state
Block time: 12 seconds
![](../img/Pasted%20image%2020251002112304.png)

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

### Potential Attacks
#### Denial-of-Service
![](../img/Pasted%20image%2020251008181544.png)
*Unbounded operation*: requires more gas as array become larger, reach the `gasLimit` ==> DoS, impossible to execute
*Griefing*: if a send/transfer call fails, the contract might get stuck
- it is possible to **force a call to fail**

![](../img/Pasted%20image%2020251009194345.png)

##### solution
Design pattern: *pull over push*
- avoid multiple nested `send()` call in a single transaction
- Isolates each *external call* into its own transaction
- let users withdraw their funds, no `push()` transfer
- gas fairness
- A trade-off between security and user experience

#### Reentrancy
![](../img/Pasted%20image%2020251008183526.png)
![](../img/Pasted%20image%2020251008183530.png)

##### solutions
Design pattern *Checks-Effects-Interactions*
- Perform checks on outputs, sender, value etc.
- Enforce **effects** and update the **state** accordingly
- Interact with other accounts via external calls or send/transfer

Finish all **internal work** (state changes) and then call **external** functions

Mutexes

#### Solidity specific hazards
##### Forcibly Sending Ether to a Contract
misuse of `this.balance`
Send ether with `selfdestruct(victimContractAddress)` will not trigger contact's fallback
**Avoid strict equality checks with the contract's balance**

`delegatecall` forwards calls from one contract to another

tx.origin ==> `msg.sender`   onlyOwner

keep `fallback` and `receive` logically minimise
- only `emit event` in `fallback`

#### Default values
Solidity sign empty/zero value automatically for every uninitialised variable

*Nomad Bridge Hack*

Always check user input
Even never accessed before, it has zero value

Keep simple
复杂的自研证明/加密构造极易出错——**尽量使用成熟库、保持简单、避免自己重写加密/证明逻辑**

#### Front-running
> 攻击者在mempool“看见”你的交易要发生，于是花更高的 gas 费，让自己的交易先执行。

Public *mempool*

Cryptographic *Commitment scheme*
![](../img/Pasted%20image%2020251009230005.png)
- Binding: a commitment can be opened only to its committed value
- Hiding: a commitment reveals no information about its committed value

Possible **DoS** and **forced gas cost**
User is forced to spend extra gas for new `tx` that posts new commitment
Attacker can continue front-running until they run out of money (to pay gas)

##### Generating Randomness
Insecure, can be manipulated by a **malicious miner**
![](../img/Pasted%20image%2020251008192842.png)

Intra-transaction information leak
If same-block `txs` share randomness source, attacker can check whether conditions are favourable **before acting**

*validate block's age*
miner is still able to keep newly-minded blocks hidden

##### Solutions
*Commit-Reveal*
![](../img/Pasted%20image%2020251009230528.png)

*2-party coin flipping via commitments*
![](../img/Pasted%20image%2020251009230659.png)

![](../img/Pasted%20image%2020251008193930.png)

#### Overflow/Underflow: number
`uint256` overflow/underflow in *Solidity* < 0.8

#### Gas Fairness
![](../img/Pasted%20image%2020251008194355.png)

## The Consensus Problem
A transaction history and/or state of the service needs to be agreed by all servers
- participants with diverging intrests

![](../img/Pasted%20image%2020251015182911.png)

![](../img/Pasted%20image%2020251015183440.png)

Doesn't matter the parties input of the agreement: All outputs are the same

Bitcoin: a < 1/2
51% attack
![](../img/590d70c4c7a669cb51ea8daf164f14e9.jpg)
![](../img/19c90b11d2c0d7f486bb0aa1cd923443.jpg)

##### Ledger Consensus Properties
*Consistency* $$\forall i,j \in \mathbf{H}, t,t' : (\text{Log}_i[t] \npreceq \text{Log}_j[t']) \rightarrow (\text{Log}_j[t'] \preceq \text{Log}_i[t])$$
对于任意两个诚实的参与者 `i` 和 `j`，以及任意时间点`t`,`t′`：
- 如果某一方的日志（账本）不是另一方日志的前缀，
- 那么反过来，另一方的日志一定是它的前缀。
所有诚实节点的账本是前缀关系，不会出现账本分叉或冲突

*Liveness* $$(\forall i \in \mathbf{H} : tx \in I_i[t]) \rightarrow (\forall i \in \mathbf{H} : tx \in \text{Log}_i[t + u])$$
where 
$\color{#bd93f9}I_j[t]$ is Transaction Input of party `j` at time `t` consistent with its log
$\color{#bd93f9}\text{Log}_j[t]$ is Log of party `j` at time `t`

对于任意一个诚实节点 `i`：
- 如果在时间 `t` 时它提交了一笔交易 `tx`, 
- 那么在经过某个有限的延迟时间 `u` 之后, 所有诚实节点的账本中都会包含这笔交易。
提交的交易最终都会上链，系统持续运行，交易最终确认

##### Bitcoin Blockchain
![](../img/Pasted%20image%2020251016002936.png)

匿名性 不可关联性 无身份认证机制 无信任

- The chain validation predicate
- The chain selection rule (max-valid)
- The proof of work function
- The main protocol loop

#### Model
- `n` parties running the protocol
- Synchronous
- Each party has a quota of `q` queries to the function `H()` in each round
- A number of `t` parties are controlled by an adversary

![](../img/169fc0a6024015bd650f5c26287d523d.jpg)
![](../img/5d4b72901580bd74c16c9f733064b6db.jpg)

Broadcast the whole book --> check the chain of hashes

#### Basis Properties
##### *Common prefix*  **(Consistency)** $$\forall r_1, r_2, (r_1 \le r_2), P_1, P_2, \text{ with } C_1, C_2 : C_1^{\lfloor k \rfloor} \preceq C_2$$
> 对任意两个诚实节点 `P1`,`P2` 在任意两个时间点 `r1`≤`r2`，
> 如果你从较早节点 `P1`​ 的区块链中去掉最后 `k` 个区块，
> 那么得到的链一定是另一个节点 `P2` 当前区块链的前缀。

所有诚实节点的区块链大部分一致，只有最近k个可能存在分歧
- **Racing**: Attacker splits from the main chain and tries to overtake the "honest chain"
- Confirmation depth: 6 confirmations
- The property holds true, in a probabilistic sense, with an error that decays exponentially in `k`.

##### *Chain Growth* **(Liveness)** $$Parameters\space\tau \in (0,1), \, s \in \mathbb{N}$$In any period of `s` rounds at least `τs` blocks are add to the chain of an honest party `P`. Where 
τ≈probability that at least one honest party finds a PoW in a round.
> 区块链会持续增长，不会陷入死锁，极大概率成立

##### *Chain Quality* **(Liveness)** $$\mu \in (0,1), \, \ell \in \mathbb{N}$$
The ratio of blocks of an `ℓ-long` segment of an honest chain produced by the adversary is bounded by `(1−μ)ℓ`
μ：链质量参数，表示诚实节点在该区段中占据的最小比例

> 在任意长度为`ℓ`的链区间中，至少有比例为`μ`的区块是由诚实节点产生的

The property holds true probabilistically with an error that exponentially decays in `ℓ`.

![](../img/Pasted%20image%2020251016015407.png)
> 对手每获得 1 个主链区块，就最多能让 1 个诚实独占区块“失效”（成孤块）。 
> 所以诚实净贡献是“诚实独占 − 对手独占”。

> 只要 $t < \tfrac{n}{2}$，就有 $\mu>0$；当 $t \to \tfrac{n}{2}$​ 时，$\mu \to 0$。
> 当$\mu >  0$, 系统才具备自愈能力

*Block Withholding Attacks*
> Attacker mines privately and releases their block at the same time an honest party releases its own block
> Assuming honest propagation favours the adversary, the honest block is dropped, reducing chain quality

*Hash operations*: $2^{78}$ hashing operations

Mining pools parallelising: work together to solve PoW for the same block
- shares

#### Dynamic Availability
*T (PoW algorithm target)*: how difficulty of the Proof of Work algorithm (probability)
![](../img/Pasted%20image%2020251015195437.png)
if T is small, the hardness increase
with the attendance increase, the hardness raise
![](../img/Pasted%20image%2020251016022441.png)

0xAf0F1AEf2d28cCA39554335C9a79914512645A90

## PoS and BFT protocol
computational power of adversary
Permissionless Protocols

Electronic waste

### Proof-of-Stake
more power, more checkers solved

lottery based on stake
Stake: The amount of digital assets a party controls
No need to consume high amounts of energy to run the stake-based lottery

#### Nakemoto Design
- Blocks are arranged on a chain (tree)
- each block points to the predecessor
- In case of conflicts, pick the longest chain
- New blocks are generated by who wins the lottery
	- PoW: computational lottery
		- Probability of winning proportional to computational power
		- Security: the majority of computational power is in the hand of honest parties
	- PoS: lottery based on stake
		- Probability of winning proportional to stake, =amount of cryptocurrency on your account
		- Security: the majority of cryptocurrency is controlled by the honest parties
	- who is winning the game is more incentivised to keep it running

*Time slot*: Protocol breaks time in *slots*
- parameter: `slot length`
- parties act based on the time slot they are in
- network is assumed **synchronous**

- The number of all assets is known: Tokens recorded on the ledger
- The **public key** that controls each asset is known
- **One block** should be created per slot
- At each slot, choose one of the assets at **random**
- The owner of the chosen asset is **eligible to produce a block** at that slot

![](../img/Pasted%20image%2020251023014831.png)

*Grinding Attack on x*: attacker can try different x to find the one that satisfies the inequality
*Content Malleability*: block's content not represent in the header
*Posterior Corruptions*: **corrupt parties after the slot passes** (who create a block in that slot), change part of the chain's history
![](../img/Pasted%20image%2020251023020230.png)

*Adaptive corruption*: `vk` that satisfies inequality is publicly known before the time slot starts, attackers can predict and corrupt a party that is known to be leader of a specific future slot

*Verify Random Function*: `VRF` $$(\pi,y) \leftarrow VRF(sk_n, s) < T \cdot stake\_factor_n$$
- 若$\color{#bd93f9}y < T \cdot \text{stake}_n$​，则当选出块者。
- 之后区块头中带上 VRF 证明 `π`，让所有人验证。

K <- miner's VRF secret key
pk <- miner's VRF public key

*Stalling Hazard*: With some `T`, no `vk` will satisfy the equation, no blocks created -> no parameter in the inequality changes

![](../img/Pasted%20image%2020251023021438.png)
Time slot into VRF, for next lottery randomness $$VRF(sk_n, s || ts) < T \cdot stake\_factor_n$$
*Key Grinding Attack*: attacker play multiple possible VRF calculations prior to committing to a particular key

*epoch* : each associated with a random string, to randomness the lottery `R`
- each epoch has its own stakeholder distribution and randomness


*Long-range attack*: a branch from an old block, increasing stake and get majority
- costless: the attacker can create an arbitrarily long chain

1. trustable checkpointing
2. chain density: the new nodes joins the system, chooses a path at each fork by following the most dense branch *Ouroboros Genesis*

### Permissioned Ledgers
**Restricted** participation: only be performed after being authorized by some other nodes
- CA, TLS/SSL
- In case of secret key leaking (break personal computer and get secret key
), blacklist of certificate **Delete the old key**

The set of participating nodes is **fixed** and determined at the onset of protocal's execution

![](../img/Pasted%20image%2020251023024429.png)
Proof-of-Authority, PoA

http://www.ietf.org/rfc/rfc3280.txt
#### BFT protocol
No need for assumptions on distribution of resources

Graded broadcast: how confident you are
Binary consensus protocol

**Communication rounds**
1. The sender sends the message M to all receivers  
2. The i-th receiver, who obtained M1,i in round 1, sends it to all receivers 
3. The i-th receiver, who obtained M2,j,i from the j-th receiver in round 2 if there is a single message that was sent by at least 2n/3 receivers, it sends it to all receivers

3t+1 rounds

### BFT-style PoS
*Algorand*: **每个 slot** 随机（按 stake 加权）**抽取一个委员会**，由委员会运行**BFT 协议**敲定新区块，并按 BFT 规则给予**终局性**；
![](../img/Pasted%20image%2020251023024947.png)


![](../img/Pasted%20image%2020251023025330.png)
“Self-healing” 是 PoS 系统与 PoW 系统在长期安全性上的最大差异。  
PoW 依赖算力市场恢复信任；  
PoS 则可以让系统**经济地惩罚攻击并自修复**。

## Anonymity
*Pseudonyms*
Fungibility: coins are interchangeable

### Transaction Anonymization
![](../img/Pasted%20image%2020251105194423.png)
shuffle

*Mimblewimble*: commitments with homomorphic property

![](../img/Pasted%20image%2020251105201001.png)

![](../img/Pasted%20image%2020251105201254.png)

![](../img/Pasted%20image%2020251105201740.png)
*Fair Swaps*: A and B exchange secrets, either none of them gets their output, or both do
- resort to a trustedn third party
- with penalties

![](../img/Pasted%20image%2020251105201819.png)

Ring signature

### Zero-Knowledge
#### ZK-SNARK
Zero-knowledge succinct non-interactive argument of knowledge
![](../img/Pasted%20image%2020251105205709.png)

*Computational soundness*:  
If the claim is false, it is unlikely that any polynomial-time prover manages to convince the verifier

*Zero-Knowledge*:  
The proof 𝜋 leaks no information about w

*Succinctness*:  
The size of the proof 𝜋 and the complexity of its verification are **independent** of the size of w and the running time of R.

#### Zerocash
![](../img/Pasted%20image%2020251112191711.png)
![](../img/Pasted%20image%2020251112191707.png)
### Network Security
Bitcoin: P2P network
Peers address book: how to maintain

Eclipse Attack

ban ADDR
validate incoming connections

Hot wallet: keys on an internet-connected computer
Cold wallet: private keys offline

## Secure Multiparty Communication
1. 
2. T-privacy: even if a subset < T parties collude, all they learn about the other parties inputs is their own outptus

T-out-of-N
![](../img/Pasted%20image%2020251112201358.png)
If P is prime, 
given T points in Zp, these exists only one polynomial q of degree t-1 at $q(x_i)=y_i$

![](../img/Pasted%20image%2020251112204102.png)
N parties maintaining a same secret and secret key

secret sharing of each key, joining

![](../img/Pasted%20image%2020251112205239.png)

Multiple gate
![](../img/Pasted%20image%2020251204025425.png)

![](../img/Pasted%20image%2020251204025445.png)

![](../img/Pasted%20image%2020251204025344.png)


![](../img/Pasted%20image%2020251204025401.png)

![](../img/Pasted%20image%2020251204025939.png)

![](../img/Pasted%20image%2020251204025409.png)

![](../img/Pasted%20image%2020251204025836.png)


