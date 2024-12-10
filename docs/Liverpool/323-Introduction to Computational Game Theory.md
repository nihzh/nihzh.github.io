## Intro
Two or more individuals (players) have to take some decisions that will influence one another’s welfare. i.e., the payoff of each player depends not only on her own decision, but also on the decisions of (a subset of) the other players.  
A *game* is a description of strategic interaction that includes the constraints on the actions that the players can take and the players’ interests, but does not specify the actions that the players do take.  
A *solution* is a systematic description of the outcomes that may emerge in a family of games.

#### Game theoretic models
1. strategic games
2. extensive games with perfect information
3. extensive games without perfect information
4. coalitional games (cooperative games)

- Strategic games: each player chooses self plan of action **once and for all**, and players' decisions are made simutaneously.
- Extensive games: specifies the popssible orders of events, each player can consider self plan of action at the **beginning also whenever she has to**.

- Perfect information: the players are fully informed about each others' moves.
- Imperfect information: the players may be imperfectly informed about each others' moves

#### Player (Decision-maker)
1. Rational: makes decisions consistently in pursuif of own, well-defined objectives
2. Intelligent: knows everything about the game, can make any inferences about the situation, and takes into account this knowledge of other decition-makers' behavior (strategically)

## Strategic games
A strategic game `Γ = < N, (Si)i∈N, (ui)i∈N >`
- a set `N` of *players*
- for each player `i`, a set `Si` of *actions*
- for each player, references over the set of *action profiles* (a combination of actions, one for each player)
- for each player `i`, the *payoff cunction* `ui : ×i∈NSi -> R` mapping each action profile into a real number
No Time
- each player chooses action once and for all, simultaneously
- when choosing her action, no player is informed of the action chosen by any other player.

### Symmetric games
- each player has the same set of actions
- each players' payoff depends only on her action and that of her opponents, not on which player she is

> A symmetric strategic game is a game `Γ = <N, (S)i∈N, (ui)i∈N >` such that, for all actions a ∈ S and for all action profiles of n − 1 players s ∈ Sn−1, `ui (a, s) = uj (a, s)  ∀i,j ∈ N`
> 如果两个玩家 i 和 j 选择了相同的策略 a ，并且其他玩家的策略组合为 s ，那么他们的收益是相同的。

## Nash Eqilibrium
The best action for any given player depends on the other players' actions. When choosing an action, a player must have in mind the actions the other players will choose. The main solution concept for a strategic game is the *Nash equilibrium*: each player chooses her best available action, given the actions chosen by all the other players.

### Pure Nash equilibrium
An action profile `s` with the property that no player `i` can do better by choosing an action different from `Si`, given that every other player j adheres to `Sj`.

No player can increase her payoff by unilaterally changing her action.

Corresponds to a steady state: if every one else adheres to it, no inidividual wishes wo deviate from it.

`Γ = <N, (Si)i∈N , (ui)i∈N >` is an action profile s = (si )i∈N such that, for all players i ∈ N, `ui (s) ≥ ui (s′i , s−i)` for all `s′i ∈ Si`. 
- (s′i , s−i ) be the action profile that results from s when player i ∈ N switches to her action s′i ∈ Si , while the rest of the players preserve their actions s−i​

### Mixed Mash equilibrium
It models a **stochastic steady state** of a strategic game: allow each player to choose a *probability distribution* over the rest of her actions.

Every *strategic* game (with finite player and actions sets) possesses at least one (mixed) Nash equilibrium.

A *strategy* `pi` for player `i ∈ N` is a probability distribution over the set of her actions: `pi : Si → [0, 1]` that:
![](../img/Pasted%20image%2020241104144849.png)
The set of strategies of player `i` is denoted by `∆(Si)`.

A *pure strategy* is a strategy that poses probability 1 to a specific action `si ∈ Si : (pi(si) = 1)`, denote by `si` for simplicity

A *strategy profile* is a combination of strategies, one for each player: `p = (pi)i∈N`. 

#### Expected payoff
The *expected payoff* of player `i∈N` is the expected value of her payoff function
![](../img/Pasted%20image%2020241104153201.png)

>A Nash equilibrium is a strategy profile `p` such that for each player `i` and 
>for each strategy `p′i` of player `i`, `ui(p) ≥ ui (p′, p−i)`.
> Equivalently
>A Nash equilibrium is a strategy profile `p` such that for each player `i` and 
>for each action `si` of player `i`, `ui(p) ≥ ui (si, p−i)`.
![](../img/Pasted%20image%2020241104155943.png)

Expected payoff to a strategy profile is a *weighted average (probability)* of her expected payoffs to her pure strategies.
![](../img/Pasted%20image%2020241104162159.png)
Thus, the expected payoff to each action to which `pi` assigns postive probability is `ui(p)` and which to every other action (`pi` assigns 0 probability) is at most `ui(p)`

#### Support
The *support* of strategy `pi` of player `i` is the subset of action of `i` where `pi` poses strictly positive probability `Support(pi) = {si ∈ Si : pi (si) > 0}`
> A strategy profile p is a Nash equilibrium if and only if, for all players i and for all si ∈ Si ,
![](../img/Pasted%20image%2020241104180017.png)
> 玩家i选择的任何分配正概率的策略都应该是最佳策略之一，给定其他玩家的策略组合`p-i`

#### Best Response
Maximizes her payoff, given the strategies `p-i` of the other players
![](../img/Pasted%20image%2020241104215412.png)
一个玩家在给定其他玩家策略的情况下, 能够使其自身收益最大化的策略, 假设其他玩家保持不变

### Symmetric Nash equilibrium
A strategy profile `p` in a symmetric strategic game (each player has the same set of actions) is a *symmetric Nash equilibrium* if it is a (pure or mixed) Nash equlibrium and `pi` is the same for every player `i`.

Every symmetric strategic game in which each player's set of actions is finite has a symmetric Nash equilibrium


### Computing all Nash equilibria
Let ×i∈N Di be our current guess of the support. If there is an equilibrium p = (pi )i∈N with support ×i∈N Di , then there must exist numbers (ωi )i∈N such that:  
![](../img/Pasted%20image%2020241105011926.png)
`∑i∈N (|Si| + 1)` equations in the same number of unknowns
- no solutions exist
- some `pi(si)` is negative, so must require `pi(si)≥0 ∀i∈N, ∀si∈Di`
- some player `i` has some other action outside Di that would give her better payoff, so must require `ωi ≥ ui(ei, p−i) ∀i∈N, ∀ei∈Si\Di`

### Strict domination
In a **strategic game**, one (pure or mixed) strategy of a player *strictly dominates* an action (pure strategy) of taht player if it is superior, no matter what the other players do.
![](Pasted%20image%2020241105020036.png)
无论其他玩家采取什么行动，选择pi都会为该玩家带来更高的收益，而选择si会带来较低的收益

> A strictly dominated action is not used with positive probability in any Nash equilibrium

### Weak domination
![](../img/Pasted%20image%2020241105021224.png)
对于**所有**其他玩家的策略组合`s-i`, 选择pi会给玩家带来**不小于**si的收益
且
对于**至少一种**其他玩家的策略组合`s-i`, 选择pi的收益要**严格大于**选择si的收益

> A weakly dominated action may be used with posidive probability in a Nash equlibrium

### Dominant actions
A *dominant stategy* occurs when one pure strategy (action) is better thatn any other strategy for one player, no matter how that players' opponents may play.
![](../img/Pasted%20image%2020241105022229.png)


### Strict Nash equilibrium
A pure strategy profile `s = (si)i∈N` such that for each player `i`, 
![](Pasted%20image%2020241105022706.png)
- unique, stable, not dependent on others stategies

### Strong Nash equilibrium
There is no nonempty set of players who could all gain by **deviating together** to some other combination of strategies that is jointly feasible for them
- when the other players who are not in this set are expected to stay with their equilibrium strategies.
不存在一个非空的玩家子集可以通过**集体偏离**当前策略组合而获得更高的收益, 不仅要求单个玩家无偏离动机, 还要求任何玩家自己都无集体偏离动机

## Bimatrix games
A special case of 2-player games

y is a best response to x if and only if all strategies in the support of y are  
(pure) best responses to x.
### Positive normalized game
Every pair of equilibrium strategies of a bimatrix game does not change upon multiplying all the entries of a payoff matrix by a constant, and upon adding the same constant to each entry.

每个玩家的收益（payoff）都经过标准化处理，以确保收益值在一个特定的正数范围内，通常是 \[0,1\], 这种标准化简化了计算并确保 ε 的定义具有一致性。
### Approximate Nash equilibrium
(x, y) is an ε-approximate Nash equilibrium if and only if both players have  
regret at most ε.
![](../img/Pasted%20image%2020241105034623.png)


Find 3/4-approximate Nash equilibrium
1. find maximizes the payoff of the row/column player
2. the row player chooses row maximum payoff with probability 1/2 each
3. the column player chooses column maximum payoff with probability 1/2 each
4. find the payoff each
5. use `maxi (Ay)i − xT Ay` and `maxj (BT x)j − xT By`.

Find 1/2-approximate Nash equlibrium
1. Choose an arbitrary row
2. take best response for the column player
3. take best response for the row player
4. the row player take each chosen row with probability 1/2 each
5. the column player take the chosen column with probability 1
6. find the payoff each and use `maxi (Ay)i − xT Ay` and `maxj (BT x)j − xT By`

## Algorithmic game theory
### Proof of Nash’s theorem
*Analysis*: computation and analysis of properties of Nash equilibria
*Design*: design games that have both good game-theoretic and algorithmic properties (algorithmic mechanism design)

Nash, 1951: 
> Every finite strategic game possess a (mixed in genral) Nash equilibrium

#### Brouwer's fixed point theorem
**Every continuous function F : D --> D from a compact convex set D ⊆ $\mathrm{R^m}$ to itself has a *fixed point*
- there exists  $x^*$ ∈ D such that F ($x^*$) = $x^*$
- *Convex set*: a set of points that, given any two points A, B in the set, the line AB lies entirely within the set
- *Compact set*: shares the basic properties of closed intervals of real numbers, including the property that continuous functions achieve a minimum and maximum.
- 凸紧集: 保证线性插值在集合内且集合是有限范围且闭合的

#### Sperner's lemma
In one mimension, If a discrete function takes only the values 0 and 1, begins at the value 0 and ends at the value 1, then it must switch values an odd number of times

*Sperner coloring* (admissible coloring): In two dimensions, **any admissible coloring of any triangulation of the unit triangle has an odd number of trichomatic triangles**

n-dimensional simplex contains a cell colored with a complete set of colors. By making the triangulation maller and smaller, the limit of the fully labeled simplices is exactly the fixed point.

### PPAD-complete
Polynomial Parity Argument on a Directed graph: 
- A *search problem* `Π` has a set of instances and each instance `l` has a set `Sol(l)` of solutions (acceptable answers)
- The search problem is *total* if $Sol(l) \ne \emptyset$ for all instances `l`
	- *TFNP*: Tatal Function Nondeterministic Polynomial
- Key: **Given an instance of a total search problem, compute a solution**
- r-Nash: r-player strategic game, is total

Subclasses of TFNP: 
- PLS, PPP, PPA
- PPAD: A directed graph whose vertices have indegree and outdegree at most 1, and with at least one source, must have a sink.

PPAD formally defined by its complete problem: END OF THE LINE
![](../img/Pasted%20image%2020241208013452.png)
在有向图中找到一个终点, 即一个汇点或者一个非起点的源点
- A search problem is in PPAD if it reduces to EOTL
- PPAD-complete: All problems in PPAD reduce to it

> The problem of computing a Nash equilibrium of a finite 4-player strategic game is PPAD-complete.
> 
> The problem of computing a Nash equilibrium of a finite 2-player strategic game is PPAD-complete.

### Potential games
Real-valued functions defined over the *pure strategy profile* set of a strategic game.

Potential functions and payoff functions are both defined over the set of *pure strategies*
- A potential function for a game is the same for all players
- Each player has own payoff function

Whenever a single player deviates from a pure strategy profile, the difference in the payoff of the deviator is as much as the corresponding difference in the value of the potential function

Locally maximize a potential function of a game are *pure Nash equilibria (PNE)*
- No player can change her strategy so that the potential is increased
- If a game admits a potential function, then it is guaranteed to have a PNE

The difference in the payoff of the deviator is related to the corresponding difference of the potential
- generalized ordinal potential functions： 收益增加时势函数一定增加（可以不减少）![](../img/Pasted%20image%2020241208175155.png)
- ordinal potential functions: 变化方向一致![](../img/Pasted%20image%2020241208175131.png)
- weighted potential functions：允许收益变化对势函数的影响不同![](../img/Pasted%20image%2020241208175057.png)
- (exact) potential functions：完全刻画每个玩家收益变化与势函数变化的关系![](../img/Pasted%20image%2020241208175234.png)
### The Finite Inprovement Property (FIP)
在一个博弈中，从任意一个纯策略组合开始， 由玩家通过一系列单方面改进策略（提高其收益的策略变更）形成的路径总是有限的
- 路径上的每一步都能严格提高当前玩家的收益
- 路径最终停止在一个不能再改进的策略组合 -- 纯策略纳什均衡

A path $λ = (λ^0, λ^1, . . .)$ is an *improvement path* with respect to `Γ` if, for all `k` ≥ 1, 
$$ui(λ^k) > ui (λ^{k−1})$$
where `i` is the unique deviator at step `k`

> Game Γ has the FIP if every improvement path is finite
> 
> Every finite ordial potential game has the FIP
> 
> Game Γ has the FIP iff Γ has a generalized ordinal potential
> 
> 当在FIP博弈中，任意玩家i在面对其他玩家固定策略时，选择不同的策略一定会带来不同的收益时，其博弈具有序数势函数（ordinal potential）

### Characterization of exact potential games
![](../img/Pasted%20image%2020241208185707.png)
精确潜在博弈：收益的变化可以完全通过一个势函数P表示
对于闭路径，势函数的总变化应该为0，所有收益的增量和减量必须在路径中完全抵消
通过验证闭路径的收益变换是否满足公式， 判断博弈是否具有精确潜在函数

### Congestion games
Any game where:
- a collection of homogeneous agents have to choose from a finite set of alternatives and
- the payoff of a player depends on the number of players choosing each alternative
is a congestion game

- a set of *players* N
- a set of *resources* M
- for each player i ∈ N, a set of $\sum_i$ of *pure strateties* of player i, where $A_i$ ∈ $\sum_i$ is a non-empty subset of resources
- for each resource j ∈ M, a non-decreasing *delay function $d_j()$* where $d_j(k)$ denotes the cost (delay) to each user of resource j, if there are exactly k players using j

- the *payoff function* expressed as the *negative* of the *cost functions*$(\lambda_i)_{i∈N}$, definded as the sum of the delays of all resources that *i* is using

![](../img/Pasted%20image%2020241208213832.png)

> Every congestion game is an exact potential game

### Isomorphic games
Two games that are idencical except reordering or renaming their pure strateties of the players.
- Bijections $g_i$: action set jections

> Every finite exact potential game is isomorphic to a congestion game

### PLS-complete
Compute a pure Nash equlibrium of congestion game --> a local search problem --> *PLS-complete*
![](../img/Pasted%20image%2020241208215212.png)

congestion game: Two PLS problems Π1 and Π2, find a mapping from the instances of Π1 to the instances of Π2

### Mechanism design
设计能够实现特定目标的机制， 即使参与者是自私的，并且可能拥有与决策相关的私人信息
机制设计模型： 使用博弈论工具来模拟代理之间的交互。在机制中，每个代理都有一个消息（或策略）空间，决策结果是代理选择的消息的函数
![](../img/Pasted%20image%2020241208224847.png)

![](../img/Pasted%20image%2020241208230231.png)
如果一个机制能激励所有代理选择对其自身最有利的策略， 并且这些策略能够呆滞实现预期的结果，则称该机制实现了预期的目标
- *主导策略实现*：每个代理都存在一个主导策略，无论其他代理选择什么策略，该策略都能最大化其收益

#### Revelation principle
启示机制
直接启示机制：For all `i` and for all $t_i$, $A_i=T_i$
如果存在一个能够以主导策略实现特定目标的机制，那么一定存在一个能够以真实报告类型作为主导策略来实现相同目标的机制。这意味着在设计机制时，我们可以不失一般性地只考虑**直接启示机制和真实报告类型作为主导策略**的情况

truthful
1. Each agent reports her input to the mechanism.  
2. The mechanism computes the desired outcome based on the reported  
types.  
3. The mechanism computes payments for each agent.

#### VCG mechanism
*generalized Vickrey-Clark-Groves mechanism*
![](../img/Pasted%20image%2020241209013835.png)

![](../img/Pasted%20image%2020241209013157.png)

## Extensive game with Perfect Information
*Extensive game*: 扩展型博弈能够更详细地描述博弈的顺序结构，允许玩家根据博弈进程改变策略，其顺序被明确定义

*Terminal history*: Each possible sequence of actions
*Player function*: determines the player who move before each action in each terminal history
- P(h): 在历史h发生后, 由哪个玩家采取下一步行动, 每个历史h对应唯一玩家P

游戏开始时，不指定玩家可用的动作，而是在玩家选择动作之后根据terminal history 和 player function推断出

作为terminal history的proper subhistory不能单独作为terminal history
- If (C, D) is a terminal history, C should not be specified as a terminal history: after C is chosen at the start of the game, some player may choose D, so that the action C does not end the game.

*Subhistories*: 子历史, `(a1, a2, . . . , am), where 1 ≤ m ≤ k`, 包括∅
*Proper subhistory*: 不是完整历史序列, i.e., 不包括最后一项的子历史

![](../img/Pasted%20image%2020241209105240.png)

Terminal history可以无限长，not finite游戏无法用树表示
*finite horizen*: the longest terminal history is finite
具有有限视野的游戏可能由无限多个terminal history：某些玩家在某些历史之后可能有无限多个动作
finite: a game has a finite horizon and finitely many terminal histories

*Perfect information*
For each player, when choose an action
1. knows all action chosen previously (has *perfect information*)
2. always move along (not simultaneously)

*Backward induction*
A player who has to move deduces, for each of her possible actions, the actions that the players (including herself) will subsequently **rationally** take, and chooses the action that yields the terminal history she most prefers.

*Strategies*
the action the player chooses for every history after which it is her turn to move
![](../img/Pasted%20image%2020241209114818.png)
A player’s strategy provides sufficient information to determine her **plan of action**: the actions she intends to take, **whatever** the other players do


*outcomes*
![](../img/Pasted%20image%2020241209115802.png)


*Nash equilibrium of extensive game*
each player has finitely many strategies:
1. list each players' strategies
2. find the outcome of each strategy profile
3. analyze as for a strategic game

The set of Nash equilibria of any extensive game with perfect information  
is the set of Nash equilibria of its strategic form.

*Subgames*
For any nonterminal history h, the subgame following h is the part of the game that remains after h has occurred.
- The subgame following the empty history ∅ is the **entire game**
- Every other subgame is called a *proper subgame*.

The players’ behavior must correspond to a steady state in every subgame
![](../img/Pasted%20image%2020241209120823.png)

![](../img/Pasted%20image%2020241209121105.png)
can be Both

### Find subgame perfect equilibria
*Backward induction*
1. finding the optimal actions of the players who move in the subgames of length 1 (the last subgames)
2. taking these actions as given, find the optimal actions of the players who move first in the subgames of length 2
3. continue working back to the beginning of the game, at each stage k finding the optimal actions of the players who move at the start of the subgames of length k, given the optimal actions we have found in all shorter subgames
![](../img/Pasted%20image%2020241209152300.png)

![](../img/Pasted%20image%2020241209152359.png)

## Network congestion game
![](../img/Pasted%20image%2020241209162037.png)
unweighted (network) congestion games are exact potential games

![](../img/Pasted%20image%2020241210102900.png)
### weighted network congestion game
![](../img/Pasted%20image%2020241209170302.png)

linear delays: x is the load on edge e
$$d_e(x)=a_e*x+b_e$$
![](../img/Pasted%20image%2020241209170520.png)

exponential delays
![](../img/Pasted%20image%2020241209171227.png)

### Load Balancing
一组加权任务被分配到一组可能具有不同速度的机器上, 是的负载在机器之间均匀分布, 目标是最小化完工时间
- machines \[m], set of pure strategies for an agent
	- speeds s
- tasks \[n], task i ∈ \[n] is managed by agent i
	- weights w
	- each taks, a assignment A:\[n] -> \[m]
- load l = $\sum_{i:j=A(i)}\frac{W_i}{s_j}$
- cost(A) = max(lj) 机器上最大的load

可以使用混合策略P=($p_i^j$),  $p_i^j=Pr\{A(i)=j\}$
expected load of machine j
$$E[l_j]=\sum_{i\in[n]}\frac{w_ip_i^j}{s_j}$$
social cost
![](../img/Pasted%20image%2020241209182739.png)
![](../img/Pasted%20image%2020241209182831.png)
The expected cost of a task on a machine is larger than the expected load of the machine, unless the task is assigned with probability 1 to this machine
在expected cost中增加机器没有被完全分配的任务的成本

Nash equilibrium
![](../img/Pasted%20image%2020241209183035.png)

![](../img/Pasted%20image%2020241209183239.png)

The ratio between the social cost of the worst Nash equilibrium and the optimal social cost, the so-called *price of anarchy*.
![](../img/Pasted%20image%2020241209214846.png)
- G(m): 所有包含m个参与者的博弈实例的集合
- Nash(G): 博弈G的所有纳什均衡策略组合的集合
- cost(P): 策略组合P下的社会成本
- opt(G): 博弈G的最优社会成本

PoA: 相同机器上的纯策略纳什均衡
![](../img/Pasted%20image%2020241209220309.png)
在最差情况下, 纳什均衡的成本最多是全局最优解的 $(2-\frac{2}{m+1})$倍

*max-weight best response policy*
1. 按权重递减的顺序激活不合理(需要更改的)代理
2. 被激活的代理执行最佳相应策略: 将其任务移动到负载最小的机器上
![](../img/Pasted%20image%2020241209224506.png)
在每个代理最多被激活一次后达到纯策略纳什均衡

![](../img/Pasted%20image%2020241210022827.png)


PoA: 均匀相关机器上的纯策略纳什均衡![](../img/Pasted%20image%2020241209224017.png)
PoA: 相同机器上的混合策略纳什均衡
![](../img/Pasted%20image%2020241210023309.png)

PoA: 均匀相关机器上的混合策略纳什均衡
![](../img/Pasted%20image%2020241210023131.png)

## Auction
### Second-price sealed-bid auctions
竞标者同时提交密封的报价, 出价最高的竞标者以第二高的报价获得拍卖品
无论其他竞标者如何行动, 竞标者都应该爆出其对拍卖品的真实估值, 以获得最大收益, 无需猜测其他竞标者的行为 (弱主导策略)
### First-price sealed-bid actions
获胜者支付自身的报价, 需要权衡获胜的概率和支付的价格
纳什均衡:
- 当两个最高报价相同
- 其中一个最高报价由估值最高的玩家提交
- 最高报价至少等于第二高的估值, 且不超过最高估值