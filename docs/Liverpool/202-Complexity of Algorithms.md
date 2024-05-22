An algorithm is a sequence of steps for performing a task in a finate amount of time.

### Loop  invariants
*Loop* invariants are useful to show correctness of an alorithm given as pseudo-code
- *Initialisation*: it is true prior to the first iteration of the loop.
- *Maintenance*, if it is true before an iteration of the loop, it remains true before the next iteration
- *Terminaation*: when the loop terminates, the invariant gives is a useful property that help show the algorithm correct

### running - time
#### primitive operations
- asignment, single plus, multiple, compare.....
#### Big-Oh Notation
Given two positive functions *f(n)* and *g(n)*, **f(n) is O(g(n))**, written as `f(n) ∈ O(g(n))`, with constants *c* and *a0*: `f(n) <= c*g(n) for all n >= n0`
- Any polynomial `akn^k + ... + a2n^2 + a1n + a0` with **ak > 0** is `O(n^k)`, also `O(n^j)` for all **j >= k**
Common functions:
- *Logarithmic* O(log n)
- *Linear* O(n)
- *Quadratic* O(n^2)
- *Polynomial* O(n^k) for a positive integer k
- *Exponential* O(a^n), a > 1

g(n) is O(f(n)) and f(n) is O(g(n))

#### Justification Techniques
- *Methemetical induction*
- *Contradiction*: Suppose the proposition is not true
- *Contrapositive argument*: p => q is equivalent to ¬q => ¬p
- *Counterexample* (disproof)

## Divide-and-Conquer
- Merge sort: `O(nlogn)`, dividing/merging is `O(n)`, recursive at most `O(log n)`
- Incremental algorithm
- *Divide*: If the input size is small then solve the problem directly; otherwise, divide the input data into two or more subsets, typically disjoint
- *Recur.*: Recursively solve the sub-problems associated with subsets
- *Conquer*: Take the solutions to sub-problems and merge into a solution to the original problem

- *recurrence relation*: `T(n)`, the worst-possible running time on an input of size **n**, relates T(n) to values of function T for problem sizes smaller than n

![](../img/9c3f036b0e1ef8d7e3654569b514109.jpg)

```
T(n) = 2^j T(n/2^j) + jcn
for j = log n
T(n) = 2^(log n)c + cn log n = Θ(n log n)
```

### Matrix Multiplication
*Volker Strassen (1969)*

### Master method
![master_method](../img/Pasted%20image%2020240522013035.png)


## Data stucture
- Arrays
- Linked List

### Rooted trees
sortable, still efficient for search, insert/delete
- **binary tree**
- max value index at root
- min value index at root

#### Data structures for rooted t-ary trees
For rooted trees where wach node has at most *t* children, and is of **bounded depth**, you can **store the tree in an array A**. This is most useful when you're woring with (almost) complete t-ary trees.

In general, two children of node `A[i]` are in `A[2 * i + 1]` and `A[2 * i + 2]`
The parent of node `A[i]` is the node in position `A[(i-1) / 2]`

#### Binary search tree (BST)
Given a node *v* string the element *e*, all element in the **left subtree** at *v* are **less than** or equal to *e*, and those in the **right subtree** at *v* are **greater than** or equal to *e*
- balanced required for efficiency
- self-balancing BSTs
	- AVL trees
	- red-black trees

#### Heap Data Structure
The elements and their keys are stored in an almost complete binary tree (most of times), every level of the binary tree (expect last), will have the maximum number of children possible.
- *Heap-order* property: In a heap T, for every node v, the key at v is less than(equal) the key stored at its parent

##### Root deletion
1. swap root with last element
2. delete last element (bottom, right-most)
3. bubble root (last) down

#### Merge Sort / Heap Sort
- **O(n log n)**
- comparison-based

## Sorting
### Counting inversions
up to `n(n-1) / 2` for the permutation, number of inversions range starts from 0

*divide-and-conquer*: **O(n log n)**: sort each sublist and merge them recurcively into a single (sorted) list, and count the inversions from each part.

### Quick sort
**Select a pivot element randomly** to avoiding the L and G are ufficiently large

### Greedy method
solves a given **optimization problem** by going through a sequence of feasible choices, *greedy-choice property*
- start from well-understood config
- iteratively makes the decition (seems best)

### Interval scheduling
- A collecction of tasks
- A single macchine that can process these tasks
- To selet a subset of the tasks in order to maximize the number of tasks that can schedule on the machine.
- Maximum utilize resources/working completion

- Basic Probability
- Sample space
- Probability spaces
- Probability function
- Independent Events
- Conditional Probability
- Random variables

```
E(X) = Pr(X is heads)*1 + Pr(X is tails)*(1+expected number of additional coin tosses until first heads appears)
```

- Randomised quicksort

### Linear-time algorithms
- Aren't comparison based
- Require a promise that the elements in the input aren't too large

#### Counting sort
Assumes that each of the n input elements is an integer between 0 and k, when k = O(n), counting sort runs in O(n) time
- Input A\[1..n], output B\[1..n], use temp storage C\[1..n]
- **stable**

1. for array *C*, puts content integer of *A* as index, the reffered value is count
2. transfer *C* to new indexes (`C[i] += C[i-1]`)
3. insert values to array *B* by new indexes

#### Radix Sort
First sort by the least significant digit. Next sort by second-least significant digit.
- non-negative integer input required

## Dynamic Programming
Optimization
- first find a recursive recursion solution to the problem


## Graphs
### Single Source shortest paths
- Dijkstra's algorithm

### All pairs shortest paths
- Bellman-ford

### Maximum flow
The maximum flow is a network is equal to capacity of a  
minimum cut in the network.
- weight graph w(e) associated with each edge e
- Directed graph in which each edge (u,v)Ee has a non-negative integer capacity
- Source s(no in-edges) and sink t(no out-edges)
- *Ford-Fulkerson* method

#### Residual Networks
- consists edges that can admit more net flow
- forward edges
- backwards edges

#### cuts in networks

### bipartite graph