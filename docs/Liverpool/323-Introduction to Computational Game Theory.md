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