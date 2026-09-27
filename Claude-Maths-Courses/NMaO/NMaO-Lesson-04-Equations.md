# Lesson 04 - Linear and Quadratic Equations

<span class="nmao-badge nmao-study">LESSON</span>

## Objective

Solve equations systematically while preserving equivalence, checking restrictions, and rejecting extraneous solutions.

## 1. Linear equations

The goal is to isolate the variable using inverse operations.

Example:

$$
3x-7=11.
$$

Add $7$:

$$
3x=18.
$$

Divide by $3$:

$$
x=6.
$$

Every operation must be applied to both sides.

## 2. Equations with fractions

First record restrictions from denominators. Then multiply by the least common denominator.

Example:

$$
\frac{x+1}{2}=\frac{x-3}{3}.
$$

There are no variable denominators. Multiply by $6$:

$$
3(x+1)=2(x-3).
$$

Expand:

$$
3x+3=2x-6.
$$

Therefore:

$$
x=-9.
$$

## 3. Quadratic equations by factorisation

Move everything to one side, factor, then use the zero-product rule:

$$
AB=0\quad\Longrightarrow\quad A=0\text{ or }B=0.
$$

Example:

$$
x^2-5x+6=0.
$$

Factor:

$$
(x-2)(x-3)=0.
$$

Therefore:

$$
x=2\quad\text{or}\quad x=3.
$$

## 4. Quadratic formula

For

$$
ax^2+bx+c=0,\qquad a\ne0,
$$

define the discriminant:

$$
\Delta=b^2-4ac.
$$

The solutions are:

$$
x=\frac{-b\pm\sqrt{\Delta}}{2a}.
$$

The discriminant tells us:

- $\Delta>0$: two distinct real solutions;
- $\Delta=0$: one repeated real solution;
- $\Delta<0$: no real solutions.

Example:

$$
2x^2+3x-2=0.
$$

Here $a=2$, $b=3$, and $c=-2$, so

$$
\Delta=3^2-4(2)(-2)=25.
$$

Thus:

$$
x=\frac{-3\pm5}{4},
$$

giving $x=\frac12$ or $x=-2$.

## 5. Extraneous solutions

Squaring both sides can create solutions that were not valid in the original equation.

Example:

$$
\sqrt{x+1}=x-1.
$$

The right side must be nonnegative, so $x\ge1$. Squaring gives:

$$
x+1=(x-1)^2,
$$

which may produce candidates. Every candidate must be checked in the original equation.

## 6. Equations with denominators

For an equation such as

$$
\frac{x-1}{x+2}=3,
$$

first state $x\ne-2$, then multiply by $x+2$:

$$
x-1=3(x+2).
$$

The restriction must remain in the final answer.

## Equation-solving checklist

- [x] Move all terms to one side for a quadratic.
- [x] Factor before using the quadratic formula.
- [x] Record denominator restrictions first.
- [x] Check solutions after squaring or multiplying by expressions involving variables.
- [x] Substitute final answers into the original equation.

## Practice

### Basic

**A.** Solve:

$$
3x-7=11.
$$

**B.** Solve:

$$
\frac{x+2}{3}=\frac{x-1}{2}.
$$

**C.** Solve:

$$
x^2-7x+12=0.
$$

### Intermediate

**D.** Solve:

$$
2x^2+x-3=0.
$$

**E.** Solve and check:

$$
\sqrt{x+5}=x-1.
$$

**F.** Solve and state the restriction:

$$
\frac{x-1}{x+2}=3.
$$

Send your attempts before asking for solutions.

## Answer key and worked solutions

> [!warning] Try the problems first
> Use this section only after writing your own attempt. For each answer, check the result in the original equation.

### A

$$
3x-7=11
$$

Add $7$ to both sides:

$$
3x=18.
$$

Divide by $3$:

$$
\boxed{x=6}.
$$

Check:

$$
3(6)-7=18-7=11.
$$

### B

$$
\frac{x+2}{3}=\frac{x-1}{2}
$$

Multiply both sides by $6$:

$$
2(x+2)=3(x-1).
$$

Expand:

$$
2x+4=3x-3.
$$

Subtract $2x$ and add $3$:

$$
7=x.
$$

Therefore:

$$
\boxed{x=7}.
$$

Check:

$$
\frac{7+2}{3}=3,
\qquad
\frac{7-1}{2}=3.
$$

### C

$$
x^2-7x+12=0
$$

Find two numbers with product $12$ and sum $-7$: they are $-3$ and $-4$.

$$
x^2-7x+12=(x-3)(x-4).
$$

Using the zero-product rule:

$$
(x-3)(x-4)=0
\quad\Longrightarrow\quad
x-3=0\text{ or }x-4=0.
$$

Therefore:

$$
\boxed{x=3\text{ or }x=4}.
$$

### D

$$
2x^2+x-3=0
$$

Split the middle term:

$$
2x^2+x-3=2x^2+3x-2x-3.
$$

Group:

$$
2x^2+3x-2x-3=x(2x+3)-1(2x+3).
$$

Factor:

$$
(2x+3)(x-1)=0.
$$

Thus:

$$
2x+3=0\quad\text{or}\quad x-1=0,
$$

so

$$
\boxed{x=-\frac32\text{ or }x=1}.
$$

### E

$$
\sqrt{x+5}=x-1
$$

Because a square root is nonnegative, the right-hand side must satisfy

$$
x-1\ge0\quad\Longrightarrow\quad x\ge1.
$$

Now square both sides:

$$
x+5=(x-1)^2=x^2-2x+1.
$$

Move everything to one side:

$$
x^2-3x-4=0.
$$

Factor:

$$
(x-4)(x+1)=0.
$$

The candidates are

$$
x=4\quad\text{or}\quad x=-1.
$$

The condition $x\ge1$ rejects $x=-1$. Check $x=4$ in the original equation:

$$
\sqrt{4+5}=\sqrt9=3=4-1.
$$

Therefore:

$$
\boxed{x=4}.
$$

### F

$$
\frac{x-1}{x+2}=3
$$

First record the restriction from the denominator:

$$
x+2\ne0\quad\Longrightarrow\quad x\ne-2.
$$

Multiply both sides by $x+2$:

$$
x-1=3(x+2).
$$

Expand:

$$
x-1=3x+6.
$$

Rearrange:

$$
-7=2x,
$$

so

$$
\boxed{x=-\frac72},
\qquad x\ne-2.
$$

The solution is allowed because $-\frac72\ne-2$. Check:

$$
\frac{-\frac72-1}{-\frac72+2}
=\frac{-\frac92}{-\frac32}=3.
$$

## Answer summary

$$
\boxed{\text{A: }x=6}
$$

$$
\boxed{\text{B: }x=7}
$$

$$
\boxed{\text{C: }x=3,4}
$$

$$
\boxed{\text{D: }x=-\frac32,1}
$$

$$
\boxed{\text{E: }x=4}
$$

$$
\boxed{\text{F: }x=-\frac72,\quad x\ne-2}
$$

## Extra practice: transition check

### G - Like D

Solve by factorisation:

$$
3x^2-x-2=0.
$$

### H - Like E

Solve and check in the original equation:

$$
\sqrt{2x+3}=x.
$$

Remember to state the condition forced by the square root before squaring. Send your attempts before asking for the solutions.

### Extra-practice solutions

#### G

$$
3x^2-x-2=0
$$

Split the middle term:

$$
3x^2-x-2=3x^2-3x+2x-2.
$$

Group and factor:

$$
3x^2-3x+2x-2=3x(x-1)+2(x-1)
=(3x+2)(x-1).
$$

Therefore:

$$
(3x+2)(x-1)=0,
$$

so

$$
\boxed{x=-\frac23\text{ or }x=1}.
$$

#### H

$$
\sqrt{2x+3}=x
$$

The left-hand side is nonnegative, so the right-hand side must be nonnegative:

$$
x\ge0.
$$

Square both sides:

$$
2x+3=x^2.
$$

Move everything to one side and factor:

$$
x^2-2x-3=0,
$$

$$
(x-3)(x+1)=0.
$$

The candidates are

$$
x=3\quad\text{or}\quad x=-1.
$$

The condition $x\ge0$ rejects $x=-1$. Check $x=3$ in the original equation:

$$
\sqrt{2(3)+3}=\sqrt9=3.
$$

Therefore:

$$
\boxed{x=3}.
$$

### I - Like H

Solve and check in the original equation:

$$
\sqrt{x+6}=x.
$$

Remember to determine the allowed values of $x$ before squaring. Send your attempt when you are finished.

#### Solution to I

$$
\sqrt{x+6}=x
$$

The left-hand side is nonnegative, so the right-hand side must be nonnegative:

$$
x\ge0.
$$

Now square both sides:

$$
x+6=x^2.
$$

Rearrange and factor:

$$
x^2-x-6=0,
$$

$$
(x-3)(x+2)=0.
$$

The candidates are

$$
x=3\quad\text{or}\quad x=-2.
$$

The condition $x\ge0$ rejects $x=-2$. Check $x=3$ in the original equation:

$$
\sqrt{3+6}=\sqrt9=3.
$$

Therefore:

$$
\boxed{x=3}.
$$

### A04 transition exercise

Solve and check in the original equation:

$$
\sqrt{2x+8}=x+1.
$$

Write every step: determine the allowed values, square, solve, reject any invalid candidate, and check the final answer in the original equation. Do this one independently before beginning A05.

#### Transition solution

$$
\sqrt{2x+8}=x+1
$$

The square root is nonnegative, so the right-hand side must also be nonnegative:

$$
x+1\ge0\quad\Longrightarrow\quad x\ge-1.
$$

This condition also guarantees that the radicand is positive, so we can square both sides:

$$
2x+8=(x+1)^2.
$$

Expand:

$$
2x+8=x^2+2x+1.
$$

Cancel $2x$ from both sides:

$$
8=x^2+1,
$$

so

$$
x^2=7.
$$

The candidates are

$$
x=\sqrt7\quad\text{or}\quad x=-\sqrt7.
$$

Since $-\sqrt7<-1$, it violates the condition $x\ge-1$ and must be rejected. Check the remaining candidate:

$$
\sqrt{2\sqrt7+8}=\sqrt7+1,
$$

because both sides are nonnegative and their squares are equal.

Therefore:

$$
\boxed{x=\sqrt7}.
$$

## Completion standard

- [ ] Complete A-F
- [ ] Check every solution in the original equation
- [ ] Correct all errors
- [ ] Solve one fresh equation without notes
