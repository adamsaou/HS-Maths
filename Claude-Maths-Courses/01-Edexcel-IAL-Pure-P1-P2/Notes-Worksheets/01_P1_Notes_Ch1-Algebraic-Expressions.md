# P1 · Chapter 1 — Algebraic Expressions

This is the bedrock. Almost every later topic assumes you can do this without conscious effort. The aim of this chapter is *fluency*, not just understanding.

---

## 1.1 Index laws (laws of exponents)

For any non-zero `a`, `b` and any powers `m`, `n`:

| Law | Rule | Example |
|-----|------|---------|
| Multiply | `a^m × a^n = a^(m+n)` | `x^3 × x^4 = x^7` |
| Divide | `a^m ÷ a^n = a^(m−n)` | `x^5 ÷ x^2 = x^3` |
| Power of a power | `(a^m)^n = a^(mn)` | `(x^2)^4 = x^8` |
| Power of a product | `(ab)^n = a^n b^n` | `(2x)^3 = 8x^3` |
| Zero power | `a^0 = 1` | `7^0 = 1` |
| Negative power | `a^(−n) = 1 / a^n` | `x^(−2) = 1/x^2` |
| Fractional power | `a^(1/n) = ⁿ√a` and `a^(m/n) = (ⁿ√a)^m` | `8^(2/3) = (³√8)^2 = 2^2 = 4` |

**The #1 beginner error:** these laws apply to *multiplication/division of the same base*, **never** to addition. `x^2 + x^3` does **not** simplify. And `(a+b)^2 ≠ a^2 + b^2`.

### Worked example 1 — simplify `(2x^2)^3 × x^4`
```
(2x^2)^3 = 2^3 × (x^2)^3 = 8x^6        [power of a product]
8x^6 × x^4 = 8x^(6+4) = 8x^10          [multiply, add powers]
```
**Answer:** `8x^10`

### Worked example 2 — evaluate `16^(−3/4)`
```
16^(−3/4) = 1 / 16^(3/4)               [negative power → reciprocal]
16^(3/4) = (⁴√16)^3 = 2^3 = 8          [fractional power: root first, then power]
So 16^(−3/4) = 1/8
```
**Answer:** `1/8`

**Strategy for fractional powers:** always do the *root first* (smaller numbers), then the power.

---

## 1.2 Expanding brackets

- Single bracket: multiply every term inside by the term outside.
- Two brackets: every term in the first × every term in the second (FOIL is just this for two-by-two).
- Always **collect like terms** at the end.

### Worked example 3 — expand and simplify `(2x − 3)(x + 5)`
```
2x·x + 2x·5 − 3·x − 3·5
= 2x^2 + 10x − 3x − 15
= 2x^2 + 7x − 15
```
**Answer:** `2x^2 + 7x − 15`

### Worked example 4 — expand `(x + 4)^2`
A square is two identical brackets. **Never** write `x^2 + 16`.
```
(x + 4)^2 = (x + 4)(x + 4) = x^2 + 4x + 4x + 16 = x^2 + 8x + 16
```
**Pattern to memorise:** `(a + b)^2 = a^2 + 2ab + b^2` and `(a − b)^2 = a^2 − 2ab + b^2`.

---

## 1.3 Factorising

Factorising is expanding in reverse — turning a sum into a product. Four tools:

1. **Common factor:** `6x^2 + 9x = 3x(2x + 3)`
2. **Quadratic trinomial** `x^2 + bx + c`: find two numbers that *multiply to c* and *add to b*.
   - `x^2 + 7x + 12 → (x + 3)(x + 4)` (3×4=12, 3+4=7)
3. **Difference of two squares:** `a^2 − b^2 = (a − b)(a + b)`
   - `x^2 − 25 = (x − 5)(x + 5)`
4. **Harder quadratics** `ax^2 + bx + c` (a ≠ 1): use the "split the middle term" method below.

### Worked example 5 — factorise `3x^2 + 10x + 8`
```
Multiply a×c = 3×8 = 24. Find two numbers multiplying to 24, adding to 10 → 6 and 4.
Split the middle term:   3x^2 + 6x + 4x + 8
Group:                   3x(x + 2) + 4(x + 2)
Common bracket:          (3x + 4)(x + 2)
```
**Answer:** `(3x + 4)(x + 2)`. Check by expanding: `3x^2 + 6x + 4x + 8 = 3x^2 + 10x + 8`. ✓

**Always verify a factorisation by expanding it back.** Costs 10 seconds, kills careless errors.

---

## 1.4 Surds

A **surd** is an irrational root left in exact form, like `√2`, `√3`, `2√5`. Exam answers are usually required in exact surd form, not as decimals.

**Rules:**
- `√(ab) = √a × √b`  → so `√12 = √(4×3) = √4 × √3 = 2√3`
- `√(a/b) = √a / √b`
- You can only add/subtract *like* surds: `3√2 + 5√2 = 8√2`, but `√2 + √3` does not simplify.

### Worked example 6 — simplify `√50 + √8`
```
√50 = √(25×2) = 5√2
√8  = √(4×2)  = 2√2
5√2 + 2√2 = 7√2
```
**Answer:** `7√2`

---

## 1.5 Rationalising the denominator

We don't leave surds in the denominator. Two cases:

**Case A — single surd:** multiply top and bottom by that surd.
```
5/√3 = (5 × √3)/(√3 × √3) = 5√3/3
```

**Case B — denominator like `a + √b`:** multiply by its **conjugate** `a − √b`. This uses difference of two squares to clear the surd.

### Worked example 7 — rationalise `6 / (4 − √2)`
```
Multiply top and bottom by the conjugate (4 + √2):

  6(4 + √2) / [(4 − √2)(4 + √2)]

Denominator: (4)^2 − (√2)^2 = 16 − 2 = 14
Numerator:   6(4 + √2) = 24 + 6√2

= (24 + 6√2)/14 = (12 + 3√2)/7      [divide top and bottom by 2]
```
**Answer:** `(12 + 3√2)/7`

---

## Chapter 1 — common pitfalls checklist

- ✗ `x^2 · x^3 = x^6` — **NO**, it's `x^5` (add powers, don't multiply them).
- ✗ `(x+3)^2 = x^2 + 9` — **NO**, it's `x^2 + 6x + 9`.
- ✗ `√(a+b) = √a + √b` — **NO**, never. `√(9+16) = 5`, not `3+4=7`.
- ✗ Forgetting to simplify the surd fraction at the end (divide out common factors).
- ✗ For `a^(m/n)`, doing the power before the root (legal, but the numbers get huge — root first).

> **Next:** do the Chapter 1 practice set, then move to Chapter 2 (Quadratics).
