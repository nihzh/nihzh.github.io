- An algorithm is a sequence of steps for performing a task in a finate amount of time.

#### Big-Oh Notation
Given two positive functions *f(n)* and *g(n)*, **f(n) is O(g(n))**, written as `f(n) ∈ O(g(n))`, with constants *c* and *a0*: `f(n) <= c*g(n) for all n >= n0`
- Any polynomial `akn^k + ... + a2n^2 + a1n + a0` with **ak > 0** is `O(n^k)`, also `O(n^j)` for all **j >= k**
Common functions:
- *Logarithmic* O(log n)
- *Linear* O(n)
- *Quadratic* O(n^2)
- *Polynomial* O(n^k) for a positive integer k
- *Exponential* O(a^n), a > 1