# P1 · Chapter 2 — Quadratics

A quadratic is anything of the form `ax^2 + bx + c` with `a ≠ 0`. This chapter is the heart of P1 — completing the square and the discriminant come back constantly in later chapters. Aim for total fluency.

---

## 2.1 Solving quadratics by factorising

If a product equals zero, at least one factor is zero. So factorise, then set each bracket to 0.

### Worked example 1 — solve `x^2 + 2x − 15 = 0`
```
Factorise: two numbers multiplying to −15, adding to +2 → +5 and −3
(x + 5)(x − 3) = 0
x + 5 = 0  →  x = −5
x − 3 = 0  →  x = 3
```
**Answer:** `x = −5` or `x = 3`

### Worked example 2 — solve `6x^2 − x − 2 = 0`
```
a×c = 6×(−2) = −12. Two numbers multiplying to −12, adding to −1 → −4 and +3.
6x^2 − 4x + 3x − 2 = 0
2x(3x − 2) + 1(3x − 2) = 0
(2x + 1)(3x − 2) = 0
x = −1/2  or  x = 2/3
```
**Answer:** `x = −1/2` or `x = 2/3`

---

## 2.2 Completing the square

We rewrite `x^2 + bx + c` as `(x + p)^2 + q`. This is the most important algebraic skill in P1 — it reveals the turning point and is the basis of the quadratic formula.

**Method (when a = 1):** half the coefficient of `x`, square it, add and subtract.
```
x^2 + bx + c = (x + b/2)^2 − (b/2)^2 + c
```

### Worked example 3 — complete the square: `x^2 + 6x + 1`
```
Half of 6 is 3.  (x + 3)^2 = x^2 + 6x + 9, which is 8 too big, so subtract 8:
x^2 + 6x + 1 = (x + 3)^2 − 9 + 1 = (x + 3)^2 − 8
```
**Answer:** `(x + 3)^2 − 8`. Minimum point at `(−3, −8)`.

### Worked example 4 — when a ≠ 1: `2x^2 − 12x + 7`
```
Factor a out of the x-terms only:
2(x^2 − 6x) + 7
Complete the square inside: x^2 − 6x = (x − 3)^2 − 9
2[(x − 3)^2 − 9] + 7 = 2(x − 3)^2 − 18 + 7 = 2(x − 3)^2 − 11
```
**Answer:** `2(x − 3)^2 − 11`. Minimum point at `(3, −11)`.

**Why it matters:** from `a(x − h)^2 + k` you instantly read the **vertex (h, k)** — the minimum (if a>0) or maximum (if a<0) of the parabola.

---

## 2.3 The quadratic formula

For `ax^2 + bx + c = 0`:
```
x = [ −b ± √(b^2 − 4ac) ] / (2a)
```
Use it when factorising is hard or when an exact surd answer is needed. **Always write b, a, c with their signs first** — sign slips here are the most common exam error.

### Worked example 5 — solve `3x^2 − 7x + 1 = 0`, exact form
```
a = 3, b = −7, c = 1
Discriminant: b^2 − 4ac = (−7)^2 − 4(3)(1) = 49 − 12 = 37
x = [ 7 ± √37 ] / 6
```
**Answer:** `x = (7 + √37)/6` or `x = (7 − √37)/6`

---

## 2.4 The discriminant — how many roots?

The part under the root, `Δ = b^2 − 4ac`, tells you the number of real solutions **without solving**:

| Discriminant | Roots | Graph vs x-axis |
|--------------|-------|-----------------|
| `b^2 − 4ac > 0` | 2 distinct real roots | crosses twice |
| `b^2 − 4ac = 0` | 1 repeated root | touches (tangent) |
| `b^2 − 4ac < 0` | no real roots | never touches |

This is a *huge* exam favourite, especially "find the values of k for which...".

### Worked example 6 — find the values of `k` for which `x^2 + kx + 9 = 0` has equal roots
```
Equal roots ⇒ discriminant = 0.
a = 1, b = k, c = 9
b^2 − 4ac = 0  →  k^2 − 4(1)(9) = 0  →  k^2 − 36 = 0  →  k^2 = 36
k = 6  or  k = −6
```
**Answer:** `k = ±6`

### Worked example 7 — find the values of `k` for which `2x^2 + kx + 8 = 0` has no real roots
```
No real roots ⇒ discriminant < 0.
b^2 − 4ac < 0  →  k^2 − 4(2)(8) < 0  →  k^2 − 64 < 0  →  k^2 < 64
−8 < k < 8
```
**Answer:** `−8 < k < 8`

---

## 2.5 Quadratic graphs (parabolas)

- `a > 0` → U-shape (happy), minimum point. `a < 0` → ∩-shape (sad), maximum point.
- **y-intercept:** set x = 0, gives `(0, c)`.
- **x-intercepts (roots):** set y = 0 and solve.
- **Vertex:** from completed-square form `a(x − h)^2 + k`, vertex is `(h, k)`. The line `x = h` is the axis of symmetry.

### Worked example 8 — sketch `y = x^2 − 4x − 5`
```
Roots:   x^2 − 4x − 5 = 0 → (x − 5)(x + 1) = 0 → x = 5, x = −1
y-int:   (0, −5)
Vertex:  x^2 − 4x − 5 = (x − 2)^2 − 9  → vertex (2, −9), axis x = 2
Shape:   a = 1 > 0, so U-shape with minimum at (2, −9).
```
Sketch: U-shape crossing the x-axis at −1 and 5, through (0, −5), lowest point (2, −9).

---

## 2.6 The hidden quadratic (disguised quadratics)

Some equations aren't quadratics in `x` but *are* quadratics in something else. Substitute `u` for the repeated chunk.

### Worked example 9 — solve `x^4 − 5x^2 + 4 = 0`
```
Let u = x^2.  Then u^2 − 5u + 4 = 0 → (u − 1)(u − 4) = 0 → u = 1 or u = 4
Back-substitute:
x^2 = 1 → x = ±1
x^2 = 4 → x = ±2
```
**Answer:** `x = ±1, ±2` (four solutions)

---

## Chapter 2 — pitfalls checklist

- ✗ Losing a solution: a square root gives **±**, and `(x+5)(x−3)=0` gives **two** answers.
- ✗ Discriminant sign slips — write a, b, c with signs *before* substituting.
- ✗ When completing the square with `a ≠ 1`, forgetting to multiply the `−(b/2)^2` term back by `a`.
- ✗ Reading the vertex of `a(x−h)^2 + k` as `(h, k)` but with the **wrong sign on h** — `(x − 3)^2` gives h = +3.
- ✗ Forgetting to back-substitute in disguised quadratics (you solved for `u`, not `x`).

> **Next:** the Chapter 1–2 practice set. Treat every answer as wrong until you've checked it.
