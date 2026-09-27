# Lesson 06 - Nonnegative Squares and Basic Inequality Proofs

<span class="nmao-badge nmao-study">LESSON</span>

## Objective

Learn to build elementary olympiad inequalities from one fundamental fact:

$$
t^2\ge0
\qquad\text{for every real }t.
$$

You will also learn how to find the equality case: the situation in which the inequality becomes an equality.

## 1. The main idea

If we want to prove that an expression is nonnegative, try to rewrite it as a square or as a sum of squares.

For every real $a$ and $b$:

$$
(a-b)^2\ge0.
$$

Expand:

$$
a^2-2ab+b^2\ge0.
$$

Rearrange:

$$
a^2+b^2\ge2ab.
$$

This is one of the most useful basic inequalities. Equality holds exactly when:

$$
(a-b)^2=0
\quad\Longleftrightarrow\quad
a=b.
$$

## 2. Completing the square

Suppose we want to prove:

$$
x^2-6x+10\ge1.
$$

Complete the square:

$$
x^2-6x+10=(x-3)^2+1.
$$

Since $(x-3)^2\ge0$:

$$
(x-3)^2+1\ge1.
$$

Equality holds when $x=3$.

The general pattern is:

$$
x^2+bx+c
=\left(x+\frac b2\right)^2+c-\frac{b^2}{4}.
$$

## 3. Three-variable square identities

The following identity is especially important:

$$
(a-b)^2+(b-c)^2+(c-a)^2\ge0.
$$

Expand the left-hand side:

$$
2(a^2+b^2+c^2-ab-bc-ca)\ge0.
$$

Therefore:

$$
a^2+b^2+c^2\ge ab+bc+ca.
$$

Equality holds when all three squares are zero, which means:

$$
a=b=c.
$$

## 4. A useful sum-of-squares proof

To prove:

$$
x^2+y^2+z^2\ge xy+yz+zx,
$$

write the difference between the two sides:

$$
x^2+y^2+z^2-xy-yz-zx
=\frac12\left((x-y)^2+(y-z)^2+(z-x)^2\right).
$$

The right-hand side is nonnegative, so the desired inequality follows. This is a complete olympiad proof because it explains both the inequality and its equality condition.

## 5. Products and nonnegative variables

If $x\ge0$ and $y\ge0$, then:

$$
(x-y)^2\ge0
\quad\Longrightarrow\quad
x^2+y^2\ge2xy.
$$

Since both sides are nonnegative, taking square roots gives:

$$
\frac{x+y}{2}\ge\sqrt{xy}.
$$

For now, focus on the square form. It is safer in proofs and works naturally with algebraic expressions.

### Part 5 explained slowly

Assume $x\ge0$ and $y\ge0$. Start with the square:

$$
(x-y)^2\ge0.
$$

Expand it:

$$
x^2-2xy+y^2\ge0.
$$

Add $2xy$ to both sides:

$$
x^2+y^2\ge2xy.
$$

This is the main result of Part 5. It says that the sum of the two squares is at least twice their product.

To understand the next form, add $2xy$ to both sides once more:

$$
x^2+2xy+y^2\ge4xy.
$$

Recognize the two sides as squares:

$$
(x+y)^2\ge4xy.
$$

Because $x\ge0$ and $y\ge0$, both $x+y$ and $\sqrt{xy}$ are nonnegative. Therefore taking square roots does not create a sign ambiguity:

$$
x+y\ge2\sqrt{xy}.
$$

Divide by $2$, which is positive:

$$
\boxed{\frac{x+y}{2}\ge\sqrt{xy}}.
$$

The left side is the average of $x$ and $y$. The right side is their geometric mean. The inequality says that for nonnegative numbers, the ordinary average is at least the geometric mean.

For example, if $x=1$ and $y=9$:

$$
\frac{x+y}{2}=5,
\qquad
\sqrt{xy}=3,
$$

so the inequality is true. Equality occurs when:

$$
(x-y)^2=0\quad\Longleftrightarrow\quad x=y.
$$

The square inequality itself is valid for all real $x,y$. The conditions $x\ge0$ and $y\ge0$ are needed for the square-root interpretation and for the geometric mean to be a real nonnegative quantity.

## 6. How to search for a proof

When asked to prove an inequality:

1. Move everything to one side.
2. Ask whether the difference factors or completes a square.
3. Try a square such as $(a-b)^2$.
4. For three variables, try a sum of pairwise squares.
5. Find equality by setting every square used in the proof equal to zero.

Never multiply an inequality by an expression of unknown sign without first determining its sign.

## Practice

### Basic

**A.** Prove that for every real $x$:

$$
x^2+4x+7\ge3.
$$

State when equality holds.

**B.** Prove that for all real $a,b$:

$$
a^2+b^2\ge2ab.
$$

State the equality condition.

### Solution to B

Start with the fact that a square is nonnegative:

$$
(a-b)^2\ge0.
$$

Expand:

$$
a^2-2ab+b^2\ge0.
$$

Add $2ab$ to both sides:

$$
\boxed{a^2+b^2\ge2ab}.
$$

Equality occurs exactly when the square is zero:

$$
(a-b)^2=0\quad\Longrightarrow\quad\boxed{a=b}.
$$

**C.** Prove that for all real $x,y,z$:

$$
x^2+y^2+z^2\ge xy+yz+zx.
$$

State the equality condition.

### Solution to C

Move the right-hand side to the left:

$$
x^2+y^2+z^2-xy-yz-zx.
$$

Rewrite this difference as a sum of squares:

$$
x^2+y^2+z^2-xy-yz-zx
=\frac12\left((x-y)^2+(y-z)^2+(z-x)^2\right).
$$

Every square is nonnegative, so the right-hand side is nonnegative. Therefore:

$$
\boxed{x^2+y^2+z^2\ge xy+yz+zx}.
$$

Equality occurs when all three squares are zero:

$$
x-y=0,\qquad y-z=0,\qquad z-x=0.
$$

Thus:

$$
\boxed{x=y=z}.
$$

### Intermediate

**D.** Find the minimum value of:

$$
x^2-8x+19.
$$

State the value of $x$ at which the minimum occurs.

### Solution to D

Complete the square:

$$
x^2-8x+19=(x-4)^2-16+19=(x-4)^2+3.
$$

Since $(x-4)^2\ge0$ for every real $x$:

$$
(x-4)^2+3\ge3.
$$

Therefore the minimum value is:

$$
\boxed{3}.
$$

Equality occurs when:

$$
(x-4)^2=0\quad\Longrightarrow\quad\boxed{x=4}.
$$

### Extra practice: like D

Find the minimum value of:

$$
2x^2-12x+25.
$$

State the value of $x$ at which the minimum occurs. Remember to factor out the coefficient of $x^2$ before completing the square.

#### Correction

First factor out the coefficient of $x^2$ from the variable terms:

$$
2x^2-12x+25=2(x^2-6x)+25.
$$

Complete the square inside the parentheses:

$$
2\left((x-3)^2-9\right)+25
=2(x-3)^2-18+25
=2(x-3)^2+7.
$$

Since $2(x-3)^2\ge0$:

$$
2(x-3)^2+7\ge7.
$$

Therefore the minimum value is:

$$
\boxed{7}.
$$

Equality occurs when:

$$
(x-3)^2=0\quad\Longrightarrow\quad\boxed{x=3}.
$$

### Why we did not divide the whole expression

The coefficient $2$ is factored only from the terms containing $x$:

$$
2x^2-12x+25=2(x^2-6x)+25.
$$

The constant $25$ stays outside because it is not multiplied by $2$. Then:

$$
2(x^2-6x)+25
=2\left((x-3)^2-9\right)+25
=2(x-3)^2+7.
$$

So we do not automatically divide the whole expression. We may divide both sides of an equation by a nonzero number. For an inequality, division by a positive number preserves its direction, while division by a negative number reverses it.

### Extra practice: leading coefficient

Find the minimum value of:

$$
3x^2+12x+14.
$$

State the value of $x$ at which the minimum occurs. Factor the coefficient of $x^2$ from the variable terms before completing the square.

#### Correction

Factor $3$ from the variable terms:

$$
3x^2+12x+14=3(x^2+4x)+14.
$$

Complete the square inside the parentheses:

$$
3\left((x+2)^2-4\right)+14
=3(x+2)^2-12+14
=3(x+2)^2+2.
$$

Since $3(x+2)^2\ge0$:

$$
3(x+2)^2+2\ge2.
$$

Therefore the minimum value is:

$$
\boxed{2}.
$$

Equality occurs when:

$$
(x+2)^2=0\quad\Longrightarrow\quad\boxed{x=-2}.
$$

### Final drill before E

Find the minimum value of:

$$
4x^2-16x+21.
$$

State the value of $x$ at which the minimum occurs. Write the solution independently using the leading-coefficient method.

#### Correction

Factor $4$ from the variable terms:

$$
4x^2-16x+21=4(x^2-4x)+21.
$$

Complete the square:

$$
4\left((x-2)^2-4\right)+21
=4(x-2)^2-16+21
=4(x-2)^2+5.
$$

Since $4(x-2)^2\ge0$:

$$
4(x-2)^2+5\ge5.
$$

Therefore the minimum value is:

$$
\boxed{5}.
$$

Equality occurs when:

$$
(x-2)^2=0\quad\Longrightarrow\quad\boxed{x=2}.
$$

**E.** Prove that for all real $a,b,c$:

$$
a^2+b^2+c^2\ge ab+ac+bc.
$$

Give a proof based on a sum of squares, not just a citation of the result.

### Solution to E

Move the right-hand side to the left:

$$
a^2+b^2+c^2-ab-ac-bc.
$$

Rewrite the difference as a sum of squares:

$$
a^2+b^2+c^2-ab-ac-bc
=\frac12\left((a-b)^2+(a-c)^2+(b-c)^2\right).
$$

Every square is nonnegative, so the right-hand side is nonnegative. Therefore:

$$
\boxed{a^2+b^2+c^2\ge ab+ac+bc}.
$$

Equality occurs when all three squares are zero:

$$
a=b,\qquad a=c,\qquad b=c.
$$

Thus the equality condition is:

$$
\boxed{a=b=c}.
$$

**F.** Let $x,y\ge0$. Prove that:

$$
x^2+y^2\ge2xy,
$$

then determine when equality holds.

### Solution to F

Start with the nonnegative square:

$$
(x-y)^2\ge0.
$$

Expand:

$$
x^2-2xy+y^2\ge0.
$$

Add $2xy$ to both sides:

$$
\boxed{x^2+y^2\ge2xy}.
$$

Equality occurs exactly when the square is zero:

$$
(x-y)^2=0\quad\Longrightarrow\quad\boxed{x=y}.
$$

The assumption $x,y\ge0$ is not needed for this square inequality itself; it is useful when connecting it to the square-root form from Part 5.

### Extra practice: like F

Let $x,y\ge0$. Prove that:

$$
4x^2+9y^2\ge12xy.
$$

You may use either the direct square method or the square-root route. State exactly when equality holds.

### How the square-root identity proves the original inequality

The square-root form says that for nonnegative numbers $u$ and $v$:

$$
\frac{u+v}{2}\ge\sqrt{uv}.
$$

To prove the original inequality for $x,y\ge0$, choose:

$$
u=x^2,\qquad v=y^2.
$$

These are nonnegative, so the identity applies:

$$
\frac{x^2+y^2}{2}
\ge\sqrt{x^2y^2}.
$$

Because $x,y\ge0$:

$$
\sqrt{x^2y^2}=\sqrt{(xy)^2}=xy.
$$

Therefore:

$$
\frac{x^2+y^2}{2}\ge xy.
$$

Multiply both sides by $2$:

$$
\boxed{x^2+y^2\ge2xy}.
$$

That is exactly the original inequality. The square-root identity is proving it because we applied the identity to the two numbers $x^2$ and $y^2$.

For the scaled exercise, choose $u=4x^2$ and $v=9y^2$. Then:

$$
\frac{4x^2+9y^2}{2}
\ge\sqrt{36x^2y^2}=6xy.
$$

Multiplying by $2$ gives:

$$
\boxed{4x^2+9y^2\ge12xy}.
$$

There is also a second route. Starting from the square-root form for $x$ and $y$:

$$
x+y\ge2\sqrt{xy},
$$

both sides are nonnegative, so squaring is safe:

$$
(x+y)^2\ge4xy.
$$

Expand and subtract $2xy$ from both sides:

$$
x^2+y^2\ge2xy.
$$

Both routes are valid. The first route is usually cleaner because it applies the identity directly to the desired terms.

### Solution to the scaled exercise: direct square method

Start with the nonnegative square:

$$
(2x-3y)^2\ge0.
$$

Expand:

$$
4x^2-12xy+9y^2\ge0.
$$

Add $12xy$ to both sides:

$$
\boxed{4x^2+9y^2\ge12xy}.
$$

Equality occurs when:

$$
(2x-3y)^2=0
\quad\Longrightarrow\quad
\boxed{2x=3y}.
$$

### Solution to the scaled exercise: square-root method

Because $x,y\ge0$, the numbers $4x^2$ and $9y^2$ are nonnegative. Apply the square-root identity to these two numbers:

$$
\frac{4x^2+9y^2}{2}
\ge\sqrt{(4x^2)(9y^2)}.
$$

Simplify:

$$
\sqrt{(4x^2)(9y^2)}
=\sqrt{36x^2y^2}
=6xy.
$$

Therefore:

$$
\frac{4x^2+9y^2}{2}\ge6xy.
$$

Multiply by $2$:

$$
\boxed{4x^2+9y^2\ge12xy}.
$$

Equality occurs when the two inputs to the square-root identity are equal:

$$
4x^2=9y^2.
$$

Since $x,y\ge0$, this is equivalent to:

$$
\boxed{2x=3y}.
$$

Send your attempts before asking for the solutions. Start with A-C for the first round.

### Solution to A

We want to prove:

$$
x^2+4x+7\ge3.
$$

Complete the square using the first two terms:

$$
x^2+4x+7=(x+2)^2-4+7=(x+2)^2+3.
$$

Since a square is nonnegative:

$$
(x+2)^2\ge0.
$$

Therefore:

$$
(x+2)^2+3\ge3,
$$

which proves the inequality. Equality occurs when:

$$
(x+2)^2=0\quad\Longrightarrow\quad\boxed{x=-2}.
$$

## Clarification: completing the square and pairwise squares

### The general completing-square pattern

Start with:

$$
x^2+bx+c.
$$

The coefficient of $x$ is $b$. When we expand a square of the form $(x+r)^2$, we get:

$$
(x+r)^2=x^2+2rx+r^2.
$$

To make the middle term equal to $bx$, choose $2r=b$, so $r=b/2$:

$$
\left(x+\frac b2\right)^2
=x^2+bx+\frac{b^2}{4}.
$$

This square contains the correct $x^2+bx$, but its constant term is $b^2/4$ instead of $c$. Correct the constant term by adding and subtracting $b^2/4$:

$$
x^2+bx+c
=x^2+bx+\frac{b^2}{4}+c-\frac{b^2}{4}.
$$

Therefore:

$$
\boxed{x^2+bx+c
=\left(x+\frac b2\right)^2+c-\frac{b^2}{4}}.
$$

The formula is just a compact version of the add-and-subtract trick. For example, when $b=-6$ and $c=10$:

$$
x^2-6x+10
=\left(x-3\right)^2+10-9
=(x-3)^2+1.
$$

If the coefficient of $x^2$ is not $1$, factor it out first. For example:

$$
2x^2+8x+3=2(x^2+4x)+3
=2\left((x+2)^2-4\right)+3.
$$

### Expanding the three pairwise squares

Expand each square separately:

$$
(a-b)^2=a^2-2ab+b^2,
$$

$$
(b-c)^2=b^2-2bc+c^2,
$$

and

$$
(c-a)^2=c^2-2ca+a^2.
$$

Now add the three lines:

$$
\begin{aligned}
&(a-b)^2+(b-c)^2+(c-a)^2\\
&=(a^2-2ab+b^2)+(b^2-2bc+c^2)+(c^2-2ca+a^2)\\
&=2a^2+2b^2+2c^2-2ab-2bc-2ca\\
&=2(a^2+b^2+c^2-ab-bc-ca).
\end{aligned}
$$

Because every square is nonnegative, the left side is at least zero. Thus:

$$
2(a^2+b^2+c^2-ab-bc-ca)\ge0.
$$

### Why can we divide by two?

Yes, divide both sides by $2$:

$$
\frac{2(a^2+b^2+c^2-ab-bc-ca)}2
\ge\frac02.
$$

Since $2$ is positive, the inequality direction stays the same. Also, $0/2=0$. Therefore:

$$
a^2+b^2+c^2-ab-bc-ca\ge0.
$$

Finally, add $ab+bc+ca$ to both sides:

$$
\boxed{a^2+b^2+c^2\ge ab+bc+ca}.
$$

Equality is obtained when all three squares are zero, which means $a=b=c$.

### Extra practice: like A

Prove that for every real $x$:

$$
x^2-10x+29\ge4.
$$

State exactly when equality holds. Use completing the square and do not look for the solution yet.

#### Correction

Complete the square using the first two terms:

$$
x^2-10x+29=(x-5)^2-25+29=(x-5)^2+4.
$$

Since $(x-5)^2\ge0$:

$$
(x-5)^2+4\ge4.
$$

Therefore the inequality is proved. Equality occurs when:

$$
(x-5)^2=0\quad\Longrightarrow\quad\boxed{x=5}.
$$

## Completion standard

- [ ] Explain why a square is nonnegative
- [ ] Complete A-F
- [ ] State equality conditions correctly
- [ ] Write one full sum-of-squares proof
- [ ] Solve one fresh inequality without notes
