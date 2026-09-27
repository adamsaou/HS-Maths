# NMaO Pre-Learning Roadmap

<span class="nmao-badge nmao-study">PRE-LEARNING</span>

> [!important] How this works
> This file supports the general curriculum in [[NMaO-Curriculum-Roadmap]]. We do not jump blindly from paper to paper. We learn the tools, practise them on simpler examples, use mocks to measure readiness, and then transfer them to NMaO problems at the appropriate level.

## The five-step learning cycle

### 1. Preview

Identify the likely topic and the prerequisite ideas. Do not read a solution to the target problem.

### 2. Learn

Study the definition, key identity, theorem, equality case, and one simple example.

### 3. Train

Solve 3-5 easier or similar problems. The goal is to recognise the technique without help.

### 4. Transfer

Attempt the NMaO problem independently. Use the normal 45-60 minute training limit unless the paper is officially timed.

### 5. Correct and retain

Record the first obstacle in [[NMaO-Corrections]], rewrite the proof, and solve one transfer problem later.

## Diagnostic example: TC 2017-2018 - Test 1

Problems 1 and 2 have already been attempted and corrected. Problems 3 and 4 show useful examples of the tools that belong in the general foundation curriculum; they are not our immediate target until the foundation blocks are complete.

### Problem 1 tools: algebraic normalisation

- Common denominators
- Symmetric sums
- Cancelling a shared factor
- Checking whether hypotheses are consistent

Core pattern:

$$
\frac1x+\frac1y+\frac1z
=\frac{xy+xz+yz}{xyz},
\qquad
\frac1{xy}+\frac1{yz}+\frac1{zx}
=\frac{x+y+z}{xyz}.
$$

### Problem 2 tools: coordinate geometry

- Put a projection line on the $x$-axis
- Use midpoint coordinates
- Use parallelogram coordinate relations
- Compare squared distances

### Problem 3 tools: inequalities

Learn AM-GM in the form

$$
u+v\ge 2\sqrt{uv},
$$

with equality when $u=v$.

For

$$
ax+\frac bx,
$$

take $u=ax$ and $v=b/x$. Then

$$
ax+\frac bx\ge 2\sqrt{ab},
$$

with equality when $ax=b/x$.

For the second inequality, pair terms:

$$
\frac{xy}{z}+\frac{xz}{y}\ge 2x,
$$

because their product is $x^2$. Do the same for $y$ and $z$, then add the three inequalities.

### Problem 4 tools: parity and pigeonhole

Every integer coordinate is either even or odd. Therefore every point belongs to one of four parity classes:

$$
(\text{even},\text{even}),\quad
(\text{even},\text{odd}),\quad
(\text{odd},\text{even}),\quad
(\text{odd},\text{odd}).
$$

Five points and four classes guarantee two points in the same class. Their coordinate differences are both even, so their midpoint has integer coordinates.

## Immediate study plan: Block A foundation

### Session A - Algebraic normalisation

- [ ] Learn AM-GM and equality conditions
- [ ] Prove $ax+b/x\ge2\sqrt{ab}$
- [ ] Solve 3 basic AM-GM problems
- [ ] Practise on a fresh, easier inequality

### Session B - Inequalities

- [ ] Reproduce the pairwise AM-GM argument
- [ ] Solve 2 similar cyclic inequalities
- [ ] Solve 2-3 fresh cyclic inequalities
- [ ] Record equality cases

### Session C - Number theory preview

- [ ] Learn divisibility and parity basics
- [ ] Solve 3 basic modular arithmetic problems
- [ ] Record questions for the next block

### Session D - Mini-mock and correction

- [ ] Complete a fresh mixed mini-mock without notes
- [ ] Correct every attempt
- [ ] Rewrite the final proofs in your own words
- [ ] Update [[NMaO-Corrections]]
- [ ] Do not retake the paper until the foundation block is complete

## Progression after the first paper

For each later paper, repeat the same cycle:

1. Preview the problems.
2. Pre-learn the missing tools.
3. Train on simpler examples.
4. Attempt the paper in the appropriate mode.
5. Correct and review before advancing.
