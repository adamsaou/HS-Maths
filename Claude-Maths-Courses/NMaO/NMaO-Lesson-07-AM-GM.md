# Lesson 07 - AM-GM and Equality Cases

<span class="nmao-badge nmao-study">LESSON</span>

## Objective

Use the arithmetic mean-geometric mean inequality to find bounds, prove inequalities, solve minimum and maximum problems, and identify equality cases precisely.

## 1. The two-variable AM-GM inequality

For nonnegative numbers $u$ and $v$:

$$
\boxed{\frac{u+v}{2}\ge\sqrt{uv}}.
$$

Equivalent forms are:

$$
u+v\ge2\sqrt{uv},
$$

and

$$
u^2+v^2\ge2uv
$$

when the inputs are chosen as $u=x$ and $v=y$, or as suitable square terms.

The arithmetic mean is the left side, and the geometric mean is the right side.

## 2. Equality is part of the answer

Equality holds exactly when the two inputs are equal:

$$
u=v.
$$

For example:

$$
x+\frac9x\ge2\sqrt{x\cdot\frac9x}=6,
\qquad x>0.
$$

Equality requires:

$$
x=\frac9x.
$$

Since $x>0$, this gives $x=3$. Therefore the minimum is $6$, reached at $x=3$.

Do not stop after finding a bound. Always solve the equality condition and verify that it is allowed.

## AM-GM explained intuitively

### Two different meanings of “mean”

For two nonnegative numbers $u$ and $v$:

- the arithmetic mean is the ordinary average, $(u+v)/2$;
- the geometric mean is the multiplicative average, $\sqrt{uv}$.

The geometric mean is the number whose square equals the product $uv$:

$$
\left(\sqrt{uv}\right)^2=uv.
$$

AM-GM says:

$$
\frac{u+v}{2}\ge\sqrt{uv}.
$$

In words: the ordinary average is never smaller than the multiplicative average.

### The balance idea

The most important intuition is that equality is reached when the two numbers are balanced:

$$
u=v.
$$

If the sum is fixed, moving the two numbers closer together increases their product. For example, the pairs $(1,9)$ and $(5,5)$ have the same sum, but:

$$
1\cdot9=9,
\qquad
5\cdot5=25.
$$

The equal pair gives the larger product.

If the product is fixed, moving the two numbers closer together decreases their sum. For example, the pairs $(1,16)$ and $(4,4)$ have the same product, but:

$$
1+16=17,
\qquad
4+4=8.
$$

The equal pair gives the smaller sum.

This is why AM-GM appears so often in olympiad minima and maxima: it detects the balanced configuration.

### Why the inequality is true

Let $p=\sqrt u$ and $q=\sqrt v$. A square is nonnegative:

$$
(p-q)^2\ge0.
$$

Expand:

$$
p^2-2pq+q^2\ge0.
$$

Replace $p^2$ by $u$, $q^2$ by $v$, and $pq$ by $\sqrt{uv}$:

$$
u-2\sqrt{uv}+v\ge0.
$$

Rearrange and divide by $2$:

$$
\boxed{\frac{u+v}{2}\ge\sqrt{uv}}.
$$

The gap between the two means is exactly:

$$
\frac{u+v}{2}-\sqrt{uv}
=\frac{(\sqrt u-\sqrt v)^2}{2}.
$$

So the gap is nonnegative, and it becomes zero exactly when $u=v$.

### How to recognize AM-GM in a problem

Look for two nonnegative expressions whose product is simple or fixed.

For example, in:

$$
x+\frac{16}{x},
\qquad x>0,
$$

the two terms are $x$ and $16/x$. Their product is always $16$, so AM-GM says their sum is smallest when the two terms are equal:

$$
x=\frac{16}{x}.
$$

This gives the equality point and the minimum. The method is not a random formula: it notices that the product is fixed and asks when the two factors are balanced.

### What do “arithmetic mean” and “geometric mean” actually mean?

#### Arithmetic mean: equal sharing of a total

The arithmetic mean is the ordinary average. Add the values, then divide by how many values there are:

$$
\operatorname{AM}(a,b)=\frac{a+b}{2}.
$$

It answers this question: if the total amount were shared equally, how much would each value receive?

For $4$ and $10$, the total is $14$, so equal sharing gives:

$$
\frac{4+10}{2}=7.
$$

The number $7$ is the additive midpoint: it is equally far from $4$ and $10$.

#### Geometric mean: equal multiplication of a product

The geometric mean asks for the equal factor that produces the same product. For two positive numbers $a$ and $b$, find $g$ satisfying:

$$
g\cdot g=ab.
$$

Therefore:

$$
g^2=ab
\quad\Longrightarrow\quad
g=\sqrt{ab}.
$$

So:

$$
\operatorname{GM}(a,b)=\sqrt{ab}.
$$

For $4$ and $16$, the product is $64$, and the equal factor is $8$:

$$
8\cdot8=4\cdot16=64.
$$

Thus their geometric mean is $8$.

#### Why is it called “geometric”?

Imagine a rectangle with side lengths $a$ and $b$. Its area is $ab$. A square with the same area has side length $g$ satisfying:

$$
g^2=ab.
$$

Hence $g=\sqrt{ab}$. The geometric mean is the side length of the equal-area square.

#### The essential difference

The two means answer different questions:

$$
\text{Arithmetic mean: equalize a sum.}
$$

$$
\text{Geometric mean: equalize a product.}
$$

For $1$ and $16$:

$$
\operatorname{AM}=\frac{17}{2},
\qquad
\operatorname{GM}=4.
$$

They differ because addition and multiplication combine quantities in different ways.

For $n$ positive numbers:

$$
\operatorname{AM}=\frac{x_1+x_2+\cdots+x_n}{n},
\qquad
\operatorname{GM}=\sqrt[n]{x_1x_2\cdots x_n}.
$$

## 3. Fixed sum gives a maximum product

Suppose $x,y\ge0$ and $x+y=s$. AM-GM gives:

$$
\frac{x+y}{2}\ge\sqrt{xy}.
$$

Squaring both sides:

$$
\frac{s^2}{4}\ge xy.
$$

Thus:

$$
\boxed{xy\le\frac{s^2}{4}}.
$$

Equality occurs when $x=y=s/2$. So among nonnegative numbers with fixed sum, the product is largest when the numbers are equal.

## 4. Fixed product gives a minimum sum

Suppose $x,y>0$ and $xy=p$. AM-GM gives:

$$
\frac{x+y}{2}\ge\sqrt{xy}=\sqrt p.
$$

Therefore:

$$
\boxed{x+y\ge2\sqrt p}.
$$

Equality occurs when $x=y=\sqrt p$.

## 5. Three-variable AM-GM

For nonnegative $a,b,c$:

$$
\boxed{\frac{a+b+c}{3}\ge\sqrt[3]{abc}}.
$$

Equivalently:

$$
a+b+c\ge3\sqrt[3]{abc}.
$$

Equality holds when:

$$
a=b=c.
$$

For example, if $abc=8$, then:

$$
a+b+c\ge3\sqrt[3]{8}=6.
$$

Equality is possible at $a=b=c=2$, so the minimum is exactly $6$.

## 6. Choosing the right form

- To bound a sum from below, use AM-GM directly.
- To bound a product from above under a fixed sum, apply AM-GM and square.
- To bound a sum from below under a fixed product, apply AM-GM directly.
- For a quotient such as $x+k/x$, use the two positive terms $x$ and $k/x$.
- Always check positivity before using square roots or AM-GM.
- Always solve the equality condition; it determines whether your bound is sharp.

## Practice

### Basic

**A.** Prove for $x,y\ge0$ that:

$$
x+y\ge2\sqrt{xy}.
$$

State the equality condition.

### Solution to A

Because $x,y\ge0$, their square roots are defined. Start with the nonnegative square:

$$
(\sqrt{x}-\sqrt{y})^2\ge0.
$$

Expand:

$$
x-2\sqrt{xy}+y\ge0.
$$

Add $2\sqrt{xy}$ to both sides:

$$
\boxed{x+y\ge2\sqrt{xy}}.
$$

Equality occurs exactly when the square is zero:

$$
\sqrt{x}=\sqrt{y}
\quad\Longrightarrow\quad
\boxed{x=y}.
$$

### Extra practice: use the same method as A

Let $a,b\ge0$. Prove that:

$$
4a+9b\ge12\sqrt{ab}.
$$

Use a square involving $\sqrt a$ and $\sqrt b$, then state exactly when equality holds.

#### Correction

Because $a,b\ge0$, start with:

$$
(2\sqrt a-3\sqrt b)^2\ge0.
$$

Expand:

$$
4a-12\sqrt{ab}+9b\ge0.
$$

Add $12\sqrt{ab}$ to both sides:

$$
\boxed{4a+9b\ge12\sqrt{ab}}.
$$

Equality occurs when the square is zero:

$$
2\sqrt a=3\sqrt b.
$$

Equivalently:

$$
\boxed{4a=9b}.
$$

**B.** Find the minimum value of:

$$
x+\frac{16}{x},
\qquad x>0.
$$

State where the minimum occurs.

### Solution to B

Since $x>0$, both terms $x$ and $16/x$ are positive. Apply AM-GM:

$$
x+\frac{16}{x}
\ge2\sqrt{x\cdot\frac{16}{x}}.
$$

Simplify the product:

$$
2\sqrt{x\cdot\frac{16}{x}}
=2\sqrt{16}=8.
$$

Therefore:

$$
\boxed{x+\frac{16}{x}\ge8}.
$$

Equality occurs when the two AM-GM inputs are equal:

$$
x=\frac{16}{x}.
$$

Since $x>0$:

$$
x^2=16\quad\Longrightarrow\quad\boxed{x=4}.
$$

Thus the minimum value is $\boxed{8}$, reached at $x=4$.

### Extra practice: like B

Find the minimum value of:

$$
3x+\frac{12}{x},
\qquad x>0.
$$

State the value of $x$ at which the minimum occurs. Apply AM-GM to the two terms exactly as they appear.

#### Correction

Since $x>0$, both terms are positive. Apply AM-GM:

$$
3x+\frac{12}{x}
\ge2\sqrt{3x\cdot\frac{12}{x}}.
$$

Simplify:

$$
2\sqrt{3x\cdot\frac{12}{x}}
=2\sqrt{36}=12.
$$

Therefore:

$$
\boxed{3x+\frac{12}{x}\ge12}.
$$

Equality occurs when the two inputs are equal:

$$
3x=\frac{12}{x}.
$$

Since $x>0$:

$$
3x^2=12
\quad\Longrightarrow\quad
x^2=4
\quad\Longrightarrow\quad
\boxed{x=2}.
$$

Thus the minimum value is $\boxed{12}$, reached at $x=2$.

### Extra practice: AM-GM minimum

Find the minimum value of:

$$
4x+\frac{9}{x},
\qquad x>0.
$$

State the value of $x$ at which the minimum occurs. Apply AM-GM to the two complete positive terms.

#### Correction

Since $x>0$, both terms are positive. Apply AM-GM:

$$
4x+\frac9x
\ge2\sqrt{4x\cdot\frac9x}.
$$

Simplify:

$$
2\sqrt{4x\cdot\frac9x}
=2\sqrt{36}=12.
$$

Therefore:

$$
\boxed{4x+\frac9x\ge12}.
$$

Equality occurs when the two AM-GM inputs are equal:

$$
4x=\frac9x.
$$

Since $x>0$:

$$
4x^2=9
\quad\Longrightarrow\quad
x^2=\frac94
\quad\Longrightarrow\quad
\boxed{x=\frac32}.
$$

Thus the minimum value is $\boxed{12}$, reached at $x=\frac32$.

### Extra practice: reinforcement

Find the minimum value of:

$$
2x+\frac8x,
\qquad x>0.
$$

State the value of $x$ at which the minimum occurs. Follow the same two steps: apply AM-GM, then set the two inputs equal.

#### Correction

Since $x>0$, both terms are positive. Apply AM-GM:

$$
2x+\frac8x
\ge2\sqrt{2x\cdot\frac8x}.
$$

Simplify:

$$
2\sqrt{2x\cdot\frac8x}
=2\sqrt{16}=8.
$$

Therefore:

$$
\boxed{2x+\frac8x\ge8}.
$$

Equality occurs when the two AM-GM inputs are equal:

$$
2x=\frac8x.
$$

Since $x>0$:

$$
2x^2=8
\quad\Longrightarrow\quad
x^2=4
\quad\Longrightarrow\quad
\boxed{x=2}.
$$

Thus the minimum value is $\boxed{8}$, reached at $x=2$.

**C.** Let $x,y\ge0$ and $x+y=12$. Find the maximum value of $xy$ and state when it occurs.

### Solution to C

Apply AM-GM to $x$ and $y$:

$$
\frac{x+y}{2}\ge\sqrt{xy}.
$$

Since $x+y=12$:

$$
6\ge\sqrt{xy}.
$$

Both sides are nonnegative, so square:

$$
36\ge xy.
$$

Therefore:

$$
\boxed{\max(xy)=36}.
$$

Equality in AM-GM occurs when:

$$
x=y.
$$

Together with $x+y=12$:

$$
\boxed{x=y=6}.
$$

### Extra practice: like C

Let $u,v\ge0$ and $u+v=14$. Find the maximum value of $uv$ and state exactly when it occurs.

#### Correction

Apply AM-GM to $u$ and $v$:

$$
\frac{u+v}{2}\ge\sqrt{uv}.
$$

Since $u+v=14$:

$$
7\ge\sqrt{uv}.
$$

Both sides are nonnegative, so square:

$$
49\ge uv.
$$

Therefore:

$$
\boxed{\max(uv)=49}.
$$

Equality in AM-GM occurs when:

$$
u=v.
$$

Together with $u+v=14$:

$$
u=v=7.
$$

Thus the maximum is reached at:

$$
\boxed{(u,v)=(7,7)}.
$$

### Intermediate

**D.** Let $a,b,c>0$ and $abc=8$. Find the minimum value of $a+b+c$ and state the equality case.

### Solution to D

Apply the three-variable AM-GM inequality:

$$
\frac{a+b+c}{3}\ge\sqrt[3]{abc}.
$$

Since $abc=8$:

$$
\frac{a+b+c}{3}\ge\sqrt[3]{8}=2.
$$

Multiply by $3$:

$$
a+b+c\ge6.
$$

Therefore the minimum value is at least $6$. Equality in three-variable AM-GM occurs when:

$$
a=b=c.
$$

Together with $abc=8$:

$$
a^3=8\quad\Longrightarrow\quad a=2.
$$

Thus $a=b=c=2$ is allowed and reaches the bound. Therefore:

$$
\boxed{\min(a+b+c)=6},
\qquad
\boxed{a=b=c=2\text{ at equality}}.
$$

### Extra practice: like D

Let $p,q,r>0$ and $pqr=27$. Find the minimum value of $p+q+r$ and state exactly when equality occurs.

#### Correction

Apply the three-variable AM-GM inequality:

$$
\frac{p+q+r}{3}\ge\sqrt[3]{pqr}.
$$

Since $pqr=27$:

$$
\frac{p+q+r}{3}\ge\sqrt[3]{27}=3.
$$

Multiply by $3$:

$$
p+q+r\ge9.
$$

Equality occurs when:

$$
p=q=r.
$$

Together with $pqr=27$:

$$
p^3=27\quad\Longrightarrow\quad p=3.
$$

Therefore:

$$
\boxed{\min(p+q+r)=9},
\qquad
\boxed{p=q=r=3\text{ at equality}}.
$$

**E.** Prove that for $x,y,z>0$:

Here $x,y,z$ are positive real numbers. They are not restricted to natural numbers unless the problem explicitly says so. Positivity is required because the reciprocal terms must be defined and because AM-GM is being applied to positive quantities.

$$
\left(x+y+z\right)\left(\frac1x+\frac1y+\frac1z\right)\ge9.
$$

Identify the equality condition.

### Hints for E

> [!hint] Hint 1
> Treat the two parentheses separately. Can you apply three-variable AM-GM to the first one?

> [!hint] Hint 2
> Apply three-variable AM-GM again to the reciprocal terms in the second parenthesis. Compute the product of those three reciprocal terms.

> [!hint] Hint 3
> Multiply the two lower bounds. The product of the two cube-root expressions should simplify because the original variables are positive.

> [!hint] Equality hint
> For equality, the three terms in each AM-GM application must be equal. What does that force about $x,y,z$?

### Solution to E

Apply three-variable AM-GM to the first parenthesis:

$$
x+y+z\ge3\sqrt[3]{xyz}.
$$

Apply it to the reciprocal terms:

$$
\frac1x+\frac1y+\frac1z
\ge3\sqrt[3]{\frac1{xyz}}.
$$

Because $x,y,z>0$, both lower bounds are positive, so we can multiply them:

$$
\left(x+y+z\right)
\left(\frac1x+\frac1y+\frac1z\right)
\ge
9\sqrt[3]{xyz}\sqrt[3]{\frac1{xyz}}.
$$

Simplify the cube roots:

$$
\sqrt[3]{xyz}\sqrt[3]{\frac1{xyz}}=1.
$$

Therefore:

$$
\boxed{\left(x+y+z\right)\left(\frac1x+\frac1y+\frac1z\right)\ge9}.
$$

For equality, the first AM-GM application requires $x=y=z$. The reciprocal AM-GM application gives the same condition. Any common positive value works, so equality occurs exactly when:

$$
\boxed{x=y=z>0}.
$$

**F.** Let $x,y>0$ and $x+y=10$. Find the maximum value of:

$$
xy.
$$

Then explain why the answer agrees with the fixed-sum product principle.

### Solution to F

Apply AM-GM to $x$ and $y$:

$$
\frac{x+y}{2}\ge\sqrt{xy}.
$$

Since $x+y=10$:

$$
5\ge\sqrt{xy}.
$$

Both sides are positive, so square:

$$
25\ge xy.
$$

Therefore:

$$
\boxed{\max(xy)=25}.
$$

Equality occurs when $x=y$. Together with $x+y=10$:

$$
\boxed{x=y=5}.
$$

This agrees with the fixed-sum product principle: the product is largest when the two positive numbers are equal.

### Extra practice: like F

Let $u,v>0$ and $u+v=18$. Find the maximum value of $uv$ and state exactly when equality occurs.

#### Correction

Apply AM-GM:

$$
\frac{u+v}{2}\ge\sqrt{uv}.
$$

Since $u+v=18$:

$$
9\ge\sqrt{uv}.
$$

Both sides are positive, so square:

$$
81\ge uv.
$$

Therefore:

$$
\boxed{\max(uv)=81}.
$$

Equality occurs when $u=v$. Together with $u+v=18$:

$$
\boxed{u=v=9}.
$$

### Extra practice: like E

Let $x,y,z>0$. Prove that:

$$
\left(2x+y+z\right)
\left(\frac1{2x}+\frac1y+\frac1z\right)\ge9.
$$

State exactly when equality occurs. Apply three-variable AM-GM to the correctly chosen terms.

#### Correction

Apply three-variable AM-GM to the first parenthesis:

$$
2x+y+z\ge3\sqrt[3]{2xyz}.
$$

Apply it to the reciprocal terms:

$$
\frac1{2x}+\frac1y+\frac1z
\ge3\sqrt[3]{\frac1{2xyz}}.
$$

Since $x,y,z>0$, multiply the two positive inequalities:

$$
\left(2x+y+z\right)
\left(\frac1{2x}+\frac1y+\frac1z\right)
\ge9\sqrt[3]{2xyz}\sqrt[3]{\frac1{2xyz}}=9.
$$

Therefore:

$$
\boxed{\left(2x+y+z\right)
\left(\frac1{2x}+\frac1y+\frac1z\right)\ge9}.
$$

Equality requires the terms in the first AM-GM application to be equal:

$$
2x=y=z.
$$

The reciprocal terms then have the same equality condition. Thus:

$$
\boxed{2x=y=z>0}.
$$

Send your attempts before asking for solutions. Start with A-C for the first round.

## Completion standard

- [ ] Use two-variable AM-GM correctly
- [ ] Solve equality conditions, not just bounds
- [ ] Complete Problems A-F
- [ ] Use three-variable AM-GM
- [ ] Complete one fresh minimum or maximum problem without notes
