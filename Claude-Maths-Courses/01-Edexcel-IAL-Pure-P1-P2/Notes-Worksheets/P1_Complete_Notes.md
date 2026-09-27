# Pure Mathematics 1 — Complete Notes

Edexcel International A-Level. Nine chapters, each with key ideas, methods, worked examples, and a pitfalls checklist. Pair each chapter with the matching worksheet in **P1_Worksheets.md**.

**Contents**
1. Algebraic expressions
2. Quadratics
3. Equations and inequalities
4. Graphs and transformations
5. Straight-line graphs (coordinate geometry)
6. Trigonometric ratios
7. Trigonometric identities and equations
8. Differentiation
9. Integration

---
---

# Chapter 1 — Algebraic Expressions

## 1.1 Index laws
`a^m·a^n = a^(m+n)` · `a^m/a^n = a^(m−n)` · `(a^m)^n = a^(mn)` · `(ab)^n = a^n b^n` · `a^0 = 1` · `a^(−n) = 1/a^n` · `a^(1/n) = ⁿ√a` · `a^(m/n) = (ⁿ√a)^m`.
Laws apply to the **same base** under × and ÷ only — never to addition. `(a+b)^2 ≠ a^2+b^2`.

**Example:** `(2x^2)^3 × x^4 = 8x^6 × x^4 = 8x^10`.
**Example:** `16^(−3/4) = 1/16^(3/4) = 1/(⁴√16)^3 = 1/2^3 = 1/8`. (Root first, then power.)

## 1.2 Expanding brackets
Every term × every term, then collect. Memorise `(a+b)^2 = a^2+2ab+b^2`, `(a−b)^2 = a^2−2ab+b^2`, `(a+b)(a−b)=a^2−b^2`.
**Example:** `(2x−3)(x+5) = 2x^2+10x−3x−15 = 2x^2+7x−15`.

## 1.3 Factorising
Tools: common factor; trinomial (numbers multiplying to `c`, adding to `b`); difference of squares; split-the-middle for `ax^2+bx+c`.
**Example:** `3x^2+10x+8`: `a·c=24`, split 6+4 → `3x^2+6x+4x+8 = 3x(x+2)+4(x+2) = (3x+4)(x+2)`. Always check by expanding.

## 1.4 Surds
`√(ab)=√a·√b`, `√(a/b)=√a/√b`. Only like surds add. `√50+√8 = 5√2+2√2 = 7√2`.

## 1.5 Rationalising
Single surd: multiply by it (`5/√3 = 5√3/3`). Form `a±√b`: multiply by conjugate `a∓√b`.
**Example:** `6/(4−√2) = 6(4+√2)/((16−2)) = (24+6√2)/14 = (12+3√2)/7`.

**Pitfalls:** `x^2·x^3=x^5` not `x^6`; `(x+3)^2 = x^2+6x+9`; `√(a+b)≠√a+√b`; simplify surd fractions fully; root before power on fractional indices.

---
---

# Chapter 2 — Quadratics

## 2.1 Solving by factorising
Set each factor to 0. `6x^2−x−2=0 → (2x+1)(3x−2)=0 → x=−1/2, 2/3`.

## 2.2 Completing the square
`x^2+bx+c = (x+b/2)^2 − (b/2)^2 + c`. For `a≠1`, factor `a` out of the x-terms first.
**Example:** `2x^2−12x+7 = 2(x^2−6x)+7 = 2[(x−3)^2−9]+7 = 2(x−3)^2−11`. Vertex `(3,−11)`.
From `a(x−h)^2+k` the vertex is `(h,k)` (min if a>0, max if a<0).

## 2.3 Quadratic formula
`x = [−b ± √(b^2−4ac)]/(2a)`. Write a, b, c with signs first.
**Example:** `3x^2−7x+1=0 → x=(7±√37)/6`.

## 2.4 The discriminant `Δ = b^2−4ac`
`Δ>0`: two real roots; `Δ=0`: one repeated root (graph touches); `Δ<0`: no real roots.
**Example:** `x^2+kx+9=0` equal roots ⇒ `k^2−36=0 ⇒ k=±6`.
**Example:** `2x^2+kx+8=0` no real roots ⇒ `k^2−64<0 ⇒ −8<k<8`.

## 2.5 Quadratic graphs
`a>0` U-shape (min), `a<0` ∩-shape (max). y-intercept `(0,c)`; roots from `y=0`; vertex & axis of symmetry from completed square.
**Example:** `y=x^2−4x−5`: roots `−1, 5`; y-int `(0,−5)`; vertex `(2,−9)`.

## 2.6 Disguised quadratics
Substitute `u` for the repeated chunk. `x^4−5x^2+4=0`, `u=x^2 ⇒ (u−1)(u−4)=0 ⇒ x=±1,±2`. Remember to back-substitute.

**Pitfalls:** lose a `±`/second root; discriminant sign slips; with `a≠1`, multiply the `−(b/2)^2` back by `a`; vertex sign of `h`; back-substitute disguised quadratics.

---
---

# Chapter 3 — Equations and Inequalities

## 3.1 Simultaneous equations (linear)
**Elimination** or **substitution**. 
**Example (elimination):** `3x+2y=7`, `5x−2y=1`. Add: `8x=8 ⇒ x=1`, then `y=2`.

## 3.2 Linear–quadratic simultaneous equations
Always **substitute** the linear into the quadratic, giving one quadratic to solve. Each x gives a matching y. Geometrically these are intersection points of a line and a curve.
**Example:** `y=x+1` and `x^2+y^2=25`. Sub: `x^2+(x+1)^2=25 ⇒ 2x^2+2x−24=0 ⇒ x^2+x−12=0 ⇒ (x+4)(x−3)=0`. So `x=−4,y=−3` and `x=3,y=4`. Points `(−4,−3)`, `(3,4)`.
If the resulting quadratic has `Δ<0`, the line misses the curve; `Δ=0` means it's a tangent.

## 3.3 Linear inequalities
Solve like equations, but **flip the sign when multiplying/dividing by a negative**.
**Example:** `5−2x < 11 ⇒ −2x < 6 ⇒ x > −3`.

## 3.4 Quadratic inequalities
Method: (1) make one side 0, (2) find the critical values (roots), (3) sketch the parabola, (4) read off where it's above/below the axis.
**Example:** `x^2−x−6 > 0`. Roots: `(x−3)(x+2)=0 ⇒ x=3,−2`. U-shape is **above** the axis outside the roots: `x<−2` or `x>3`.
**Example:** `x^2−x−6 ≤ 0` is **between** the roots: `−2 ≤ x ≤ 3`.
Rule of thumb for `a>0`: `>0` → "outside" the roots; `<0` → "between" the roots.

## 3.5 Inequalities on graphs / regions
A region like `y < f(x)` is below the curve; `y > f(x)` above. Dashed line for strict `<,>`; solid for `≤,≥`. Shade the set satisfying all conditions.

**Pitfalls:** forgetting to flip the inequality on ÷ by negative; giving a single interval when the answer is two (`x<−2 or x>3`); using "and" vs "or" wrongly; for line–curve problems, find **both** coordinates.

---
---

# Chapter 4 — Graphs and Transformations

## 4.1 Standard curve shapes
- **Cubic** `y=ax^3+...`: if `a>0` rises left-to-right (bottom-left to top-right) with up to two turning points.
- **Quartic** `y=ax^4+...`: if `a>0`, both ends up (W or U-ish).
- **Reciprocal** `y=k/x`: two branches, asymptotes the x- and y-axes.
- **`y=k/x^2`**: both branches above the x-axis (if k>0).
To sketch a factorised polynomial, find where it crosses the x-axis (each factor = 0) and the y-intercept, then join with the right end-behaviour. A **repeated factor** `(x−a)^2` means the curve *touches* at `x=a`; `(x−a)^3` gives a point of inflection on the axis.
**Example:** `y=(x+1)(x−2)(x−3)` crosses at `−1, 2, 3`; y-intercept `(0, 6)`; positive cubic shape.

## 4.2 Intersection of graphs
Number of intersections of `y=f(x)` and `y=g(x)` = number of solutions of `f(x)=g(x)`.

## 4.3 Transformations of `y=f(x)`
| Transformation | Effect | Direction |
|---|---|---|
| `f(x)+a` | up `a` | vertical, "expected" |
| `f(x+a)` | left `a` | horizontal, **opposite** to sign |
| `f(x−a)` | right `a` | horizontal, opposite |
| `af(x)` | vertical stretch, factor `a` | y-values ×a |
| `f(ax)` | horizontal stretch, factor `1/a` | x-values ÷a |
| `−f(x)` | reflect in the **x-axis** | |
| `f(−x)` | reflect in the **y-axis** | |

**Key intuition:** changes *outside* `f` act on `y` and behave as expected; changes *inside* `f` act on `x` and behave the **opposite** way.
**Example:** `y=x^2` → `y=(x−3)^2+2` is a shift right 3, up 2; vertex moves `(0,0)→(3,2)`.

**Pitfalls:** `f(x+2)` moves **left** (not right); `f(2x)` **compresses** horizontally (factor ½), it doesn't stretch; apply transformations to key points (intercepts, turning points) to re-sketch reliably.

---
---

# Chapter 5 — Straight-Line Graphs (Coordinate Geometry)

## 5.1 Equation forms
- `y = mx + c`: gradient `m`, y-intercept `c`.
- `y − y₁ = m(x − x₁)`: line through `(x₁,y₁)` with gradient `m` — the workhorse form.
- `ax + by + c = 0`: general form (often required for final answers; clear fractions).

## 5.2 Gradient, midpoint, distance
For points `A(x₁,y₁)`, `B(x₂,y₂)`:
- Gradient `m = (y₂−y₁)/(x₂−x₁)`
- Midpoint `= ((x₁+x₂)/2, (y₁+y₂)/2)`
- Distance `AB = √[(x₂−x₁)² + (y₂−y₁)²]`

## 5.3 Parallel and perpendicular
- Parallel ⇒ **equal** gradients.
- Perpendicular ⇒ gradients multiply to **−1** (i.e. `m₂ = −1/m₁`, negative reciprocal).
**Example:** Line through `(2,5)` perpendicular to `y=3x−1`. New gradient `−1/3`: `y−5 = −⅓(x−2) ⇒ x+3y−17=0`.

## 5.4 Modelling
Real contexts: gradient = rate of change, intercept = starting value. Be able to interpret both.

**Pitfalls:** sign errors in the gradient formula (keep the order consistent top and bottom); perpendicular gradient is the **negative reciprocal**, not just the reciprocal; when asked for `ax+by+c=0`, eliminate fractions and set `=0`.

---
---

# Chapter 6 — Trigonometric Ratios

## 6.1 Right-angled triangles (SOH-CAH-TOA)
`sin θ = opp/hyp`, `cos θ = adj/hyp`, `tan θ = opp/adj`.

## 6.2 Sine rule (non-right triangles)
`a/sin A = b/sin B = c/sin C`. Use when you have a side and its opposite angle. Watch the **ambiguous case** (two possible angles when finding an angle from a sine).

## 6.3 Cosine rule
`a² = b² + c² − 2bc·cos A`. Use for SAS (two sides + included angle) or SSS (three sides → find an angle: `cos A = (b²+c²−a²)/(2bc)`).

## 6.4 Area of a triangle
`Area = ½ ab·sin C` (two sides and the included angle).
**Example:** sides 7 and 9 with included angle 40° → `½·7·9·sin40° ≈ 20.2`.

## 6.5 Graphs of sin, cos, tan
- `y=sin x`: wave from `(0,0)`, range `[−1,1]`, period 360°.
- `y=cos x`: wave from `(0,1)`, range `[−1,1]`, period 360°.
- `y=tan x`: period 180°, asymptotes at `90°, 270°, …`.
Know the **exact values** at `0, 30, 45, 60, 90°`: e.g. `sin30=½`, `cos30=√3/2`, `tan45=1`, `sin60=√3/2`.

**Pitfalls:** calculator in the wrong mode (degrees vs radians); choosing sine rule when no side–opposite-angle pair exists (use cosine rule); forgetting the ambiguous-case second angle; mixing up which sides are "included".

---
---

# Chapter 7 — Trigonometric Identities and Equations

## 7.1 The two key identities
1. `sin²θ + cos²θ = 1`
2. `tan θ = sin θ / cos θ`
Rearrangements you'll use constantly: `sin²θ = 1 − cos²θ` and `cos²θ = 1 − sin²θ`.

## 7.2 Proving identities
Work on **one side only** until it equals the other. Typical move: replace `tan` with `sin/cos`, or `sin²` with `1−cos²`, then simplify.
**Example:** show `(1−cos²θ)/cosθ = sinθ·tanθ`. LHS `= sin²θ/cosθ = sinθ·(sinθ/cosθ) = sinθ·tanθ`. ∎

## 7.3 Solving trig equations in a given interval
Steps: (1) get `sin/cos/tan (something) = value`; (2) take the inverse for the **principal value**; (3) use symmetry/period to get **all** solutions in the stated range.
- `sin`: second solution `180° − θ` (then add/subtract 360° as needed).
- `cos`: second solution `360° − θ` (i.e. `±θ`).
- `tan`: solutions repeat every `180°`.

**Example:** solve `sin x = 0.5`, `0 ≤ x < 360°`. Principal `30°`; sine also positive at `180−30 = 150°`. → `x = 30°, 150°`.

## 7.4 Quadratic trig equations
Substitute a single ratio. **Example:** `2sin²x + sin x − 1 = 0`, `0 ≤ x < 360°`. Let `s=sin x`: `(2s−1)(s+1)=0 ⇒ s=½ or s=−1`. `sin x=½ ⇒ x=30°,150°`; `sin x=−1 ⇒ x=270°`. → `x=30°,150°,270°`.

If the equation mixes `sin²` and `cos`, use `sin²x = 1−cos²x` to make it all in one ratio first.

**Pitfalls:** giving only the principal value (missing the symmetric solution); wrong symmetry rule (sin vs cos); not converting `sin²` to `cos` when the equation also has `cos`; dropping solutions when the interval is large.

---
---

# Chapter 8 — Differentiation

## 8.1 The idea
The derivative `f'(x)` (also `dy/dx`) is the **gradient function** — it gives the slope of the curve at any `x`.

## 8.2 From first principles (must be able to state)
`f'(x) = lim_{h→0} [f(x+h) − f(x)] / h`.
For `f(x)=x²`: `[(x+h)²−x²]/h = (2xh+h²)/h = 2x+h → 2x` as `h→0`. So `f'(x)=2x`.

## 8.3 The power rule (the everyday tool)
`d/dx (x^n) = n·x^(n−1)`, for any `n`. Differentiate term by term; constants differentiate to 0; a constant multiple stays.
**Example:** `y = 3x⁴ − 2x² + 5 ⇒ dy/dx = 12x³ − 4x`.
Works for negative/fractional powers too: rewrite first. `y = 1/x = x⁻¹ ⇒ dy/dx = −x⁻² = −1/x²`. `y=√x = x^{1/2} ⇒ dy/dx = ½x^{−1/2}`.

## 8.4 Tangents and normals
At `x=a`: gradient of tangent `= f'(a)`; gradient of normal `= −1/f'(a)`. Use the point `(a, f(a))` with `y−y₁=m(x−x₁)`.
**Example:** `y=x²` at `x=3`: point `(3,9)`, `f'(3)=6`. Tangent `y−9=6(x−3) ⇒ y=6x−9`. Normal gradient `−1/6`: `y−9=−⅙(x−3)`.

## 8.5 Increasing / decreasing
`f'(x)>0` ⇒ increasing; `f'(x)<0` ⇒ decreasing. Solve the inequality to find intervals.

## 8.6 Stationary points and their nature
Stationary where `f'(x)=0`. Classify with the **second derivative** `f''(x)`: `f''>0` ⇒ minimum, `f''<0` ⇒ maximum (if `f''=0`, test gradient either side).
**Example:** `y=x³−3x²`. `f'=3x²−6x=3x(x−2)=0 ⇒ x=0,2`. `f''=6x−6`. At `x=0`: `f''=−6<0` → max `(0,0)`. At `x=2`: `f''=6>0` → min `(2,−4)`.

**Pitfalls:** forgetting to rewrite roots/fractions as powers before differentiating; the derivative of a constant is 0 (not the constant); normal gradient is the negative reciprocal; second-derivative test sign convention (positive = minimum).

---
---

# Chapter 9 — Integration

## 9.1 Indefinite integration (reverse of differentiation)
`∫ x^n dx = x^(n+1)/(n+1) + C`, for `n ≠ −1`. **Always add `+ C`.** Integrate term by term.
**Example:** `∫ (3x² − 4x + 1) dx = x³ − 2x² + x + C`. (Check: differentiate to recover the integrand.)

## 9.2 Finding C with a point
If the curve passes through a known point, substitute to find `C`.
**Example:** a curve has `dy/dx = 2x` and passes through `(1, 4)`. Then `y = x² + C`; `4 = 1 + C ⇒ C=3`, so `y = x² + 3`.

## 9.3 Definite integration
`∫_a^b f(x) dx = F(b) − F(a)`, where `F` is any antiderivative (no `+C` needed — it cancels).
**Example:** `∫_1^2 3x² dx = [x³]_1^2 = 8 − 1 = 7`.

## 9.4 Area under a curve
For a curve **above** the x-axis between `x=a` and `x=b`, the area `= ∫_a^b y dx`. If part is **below** the axis the integral is negative there — split at the roots and take the modulus of each piece, then add.
**Example:** area under `y=x²` from 0 to 3 `= [x³/3]_0^3 = 9`.

## 9.5 Area between a curve and a line
Area `= ∫ (top curve − bottom curve) dx` between their intersection points (found by solving them simultaneously).

**Pitfalls:** forgetting `+C` on indefinite integrals; the rule fails for `n=−1` (that case is `ln`, in P2); a negative definite integral means area below the axis — handle signs; for "area between", integrate top minus bottom, and find the limits from the intersections.

---

*End of P1 notes. Work each chapter alongside its worksheet, and log every error.*

