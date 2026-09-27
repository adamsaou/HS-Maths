# Lesson 08 - Cauchy-Schwarz and Useful Sum Estimates

<span class="nmao-badge nmao-study">LESSON</span>

## Objective

Understand what Cauchy-Schwarz is measuring before learning its formulas. Then use that idea to estimate ordinary sums, reciprocal expressions, and weighted fractions.

## 0. Start here: the idea before the formula

Imagine that we have two lists of numbers:

$$
(a,b)
\qquad\text{and}\qquad
(c,d).
$$

We pair the entries in the same positions and add their products:

$$
ac+bd.
$$

This is the **matching score** of the two lists. Cauchy-Schwarz answers this question:

> How large can the matching score be, given the sizes of the two lists?

The sizes are measured using squares:

$$
a^2+b^2
\qquad\text{and}\qquad
c^2+d^2.
$$

The matching score is largest when the lists have the same proportion.

### A perfectly matched example

Take:

$$
(a,b)=(1,2),
\qquad
(c,d)=(2,4).
$$

The second list is twice the first, so they are perfectly matched. Their matching score is:

$$
ac+bd=1\cdot2+2\cdot4=10.
$$

Its square is:

$$
(ac+bd)^2=100.
$$

The product of the two squared sizes is:

$$
(a^2+b^2)(c^2+d^2)
=(1^2+2^2)(2^2+4^2)
=5\cdot20
=100.
$$

The two sides are equal because the lists have the same proportion.

### A mismatched example

Now compare:

$$
(1,2)
\qquad\text{and}\qquad
(4,2).
$$

Their matching score gives:

$$
(1\cdot4+2\cdot2)^2=8^2=64,
$$

but the product of their squared sizes is:

$$
(1^2+2^2)(4^2+2^2)=5\cdot20=100.
$$

The score is now below the maximum because the lists do not have the same proportion.

This is the intuition behind Cauchy-Schwarz:

> Matching gives equality; mismatch creates a gap.

## 1. The two-variable form

For all real numbers $a,b,c,d$:

$$
\boxed{(a^2+b^2)(c^2+d^2)\ge(ac+bd)^2}.
$$

The expression $ac+bd$ is the matching score introduced above. Cauchy-Schwarz says that its square cannot exceed the product of the two squared sizes.

The pairs can also be viewed as arrows, and $ac+bd$ is then called their dot product. That geometric language is useful later, but it is not needed to understand the first applications.

Equality occurs exactly when the two lists are perfectly matched, meaning that one is a multiple of the other. There is a real number $k$ such that:

$$
a=kc,\qquad b=kd.
$$

If the denominators are nonzero, this can be written as:

$$
\frac ac=\frac bd.
$$

## 2. The proof by a nonnegative square

The proof measures the mismatch. For the two lists, that mismatch is:

$$
ad-bc.
$$

If the lists have the same proportion, then $ad=bc$ and the mismatch is zero. Otherwise it is nonzero. In either case, its square cannot be negative:

$$
(ad-bc)^2\ge0.
$$

Now expand the difference between the two sides of the desired inequality:

$$
\begin{aligned}
&(a^2+b^2)(c^2+d^2)-(ac+bd)^2\\
&=(a^2c^2+a^2d^2+b^2c^2+b^2d^2)
 -(a^2c^2+2abcd+b^2d^2)\\
&=a^2d^2-2abcd+b^2c^2\\
&=(ad-bc)^2\ge0.
\end{aligned}
$$

This identity says that the gap between the two sides is exactly the square of the mismatch. Since the gap is nonnegative, the first expression is at least the second:

$$
(a^2+b^2)(c^2+d^2)\ge(ac+bd)^2.
$$

## 3. Screenshot algebra clarification

The earlier line began with:

$$
a^2d^2-2abcd+b^2c^2\ge0.
$$

If we add $2abcd$ to both sides, we get:

$$
a^2d^2-2abcd+b^2c^2+2abcd
\ge0+2abcd.
$$

The opposite terms cancel on the left:

$$
\boxed{a^2d^2+b^2c^2\ge2abcd}.
$$

The version that still has $+2abcd$ on the left is an algebra mistake. This rearrangement is also unnecessary for proving Cauchy-Schwarz; the difference identity in Section 2 is the clean proof.

## 4. Equal-coefficient sum estimates

Suppose we want to estimate the ordinary sum $a+b$. First notice that it can be written as a matching score:

$$
a+b=a\cdot1+b\cdot1.
$$

This tells us to compare $(a,b)$ with the pair $(1,1)$:

$$
(a^2+b^2)(1^2+1^2)\ge(a+b)^2.
$$

Therefore:

$$
\boxed{(a+b)^2\le2(a^2+b^2)}.
$$

For three variables, the same idea gives:

$$
\boxed{(a+b+c)^2\le3(a^2+b^2+c^2)}.
$$

Equality occurs when all the variables are equal.

### Why the equality condition makes sense

The pair $(1,1)$ is perfectly balanced. To match its proportion, $(a,b)$ must also be balanced, so $a=b$.

Likewise, the triple $(1,1,1)$ is perfectly balanced. The triple $(a,b,c)$ matches it exactly when $a=b=c$.

So for a fixed value of $a^2+b^2+c^2$, the sum $a+b+c$ is largest when the available squared size is shared equally.

## 5. A maximum from a fixed sum of squares

Suppose:

$$
x^2+y^2+z^2=14.
$$

Cauchy-Schwarz gives:

$$
(x+y+z)^2\le3(x^2+y^2+z^2)=42.
$$

Hence:

$$
|x+y+z|\le\sqrt{42}.
$$

Therefore the maximum value of $x+y+z$ is:

$$
\boxed{\sqrt{42}}.
$$

Equality for the maximum requires:

$$
\boxed{x=y=z=\sqrt{\frac{14}{3}}}.
$$

The intuition is that making one variable much larger forces the others to become smaller because the total $x^2+y^2+z^2$ is fixed. That imbalance wastes part of the possible ordinary sum. Equal values produce the largest sum.

## 6. Reciprocal sums

Do not try to guess the square roots mechanically. Start by looking at what we want Cauchy-Schwarz to create:

$$
x+y+z
\qquad\text{and}\qquad
\frac1x+\frac1y+\frac1z.
$$

Because Cauchy-Schwarz squares the entries in each list, an entry whose square is $x$ must be $\sqrt{x}$. An entry whose square is $1/x$ must be $1/\sqrt{x}$.

Therefore, for positive $x,y,z$, use the two lists:

$$
\left(\sqrt{x},\sqrt{y},\sqrt{z}\right)
$$

and

$$
\left(\frac1{\sqrt{x}},\frac1{\sqrt{y}},\frac1{\sqrt{z}}\right).
$$

Each pair multiplies to $1$:

$$
\sqrt{x}\cdot\frac1{\sqrt{x}}=1.
$$

There are three variables, so the matching score is $1+1+1=3$. Cauchy-Schwarz gives:

$$
3^2\le
\left(x+y+z\right)
\left(\frac1x+\frac1y+\frac1z\right).
$$

Thus:

$$
\boxed{\left(x+y+z\right)
\left(\frac1x+\frac1y+\frac1z\right)\ge9}.
$$

Equality occurs when the two vectors are proportional, which gives:

$$
\boxed{x=y=z}.
$$

This is a second proof of the A07 reciprocal problem.

### Reciprocal sums explained slowly

The target has the shape:

$$
\left(x+y+z\right)
\left(\frac1x+\frac1y+\frac1z\right).
$$

To use Cauchy-Schwarz, choose one vector whose squared length produces the first parenthesis and another whose squared length produces the second parenthesis.

Set:

$$
U=\left(\sqrt{x},\sqrt{y},\sqrt{z}\right),
$$

and

$$
V=\left(\frac1{\sqrt{x}},\frac1{\sqrt{y}},\frac1{\sqrt{z}}\right).
$$

This choice is deliberate. Squaring the entries of $U$ gives:

$$
\|U\|^2=x+y+z.
$$

Squaring the entries of $V$ gives:

$$
\|V\|^2=\frac1x+\frac1y+\frac1z.
$$

Now calculate their dot product:

$$
\begin{aligned}
U\cdot V
&=\sqrt{x}\cdot\frac1{\sqrt{x}}
 +\sqrt{y}\cdot\frac1{\sqrt{y}}
 +\sqrt{z}\cdot\frac1{\sqrt{z}}\\
&=1+1+1=3.
\end{aligned}
$$

Cauchy-Schwarz says:

$$
(U\cdot V)^2\le\|U\|^2\|V\|^2.
$$

Substitute the three quantities we calculated:

$$
3^2\le
\left(x+y+z\right)
\left(\frac1x+\frac1y+\frac1z\right).
$$

Therefore:

$$
\boxed{\left(x+y+z\right)
\left(\frac1x+\frac1y+\frac1z\right)\ge9}.
$$

### Equality intuition

Equality in Cauchy-Schwarz occurs when the two vectors are proportional:

$$
U=kV.
$$

From the first coordinate:

$$
\sqrt{x}=\frac{k}{\sqrt{x}}
\quad\Longrightarrow\quad x=k.
$$

The other coordinates similarly give $y=k$ and $z=k$. Hence:

$$
\boxed{x=y=z>0}.
$$

### Recognition recipe

When you see a product of a sum and its reciprocal sum:

1. Put square roots in the first vector.
2. Put reciprocal square roots in the second vector.
3. Their squared lengths become the two sums.
4. Their dot product becomes one for each variable.
5. Square the dot product and apply Cauchy-Schwarz.

For three variables the dot product is $3$, so the lower bound is $3^2=9$. For $n$ positive variables, the same pattern gives the lower bound $n^2$.

## 7. Weighted Cauchy-Schwarz

For positive $p,q$ and real $u,v$:

$$
\boxed{\frac{u^2}{p}+\frac{v^2}{q}\ge\frac{(u+v)^2}{p+q}}.
$$

This form is easier to understand by asking which entry has square $u^2/p$. It is:

$$
\frac{u}{\sqrt p}.
$$

To make the matching product equal to $u$, pair it with $\sqrt p$:

$$
\frac{u}{\sqrt p}\cdot\sqrt p=u.
$$

This motivates applying Cauchy-Schwarz to:

$$
\left(\frac{u}{\sqrt p},\frac{v}{\sqrt q}\right)
\quad\text{and}\quad
(\sqrt p,\sqrt q).
$$

Their dot product is $u+v$, so the inequality follows. Equality occurs when the vectors are proportional:

$$
\boxed{\frac{u}{p}=\frac{v}{q}}.
$$

For more than two terms, this is often called the Engel form or Titu Andreescu's lemma.

## 8. How to choose the vectors

When using Cauchy-Schwarz, first ask what squared terms and matching products you want. Then write the two lists explicitly.

- To estimate a plain sum, pair the variables with a vector of ones.
- To create reciprocal terms, pair square roots with reciprocal square roots.
- To handle denominators, place the denominator under a square root in one vector and its square root in the other.
- After obtaining a bound, solve the proportionality condition to check equality.

## 9. First-pass learning plan

Do not try to master every form at once.

### First round

Understand these three ideas:

1. $ac+bd$ is a matching score.
2. The gap between the two sides is the nonnegative square $(ad-bc)^2$.
3. Equality means that the two lists have the same proportion.

Then attempt Problems A-C.

### Second round

Learn why square roots create reciprocal sums, then attempt Problem D.

### Third round

Learn the weighted form, then attempt Problems E-F.

## Practice

### Basic

**A.** Prove for all real $a,b$:

$$
(a+b)^2\le2(a^2+b^2).
$$

State the equality condition.

**B.** Prove for all real $x,y,z$:

$$
(x+y+z)^2\le3(x^2+y^2+z^2).
$$

State the equality condition.

**C.** Let $x^2+y^2+z^2=14$. Find the maximum value of $x+y+z$.

### Intermediate

**D.** Give a Cauchy-Schwarz proof that for $x,y,z>0$:

$$
\left(x+y+z\right)
\left(\frac1x+\frac1y+\frac1z\right)\ge9.
$$

State the equality condition.

**D-transfer.** Let $a,b,c,d>0$. Prove using Cauchy-Schwarz that:

$$
(a+b+c+d)
\left(\frac1a+\frac1b+\frac1c+\frac1d\right)
\ge16.
$$

State the equality condition. Write the two lists you use before applying the inequality.

**E.** Let $p,q>0$ and $u,v\in\mathbb R$. Prove that:

$$
\frac{u^2}{p}+\frac{v^2}{q}\ge\frac{(u+v)^2}{p+q}.
$$

State the equality condition.

**E-transfer.** Let $p,q,r>0$ and $u,v,w\in\mathbb R$. Prove that:

$$
\frac{u^2}{p}+\frac{v^2}{q}+\frac{w^2}{r}
\ge
\frac{(u+v+w)^2}{p+q+r}.
$$

State the equality condition. Begin by choosing two lists whose matching score is $u+v+w$.

**F.** Let $a,b,c>0$. Prove:

$$
\frac{a^2}{b}+\frac{b^2}{c}+\frac{c^2}{a}\ge a+b+c.
$$

Identify the equality case.

**F-transfer: final A08 check.** Let $a,b,c>0$. Prove that:

$$
\frac{a^2}{b+c}
+\frac{b^2}{c+a}
+\frac{c^2}{a+b}
\ge
\frac{a+b+c}{2}.
$$

State the equality condition. Solve this without notes or a worked example. If the proof and equality case are correct, A08 is ready for completion.

**F-transfer 2.** Let $a,b,c,d>0$. Prove that:

$$
\frac{a^2}{b+c+d}
+\frac{b^2}{c+d+a}
+\frac{c^2}{d+a+b}
+\frac{d^2}{a+b+c}
\ge
\frac{a+b+c+d}{3}.
$$

State the equality condition. Count how many times each variable appears when all four denominators are added.

Send your attempts before asking for solutions. Start with A-C for the first round.

## Solutions requested: Problems A and B

### Problem A

Apply Cauchy-Schwarz to $(a,b)$ and $(1,1)$:

$$
(a\cdot1+b\cdot1)^2
\le(a^2+b^2)(1^2+1^2).
$$

Therefore:

$$
\boxed{(a+b)^2\le2(a^2+b^2)}.
$$

Equality occurs when $(a,b)$ is proportional to $(1,1)$, so:

$$
\boxed{a=b}.
$$

### Problem B

Apply Cauchy-Schwarz to $(x,y,z)$ and $(1,1,1)$:

$$
(x\cdot1+y\cdot1+z\cdot1)^2
\le(x^2+y^2+z^2)(1^2+1^2+1^2).
$$

Therefore:

$$
\boxed{(x+y+z)^2\le3(x^2+y^2+z^2)}.
$$

Equality occurs when $(x,y,z)$ is proportional to $(1,1,1)$, so:

$$
\boxed{x=y=z}.
$$

### Problem C

From Problem B:

$$
(x+y+z)^2\le3(x^2+y^2+z^2).
$$

Using $x^2+y^2+z^2=14$ gives:

$$
(x+y+z)^2\le3\cdot14=42.
$$

Hence:

$$
x+y+z\le\sqrt{42}.
$$

Equality requires $x=y=z$. Let their common value be $t$. Then:

$$
3t^2=14,
$$

so:

$$
t=\pm\sqrt{\frac{14}{3}}.
$$

For the maximum sum, choose the positive value:

$$
x=y=z=\sqrt{\frac{14}{3}}.
$$

Therefore the maximum is:

$$
\boxed{\sqrt{42}}.
$$

### Problem D-transfer

Use the two lists:

$$
\left(\sqrt a,\sqrt b,\sqrt c,\sqrt d\right)
$$

and:

$$
\left(\frac1{\sqrt a},\frac1{\sqrt b},
\frac1{\sqrt c},\frac1{\sqrt d}\right).
$$

Their matching score is:

$$
\sqrt a\cdot\frac1{\sqrt a}
+\sqrt b\cdot\frac1{\sqrt b}
+\sqrt c\cdot\frac1{\sqrt c}
+\sqrt d\cdot\frac1{\sqrt d}
=4.
$$

Applying Cauchy-Schwarz gives:

$$
4^2\le
(a+b+c+d)
\left(\frac1a+\frac1b+\frac1c+\frac1d\right).
$$

Therefore:

$$
\boxed{
(a+b+c+d)
\left(\frac1a+\frac1b+\frac1c+\frac1d\right)
\ge16
}.
$$

Equality occurs when the two lists are proportional. This requires:

$$
\sqrt a=\frac{k}{\sqrt a},\quad
\sqrt b=\frac{k}{\sqrt b},\quad
\sqrt c=\frac{k}{\sqrt c},\quad
\sqrt d=\frac{k}{\sqrt d}.
$$

Thus $a=b=c=d=k$, so the equality condition is:

$$
\boxed{a=b=c=d>0}.
$$

### Problem E

Use the two lists:

$$
\left(\frac{u}{\sqrt p},\frac{v}{\sqrt q}\right)
\qquad\text{and}\qquad
(\sqrt p,\sqrt q).
$$

Their matching score is:

$$
\frac{u}{\sqrt p}\cdot\sqrt p
+\frac{v}{\sqrt q}\cdot\sqrt q
=u+v.
$$

Applying Cauchy-Schwarz gives:

$$
(u+v)^2
\le
\left(\frac{u^2}{p}+\frac{v^2}{q}\right)(p+q).
$$

Since $p,q>0$, we have $p+q>0$. Dividing both sides by $p+q$ therefore preserves the inequality:

$$
\boxed{
\frac{u^2}{p}+\frac{v^2}{q}
\ge\frac{(u+v)^2}{p+q}
}.
$$

Equality occurs when the two lists are proportional. For some real number $k$:

$$
\frac{u}{\sqrt p}=k\sqrt p,
\qquad
\frac{v}{\sqrt q}=k\sqrt q.
$$

Hence:

$$
u=kp,
\qquad
v=kq,
$$

which is equivalent to:

$$
\boxed{\frac up=\frac vq}.
$$

### Problem E-transfer

Use the two lists:

$$
\left(\frac{u}{\sqrt p},\frac{v}{\sqrt q},\frac{w}{\sqrt r}\right)
$$

and:

$$
(\sqrt p,\sqrt q,\sqrt r).
$$

Their matching score is:

$$
\frac{u}{\sqrt p}\cdot\sqrt p
+\frac{v}{\sqrt q}\cdot\sqrt q
+\frac{w}{\sqrt r}\cdot\sqrt r
=u+v+w.
$$

Applying Cauchy-Schwarz gives:

$$
(u+v+w)^2
\le
\left(\frac{u^2}{p}+\frac{v^2}{q}+\frac{w^2}{r}\right)
(p+q+r).
$$

Since $p,q,r>0$, we have $p+q+r>0$. Dividing by this positive quantity gives:

$$
\boxed{
\frac{u^2}{p}+\frac{v^2}{q}+\frac{w^2}{r}
\ge
\frac{(u+v+w)^2}{p+q+r}
}.
$$

Equality occurs when the two lists are proportional. For some real $k$:

$$
\frac{u}{\sqrt p}=k\sqrt p,
\qquad
\frac{v}{\sqrt q}=k\sqrt q,
\qquad
\frac{w}{\sqrt r}=k\sqrt r.
$$

Thus $u=kp$, $v=kq$, and $w=kr$. Therefore the equality condition is:

$$
\boxed{\frac up=\frac vq=\frac wr}.
$$

### Problem F

Apply the three-term weighted Cauchy-Schwarz inequality with numerators $a,b,c$ and denominators $b,c,a$:

$$
\frac{a^2}{b}+\frac{b^2}{c}+\frac{c^2}{a}
\ge
\frac{(a+b+c)^2}{b+c+a}.
$$

Since $b+c+a=a+b+c>0$, the right side simplifies to:

$$
\frac{(a+b+c)^2}{a+b+c}=a+b+c.
$$

Therefore:

$$
\boxed{
\frac{a^2}{b}+\frac{b^2}{c}+\frac{c^2}{a}
\ge a+b+c
}.
$$

Equality in the weighted form requires:

$$
\frac ab=\frac bc=\frac ca.
$$

Let the common positive ratio be $k$. Multiplying the three ratios gives:

$$
\frac ab\cdot\frac bc\cdot\frac ca=k^3.
$$

The left side equals $1$, so $k^3=1$. Since $k>0$, we have $k=1$. Hence:

$$
\boxed{a=b=c>0}.
$$

### Problem F-transfer

Apply weighted Cauchy-Schwarz with numerators $a,b,c$ and denominators $b+c,c+a,a+b$:

$$
\frac{a^2}{b+c}
+\frac{b^2}{c+a}
+\frac{c^2}{a+b}
\ge
\frac{(a+b+c)^2}
{(b+c)+(c+a)+(a+b)}.
$$

The denominator on the right simplifies to:

$$
(b+c)+(c+a)+(a+b)=2(a+b+c).
$$

Therefore:

$$
\begin{aligned}
\frac{a^2}{b+c}
+\frac{b^2}{c+a}
+\frac{c^2}{a+b}
&\ge
\frac{(a+b+c)^2}{2(a+b+c)}\\
&=\boxed{\frac{a+b+c}{2}}.
\end{aligned}
$$

The cancellation is valid because $a+b+c>0$.

Equality in weighted Cauchy-Schwarz requires:

$$
\frac{a}{b+c}
=\frac{b}{c+a}
=\frac{c}{a+b}
=k
$$

for some positive $k$. Thus:

$$
a=k(b+c),
\qquad
b=k(c+a),
\qquad
c=k(a+b).
$$

Adding these equations gives:

$$
a+b+c=2k(a+b+c).
$$

Since $a+b+c>0$, it follows that $k=1/2$. Hence:

$$
2a=b+c,
\qquad
2b=c+a,
\qquad
2c=a+b.
$$

Subtracting the first two equations gives:

$$
\begin{aligned}
2a-2b&=(b+c)-(c+a)\\
2a-2b&=b-a\\
3a-3b&=0\\
3(a-b)&=0.
\end{aligned}
$$

Because $3\ne0$, this gives $a-b=0$, so $a=b$. Substituting $b=a$ into $2a=b+c$ gives:

$$
2a=a+c,
$$

and hence $c=a$. Therefore equality occurs exactly when:

$$
\boxed{a=b=c>0}.
$$

## Completion standard

- [x] Understand the vector/proportionality meaning
- [x] Complete Problems A-F
- [x] State equality conditions correctly
- [x] Use Cauchy-Schwarz in a reciprocal problem
- [x] Use the weighted form once without notes
