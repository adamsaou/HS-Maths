# NMaO Corrections and Review

<span class="nmao-badge nmao-correction">CORRECTIONS LOG</span>

> [!important] Correction principle
> A correction is not just reading the answer. Reconstruct the idea, identify the first error, and later solve a related problem independently.

## Correction workflow

1. Reattempt the problem without looking at the solution.
2. Compare the attempt with the correct argument.
3. Locate the **first** incorrect or unjustified step.
4. Classify the error.
5. Write the clean proof in LaTeX.
6. Add a transfer problem or review date.
7. Revisit until the method works without help.

## Error categories

- **K:** knowledge gap
- **I:** incorrect idea or strategy
- **C:** calculation or algebra error
- **L:** logical gap or missing case
- **P:** proof-writing problem
- **T:** time management or problem selection

## Review queue

| Problem | Topic | Error code | Review date | Status |
|---|---|---|---|---|
| | | | | |

## Correction records

### TC 2017-2018 - Test 1 - Problem 1 - 2026-09-16

- Topic: Algebra and inequalities
- Error code: L / source check required
- Difficulty: Appropriate for current TC training
- First important observation: Setting
  $$
  a=\frac1x,\qquad b=\frac1y,\qquad c=\frac1z
  $$
  gives
  $$
  a+b+c=\sqrt2,\qquad ab+bc+ca=2.
  $$
- What was correct: The transformation
  $$
  \frac{x+y+z}{xy+yz+zx}
  =
  \frac{ab+bc+ca}{a+b+c}
  $$
  is correct. If the conditions are consistent, it would give $\sqrt2$.
- Missing idea: Always check whether the hypotheses are possible before calculating the requested expression.
- In-depth algebra idea:

  Name the three repeated pieces:
  $$
  R=x+y+z,\qquad S=xy+xz+yz,\qquad P=xyz.
  $$
  The first condition is
  $$
  \frac1x+\frac1y+\frac1z
  =\frac{yz+xz+xy}{xyz}
  =\frac SP
  =\sqrt2.
  $$
  The second condition is
  $$
  \frac1{xy}+\frac1{yz}+\frac1{zx}
  =\frac z{xyz}+\frac x{xyz}+\frac y{xyz}
  =\frac RP
  =2.
  $$
  The target is $R/S$. Both given equations contain the same factor $1/P$, so divide them:
  $$
  \frac{R/P}{S/P}=\frac RS
  =\frac2{\sqrt2}
  =\sqrt2.
  $$
  This is the central pattern: when two expressions have the same denominator or common factor, divide them to cancel the part you do not need. We never need to find $x$, $y$, and $z$ individually.

  The numerator checklist is:
  $$
  \frac1x+\frac1y+\frac1z
  \longrightarrow yz+xz+xy,
  \qquad
  \frac1{xy}+\frac1{yz}+\frac1{zx}
  \longrightarrow z+x+y.
  $$
  The first numerator contains pairwise products; the second numerator contains the individual variables.
- Consistency check:
  $$
  (a+b+c)^2
  =a^2+b^2+c^2+2(ab+bc+ca).
  $$
  Since $a,b,c>0$, we have $a^2+b^2+c^2\ge ab+bc+ca$. Therefore
  $$
  (a+b+c)^2\ge 3(ab+bc+ca)=6,
  $$
  but the stated condition gives $(a+b+c)^2=2$. This is impossible.
- Why the factor $3$ appears:

  Set $q=ab+bc+ca$. The identity
  $$
  (a+b+c)^2=a^2+b^2+c^2+2q
  $$
  contains two copies of $q$ explicitly. Also,
  $$
  a^2+b^2+c^2\ge q,
  $$
  because
  $$
  (a-b)^2+(b-c)^2+(c-a)^2
  =2(a^2+b^2+c^2-q)\ge0.
  $$
  Therefore the square contains at least one more copy of $q$:
  $$
  (a+b+c)^2
  \ge q+2q
  =3q
  =3(ab+bc+ca).
  $$
  In this problem, $q=2$, so $(a+b+c)^2\ge6$, contradicting $(\sqrt2)^2=2$.
- Provisional conclusion: If the second right-hand side really is $2$, there are no such positive real numbers, so the problem statement contains a typo or the intended answer is that no triple exists. If the second right-hand side is a different value, we must recheck the calculation.
- Status: Source statement must be verified before marking mastered.

### TC 2017-2018 - Test 1 - Problem 2 - 2026-09-16

- Topic: Euclidean geometry and vectors
- Error code: P / L
- Difficulty: Appropriate for current TC training
- What was correct: You identified the useful relations
  $$
  \overrightarrow{AI}=\overrightarrow{AB}+\overrightarrow{BI}
  \quad\text{and}\quad
  \overrightarrow{BI}=\frac12\overrightarrow{BC}.
  $$
  Your diagrams and vector direction were promising.
- First missing step: Because $H$ is the orthogonal projection of $D$ onto $(AI)$, the proof must explicitly write the projection formula for $\overrightarrow{AH}$.
- Clean proof:

  Let
  $$
  \mathbf u=\overrightarrow{AB},\qquad
  \mathbf v=\overrightarrow{BI}.
  $$
  Since $I$ is the midpoint of $[BC]$ and $ABCD$ is a parallelogram,
  $$
  \overrightarrow{AD}=2\mathbf v,\qquad
  \overrightarrow{AI}=\mathbf u+\mathbf v.
  $$
  Put $\mathbf w=\mathbf u+\mathbf v$. Since $H$ is the projection of $D$ onto the line directed by $\mathbf w$,
  $$
  \overrightarrow{AH}
  =
  \frac{(2\mathbf v)\cdot\mathbf w}{\mathbf w\cdot\mathbf w}\mathbf w.
  $$
  Define
  $$
  \lambda=\frac{\mathbf v\cdot\mathbf w}{\mathbf w\cdot\mathbf w}.
  $$
  Then $\overrightarrow{AH}=2\lambda\mathbf w$. Also
  $$
  \overrightarrow{AC}=\mathbf u+2\mathbf v=\mathbf w+\mathbf v.
  $$
  Hence
  $$
  \overrightarrow{CH}
  =\overrightarrow{AH}-\overrightarrow{AC}
  =(2\lambda-1)\mathbf w-\mathbf v.
  $$
  Using $\mathbf v\cdot\mathbf w=\lambda\|\mathbf w\|^2$, direct expansion gives
  $$
  \begin{aligned}
  \|\overrightarrow{CH}\|^2
  &=(2\lambda-1)^2\|\mathbf w\|^2
    -2(2\lambda-1)(\mathbf v\cdot\mathbf w)
    +\|\mathbf v\|^2\\
  &=\|\mathbf w\|^2-2(\mathbf v\cdot\mathbf w)+\|\mathbf v\|^2\\
  &=\|\mathbf w-\mathbf v\|^2\\
  &=\|\mathbf u\|^2.
  \end{aligned}
  $$
  But $\|\mathbf u\|=AB=CD$, so $\boxed{CH=CD}$.
- Intuitive coordinate proof:

  The projection tells us to choose $AI$ as the $x$-axis. Put
  $$
  A=(0,0),\qquad I=(p,0),\qquad D=(q,r).
  $$
  In a parallelogram, $C=B+D$ in vector notation. Since $I$ is the midpoint of $BC$,
  $$
  I=\frac{B+C}{2}
   =\frac{B+(B+D)}2
   =B+\frac D2.
  $$
  Therefore
  $$
  B=I-\frac D2,\qquad C=I+\frac D2
   =\left(p+\frac q2,\frac r2\right).
  $$
  Because $H$ is the projection of $D=(q,r)$ onto the $x$-axis,
  $$
  H=(q,0).
  $$
  Now compare the two vectors:
  $$
  \overrightarrow{CH}
  =\left(\frac q2-p,-\frac r2\right),
  \qquad
  \overrightarrow{CD}
  =\left(\frac q2-p,\frac r2\right).
  $$
  They have the same horizontal component and opposite vertical components. They are mirror images, so their lengths are equal:
  $$
  CH^2=\left(\frac q2-p\right)^2+\left(\frac r2\right)^2=CD^2.
  $$
  Hence $\boxed{CH=CD}$.
- Recognition pattern:
  - Projection onto a line: make that line the $x$-axis.
  - Midpoint: use the average of coordinates.
  - Parallelogram: use $C=B+D$ after placing $A$ at the origin.
  - Equal lengths: compare squared distances.
- Transfer task: Rewrite this proof using your own notation and explain exactly where the projection formula is used.
- Status: Corrected; transfer rewrite pending.

### Template

### A08 F-transfer - 2026-09-26

- Topic: Cauchy-Schwarz / weighted fractions
- Error code: I
- What was correct: The weighted Cauchy-Schwarz strategy was appropriate, and the first list correctly used $a/\sqrt{b+c}$, $b/\sqrt{c+a}$, and $c/\sqrt{a+b}$ so that its squared size equals the left-hand side.
- First incorrect step: The second list used unrelated square-root terms, so the matching score developed extra radicals instead of simplifying to $a+b+c$.
- Missing idea: Pair each denominator-containing entry with its cancelling square root. Use $\sqrt{b+c}$ with $a/\sqrt{b+c}$, and similarly for the other terms.
- Next attempt: Recalculate the matching score and the squared size of the second list, apply Cauchy-Schwarz, and derive the equality condition independently.
- Clean proof: Added to [[NMaO-Lesson-08-Cauchy-Schwarz]] and [[NMaO-Live-Study-Notes]].
- Review evidence: Solved the four-variable close variant F-transfer 2 independently, including the equality case.
- Status: Reviewed and mastered.

#### Paper - Problem - Date

- Topic:
- Error code:
- Difficulty:
- First incorrect step:
- What was correct:
- Missing idea:
- Correct proof:

$$
\text{Write the central argument here.}
$$

- Transfer problem:
- Review dates:
- Status: open / reviewed / mastered

## Mastery rule

### A01 practice check - 2026-09-17

- **Problem A:** Correct. You rewrote
  $$
  \frac1a+\frac1b+\frac1c
  =\frac{ab+ac+bc}{abc}.
  $$
- **Problem B:** Correct answer, with a notation issue. Keep one convention throughout:
  $$
  s_1=a+b+c,\qquad
  s_2=ab+bc+ca,\qquad
  s_3=abc.
  $$
  Then
  $$
  \frac{s_2}{s_3}=6,\qquad
  \frac{s_1}{s_3}=9.
  $$
  Therefore
  $$
  \frac{a+b+c}{ab+bc+ca}
  =\frac{s_1}{s_2}
  =\frac{s_1/s_3}{s_2/s_3}
  =\frac96
  =\boxed{\frac32}.
  $$
- **Problem C:** Correct. The useful expressions are
  $$
  \frac1a+\frac1b+\frac1c
  \quad\text{and}\quad
  \frac1{ab}+\frac1{bc}+\frac1{ca}.
  $$
- **Main correction:** Do not redefine $s_1,s_2,s_3$ halfway through a solution. The labels are arbitrary, but consistency is essential.
- **Status:** Basic technique understood; one transfer problem remains before marking A01 complete.

### A01 transfer check - 2026-09-17

- The common-denominator rewrites were correct:
  $$
  \frac1x+\frac1y+\frac1z
  =\frac{xy+xz+yz}{xyz}=8,
  $$
  and
  $$
  \frac1{xy}+\frac1{yz}+\frac1{zx}
  =\frac{x+y+z}{xyz}=3.
  $$
- The final answer was correct:
  $$
  \frac{xy+xz+yz}{x+y+z}
  =\frac83.
  $$
- Notation note: you used $s_1=xyz$, $s_2=x+y+z$, and $s_3=xy+xz+yz$. This is allowed if stated and used consistently, but our standard convention is
  $$
  s_1=x+y+z,\qquad s_2=xy+xz+yz,\qquad s_3=xyz.
  $$
- Status: A01 complete. Continue monitoring notation consistency.

### A02 practice check - 2026-09-17

- **A:** Correct:
  $$
  (2x-3)^2=4x^2-12x+9.
  $$
- **B:** Correct:
  $$
  x^2-16=(x-4)(x+4).
  $$
- **C:** Correct grouping:
  $$
  x^2+7x+12
  =x^2+3x+4x+12
  =x(x+3)+4(x+3)
  =(x+3)(x+4).
  $$
- **D:** Correct difference of squares:
  $$
  4a^2-25b^2=(2a-5b)(2a+5b).
  $$
- **E:** Correct substitution $u=x^2$, followed by complete factorisation:
  $$
  x^4-5x^2+4
  =(x-1)(x+1)(x-2)(x+2).
  $$
- **F:** Correct identity proof. When subtracting $(x-y)^2$, remember that every sign inside the bracket changes.
- **Formula note:** If the first identity at the top is
  $$
  a^3\pm b^3=(a\pm b)(a^2\mp ab+b^2),
  $$
  then it is correct. The middle sign is opposite to the outside sign.
- Status: Exercises A-F correct; one transfer problem remains before A02 is complete.

### A02 transfer correction - 2026-09-17

- Correct start: setting $u=x^2$ was exactly the right substitution.
- Useful but incomplete observation:
  $$
  4u^2-13u+9=(2u-3)^2-u.
  $$
  This identity does not expose the required factors efficiently.
- Factor the quadratic in $u$ by splitting the middle term:
  $$
  4u^2-13u+9
  =4u^2-9u-4u+9
  =(u-1)(4u-9).
  $$
- Substitute back and use two difference-of-squares identities:
  $$
  4x^4-13x^2+9
  =(x^2-1)(4x^2-9)
  =(x-1)(x+1)(2x-3)(2x+3).
  $$
- Status: Corrected; rewrite the factorisation once independently before marking A02 complete.

### A03 practice check - 2026-09-17

- **A:** Correct power simplification.
- **B:** Correct conversion to positive exponents:
  $$
  \frac{a^{-3}b^2}{c^{-2}}
  =\frac{b^2c^2}{a^3}.
  $$
- **C:** The simplification is correct:
  $$
  \frac{x^2-25}{x^2+5x}
  =\frac{(x-5)(x+5)}{x(x+5)}
  =\frac{x-5}{x}.
  $$
  However, the original denominator gives two restrictions:
  $$
  x\ne0,\qquad x\ne-5.
  $$
- **D:** The simplification is correct:
  $$
  \frac{x^2-4x+4}{x^2-4}
  =\frac{(x-2)^2}{(x-2)(x+2)}
  =\frac{x-2}{x+2}.
  $$
  The original denominator gives:
  $$
  x\ne2,\qquad x\ne-2.
  $$
- **E:** Correct:
  $$
  \frac{a^2-b^2}{a^2+2ab+b^2}
  =\frac{(a-b)(a+b)}{(a+b)^2}
  =\frac{a-b}{a+b},
  $$
  with restriction $a+b\ne0$.
- **F:** Correct reasoning. The numerator $x+5$ is not a product containing $x$, so $x$ cannot be cancelled. The expression is not generally equal to $5$; for example, at $x=1$ it equals $6$.
- Main lesson: restrictions come from the original denominator, including factors that are later cancelled.
- Status: A-F mostly correct; restriction transfer problem pending.

### A03 transfer correction - 2026-09-17

- Correct factorisation:
  $$
  x^2-9=(x-3)(x+3),
  $$
  and
  $$
  x^2-x-6=(x-3)(x+2).
  $$
- Correct cancellation:
  $$
  \frac{x^2-9}{x^2-x-6}
  =\frac{(x-3)(x+3)}{(x-3)(x+2)}
  =\frac{x+3}{x+2}.
  $$
- The original denominator is zero when
  $$
  x=3\quad\text{or}\quad x=-2.
  $$
  Therefore the restrictions are
  $$
  x\ne3,\qquad x\ne-2.
  $$
- Important distinction: roots of the numerator do not create restrictions. The restrictions come only from the original denominator.
- Status: Corrected; rewrite the final line with the correct restrictions before marking A03 complete.

Mark a correction **mastered** only after solving the original problem or a close variant independently at least once after a delay.

### A05 classification clarification - 2026-09-18

The distinction between Problems D and E was clarified:

- **D:** infinitely many solutions, because the two equations represent the same line. A parameter such as $t$ can describe the complete family of solutions.
- **E:** no solution, because the equations contradict each other after elimination. There is no parameterized family for E.

The student solved the numerical systems correctly; this was only a classification-description omission.

### A06 clarification - 2026-09-18

The completing-square formula comes from expanding a trial square and correcting its constant term:

$$
x^2+bx+c
=\left(x+\frac b2\right)^2+c-\frac{b^2}{4}.
$$

For the three-variable identity, each square term appears twice after expansion, producing the factor $2$:

$$
(a-b)^2+(b-c)^2+(c-a)^2
=2(a^2+b^2+c^2-ab-bc-ca).
$$

Dividing by $2$ is valid because $2>0$, so the inequality direction does not change, and $0/2=0$.

### A06 minimum-value clarification - 2026-09-18

For the extra exercise, the minimum is $7$, not $\frac72$.

The decisive line is:

$$
2x^2-12x+25
=2(x^2-6x)+25
=2\left((x-3)^2-9\right)+25
=2(x-3)^2+7.
$$

The constant calculation is:

$$
-18+25=7,
$$

not $7/2$. Since the square term is nonnegative, the minimum is $7$, reached at $x=3$. A direct check confirms it:

$$
2(3)^2-12(3)+25=18-36+25=7.
$$
