# Lesson 05 - Systems of Equations

<span class="nmao-badge nmao-study">LESSON</span>

## Objective

Learn to solve two equations together, choose an efficient method, and recognize whether a system has one solution, no solution, or infinitely many solutions.

## 1. What is a system?

A system asks us to find values that satisfy several equations at the same time.

For example:

$$
\begin{cases}
x+y=7\\
x-y=1
\end{cases}
$$

The answer is an ordered pair $(x,y)$ that makes both equations true.

## 2. Substitution

Use substitution when one variable is already isolated, or can be isolated easily.

Consider:

$$
\begin{cases}
x+y=7\\
x-y=1
\end{cases}
$$

From the first equation:

$$
x=7-y.
$$

Substitute this into the second equation:

$$
(7-y)-y=1.
$$

Therefore:

$$
7-2y=1
\quad\Longrightarrow\quad
y=3.
$$

Substitute back:

$$
x=7-3=4.
$$

Thus the solution is:

$$
\boxed{(x,y)=(4,3)}.
$$

## 3. Elimination

Use elimination when adding or subtracting the equations can cancel one variable.

Consider:

$$
\begin{cases}
2x+3y=13\\
4x-3y=5
\end{cases}
$$

Add the equations. The $y$-terms cancel:

$$
6x=18.
$$

Hence:

$$
x=3.
$$

Substitute into the first equation:

$$
2(3)+3y=13
\quad\Longrightarrow\quad
3y=7
\quad\Longrightarrow\quad
y=\frac73.
$$

Therefore:

$$
\boxed{(x,y)=\left(3,\frac73\right)}.
$$

If the coefficients are not already opposites, multiply one or both equations first. The goal is to create matching coefficients, then add or subtract.

## 4. Which method should I choose?

- Choose substitution when a variable has coefficient $1$ or $-1$, or is already isolated.
- Choose elimination when coefficients can be made opposites with a small multiplication.
- In a timed problem, compare both methods briefly and choose the one with less expansion.

## 5. Checking a solution

Always substitute the ordered pair into both original equations. A pair is a solution only if both equations work.

For a system

$$
\begin{cases}
ax+by=c\\
dx+ey=f,
\end{cases}
$$

the graph consists of two lines:

- one intersection point means one solution;
- parallel distinct lines mean no solution;
- the same line means infinitely many solutions.

Algebraically, after elimination:

$$
0=k,\qquad k\ne0
$$

means no solution, while

$$
0=0
$$

means infinitely many solutions and one equation is redundant.

## 6. Word-problem translation

Translate the words into equations before solving. Define the variables clearly.

If two numbers have sum $31$ and difference $7$, let them be $x$ and $y$:

$$
\begin{cases}
x+y=31\\
x-y=7.
\end{cases}
$$

The system gives the two numbers. Do not begin calculations until every condition has been represented by an equation.

## Practice

### Basic

**A.** Solve by elimination:

$$
\begin{cases}
x+y=9\\
x-y=3
\end{cases}
$$

**B.** Solve by substitution:

$$
\begin{cases}
x=2y+1\\
3x-y=14
\end{cases}
$$

### Intermediate

**C.** Solve efficiently:

$$
\begin{cases}
3x+2y=16\\
5x-2y=8
\end{cases}
$$

**D.** Determine whether the system has one solution, no solution, or infinitely many solutions:

$$
\begin{cases}
2x+4y=6\\
x+2y=3
\end{cases}
$$

**E.** Determine whether the system has one solution, no solution, or infinitely many solutions:

$$
\begin{cases}
2x+4y=6\\
x+2y=5
\end{cases}
$$

### Application

**F.** Two numbers have sum $31$ and difference $7$. Find the two numbers by writing and solving a system.

Send your attempts before asking for the solutions. Start with A-C if you want a shorter first round.

## Answer key and worked solutions

### A

$$
\begin{cases}
x+y=9\\
x-y=3
\end{cases}
$$

Add the equations:

$$
2x=12\quad\Longrightarrow\quad x=6.
$$

Substitute into the first equation:

$$
6+y=9\quad\Longrightarrow\quad y=3.
$$

Therefore:

$$
\boxed{(x,y)=(6,3)}.
$$

### B

$$
\begin{cases}
x=2y+1\\
3x-y=14
\end{cases}
$$

Substitute the first equation into the second:

$$
3(2y+1)-y=14.
$$

Expand and simplify:

$$
6y+3-y=14
\quad\Longrightarrow\quad
5y=11
\quad\Longrightarrow\quad
y=\frac{11}{5}.
$$

Now find $x$:

$$
x=2\left(\frac{11}{5}\right)+1
=\frac{22}{5}+\frac55
=\frac{27}{5}.
$$

Therefore:

$$
\boxed{(x,y)=\left(\frac{27}{5},\frac{11}{5}\right)}.
$$

### C

$$
\begin{cases}
3x+2y=16\\
5x-2y=8
\end{cases}
$$

Add the equations:

$$
8x=24\quad\Longrightarrow\quad x=3.
$$

Substitute into the first equation:

$$
3(3)+2y=16
\quad\Longrightarrow\quad
2y=7
\quad\Longrightarrow\quad
y=\frac72.
$$

Therefore:

$$
\boxed{(x,y)=\left(3,\frac72\right)}.
$$

### D

$$
\begin{cases}
2x+4y=6\\
x+2y=3
\end{cases}
$$

Multiply the second equation by $2$:

$$
2x+4y=6.
$$

This is exactly the first equation, so both equations describe the same line. The system has infinitely many solutions.

Writing $y=t$, we have:

$$
x+2t=3\quad\Longrightarrow\quad x=3-2t.
$$

Thus all solutions are:

$$
\boxed{(x,y)=(3-2t,t),\quad t\in\mathbb R}.
$$

### E

$$
\begin{cases}
2x+4y=6\\
x+2y=5
\end{cases}
$$

Multiply the second equation by $2$:

$$
2x+4y=10.
$$

The first equation says the same left-hand side equals $6$, while the second says it equals $10$. This would require

$$
6=10,
$$

which is impossible. Therefore:

$$
\boxed{\text{The system has no solution}.}
$$

### F

Let the numbers be $x$ and $y$. The conditions give:

$$
\begin{cases}
x+y=31\\
x-y=7
\end{cases}
$$

Add the equations:

$$
2x=38\quad\Longrightarrow\quad x=19.
$$

Substitute into the first equation:

$$
19+y=31\quad\Longrightarrow\quad y=12.
$$

Therefore the two numbers are:

$$
\boxed{19\text{ and }12}.
$$

## Answer summary

$$
\boxed{\text{A: }(6,3)}
\qquad
\boxed{\text{B: }\left(\frac{27}{5},\frac{11}{5}\right)}
$$

$$
\boxed{\text{C: }\left(3,\frac72\right)}
\qquad
\boxed{\text{D: infinitely many solutions}}
$$

$$
\boxed{\text{E: no solution}}
\qquad
\boxed{\text{F: }19\text{ and }12}
$$

## Extra practice: parameterized solutions

### G

Determine whether the system has one solution, no solution, or infinitely many solutions. If it has infinitely many solutions, express all of them using a parameter $t$:

$$
\begin{cases}
4x-2y=8\\
2x-y=4
\end{cases}
$$

Do not just state the type of solution. Write the complete solution set in parametric form.

#### Solution to G

The first equation is twice the second equation:

$$
2(2x-y)=2(4)
\quad\Longrightarrow\quad
4x-2y=8.
$$

Therefore both equations describe the same line, so the system has infinitely many solutions.

Use the second equation:

$$
2x-y=4
\quad\Longrightarrow\quad
y=2x-4.
$$

Let $x=t$, where $t\in\mathbb R$. Then:

$$
y=2t-4.
$$

Thus the complete solution set is:

$$
\boxed{(x,y)=(t,2t-4),\quad t\in\mathbb R}.
$$

For example, $t=2$ gives $(x,y)=(2,0)$, which satisfies both original equations.

## Completion standard

- [x] Understand substitution and elimination
- [x] Complete Problems A-F
- [x] Classify systems with no solution or infinitely many solutions
- [x] Check both original equations
- [x] Complete one fresh system without notes
