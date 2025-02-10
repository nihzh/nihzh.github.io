### Affine cipher
> Suppose `gcd(a, 26) = d > 1`, then $\color{#bd93f9}ax\equiv 0\pmod{26}$ has two disgtinguish solution

#### Bili -- 乘法逆元
[https://www.bilibili.com/video/BV195411w75c]
找到$\color{#bd93f9}a_{inv}$使得$\color{#bd93f9}\frac{b}{a}\%p$ = $\color{#bd93f9}(b*a_{inv})\%p$
乘`a`得到
$$\color{#bd93f9}b*(a_{inv} * a-1)\equiv 0\pmod{p}$$

then, 因为`b`可以是任何数, 要使公式恒为真, 则有
$$\color{#bd93f9}a_{inv}*a\equiv1\pmod{p}$$ ^d87cf4

即 **当且仅当`a`, `p`互质时, 乘法逆元存在**

##### 扩展欧几里得算法
求 `ax + by = gcd(a, b)`, 求解线性同余方程
[[#^d87cf4|上式]]转换, 添加项`py`得到
$$\color{#bd93f9}a*a_{inv} + py = 1$$
需要`a`, `p` 互质即可满足算法

```cpp
void exgcd(int a, int b, int &x, int &y){
	if (b == 0) { x = 1; y = 0; }
	int gcd = exgcd(b, a%b, y, x);
	y -= (a/b) * x
}

int get_inv(int a, int p){
	int x = 1, y = 0;
	exgcd(a, p, x, y);
	return (x%p + p) % p;
}
```

![](../img/Pasted%20image%2020250209033331.png)
