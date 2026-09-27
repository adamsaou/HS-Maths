# Lesson 09 - Homogeneity and Substitutions

<span class="nmao-badge nmao-study">LESSON</span>

## Objective

Recognise when an expression keeps the same shape under scaling, use a legal normalisation, and choose substitutions that remove repeated algebraic structure.

## 0. Start here: shape versus size

Consider:

$$
(x+y)^2\ge4xy.
$$

If both variables are multiplied by $10$, both sides are multiplied by $10^2$. The numbers become larger, but the inequality keeps the same shape.

This is the intuition behind **homogeneity**:

> A homogeneous statement cares about the proportions between variables, not their common size.

The pairs $(1,2)$, $(2,4)$, and $(10,20)$ have the same proportion. A homogeneous inequality treats them as scaled versions of the same situation.

This lets us choose a convenient size. If $x,y>0$, we may scale them so that $x+y=1$. We are replacing them by a proportional pair that is easier to study.

## 1. Degree

For one term, add the exponents of its variables. The term $x^2y^3$ has degree $2+3=5$.

An expression is homogeneous when all its terms have the same total degree.

$$
x^2+3xy+y^2
$$

is homogeneous of degree $2$. The expression $x^3+xy^2$ is homogeneous of degree $3$. However, $x^2+y$ is not homogeneous because its terms have degrees $2$ and $1$.

## 2. The scaling test

Replace every variable by a scaled version:

$$
x\mapsto tx,
\qquad y\mapsto ty.
$$

For example:

$$
(tx)^2+(tx)(ty)+(ty)^2
=t^2(x^2+xy+y^2).
$$

The common factor $t^2$ confirms degree $2$.

Fractions can also be homogeneous. Under $a,b,c\mapsto ta,tb,tc$:

$$
\frac{a^2}{b+c}
\mapsto
\frac{t^2a^2}{t(b+c)}
=t\frac{a^2}{b+c}.
$$

So this fraction has degree $1$.

For $(a+b)(1/a+1/b)$, the first factor scales by $t$ and the second by $1/t$. They cancel, so the expression has degree $0$.

## 3. Normalisation

If every part of an inequality has the same degree, common scaling preserves the statement. We may then choose a convenient condition, such as:

$$
x+y+z=1
$$

or:

$$
xyz=1.
$$

The choice must simplify the expression we actually have.

For $x,y>0$, the inequality $(x+y)^2\ge4xy$ is homogeneous of degree $2$. Scaling by $t=1/(x+y)$ makes the new variables sum to $1$, and the target becomes $1\ge4xy$.

### Important warning

Do not normalise a non-homogeneous statement. For example, $x^2+y^2\ge x+y$ has different degrees on its two sides. Scaling changes the comparison, so we cannot freely assume $x+y=1$.

## 4. Ratio substitution

In a homogeneous problem with two positive variables, the common size often cancels. The information that remains is their ratio.

Set:

$$
t=\frac xy>0.
$$

Then $x=ty$. For example:

$$
\frac{x^2+xy+y^2}{xy}
=\frac{t^2y^2+ty^2+y^2}{ty^2}
=t+1+\frac1t.
$$

AM-GM gives $t+1/t\ge2$, so:

$$
\frac{x^2+xy+y^2}{xy}\ge3.
$$

Equality occurs when $t=1$, meaning $x=y$.

## 5. Repeated-expression substitution

A substitution is useful when it replaces a repeated complicated piece by one simple symbol.

Consider:

$$
x^4-10x^2+9=0.
$$

Set $u=x^2$. Because $x$ is real, remember that $u\ge0$. The equation becomes:

$$
u^2-10u+9=0,
$$

so:

$$
(u-1)(u-9)=0.
$$

Thus $u=1$ or $u=9$. Returning to $x$ gives:

$$
\boxed{x=\pm1,\ \pm3}.
$$

Always return to the original variable and check restrictions introduced by the substitution.

## 6. Homogenising with a given constraint

Sometimes a condition can replace a constant and reveal a homogeneous statement.

Suppose $x+y=1$. To prove:

$$
x^2+y^2\ge\frac12,
$$

use $1=x+y$ to rewrite the target as:

$$
x^2+y^2\ge\frac{(x+y)^2}{2}.
$$

This is equivalent to $(x-y)^2\ge0$. Equality occurs when $x=y=1/2$.

Only use this method when the stated constraint genuinely allows the replacement.

## 7. How to choose a method

- If every term has the same degree, test whether normalising a sum or product simplifies the problem.
- If a two-variable expression depends only on their proportion, try $t=x/y$.
- If powers such as $x^4$ and $x^2$ repeat, try $u=x^2$.
- If the same longer expression repeats, give it a new name.
- If a constant appears with a constraint such as $x+y=1$, use the constraint to homogenise.
- After every substitution, record its domain and return to the original variables.

## Practice

### Basic

**A.** Decide whether each expression is homogeneous. If it is, state its degree.

1. $x^2+3xy+y^2$
2. $x^3+xy$
3. $\dfrac{a^2+b^2}{a+b}$
4. $(x+y)\left(\dfrac1x+\dfrac1y\right)$ for $x,y>0$

**B.** Under $a,b,c\mapsto ta,tb,tc$, determine the scaling factor of:

1. $\dfrac{a^2}{b+c}$
2. $\dfrac{ab}{(a+b)^2}$

**C.** Let $x,y>0$. Set $t=x/y$ and find the minimum of:

$$
\frac{x^2+3xy+y^2}{xy}.
$$

State the equality condition.

**D.** Solve over the real numbers using $u=x^2$:

$$
x^4-13x^2+36=0.
$$

### Intermediate

**E.** Let $x,y>0$. Prove:

$$
\frac{x^2+y^2}{x+y}\ge\frac{x+y}{2}.
$$

First identify the degree, then prove it either by normalising $x+y=1$ or directly.

**F.** Let $a,b,c>0$ with $a+b+c=1$. Prove:

$$
a^2+b^2+c^2\ge\frac13.
$$

Rewrite the constant using the given condition before applying a familiar inequality.

**G.** Let $x,y>0$. Prove using $t=x/y$ that:

$$
\frac{(x+y)^2}{xy}\ge4.
$$

State the equality condition.

## First study round

Read Sections 0-3, then attempt Problems A and B. Do not continue to ratio substitution until degree, scaling, and legal normalisation are clear.

## Completion standard

- [ ] Recognise homogeneous and non-homogeneous expressions
- [ ] Determine degree using the scaling test
- [ ] Use one legal normalisation
- [ ] Use a ratio substitution
- [ ] Use a repeated-power substitution and return to the original variable
- [ ] Complete one mixed transfer problem without notes
