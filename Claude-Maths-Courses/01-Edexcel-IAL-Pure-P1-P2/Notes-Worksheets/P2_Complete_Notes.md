# Pure Mathematics 2 — Complete Notes

Edexcel International A-Level. Eight chapters. Pair each with the matching worksheet in **P2_Worksheets.md**.

*Note: chapter order follows the standard IAL P2 syllabus; the exact ordering in your specific book may differ slightly, but every topic here is on the P2 spec. I'll confirm against your file once the reader is available.*

**Contents**
1. Algebraic methods (division, factor & remainder theorems, proof)
2. Coordinate geometry — circles
3. Exponentials and logarithms
4. The binomial expansion
5. Sequences and series
6. Radian measure (arc length & sector area)
7. Differentiation — applications & optimisation
8. Integration — area & the trapezium rule

---
---

# Chapter 1 — Algebraic Methods

## 1.1 Algebraic fractions
Factorise top and bottom, then cancel common factors.
**Example:** `(x²−9)/(x²+5x+6) = (x−3)(x+3) / [(x+2)(x+3)] = (x−3)/(x+2)`.

## 1.2 Polynomial (long) division
To divide a polynomial by `(x − a)`, use long division or "matching coefficients". The result is `quotient + remainder/(x−a)`.
**Example:** `x³ − 2x² − 5x + 6 ÷ (x − 1)` gives `x² − x − 6` exactly (remainder 0), so `x³−2x²−5x+6 = (x−1)(x²−x−6) = (x−1)(x−3)(x+2)`.

## 1.3 The remainder theorem
When `f(x)` is divided by `(x − a)`, the remainder is `f(a)`. (Divided by `(bx − a)`, remainder is `f(a/b)`.)
**Example:** `f(x)=x³+2x²−3x+4` divided by `(x−2)`: remainder `= f(2) = 8+8−6+4 = 14`.

## 1.4 The factor theorem
`(x − a)` is a factor of `f(x)` **if and only if** `f(a) = 0`. This is the standard route to factorising cubics: test small values `±1, ±2, …` until one gives 0, then divide out.
**Example:** factorise `f(x)=x³−3x²−x+3`. `f(1)=1−3−1+3=0`, so `(x−1)` is a factor. Dividing: `x³−3x²−x+3=(x−1)(x²−2x−3)=(x−1)(x−3)(x+1)`.

## 1.5 Proof
- **Proof by deduction:** argue directly from known facts.
- **Proof by exhaustion:** check all cases.
- **Disproof by counterexample:** one example that fails kills a claim.
Use clear algebra; e.g. an even number is `2n`, an odd number `2n+1`; consecutive integers `n, n+1`.

**Pitfalls:** sign errors in division; remember remainder theorem uses `f(a)`, where the divisor is `(x−a)` (so for `(x+3)` use `f(−3)`); always check a cubic factorisation by expanding or by a second value.

---
---

# Chapter 2 — Coordinate Geometry: Circles

## 2.1 Equation of a circle
Centre `(a, b)`, radius `r`: `(x − a)² + (y − b)² = r²`.

## 2.2 General form
`x² + y² + 2gx + 2fy + c = 0`. **Complete the square** in x and in y to find the centre and radius.
**Example:** `x² + y² − 6x + 4y − 12 = 0`.
`(x−3)² − 9 + (y+2)² − 4 − 12 = 0 ⇒ (x−3)² + (y+2)² = 25`. Centre `(3, −2)`, radius `5`.

## 2.3 Key circle facts (these solve most problems)
- The **tangent** at a point is **perpendicular to the radius** drawn to that point.
- The **perpendicular from the centre to a chord bisects** the chord.
- The angle in a **semicircle** is `90°` (a triangle inscribed with the diameter as one side is right-angled).

**Example (tangent):** circle centre `(3, −2)`, find the tangent at point `P(6, 2)` (on the circle). Radius gradient `= (2−(−2))/(6−3) = 4/3`. Tangent gradient `= −3/4`. Tangent: `y − 2 = −¾(x − 6) ⇒ 3x + 4y − 26 = 0`.

## 2.4 Intersections of a line and a circle
Substitute the line into the circle equation → quadratic in `x`. Discriminant tells you: 2 roots = line cuts the circle (secant), `Δ=0` = tangent, `Δ<0` = misses.

**Pitfalls:** sign of the centre — `(x−3)²` ⇒ `a = +3`, but the general form has `+2gx` so `g = −3`; remember `r` is the square root of the right-hand side; the tangent gradient is the **negative reciprocal** of the radius gradient.

---
---

# Chapter 3 — Exponentials and Logarithms

## 3.1 Exponential functions
`y = aˣ` (a>0): passes through `(0,1)`, increasing if `a>1`. The special base **`e ≈ 2.718`** gives `y = eˣ`, whose gradient equals itself.

## 3.2 Logarithms — definition
`log_a x = y ⟺ aʸ = x`. A log answers "what power?". `log₂ 8 = 3` because `2³ = 8`. **`ln x` means `log_e x`**, the inverse of `eˣ`.

## 3.3 The laws of logs
- `log(xy) = log x + log y`
- `log(x/y) = log x − log y`
- `log(xᵏ) = k·log x`
- `log_a a = 1`, `log_a 1 = 0`

## 3.4 Solving equations
For `aˣ = b`, take logs of both sides: `x = log b / log a` (or use `ln`).
**Example:** `3ˣ = 20 ⇒ x = ln20/ln3 ≈ 2.727`.
**Example (log laws):** `2 log x − log 3 = log 12 ⇒ log(x²/3) = log 12 ⇒ x²/3 = 12 ⇒ x² = 36 ⇒ x = 6` (reject `−6`, log needs `x>0`).

## 3.5 Exponential models
Growth/decay `y = A·eᵏᵗ`. Use given data points to find `A` and `k` (take `ln` to linearise).

**Pitfalls:** `log(x+y) ≠ log x + log y` (the law is for products); always discard non-positive solutions for `log x`; keep the base consistent; `ln e = 1`, `ln 1 = 0`.

---
---

# Chapter 4 — The Binomial Expansion

## 4.1 Pascal's triangle and `nCr`
The coefficients of `(a+b)ⁿ` are row `n` of Pascal's triangle, or `nCr = n! / [r!(n−r)!]` (the `nCr` button on your calculator).

## 4.2 The binomial theorem (positive integer n)
`(a + b)ⁿ = Σ_{r=0}^{n} nCr · a^{n−r} · bʳ`
`= aⁿ + nC1·a^{n−1}b + nC2·a^{n−2}b² + … + bⁿ`.

**Example:** `(2 + x)⁴ = 16 + 4(8)x + 6(4)x² + 4(2)x³ + x⁴ = 16 + 32x + 24x² + 8x³ + x⁴`.

## 4.3 Finding a single term / coefficient
The term in `bʳ` is `nCr · a^{n−r} · bʳ`. You usually don't expand everything — just pick the term you need.
**Example:** coefficient of `x³` in `(1 + 2x)⁵` is `5C3 · 1² · (2x)³ = 10 · 8x³ = 80x³`, so the coefficient is `80`.

**Example (with a coefficient inside):** term in `x²` of `(3 − x)⁶` is `6C2 · 3⁴ · (−x)² = 15 · 81 · x² = 1215x²`.

**Pitfalls:** include the powers of the numerical part (`2ˣ`, `3ˣ`) — a very common slip; track the sign when the bracket has a minus; `r` counts from 0, so the term in `xʳ` is the `(r+1)`th term.

---
---

# Chapter 5 — Sequences and Series

## 5.1 Arithmetic sequences (common difference `d`)
- `n`th term: `uₙ = a + (n − 1)d`
- Sum of `n` terms: `Sₙ = n/2·[2a + (n − 1)d] = n/2·(a + l)`, where `l` is the last term.
**Example:** `a = 3, d = 5`. 10th term `= 3 + 9(5) = 48`. `S₁₀ = 10/2·(2·3 + 9·5) = 5(51) = 255`.

## 5.2 Geometric sequences (common ratio `r`)
- `n`th term: `uₙ = a·r^{n−1}`
- Sum of `n` terms: `Sₙ = a(1 − rⁿ)/(1 − r)`
- **Sum to infinity** (only if `|r| < 1`): `S∞ = a/(1 − r)`
**Example:** `a = 2, r = 3`. 5th term `= 2·3⁴ = 162`. `S₅ = 2(3⁵ − 1)/(3 − 1) = 2(242)/2 = 242`.
**Example (sum to infinity):** `a = 8, r = ½ ⇒ S∞ = 8/(1 − ½) = 16`.

## 5.3 Sigma notation
`Σ_{r=1}^{n} uᵣ` means add the terms. Recognise whether it's arithmetic or geometric, then use the right sum formula.

**Pitfalls:** mixing the AP and GP formulas; sum-to-infinity only exists for `|r|<1`; `n`th-term uses `n−1`, not `n`; read off `a` (first term) and `d` or `r` carefully.

---
---

# Chapter 6 — Radian Measure

## 6.1 Radians
`π radians = 180°`. To convert: degrees → radians ×`π/180`; radians → degrees ×`180/π`. Common: `30°=π/6`, `45°=π/4`, `60°=π/3`, `90°=π/2`.

## 6.2 Arc length and sector area (θ in radians)
- Arc length: `s = rθ`
- Sector area: `A = ½ r²θ`
**Example:** `r = 6, θ = 1.2`: arc `= 6(1.2) = 7.2`; sector area `= ½(36)(1.2) = 21.6`.

## 6.3 Area of a segment
Segment = sector − triangle: `A = ½ r²θ − ½ r² sin θ = ½ r²(θ − sin θ)`.

**Pitfalls:** `s = rθ` and `A = ½r²θ` **only work in radians** — convert first; set your calculator to radian mode for these; don't confuse arc length with chord length.

---
---

# Chapter 7 — Differentiation: Applications & Optimisation

## 7.1 Recap of the tools
`dy/dx` is the gradient; `d²y/dx²` is its rate of change. Stationary points where `dy/dx = 0`; classify with `d²y/dx²` (`>0` min, `<0` max).

## 7.2 Increasing / decreasing
`f'(x) > 0` increasing; `f'(x) < 0` decreasing. State intervals by solving the inequality.

## 7.3 Optimisation (the main P2 skill)
Real problems: maximise area/volume or minimise cost/material. Standard recipe:
1. Write the quantity to optimise as a formula (often two variables).
2. Use the **constraint** to eliminate one variable, leaving a function of one variable.
3. Differentiate, set `= 0`, solve.
4. **Justify** it's a max/min (second derivative), and answer the actual question (often the value, not just the `x`).

**Worked example:** A rectangular pen uses a wall for one side; `40 m` of fencing makes the other three sides. Maximise the area.
Let width `x`, length `y`. Constraint: `2x + y = 40 ⇒ y = 40 − 2x`.
Area `A = xy = x(40 − 2x) = 40x − 2x²`.
`dA/dx = 40 − 4x = 0 ⇒ x = 10`, so `y = 20`. `d²A/dx² = −4 < 0` ⇒ maximum.
**Maximum area `= 10 × 20 = 200 m²`.**

**Pitfalls:** forgetting to use the constraint (you must reduce to one variable); not justifying max vs min; answering with `x` when the question wants the area/volume; including the right domain (lengths must be positive).

---
---

# Chapter 8 — Integration: Area & the Trapezium Rule

## 8.1 Definite integrals and area
`∫_a^b y dx = F(b) − F(a)`. For a curve above the x-axis this is the area beneath it. Below the axis the integral is negative — split at roots and take magnitudes.
**Example:** `∫₁³ (2x) dx = [x²]₁³ = 9 − 1 = 8`.

## 8.2 Area between a curve and a line
Find intersection points, then `∫ (top − bottom) dx` between them.
**Example:** area enclosed by `y = x²` and `y = x + 2`. Intersect: `x² = x + 2 ⇒ x = −1, 2`. Area `= ∫₋₁² [(x+2) − x²] dx = [x²/2 + 2x − x³/3]₋₁²`.
At `2`: `2 + 4 − 8/3 = 6 − 8/3 = 10/3`. At `−1`: `½ − 2 + 1/3 = −7/6`. Area `= 10/3 − (−7/6) = 20/6 + 7/6 = 27/6 = 4.5`.

## 8.3 The trapezium rule (numerical estimate)
When you can't integrate exactly, estimate with strips of equal width `h = (b−a)/n`:
`∫_a^b y dx ≈ (h/2)·[ y₀ + yₙ + 2(y₁ + y₂ + … + y_{n−1}) ]`.
**Example:** estimate `∫₁⁴ (1/x) dx` with 3 strips (`h = 1`). Ordinates at `x = 1,2,3,4`: `y = 1, 0.5, 0.3333, 0.25`.
`≈ (1/2)[1 + 0.25 + 2(0.5 + 0.3333)] = 0.5[1.25 + 1.6667] = 1.46` (3 s.f.). (Exact `ln4 ≈ 1.386`.)
The rule **overestimates** for a curve that bends upward (convex), and underestimates for concave.

**Pitfalls:** the first and last ordinates are **not** doubled; `h = (b−a)/n` where `n` = number of strips = (number of ordinates − 1); for "area between", integrate top minus bottom over the correct limits; watch negative areas below the axis.

---

*End of P2 notes. With P1 + P2 mastered, your maths will sit well above IGCSE level — exactly the signal you want for Harrow.*

