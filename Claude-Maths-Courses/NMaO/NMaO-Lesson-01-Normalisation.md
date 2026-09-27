# Lesson 01 - Common-Denominator Normalisation

<span class="nmao-badge nmao-study">LESSON</span>

## Objective

Learn to rewrite reciprocal expressions so that a common factor cancels, without solving for the individual variables.

## 1. The basic pattern

To combine

$$
\frac1x+\frac1y+\frac1z,
$$

use the common denominator $xyz$:

$$
\frac1x=\frac{yz}{xyz},\qquad
\frac1y=\frac{xz}{xyz},\qquad
\frac1z=\frac{xy}{xyz}.
$$

Therefore,

$$
\frac1x+\frac1y+\frac1z
=\frac{xy+xz+yz}{xyz}.
$$

For pairwise reciprocal products:

$$
\frac1{xy}=\frac z{xyz},\qquad
\frac1{yz}=\frac x{xyz},\qquad
\frac1{zx}=\frac y{xyz},
$$

so

$$
\frac1{xy}+\frac1{yz}+\frac1{zx}
=\frac{x+y+z}{xyz}.
$$

## 2. Symmetric sums

It is useful to name the expressions:

$$
s_1=x+y+z,\qquad
s_2=xy+xz+yz,\qquad
s_3=xyz.
$$

They are called symmetric because their values do not change when $x,y,z$ are rearranged.

The two identities become

$$
\frac1x+\frac1y+\frac1z=\frac{s_2}{s_3},
\qquad
\frac1{xy}+\frac1{yz}+\frac1{zx}=\frac{s_1}{s_3}.
$$

If the target is $s_1/s_2$, divide the second identity by the first:

$$
\frac{\frac{s_1}{s_3}}{\frac{s_2}{s_3}}
=\frac{s_1}{s_2}.
$$

The unwanted factor $s_3$ disappears.

## 3. Worked example

Suppose

$$
\frac1x+\frac1y+\frac1z=\frac56
$$

and

$$
\frac1{xy}+\frac1{yz}+\frac1{zx}=\frac12.
$$

Find

$$
\frac{x+y+z}{xy+xz+yz}.
$$

Using the identities:

$$
\frac{s_2}{s_3}=\frac56,\qquad
\frac{s_1}{s_3}=\frac12.
$$

Divide:

$$
\frac{s_1}{s_2}
=\frac{\frac12}{\frac56}
=\frac35.
$$

There is no need to find $x$, $y$, or $z$.

## 4. Recognition checklist

When you see reciprocal expressions:

- [x] Identify the common denominator.
- [x] Rewrite every term separately.
- [x] Name repeated symmetric expressions if useful.
- [x] Compare the rewritten equations with the target.
- [x] Divide only when the denominator is known to be nonzero.
- [x] Check whether the hypotheses are consistent.

## Practice - attempt without help

### Problem A

Rewrite the following in terms of

$$
s_1=a+b+c,\qquad s_2=ab+bc+ca,\qquad s_3=abc:
$$

$$
\frac1a+\frac1b+\frac1c.
$$

### Problem B

Suppose $a,b,c\ne0$ and

$$
\frac1a+\frac1b+\frac1c=6,
\qquad
\frac1{ab}+\frac1{bc}+\frac1{ca}=9.
$$

Find

$$
\frac{a+b+c}{ab+bc+ca}.
$$

### Problem C

Without calculating $x,y,z$, explain which two reciprocal expressions would help find

$$
\frac{x+y+z}{xy+xz+yz}.
$$

## Session record

- Date:
- Problems attempted:
- What felt automatic:
- What needs practice:
- Next lesson:
