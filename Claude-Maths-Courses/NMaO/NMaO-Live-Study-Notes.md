# NMaO Live Study Notes

<span class="nmao-badge nmao-study">LIVE LATEX NOTES</span>

> [!info] How this file works
> This is the readable Markdown version of our actual study explanations. Mathematics is written in LaTeX so Obsidian can render it properly. I will append the important explanations, examples, and conclusions here as we study.

> [!important] Reading rule
> All equations, algebra, proofs, worked examples, and mathematical solutions belong in this file. Chat messages should remain plain-text summaries and instructions.

## 2026-09-16 - TC 2017-2018 Test 1

### Problem 1: normalisation

The target was

$$
\frac{x+y+z}{xy+xz+yz}.
$$

The given expressions become

$$
\frac1x+\frac1y+\frac1z
=\frac{xy+xz+yz}{xyz},
$$

and

$$
\frac1{xy}+\frac1{yz}+\frac1{zx}
=\frac{x+y+z}{xyz}.
$$

Dividing the second equation by the first cancels the common factor $xyz$:

$$
\frac{
\frac{x+y+z}{xyz}
}{
\frac{xy+xz+yz}{xyz}
}
=\frac{2}{\sqrt2}
=\sqrt2.
$$

So the intended ratio is

$$
\boxed{\sqrt2}.
$$

However, the photographed conditions appear inconsistent. If

$$
a=\frac1x,\qquad b=\frac1y,\qquad c=\frac1z,
$$

then

$$
a+b+c=\sqrt2,\qquad ab+bc+ca=2.
$$

But

$$
(a+b+c)^2=a^2+b^2+c^2+2(ab+bc+ca).
$$

Also,

$$
a^2+b^2+c^2\ge ab+bc+ca,
$$

because

$$
(a-b)^2+(b-c)^2+(c-a)^2
=2(a^2+b^2+c^2-ab-bc-ca)\ge0.
$$

Therefore,

$$
(a+b+c)^2
\ge (ab+bc+ca)+2(ab+bc+ca)
=3(ab+bc+ca)
=6.
$$

But $(a+b+c)^2=(\sqrt2)^2=2$, which is impossible. The statement likely contains a typo.

### Problem 2: coordinate proof idea

The most practical idea is to use the projection. Since $H$ is the projection of $D$ onto $AI$, choose $AI$ as the $x$-axis:

$$
A=(0,0),\qquad I=(p,0),\qquad D=(q,r).
$$

Because $I$ is the midpoint of $BC$ and $ABCD$ is a parallelogram,

$$
I=\frac{B+C}{2}
=\frac{B+(B+D)}2
=B+\frac D2.
$$

Hence

$$
C=I+\frac D2
=\left(p+\frac q2,\frac r2\right).
$$

The projection of $D=(q,r)$ onto the $x$-axis is

$$
H=(q,0).
$$

Therefore,

$$
\overrightarrow{CH}
=\left(\frac q2-p,-\frac r2\right),
$$

while

$$
\overrightarrow{CD}
=\left(\frac q2-p,\frac r2\right).
$$

These vectors are mirror images, so they have the same length:

$$
CH^2
=\left(\frac q2-p\right)^2+\left(\frac r2\right)^2
=CD^2.
$$

Thus

$$
\boxed{CH=CD}.
$$

## 2026-09-17 - Block A, Lesson 1

### Common-denominator normalisation

Define the symmetric sums

$$
s_1=x+y+z,\qquad
s_2=xy+xz+yz,\qquad
s_3=xyz.
$$

Then

$$
\frac1x+\frac1y+\frac1z=\frac{s_2}{s_3},
$$

and

$$
\frac1{xy}+\frac1{yz}+\frac1{zx}=\frac{s_1}{s_3}.
$$

If the target is $s_1/s_2$, divide the two equations:

$$
\frac{\frac{s_1}{s_3}}{\frac{s_2}{s_3}}
=\frac{s_1}{s_2}.
$$

The main lesson is: when two equations contain the same unwanted factor, divide them so that the factor cancels.

### Notation question

If

$$
P_A=\frac1x+\frac1y+\frac1z,
$$

then

$$
P_A=\frac{s_2}{s_3}.
$$

Similarly,

$$
P_B=\frac1{xy}+\frac1{yz}+\frac1{zx}
=\frac{s_1}{s_3}.
$$

### Current practice

Complete Problems A, B, and C in [[NMaO-Lesson-01-Normalisation]], then send the attempts for correction.

### Practice check

The three exercises were checked:

- Problem A: correct common-denominator normalisation.
- Problem B: correct answer $\frac32$; the only issue was changing the labels $s_1,s_2,s_3$.
- Problem C: correct identification of the two reciprocal expressions.

Use the fixed convention:

$$
s_1=a+b+c,\qquad
s_2=ab+bc+ca,\qquad
s_3=abc.
$$

Then for Problem B:

$$
\frac{s_2}{s_3}=6,\qquad
\frac{s_1}{s_3}=9,
$$

so

$$
\frac{s_1}{s_2}
=\frac{9}{6}
=\boxed{\frac32}.
$$

The technique is understood. One transfer problem remains before A01 is marked complete.

### Label clarification

Yes, use the same labels in Problem C:

$$
s_1=a+b+c,\qquad
s_2=ab+bc+ca,\qquad
s_3=abc.
$$

Then Problem C uses:

$$
\frac1a+\frac1b+\frac1c=\frac{s_2}{s_3},
\qquad
\frac1{ab}+\frac1{bc}+\frac1{ca}=\frac{s_1}{s_3}.
$$

The target is

$$
\frac{a+b+c}{ab+bc+ca}=\frac{s_1}{s_2}.
$$

The letters $s_1,s_2,s_3$ are arbitrary labels; the important rule is not to change their meanings during the solution.

### A01 transfer problem

Assume nonzero numbers $x,y,z$ satisfy

$$
\frac1x+\frac1y+\frac1z=8,
\qquad
\frac1{xy}+\frac1{yz}+\frac1{zx}=3.
$$

Find

$$
\frac{xy+xz+yz}{x+y+z}.
$$

Do not solve for $x,y,z$. Use the fixed definitions

$$
s_1=x+y+z,\qquad
s_2=xy+xz+yz,\qquad
s_3=xyz.
$$

When this is correct, A01 is complete and we move to **A02: Algebraic identities and factorisation**.

### A01 transfer check

The transfer solution was correct:

$$
\frac{xy+xz+yz}{xyz}=8,
\qquad
\frac{x+y+z}{xyz}=3.
$$

Therefore,

$$
\frac{xy+xz+yz}{x+y+z}
=\frac{8}{3}.
$$

The only issue was that the labels were arranged nonstandardly. The solution remained valid because the meanings were stated and used consistently. From now on use:

$$
s_1=x+y+z,\qquad
s_2=xy+xz+yz,\qquad
s_3=xyz.
$$

**A01 status: complete. Next lesson: A02 - Algebraic Identities and Factorisation.**

### A02 practice check

Problems A-F were checked and are correct:

$$
(2x-3)^2=4x^2-12x+9,
$$

$$
x^2+7x+12=(x+3)(x+4),
$$

$$
x^4-5x^2+4=(x-1)(x+1)(x-2)(x+2),
$$

and

$$
(x+y)^2-(x-y)^2=4xy.
$$

The main techniques used were difference of squares, grouping, substitution, and careful sign distribution.

### A02 transfer problem

Factor completely:

$$
4x^4-13x^2+9.
$$

Suggested first recognition: this is a quadratic in $x^2$, but do not look for the solution yet. After this is checked, A02 is complete.

## Ongoing session template

### Date - Topic

**Student question:**  

**Explanation:**  

**Important formulas:**  

**Example:**  

**Student attempt:**  

**Correction:**  

**Next task:**  

## 2026-09-17 - A02: Algebraic identities and factorisation

### Core identities

We began the next lesson with:

$$
(a+b)^2=a^2+2ab+b^2,
\qquad
(a-b)^2=a^2-2ab+b^2,
$$

$$
a^2-b^2=(a-b)(a+b),
$$

and

$$
a^3-b^3=(a-b)(a^2+ab+b^2).
$$

The reason factorisation matters is that it converts a sum into a product, revealing zeros, signs, cancellations, and equality cases.

The full explanation and Problems A-F are in [[NMaO-Lesson-02-Identities-Factorisation]].

### A02 transfer check

Your substitution was correct:

$$
u=x^2.
$$

The expression became

$$
4u^2-13u+9.
$$

Your observation

$$
4u^2-13u+9=(2u-3)^2-u
$$

is also algebraically correct, but it is not the most useful factorisation route. The clean method is to find two terms whose product is $4\cdot9=36$ and whose sum is $-13$:

$$
-9+(-4)=-13,
\qquad
(-9)(-4)=36.
$$

Split the middle term:

$$
4u^2-13u+9
=4u^2-9u-4u+9.
$$

Group:

$$
4u^2-9u-4u+9
=u(4u-9)-1(4u-9)
=(u-1)(4u-9).
$$

Substitute back $u=x^2$:

$$
(x^2-1)(4x^2-9).
$$

Factor both differences of squares:

$$
x^2-1=(x-1)(x+1),
$$

$$
4x^2-9=(2x-3)(2x+3).
$$

Therefore:

$$
\boxed{
4x^4-13x^2+9
=(x-1)(x+1)(2x-3)(2x+3)
}.
$$

The method to remember is: factor the quadratic in $u$ first, then substitute back.

### A02 completion

The corrected transfer factorisation was rewritten independently and accepted. A02 is complete.

Next lesson: [[NMaO-Lesson-03-Fractions-Powers]].

## 2026-09-17 - A03 practice check

Problems A, B, E, and F were correct. Problems C and D were simplified correctly, but each was missing one restriction:

$$
\frac{x^2-25}{x^2+5x}
=\frac{x-5}{x},
\qquad
x\ne0,-5,
$$

and

$$
\frac{x^2-4x+4}{x^2-4}
=\frac{x-2}{x+2},
\qquad
x\ne2,-2.
$$

The restriction comes from the **original denominator**, even if the factor is cancelled later.

For F, $x$ cannot be cancelled from $x+5$ because $x+5$ is a sum, not a product containing $x$.

### A03 transfer problem

Simplify completely and state every restriction:

$$
\frac{x^2-9}{x^2-x-6}.
$$

Do not look for the solution yet. This problem specifically tests factoring and original-denominator restrictions.

### A03 transfer check

The factorisation and cancellation were correct:

$$
\frac{x^2-9}{x^2-x-6}
=\frac{(x-3)(x+3)}{(x-3)(x+2)}
=\frac{x+3}{x+2}.
$$

The original denominator is zero at $x=3$ and $x=-2$, so those are the restrictions. The roots of the numerator do not become restrictions.

Rewrite the final answer once with the correct excluded values. Then A03 is complete.

### Detailed solution

We want to simplify

$$
\frac{x^2-9}{x^2-x-6}.
$$

#### Step 1: Find the restrictions first

The denominator cannot be zero:

$$
x^2-x-6\ne0.
$$

To factor it, find two numbers whose product is $-6$ and whose sum is $-1$. These numbers are $-3$ and $2$:

$$
x^2-x-6=(x-3)(x+2).
$$

Therefore the denominator is zero when $x=3$ or $x=-2$. The original expression is defined only when

$$
x\ne3,\qquad x\ne-2.
$$

#### Step 2: Factor the numerator

The numerator is a difference of squares:

$$
x^2-9=x^2-3^2=(x-3)(x+3).
$$

#### Step 3: Substitute the factors

$$
\frac{x^2-9}{x^2-x-6}
=\frac{(x-3)(x+3)}{(x-3)(x+2)}.
$$

#### Step 4: Cancel the common factor

Because the original restriction already tells us $x\ne3$, the factor $x-3$ is nonzero and can be cancelled:

$$
\frac{(x-3)(x+3)}{(x-3)(x+2)}
=\frac{x+3}{x+2}.
$$

#### Final answer

$$
\boxed{
\frac{x^2-9}{x^2-x-6}
=\frac{x+3}{x+2}
}
\qquad
\text{for }x\ne3,-2.
$$

The value $x=-3$ is not a restriction because it makes the numerator zero, not the original denominator. At $x=-3$, the original expression is defined and its value is $0$.

### A03 transition check

Simplify completely and state every restriction:

$$
\frac{x^2+5x+6}{x^2+x-6}.
$$

Use the full process:

1. Find restrictions from the original denominator.
2. Factor the numerator and denominator.
3. Cancel only common factors.
4. State the simplified expression together with the restrictions.

Do not look for the solution yet. This is the final confirmation before moving to A04.

### A03 transition solution

Start with

$$
\frac{x^2+5x+6}{x^2+x-6}.
$$

#### Step 1: Find restrictions

The original denominator must be nonzero:

$$
x^2+x-6\ne0.
$$

Factor it:

$$
x^2+x-6=(x+3)(x-2).
$$

Therefore:

$$
x\ne-3,\qquad x\ne2.
$$

#### Step 2: Factor the numerator

Find two numbers whose product is $6$ and whose sum is $5$:

$$
x^2+5x+6=(x+2)(x+3).
$$

#### Step 3: Cancel the common factor

$$
\frac{x^2+5x+6}{x^2+x-6}
=\frac{(x+2)(x+3)}{(x+3)(x-2)}
=\frac{x+2}{x-2}.
$$

The restriction $x\ne-3$ must remain, even though the factor $x+3$ was cancelled.

#### Final answer

$$
\boxed{
\frac{x^2+5x+6}{x^2+x-6}
=\frac{x+2}{x-2}
}
\qquad
\text{for }x\ne-3,2.
$$

Rewrite this solution once without looking before moving to A04.

### A03 retry problem

Simplify completely and state every restriction:

$$
\frac{x^2+4x+3}{x^2+5x+4}.
$$

Use this checklist:

1. Factor the original denominator.
2. Write its restrictions.
3. Factor the numerator.
4. Cancel only common factors.
5. Keep the original restrictions in the final answer.

Send your attempt before asking for the solution.

### A03 retry correction

We simplify

$$
\frac{x^2+4x+3}{x^2+5x+4}.
$$

First factor the denominator:

$$
x^2+5x+4=(x+1)(x+4).
$$

Therefore the original expression requires

$$
x\ne-1,\qquad x\ne-4.
$$

Now factor the numerator:

$$
x^2+4x+3=(x+1)(x+3).
$$

Substitute the factors:

$$
\frac{x^2+4x+3}{x^2+5x+4}
=\frac{(x+1)(x+3)}{(x+1)(x+4)}.
$$

Cancel the common factor $x+1$. The restriction $x\ne-1$ remains because it came from the original denominator:

$$
\boxed{
\frac{x^2+4x+3}{x^2+5x+4}
=\frac{x+3}{x+4}
}
\qquad
\text{for }x\ne-1,-4.
$$

The method is now the same every time: denominator restrictions first, factor both parts, cancel factors, preserve all original restrictions.

### A03 completion

The retry correction was reviewed and rewritten. A03 is complete.

Next lesson: [[NMaO-Lesson-04-Equations]].

## 2026-09-17 - A04: Linear and quadratic equations

The next lesson covers solving equations systematically:

- Linear equations
- Fractions and denominator restrictions
- Quadratics by factorisation
- The discriminant and quadratic formula
- Checking for extraneous solutions after squaring

The full lesson and Problems A-F are in [[NMaO-Lesson-04-Equations]].

### A04 answer key

The complete worked solutions are in the answer-key section of [[NMaO-Lesson-04-Equations]]. The final results are:

$$
\boxed{\text{A: }x=6},
\qquad
\boxed{\text{B: }x=7},
$$

$$
\boxed{\text{C: }x=3,4},
\qquad
\boxed{\text{D: }x=-\frac32,1},
$$

$$
\boxed{\text{E: }x=4},
\qquad
\boxed{\text{F: }x=-\frac72,\quad x\ne-2}.
$$

Important checks:

- For E, squaring produces the candidate $x=-1$, but the original equation requires the right side to be nonnegative, so only $x=4$ remains.
- For F, the original denominator gives the restriction $x\ne-2$.

### A04 extra practice

Two transition problems were added to [[NMaO-Lesson-04-Equations]]:

- G: a factorable quadratic, similar to Problem D.
- H: a square-root equation, similar to Problem E, requiring a domain check and substitution into the original equation.

The extra-practice results are recorded in the lesson’s solution section:

$$
\boxed{\text{G: }x=-\frac23,1}
$$

$$
\boxed{\text{H: }x=3}
$$

For H, squaring also creates the candidate $x=-1$, but the original equation requires $x\ge0$, so $x=-1$ must be rejected.

One new transfer problem was added:

- I: another square-root equation requiring a domain check, squaring, and an original-equation verification.

Problem I was solved as follows:

$$
\sqrt{x+6}=x
\Longrightarrow x\ge0
\Longrightarrow x+6=x^2
\Longrightarrow (x-3)(x+2)=0.
$$

The candidate $x=-2$ violates $x\ge0$, while $x=3$ checks in the original equation. Therefore:

$$
\boxed{x=3}.
$$

The coefficient $2$ is factored only from the terms containing $x$; the constant stays outside:

$$
2x^2-12x+25=2(x^2-6x)+25=2(x-3)^2+7.
$$

We do not automatically divide the whole expression. Division is allowed on both sides of an equation by a nonzero number; for inequalities, a positive divisor preserves the direction and a negative divisor reverses it.

Another leading-coefficient minimum-value exercise was added to [[NMaO-Lesson-06-Nonnegative-Squares]].

Its correction is:

$$
3x^2+12x+14=3(x+2)^2+2\ge2.
$$

The minimum is $2$, reached at:

$$
\boxed{x=-2}.
$$

A final independent leading-coefficient drill was added before Problem E in [[NMaO-Lesson-06-Nonnegative-Squares]].

Its correction is:

$$
4x^2-16x+21=4(x-2)^2+5\ge5.
$$

The minimum is $5$, reached at:

$$
\boxed{x=2}.
$$

### A06 Problem E solution

Rewrite the difference between the two sides:

$$
a^2+b^2+c^2-ab-ac-bc
=\frac12\left((a-b)^2+(a-c)^2+(b-c)^2\right)\ge0.
$$

Therefore:

$$
\boxed{a^2+b^2+c^2\ge ab+ac+bc}.
$$

Equality requires all three squares to vanish, so:

$$
\boxed{a=b=c}.
$$

### A06 Problem F solution

Use the nonnegative square:

$$
(x-y)^2\ge0
\Longrightarrow
x^2-2xy+y^2\ge0.
$$

Adding $2xy$ gives:

$$
\boxed{x^2+y^2\ge2xy}.
$$

Equality occurs exactly when:

$$
\boxed{x=y}.
$$

The student's method for A was also correct: substitute $u=x$ and $v=y$ directly into the AM-GM statement, then multiply the resulting inequality by the positive number $2$ to obtain the requested form. Equality comes from $u=v$, hence $x=y$.

The student used the square-root route for F. This is valid because $x,y\ge0$:

$$
\frac{x+y}{2}\ge\sqrt{xy}
\Longrightarrow
x+y\ge2\sqrt{xy}.
$$

Both sides are nonnegative, so squaring preserves the inequality:

$$
(x+y)^2\ge4xy
\Longrightarrow
x^2+y^2\ge2xy.
$$

This proof is correct, although the direct square proof is shorter. Equality still occurs when $x=y$.

An additional scaled inequality, similar to F, was added to [[NMaO-Lesson-06-Nonnegative-Squares]].

### How the square-root identity proves the target

Apply

$$
\frac{u+v}{2}\ge\sqrt{uv}
$$

to $u=x^2$ and $v=y^2$:

$$
\frac{x^2+y^2}{2}\ge\sqrt{x^2y^2}=xy,
$$

where $x,y\ge0$. Multiplying by $2$ gives:

$$
\boxed{x^2+y^2\ge2xy}.
$$

For the scaled problem, apply it to $u=4x^2$ and $v=9y^2$:

$$
\frac{4x^2+9y^2}{2}\ge6xy
\Longrightarrow
\boxed{4x^2+9y^2\ge12xy}.
$$

So the identity proves the target by choosing its two inputs to be exactly the square terms appearing in the target.

### Scaled exercise: both complete methods

Direct square method:

$$
(2x-3y)^2\ge0
\Longrightarrow
4x^2+9y^2\ge12xy.
$$

Square-root method:

$$
\frac{4x^2+9y^2}{2}
\ge\sqrt{(4x^2)(9y^2)}=6xy
\Longrightarrow
4x^2+9y^2\ge12xy.
$$

Both methods give the same equality condition:

$$
\boxed{2x=3y}.
$$

### A04 transition checkpoint

Because the previous radical equations were solved after viewing their solutions, one independent checkpoint was added to [[NMaO-Lesson-04-Equations]]. It requires the complete process: domain condition, squaring, solving, rejecting invalid candidates, and checking the final result in the original equation.

The transition solution gives:

$$
\sqrt{2x+8}=x+1
\Longrightarrow x\ge-1
\Longrightarrow x^2=7.
$$

The candidate $x=-\sqrt7$ violates the domain condition, while $x=\sqrt7$ checks in the original equation. Therefore:

$$
\boxed{x=\sqrt7}.
$$

### A04 completion

The independent transition checkpoint was solved correctly. This confirms the full radical-equation workflow: domain condition, squaring, solving, rejecting invalid candidates, and checking in the original equation.

**A04 status: complete.** Next lesson: A05 - Systems of Equations.

## 2026-09-18 - A05: Systems of equations

The new lesson introduces substitution, elimination, solution checking, and the three possible system types: one solution, no solution, or infinitely many solutions.

The full explanation and Problems A-F are in [[NMaO-Lesson-05-Systems-of-Equations]].

### A05 answer key

The complete worked solutions are in the answer-key section of [[NMaO-Lesson-05-Systems-of-Equations]]. The final results are:

$$
\boxed{\text{A: }(6,3)},
\qquad
\boxed{\text{B: }\left(\frac{27}{5},\frac{11}{5}\right)},
$$

$$
\boxed{\text{C: }\left(3,\frac72\right)},
\qquad
\boxed{\text{D: infinitely many solutions},}
$$

$$
\boxed{\text{E: no solution}},
\qquad
\boxed{\text{F: }19\text{ and }12}.
$$

For D, both equations are the same line. For E, elimination produces a contradiction, so the lines are parallel and distinct.

### A05 correction note

The parameterized family belongs to **D**, the system with infinitely many solutions. **E** has no solution, so it cannot have a parameterized family. The numerical solving was correct; only this classification detail needed clarification.

An additional parameterization exercise, Problem G, was added to [[NMaO-Lesson-05-Systems-of-Equations]]. It asks for the complete family of solutions to a system representing one line.

Problem G was solved by observing that one equation is a multiple of the other. Letting $x=t$ gives:

$$
\boxed{(x,y)=(t,2t-4),\quad t\in\mathbb R}.
$$

The student's form is also correct. Choosing $y=t$ gives:

$$
2x-t=4
\quad\Longrightarrow\quad
x=\frac{t}{2}+2,
$$

so:

$$
\boxed{(x,y)=\left(\frac{t}{2}+2,t\right),\quad t\in\mathbb R}.
$$

These are two different parameter choices for the same line.

### A05 completion

The systems practice and the parameterized-solution transfer problem were completed successfully. **A05 status: complete.**

Next lesson: A06 - Nonnegative squares and basic inequality proofs.

## 2026-09-18 - A06: Nonnegative squares and basic inequality proofs

The new lesson develops the olympiad technique of rewriting a difference as a square or a sum of squares. It emphasizes completing the square, the three-variable pairwise-square identity, and equality conditions.

The full explanation and Problems A-F are in [[NMaO-Lesson-06-Nonnegative-Squares]].

### A06 clarification: completing the square and pairwise squares

For the general pattern, expand a trial square:

$$
\left(x+\frac b2\right)^2=x^2+bx+\frac{b^2}{4}.
$$

The extra constant $b^2/4$ is corrected by subtracting it and adding the desired constant $c$:

$$
\boxed{x^2+bx+c
=\left(x+\frac b2\right)^2+c-\frac{b^2}{4}}.
$$

For the pairwise-square identity, expand term by term:

$$
\begin{aligned}
&(a-b)^2+(b-c)^2+(c-a)^2\\
&=(a^2-2ab+b^2)+(b^2-2bc+c^2)+(c^2-2ca+a^2)\\
&=2a^2+2b^2+2c^2-2ab-2bc-2ca\\
&=2(a^2+b^2+c^2-ab-bc-ca).
\end{aligned}
$$

The original expression is a sum of nonnegative squares, so it is at least zero. Since $2$ is positive, divide both sides by $2$ without reversing the inequality; $0/2$ is still zero:

$$
a^2+b^2+c^2-ab-bc-ca\ge0.
$$

Adding $ab+bc+ca$ gives:

$$
\boxed{a^2+b^2+c^2\ge ab+bc+ca}.
$$

Equality requires all three squares to be zero, hence $a=b=c$.

### A06 Part 5 clarification

For nonnegative $x$ and $y$, begin with:

$$
(x-y)^2\ge0
\Longrightarrow
x^2+y^2\ge2xy.
$$

Add $2xy$ to both sides:

$$
(x+y)^2\ge4xy.
$$

Since $x+y$ and $\sqrt{xy}$ are nonnegative, take square roots safely:

$$
x+y\ge2\sqrt{xy}.
$$

Divide by the positive number $2$:

$$
\boxed{\frac{x+y}{2}\ge\sqrt{xy}}.
$$

This means the ordinary average is at least the geometric mean. Equality occurs exactly when $x=y$. The nonnegative assumptions are needed for the square-root form; the original square inequality works for all real $x,y$.

### A06 Problem A solution

Complete the square:

$$
x^2+4x+7=(x+2)^2+3\ge3.
$$

Equality occurs when the square is zero:

$$
\boxed{x=-2}.
$$

An additional completing-the-square exercise, similar to Problem A, was added to [[NMaO-Lesson-06-Nonnegative-Squares]].

Its correction is:

$$
x^2-10x+29=(x-5)^2+4\ge4,
$$

with equality at

$$
\boxed{x=5}.
$$

### A06 Problem B solution

Use the nonnegative square:

$$
(a-b)^2\ge0
\Longrightarrow
a^2-2ab+b^2\ge0.
$$

Adding $2ab$ gives:

$$
\boxed{a^2+b^2\ge2ab}.
$$

Equality occurs exactly when $a=b$.

### A06 Problem C solution

Rewrite the difference between the two sides:

$$
x^2+y^2+z^2-xy-yz-zx
=\frac12\left((x-y)^2+(y-z)^2+(z-x)^2\right)\ge0.
$$

Therefore:

$$
\boxed{x^2+y^2+z^2\ge xy+yz+zx}.
$$

Equality requires all three squares to vanish, so:

$$
\boxed{x=y=z}.
$$

### A06 Problem D solution

Complete the square:

$$
x^2-8x+19=(x-4)^2+3\ge3.
$$

Therefore the minimum value is $3$, reached when:

$$
\boxed{x=4}.
$$

An additional minimum-value exercise, similar to Problem D but with a leading coefficient, was added to [[NMaO-Lesson-06-Nonnegative-Squares]].

Its correction is:

$$
2x^2-12x+25=2(x-3)^2+7\ge7.
$$

The minimum is $7$, reached at:

$$
\boxed{x=3}.
$$

### A06 completion

The core practice, minimum-value drills, sum-of-squares proofs, and scaled square-root transfer problem were completed successfully. **A06 status: complete.**

Next lesson: A07 - AM-GM and equality cases.

## 2026-09-18 - A07: AM-GM and equality cases

The new lesson develops the arithmetic mean-geometric mean inequality, equality conditions, fixed-sum product maxima, fixed-product sum minima, and three-variable applications.

The full explanation and Problems A-F are in [[NMaO-Lesson-07-AM-GM]].

### A07 AM-GM intuition

AM-GM compares two averages of nonnegative numbers:

$$
\frac{u+v}{2}\ge\sqrt{uv}.
$$

The core idea is balance. With a fixed sum, equal numbers give the largest product. With a fixed product, equal numbers give the smallest sum. Equality always occurs when the two inputs are equal.

The proof comes from:

$$
\frac{u+v}{2}-\sqrt{uv}
=\frac{(\sqrt u-\sqrt v)^2}{2}\ge0.
$$

So the difference between the means is literally a nonnegative square. In a problem such as $x+16/x$, the two terms have fixed product, so AM-GM says the minimum occurs when the terms balance.

### Definitions of the two means

The arithmetic mean is the ordinary average, representing equal sharing of a total:

$$
\operatorname{AM}(a,b)=\frac{a+b}{2}.
$$

The geometric mean is the equal factor whose repeated multiplication gives the product:

$$
g^2=ab
\quad\Longrightarrow\quad
\operatorname{GM}(a,b)=\sqrt{ab}.
$$

Geometrically, $\sqrt{ab}$ is the side of a square with the same area as a rectangle with sides $a$ and $b$. Thus AM equalizes sums, while GM equalizes products.

### A07 Problem A solution

For $x,y\ge0$:

$$
(\sqrt{x}-\sqrt{y})^2\ge0
\Longrightarrow
x+y\ge2\sqrt{xy}.
$$

Equality occurs exactly when:

$$
\boxed{x=y}.
$$

An additional exercise was added to [[NMaO-Lesson-07-AM-GM]] to practise the same square-root substitution method with scaled terms.

Its correction is:

$$
(2\sqrt a-3\sqrt b)^2\ge0
\Longrightarrow
\boxed{4a+9b\ge12\sqrt{ab}}.
$$

Equality occurs when:

$$
\boxed{2\sqrt a=3\sqrt b}
\qquad\text{or equivalently}\qquad
\boxed{4a=9b}.
$$

### A07 Problem B solution

For $x>0$, apply AM-GM to $x$ and $16/x$:

$$
x+\frac{16}{x}\ge2\sqrt{16}=8.
$$

Equality requires $x=16/x$, so $x=4$. Therefore the minimum is $8$.

An additional AM-GM minimum problem, similar to B but with coefficients, was added to [[NMaO-Lesson-07-AM-GM]].

Its correction is:

$$
3x+\frac{12}{x}\ge2\sqrt{36}=12.
$$

Equality requires $3x=12/x$, giving $x=2$. The minimum is $12$.

Another AM-GM minimum problem was added to [[NMaO-Lesson-07-AM-GM]], with a non-integer equality point.

Its correction is:

$$
4x+\frac9x\ge2\sqrt{36}=12.
$$

Equality requires $4x=9/x$, giving:

$$
\boxed{x=\frac32}.
$$

A simpler reinforcement problem was added to [[NMaO-Lesson-07-AM-GM]] so the AM-GM setup and equality equation can be practised with an integer equality point.

Its correction is:

$$
2x+\frac8x\ge2\sqrt{16}=8.
$$

Equality requires $2x=8/x$, giving $x=2$. The minimum is $8$.

### A07 Problem D solution

Using three-variable AM-GM and $abc=8$:

$$
\frac{a+b+c}{3}\ge\sqrt[3]{abc}=2
\Longrightarrow
a+b+c\ge6.
$$

Equality requires $a=b=c$, and the product condition then gives $a=b=c=2$. The minimum is $6$.

An additional fixed-sum product problem, similar to C, was added to [[NMaO-Lesson-07-AM-GM]].

An additional three-variable fixed-product problem, similar to D, was added to [[NMaO-Lesson-07-AM-GM]].

Its correction is:

$$
\frac{p+q+r}{3}\ge\sqrt[3]{27}=3
\Longrightarrow
p+q+r\ge9.
$$

Equality occurs at $p=q=r=3$, so the minimum is $9$.

The fixed-sum exercise similar to C has solution:

$$
\frac{u+v}{2}=7\ge\sqrt{uv}
\Longrightarrow
\boxed{uv\le49}.
$$

Equality occurs at:

$$
\boxed{u=v=7}.
$$

### A07 Problem C solution

For the original condition $x+y=12$:

$$
\frac{x+y}{2}=6\ge\sqrt{xy}
\Longrightarrow
\boxed{xy\le36}.
$$

Equality occurs when:

$$
\boxed{x=y=6}.
$$

### A07 domain clarification for E

The variables in Problem E are positive real numbers. They are not required to be natural numbers. The condition $x,y,z>0$ ensures the reciprocal terms are defined and AM-GM applies.

Progressive hints for Problem E were added to [[NMaO-Lesson-07-AM-GM]]. The intended route is to apply three-variable AM-GM separately to the two parentheses, simplify the two cube-root products, and then combine the bounds. The equality condition requires the terms in each application to be equal.

### A07 Problem E solution

Apply three-variable AM-GM twice:

$$
x+y+z\ge3\sqrt[3]{xyz},
$$

$$
\frac1x+\frac1y+\frac1z
\ge3\sqrt[3]{\frac1{xyz}}.
$$

Multiplying gives:

$$
\left(x+y+z\right)\left(\frac1x+\frac1y+\frac1z\right)
\ge9.
$$

Equality occurs exactly when:

$$
\boxed{x=y=z>0}.
$$

An additional weighted reciprocal AM-GM exercise, similar to E, was added to [[NMaO-Lesson-07-AM-GM]].

Its correction uses three-variable AM-GM on $2x,y,z$ and on their reciprocals:

$$
2x+y+z\ge3\sqrt[3]{2xyz},
$$

$$
\frac1{2x}+\frac1y+\frac1z
\ge3\sqrt[3]{\frac1{2xyz}}.
$$

Multiplication gives the required lower bound $9$. Equality occurs when:

$$
\boxed{2x=y=z>0}.
$$

### A07 Problem F solution

Since $x+y=10$:

$$
\frac{x+y}{2}=5\ge\sqrt{xy}
\Longrightarrow
\boxed{xy\le25}.
$$

Equality occurs at:

$$
\boxed{x=y=5}.
$$

An additional fixed-sum maximum-product exercise, similar to F, was added to [[NMaO-Lesson-07-AM-GM]].

Its correction is:

$$
\frac{u+v}{2}=9\ge\sqrt{uv}
\Longrightarrow
\boxed{uv\le81}.
$$

Equality occurs at:

$$
\boxed{u=v=9}.
$$

### A07 completion

The AM-GM practice set and transfer problems were completed successfully, including equality conditions, reciprocal expressions, fixed-sum products, fixed-product sums, and three-variable applications. **A07 status: complete.**

Next lesson: A08 - Cauchy-Schwarz and useful sum estimates.

## 2026-09-20 - A08: Cauchy-Schwarz and useful sum estimates

The new lesson introduces the Cauchy-Schwarz inequality, proportionality and equality, sum estimates, reciprocal sums, and the weighted denominator form.

The full explanation and Problems A-F are in [[NMaO-Lesson-08-Cauchy-Schwarz]].

### A08 screenshot clarification

In the Cauchy-Schwarz derivation, adding $2abcd$ means adding it to both sides:

$$
a^2d^2-2abcd+b^2c^2\ge0
\Longrightarrow
a^2d^2+b^2c^2\ge2abcd.
$$

You are correct: the negative term cancels with the added positive term. The screenshot’s version with $+2abcd$ still on the left is an algebra mistake. The corrected line is equivalent to the original square inequality, and the clean proof is:

$$
(a^2+b^2)(c^2+d^2)-(ac+bd)^2=(ad-bc)^2\ge0.
$$

### A08 reciprocal sums, explained slowly

For a product of a sum and a reciprocal sum, choose:

$$
U=(\sqrt{x},\sqrt{y},\sqrt{z}),
\qquad
V=\left(\frac1{\sqrt{x}},\frac1{\sqrt{y}},\frac1{\sqrt{z}}\right).
$$

Their squared lengths are exactly the two desired sums:

$$
\|U\|^2=x+y+z,
\qquad
\|V\|^2=\frac1x+\frac1y+\frac1z.
$$

Their dot product is fixed because every pair cancels:

$$
U\cdot V=1+1+1=3.
$$

Cauchy-Schwarz gives:

$$
3^2\le
\left(x+y+z\right)
\left(\frac1x+\frac1y+\frac1z\right).
$$

Equality means the vectors are proportional, forcing $x=y=z$.

## 2026-09-24 - A08 intuitive restart

### The one idea behind Cauchy-Schwarz

Cauchy-Schwarz looks complicated because it uses four letters, but its meaning is simple:

> When two pairs point in the same proportion, their mixed sum is as large as possible. If their proportions do not match, some potential is lost.

For two pairs $(a,b)$ and $(c,d)$, the mixed sum is:

$$
ac+bd.
$$

The sizes of the two pairs are measured by:

$$
a^2+b^2
\qquad\text{and}\qquad
c^2+d^2.
$$

Cauchy-Schwarz says:

$$
\boxed{(ac+bd)^2\le (a^2+b^2)(c^2+d^2)}.
$$

The left side measures how strongly the pairs work together. The right side is the greatest value their combined sizes could allow.

### Why it is true

The difference between the right side and the left side is exactly one square:

$$
\begin{aligned}
&(a^2+b^2)(c^2+d^2)-(ac+bd)^2\\
&=(ad-bc)^2.
\end{aligned}
$$

Every real square is nonnegative, so:

$$
(ad-bc)^2\ge0.
$$

Therefore the right side can never be smaller than the left side. This proves the inequality.

The quantity $ad-bc$ measures the mismatch between the two pairs. If the mismatch is zero, nothing is lost and equality occurs:

$$
ad-bc=0
\quad\Longleftrightarrow\quad
ad=bc.
$$

When the relevant denominators are nonzero, this means:

$$
\frac ac=\frac bd.
$$

So equality means that the two pairs have the same proportion.

### A numerical picture

Take the pairs $(1,2)$ and $(2,4)$. They have the same proportion because the second pair is twice the first. Then:

$$
(1\cdot2+2\cdot4)^2=10^2=100,
$$

and:

$$
(1^2+2^2)(2^2+4^2)=5\cdot20=100.
$$

There is equality.

Now take $(1,2)$ and $(4,2)$. Their proportions do not match. Then:

$$
(1\cdot4+2\cdot2)^2=8^2=64,
$$

while:

$$
(1^2+2^2)(4^2+2^2)=5\cdot20=100.
$$

The mismatch creates a gap of $36$.

### Why a pair of ones estimates an ordinary sum

To produce $a+b$, multiply $a$ and $b$ by $1$:

$$
a+b=a\cdot1+b\cdot1.
$$

Apply Cauchy-Schwarz to $(a,b)$ and $(1,1)$:

$$
(a+b)^2
\le(a^2+b^2)(1^2+1^2)
=2(a^2+b^2).
$$

Thus:

$$
\boxed{(a+b)^2\le2(a^2+b^2)}.
$$

Equality requires $(a,b)$ to have the same proportion as $(1,1)$, so:

$$
\boxed{a=b}.
$$

For three numbers, pair $(x,y,z)$ with $(1,1,1)$:

$$
\boxed{(x+y+z)^2\le3(x^2+y^2+z^2)}.
$$

Equality occurs when:

$$
\boxed{x=y=z}.
$$

The intuition is that, for a fixed amount of squared size, the ordinary sum is largest when that size is shared equally.

### The fixed-sum-of-squares problem

If:

$$
x^2+y^2+z^2=14,
$$

then:

$$
(x+y+z)^2\le3\cdot14=42.
$$

Therefore:

$$
x+y+z\le\sqrt{42}.
$$

The maximum is reached when $x=y=z$. Since their squares add to $14$:

$$
3x^2=14,
$$

so the equality point is:

$$
x=y=z=\sqrt{\frac{14}{3}}.
$$

Hence the maximum is:

$$
\boxed{\sqrt{42}}.
$$

### Why square roots appear in reciprocal problems

Suppose the target contains both $x$ and $1/x$. We want entries whose squares give those terms. The natural choices are therefore:

$$
\sqrt{x}
\qquad\text{and}\qquad
\frac1{\sqrt{x}}.
$$

Their squares are $x$ and $1/x$, while their product is especially simple:

$$
\sqrt{x}\cdot\frac1{\sqrt{x}}=1.
$$

For three positive numbers, use the two triples:

$$
(\sqrt{x},\sqrt{y},\sqrt{z})
$$

and:

$$
\left(\frac1{\sqrt{x}},\frac1{\sqrt{y}},\frac1{\sqrt{z}}\right).
$$

The three paired products add to $3$, so Cauchy-Schwarz gives:

$$
3^2\le
(x+y+z)
\left(\frac1x+\frac1y+\frac1z\right).
$$

Therefore:

$$
\boxed{(x+y+z)
\left(\frac1x+\frac1y+\frac1z\right)\ge9}.
$$

Equality again means balance:

$$
\boxed{x=y=z>0}.
$$

### A recognition guide

Do not begin by memorising many versions. Ask what you want the squared entries to produce:

1. For an ordinary sum, use a pair or triple of ones.
2. For a sum and its reciprocal sum, use square roots and reciprocal square roots.
3. For fractions such as $u^2/p$, write the corresponding entry as $u/\sqrt p$.
4. Always check equality by asking when the two lists have the same proportion.

For the first study round, it is enough to understand the core inequality and the pair-of-ones idea. The reciprocal and weighted forms can be learned after Problems A-C.

### A08 Problem A - solution

We want to prove, for all real $a,b$:

$$
(a+b)^2\le2(a^2+b^2).
$$

Apply Cauchy-Schwarz to the two lists $(a,b)$ and $(1,1)$:

$$
(a\cdot1+b\cdot1)^2
\le(a^2+b^2)(1^2+1^2).
$$

Therefore:

$$
\boxed{(a+b)^2\le2(a^2+b^2)}.
$$

Equality occurs when the two lists are proportional. Since the second list is $(1,1)$, this requires:

$$
\boxed{a=b}.
$$

We can also see the same result directly by subtracting the left side from the right side:

$$
\begin{aligned}
2(a^2+b^2)-(a+b)^2
&=2a^2+2b^2-a^2-2ab-b^2\\
&=a^2-2ab+b^2\\
&=(a-b)^2\ge0.
\end{aligned}
$$

The gap is $(a-b)^2$, so it becomes zero exactly when $a=b$.

### A08 Problem B - solution

We want to prove, for all real $x,y,z$:

$$
(x+y+z)^2\le3(x^2+y^2+z^2).
$$

Apply Cauchy-Schwarz to the two lists $(x,y,z)$ and $(1,1,1)$:

$$
(x\cdot1+y\cdot1+z\cdot1)^2
\le(x^2+y^2+z^2)(1^2+1^2+1^2).
$$

Since $1^2+1^2+1^2=3$, this becomes:

$$
\boxed{(x+y+z)^2\le3(x^2+y^2+z^2)}.
$$

Equality occurs when the two lists are proportional. Because the second list is $(1,1,1)$, this requires:

$$
\boxed{x=y=z}.
$$

The equality condition matches the intuition: the ordinary sum is largest relative to the squared size when the three numbers are balanced.

### A08 Problem C - solution

We are given:

$$
x^2+y^2+z^2=14.
$$

From Problem B:

$$
(x+y+z)^2\le3(x^2+y^2+z^2).
$$

Substituting the given value gives:

$$
(x+y+z)^2\le3\cdot14=42.
$$

Thus:

$$
x+y+z\le\sqrt{42}.
$$

Equality in Cauchy-Schwarz requires $x=y=z$. If their common value is $t$, then:

$$
3t^2=14,
$$

so:

$$
t=\pm\sqrt{\frac{14}{3}}.
$$

The positive value gives the maximum sum:

$$
x=y=z=\sqrt{\frac{14}{3}}.
$$

Therefore:

$$
\boxed{\max(x+y+z)=\sqrt{42}}.
$$

The negative equality point gives the minimum $-\sqrt{42}$, not the maximum.

### A08 transfer exercise similar to Problem D

Let $a,b,c,d>0$. Prove using Cauchy-Schwarz that:

$$
(a+b+c+d)
\left(\frac1a+\frac1b+\frac1c+\frac1d\right)
\ge16.
$$

State the equality condition. Before applying Cauchy-Schwarz, explicitly write the two lists whose squared sizes produce the two parentheses.

Try the exercise independently before requesting a hint or solution.

### A08 D-transfer solution

Use the two lists:

$$
U=\left(\sqrt a,\sqrt b,\sqrt c,\sqrt d\right)
$$

and:

$$
V=\left(\frac1{\sqrt a},\frac1{\sqrt b},
\frac1{\sqrt c},\frac1{\sqrt d}\right).
$$

Their matching score is:

$$
U\cdot V=1+1+1+1=4.
$$

Their squared sizes are:

$$
\|U\|^2=a+b+c+d
$$

and:

$$
\|V\|^2=\frac1a+\frac1b+\frac1c+\frac1d.
$$

Cauchy-Schwarz gives:

$$
(U\cdot V)^2\le\|U\|^2\|V\|^2.
$$

Therefore:

$$
4^2\le
(a+b+c+d)
\left(\frac1a+\frac1b+\frac1c+\frac1d\right),
$$

so:

$$
\boxed{
(a+b+c+d)
\left(\frac1a+\frac1b+\frac1c+\frac1d\right)
\ge16
}.
$$

Equality occurs when $U$ and $V$ are proportional. This forces:

$$
\boxed{a=b=c=d>0}.
$$

### A08 Problem E - solution

Use the two lists:

$$
U=\left(\frac{u}{\sqrt p},\frac{v}{\sqrt q}\right)
$$

and:

$$
V=(\sqrt p,\sqrt q).
$$

Their matching score is:

$$
U\cdot V
=\frac{u}{\sqrt p}\cdot\sqrt p
+\frac{v}{\sqrt q}\cdot\sqrt q
=u+v.
$$

Their squared sizes are:

$$
\|U\|^2=\frac{u^2}{p}+\frac{v^2}{q},
\qquad
\|V\|^2=p+q.
$$

Cauchy-Schwarz gives:

$$
(u+v)^2
\le
\left(\frac{u^2}{p}+\frac{v^2}{q}\right)(p+q).
$$

Because $p,q>0$, the number $p+q$ is positive. Divide by it without changing the inequality direction:

$$
\boxed{
\frac{u^2}{p}+\frac{v^2}{q}
\ge\frac{(u+v)^2}{p+q}
}.
$$

Equality requires $U$ and $V$ to be proportional. Thus, for some real $k$:

$$
\frac{u}{\sqrt p}=k\sqrt p,
\qquad
\frac{v}{\sqrt q}=k\sqrt q.
$$

This gives $u=kp$ and $v=kq$, so equality occurs exactly when:

$$
\boxed{\frac up=\frac vq}.
$$

### A08 transfer exercise similar to Problem E

Let $p,q,r>0$ and $u,v,w\in\mathbb R$. Prove that:

$$
\frac{u^2}{p}+\frac{v^2}{q}+\frac{w^2}{r}
\ge
\frac{(u+v+w)^2}{p+q+r}.
$$

State the equality condition. Begin by choosing two lists whose matching score is $u+v+w$.

Try it independently before requesting the solution.

### A08 E-transfer solution

Use:

$$
U=\left(\frac{u}{\sqrt p},\frac{v}{\sqrt q},\frac{w}{\sqrt r}\right)
$$

and:

$$
V=(\sqrt p,\sqrt q,\sqrt r).
$$

Their matching score and squared sizes are:

$$
U\cdot V=u+v+w,
$$

$$
\|U\|^2=\frac{u^2}{p}+\frac{v^2}{q}+\frac{w^2}{r},
\qquad
\|V\|^2=p+q+r.
$$

Cauchy-Schwarz gives:

$$
(u+v+w)^2
\le
\left(\frac{u^2}{p}+\frac{v^2}{q}+\frac{w^2}{r}\right)
(p+q+r).
$$

Because $p+q+r>0$, divide by it to obtain:

$$
\boxed{
\frac{u^2}{p}+\frac{v^2}{q}+\frac{w^2}{r}
\ge
\frac{(u+v+w)^2}{p+q+r}
}.
$$

Equality requires $U$ and $V$ to be proportional. This gives $u=kp$, $v=kq$, and $w=kr$ for some real $k$. Equivalently:

$$
\boxed{\frac up=\frac vq=\frac wr}.
$$

### A08 Problem F - solution

Apply the three-term weighted Cauchy-Schwarz inequality with:

$$
(u,v,w)=(a,b,c)
$$

and:

$$
(p,q,r)=(b,c,a).
$$

Then:

$$
\frac{a^2}{b}+\frac{b^2}{c}+\frac{c^2}{a}
\ge
\frac{(a+b+c)^2}{b+c+a}.
$$

Because $a+b+c>0$:

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

Equality requires:

$$
\frac ab=\frac bc=\frac ca.
$$

If their common positive value is $k$, multiplying the ratios gives $k^3=1$, so $k=1$. Thus equality occurs exactly when:

$$
\boxed{a=b=c>0}.
$$

## 2026-09-26 - A08 F-transfer 2 review

The submitted handwritten proof is correct.

The first list was chosen so that its squared size is the target left-hand side:

$$
U=\left(
\frac{a}{\sqrt{b+c+d}},
\frac{b}{\sqrt{c+d+a}},
\frac{c}{\sqrt{d+a+b}},
\frac{d}{\sqrt{a+b+c}}
\right).
$$

The matching second list was:

$$
V=\left(
\sqrt{b+c+d},
\sqrt{c+d+a},
\sqrt{d+a+b},
\sqrt{a+b+c}
\right).
$$

This correctly gives:

$$
U\cdot V=a+b+c+d.
$$

The denominator sum was also simplified correctly. Each variable occurs in three denominators, so:

$$
\|V\|^2=3(a+b+c+d).
$$

Therefore Cauchy-Schwarz gives:

$$
(a+b+c+d)^2
\le
3(a+b+c+d)
\left(
\frac{a^2}{b+c+d}
+\frac{b^2}{c+d+a}
+\frac{c^2}{d+a+b}
+\frac{d^2}{a+b+c}
\right).
$$

Since $a+b+c+d>0$, division gives the required inequality:

$$
\boxed{
\frac{a^2}{b+c+d}
+\frac{b^2}{c+d+a}
+\frac{c^2}{d+a+b}
+\frac{d^2}{a+b+c}
\ge
\frac{a+b+c+d}{3}
}.
$$

The equality analysis was correct. Proportionality gives:

$$
\frac{a}{b+c+d}
=\frac{b}{c+d+a}
=\frac{c}{d+a+b}
=\frac{d}{a+b+c}
=k.
$$

Adding the resulting four equations gives $k=1/3$. Subtracting pairs then forces:

$$
\boxed{a=b=c=d>0}.
$$

This successful independent transfer completes A08.

## 2026-09-26 - A09: Homogeneity and substitutions

The new lesson begins with the difference between **shape** and **size**. A homogeneous statement keeps the same algebraic shape when every variable is multiplied by the same positive factor.

For example:

$$
(x+y)^2\ge4xy
$$

is homogeneous of degree $2$, because replacing $(x,y)$ by $(tx,ty)$ multiplies both sides by $t^2$.

This means the statement depends on the proportion $x:y$, not their common size. We may therefore scale positive variables to a convenient condition such as $x+y=1$.

By contrast, $x^2+y^2\ge x+y$ is not homogeneous because its two sides scale differently. A free normalisation is not valid there.

The first study task is to read Sections 0-3 of [[NMaO-Lesson-09-Homogeneity-Substitutions]] and attempt Problems A-B.

### A08 F-transfer 2

Let $a,b,c,d>0$. Prove that:

$$
\frac{a^2}{b+c+d}
+\frac{b^2}{c+d+a}
+\frac{c^2}{d+a+b}
+\frac{d^2}{a+b+c}
\ge
\frac{a+b+c+d}{3}.
$$

State the equality condition. As a first observation, count how many times each variable occurs in the sum of the four denominators.

Attempt this without looking back at the previous F-transfer solution.

### A08 F-transfer - final completion check

Let $a,b,c>0$. Prove that:

$$
\frac{a^2}{b+c}
+\frac{b^2}{c+a}
+\frac{c^2}{a+b}
\ge
\frac{a+b+c}{2}.
$$

State the equality condition.

This is the final A08 transfer check. Solve it without notes or a worked example. A correct weighted Cauchy-Schwarz setup, simplification, and equality condition will provide the evidence needed to complete A08 and move to A09.

### A08 F-transfer attempt feedback - 2026-09-26

The attempt is going in the right direction because it recognises weighted Cauchy-Schwarz and correctly begins the first list with:

$$
U=\left(
\frac{a}{\sqrt{b+c}},
\frac{b}{\sqrt{c+a}},
\frac{c}{\sqrt{a+b}}
\right).
$$

Its squared size is exactly the left-hand side:

$$
\|U\|^2
=\frac{a^2}{b+c}
+\frac{b^2}{c+a}
+\frac{c^2}{a+b}.
$$

The first wrong turn is the choice of the second list. Entries such as $\sqrt{a/2}$ do not cancel the denominators in $U$, so the matching score becomes complicated instead of producing $a+b+c$.

#### Strategic hint

Choose each entry of the second list so that its product with the corresponding entry of $U$ is simply the numerator:

$$
\frac{a}{\sqrt{b+c}}\cdot\boxed{\phantom{\sqrt{b+c}}}=a.
$$

This should lead to:

$$
V=\left(\sqrt{b+c},\sqrt{c+a},\sqrt{a+b}\right).
$$

Now calculate these two quantities before continuing:

$$
U\cdot V,
$$

and:

$$
\|V\|^2=(b+c)+(c+a)+(a+b).
$$

Simplify the latter by counting how many times each variable occurs. Then apply:

$$
(U\cdot V)^2\le\|U\|^2\|V\|^2.
$$

For equality, use the weighted-form condition:

$$
\frac{a}{b+c}=\frac{b}{c+a}=\frac{c}{a+b},
$$

and determine when this is possible for positive $a,b,c$.

### A08 F-transfer - full solution

Use weighted Cauchy-Schwarz with numerators $a,b,c$ and denominators $b+c,c+a,a+b$:

$$
\frac{a^2}{b+c}
+\frac{b^2}{c+a}
+\frac{c^2}{a+b}
\ge
\frac{(a+b+c)^2}
{(b+c)+(c+a)+(a+b)}.
$$

Each variable appears twice in the denominator sum, so:

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

For equality, weighted Cauchy-Schwarz requires:

$$
\frac{a}{b+c}
=\frac{b}{c+a}
=\frac{c}{a+b}
=k.
$$

Thus:

$$
a=k(b+c),
\qquad
b=k(c+a),
\qquad
c=k(a+b).
$$

Adding the three equations gives:

$$
a+b+c=2k(a+b+c).
$$

Since $a+b+c>0$, we obtain $k=1/2$. Therefore:

$$
2a=b+c,
\qquad
2b=c+a,
\qquad
2c=a+b.
$$

“Subtract the first two equations” means subtract the entire second equation from the entire first equation. Starting from:

$$
2a=b+c
$$

and:

$$
2b=c+a,
$$

we subtract left side from left side and right side from right side:

$$
\begin{aligned}
2a-2b&=(b+c)-(c+a)\\
2a-2b&=b-a\\
3a-3b&=0\\
3(a-b)&=0.
\end{aligned}
$$

Thus $a=b$. Substituting $b=a$ into $2a=b+c$ gives $2a=a+c$, so $c=a$. Hence equality occurs exactly when:

$$
\boxed{a=b=c>0}.
$$
