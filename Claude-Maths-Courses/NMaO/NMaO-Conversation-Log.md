# NMaO Conversation Log

<span class="nmao-badge nmao-study">CONVERSATION LOG</span>

> [!info] Purpose
> This page records the important parts of our study conversations: explanations, decisions, questions, corrections, and next actions. Detailed mathematics belongs in lesson and correction files; this page preserves the learning story.

For the readable LaTeX version of the actual explanations, see [[NMaO-Live-Study-Notes]].

## 2026-09-17 - Starting the foundation curriculum

### Decision

We agreed to study the general TC toolkit first, use mocks to measure readiness, and climb gradually toward 1BAC. The 2017 paper attempt is diagnostic evidence, not a completed paper.

### Current pathway

1. Pre-learn concepts.
2. Learn methods through examples.
3. Train on basic and intermediate problems.
4. Complete mini-mocks.
5. Correct mistakes.
6. Take full mocks at the appropriate level.
7. Advance only when the evidence supports it.

See [[NMaO-Curriculum-Roadmap]] and [[NMaO-Lesson-Index]].

### Current lesson

We began **A01: Common-Denominator Normalisation and Symmetric Sums**.

We defined:

$$
s_1=x+y+z,\qquad
s_2=xy+xz+yz,\qquad
s_3=xyz.
$$

Then:

$$
\frac1x+\frac1y+\frac1z=\frac{s_2}{s_3},
\qquad
\frac1{xy}+\frac1{yz}+\frac1{zx}=\frac{s_1}{s_3}.
$$

The important idea is that dividing these expressions cancels the shared factor $s_3$.

### Question discussed

The student asked whether $P_A=s_2/s_3$. We confirmed:

$$
P_A=\frac1x+\frac1y+\frac1z=\frac{s_2}{s_3}.
$$

Similarly:

$$
P_B=\frac1{xy}+\frac1{yz}+\frac1{zx}=\frac{s_1}{s_3}.
$$

### Previous paper insight

In TC 2017-2018 Test 1 Problem 1, the normalisation method gives the intended ratio $\sqrt2$, but the photographed hypotheses appear inconsistent. This is recorded in [[NMaO-Corrections]].

### Next action

- [ ] Complete Practice Problems A, B, and C in [[NMaO-Lesson-01-Normalisation]].
- [ ] Review the answers with Codex.
- [ ] Record any mistakes in [[NMaO-Corrections]].
- [ ] Continue with the next A01 training problems.

## Conversation entry template

## Compact session context - 2026-09-20

### Study progress

- A04 Equations: complete. The student successfully handled restrictions, squaring, extraneous candidates, and the independent radical-equation transition.
- A05 Systems of Equations: complete. The student solved substitution and elimination systems, classified no-solution and infinitely-many-solution cases, and correctly parameterized an infinite family using either variable as the parameter.
- A06 Nonnegative Squares: complete. The student learned completing the square, leading coefficients, pairwise sums of squares, equality cases, and both direct-square and square-root proofs.
- A07 AM-GM: complete. The student learned arithmetic versus geometric means, balance intuition, fixed-sum product maxima, fixed-product sum minima, three-variable AM-GM, reciprocal products, weighted terms, and equality conditions.
- A08 Cauchy-Schwarz: in progress. The lesson was audited and rewritten cleanly.

### Important correction

In the screenshot algebra, starting from

$$
a^2d^2-2abcd+b^2c^2\ge0
$$

and adding $2abcd$ to both sides produces

$$
a^2d^2+b^2c^2\ge2abcd,
$$

because the two opposite terms cancel on the left. The version retaining $+2abcd$ on the left is an algebra mistake. The clean Cauchy-Schwarz proof uses

$$
(a^2+b^2)(c^2+d^2)-(ac+bd)^2=(ad-bc)^2\ge0.
$$

### Current next step

Read [[NMaO-Lesson-08-Cauchy-Schwarz]] and attempt Problems A-C. Keep mathematical explanations in the lesson/live notes using LaTeX; keep chat replies plain-text.

## 2026-09-26 - A08 completed and A09 started

### Study progress

- The student independently solved the four-variable weighted Cauchy-Schwarz transfer problem.
- The inequality setup, denominator count, division, and equality analysis were correct.
- A08 Cauchy-Schwarz is complete.
- A09 Homogeneity and Substitutions is now in progress.

### Current next step

Read Sections 0-3 of [[NMaO-Lesson-09-Homogeneity-Substitutions]] and attempt Problems A-B.

### YYYY-MM-DD - Session title

**Student question:**  

**Explanation given:**  

**Important mathematical idea:**  

**Files updated:**  

**Student's next attempt:**  

**Next session:**  
