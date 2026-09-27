# Chapitre 1 — Logique mathématique (Notion de logique)

## 1. Proposition logique (proposition)

Une **proposition** est un énoncé qui a une valeur de vérité unique : soit **vraie (V)**, soit **fausse (F)**, jamais les deux, jamais aucune des deux.

Exemple : "Rabat est la capitale du Maroc" → proposition, vraie.
Contre-exemple : "Les mathématiques sont difficiles" → pas une proposition (opinion, pas de valeur de vérité fixe).

## 2. Connecteurs logiques (logical connectives)

On note P, Q des propositions.

### Négation (negation) — non P (¬P)

| P | non P |
|---|---|
| V | F |
| F | V |

### Conjonction (conjunction) — P et Q (P ∧ Q)

Vraie seulement si **les deux** sont vraies.

| P | Q | P et Q |
|---|---|---|
| V | V | V |
| V | F | F |
| F | V | F |
| F | F | F |

### Disjonction (disjunction) — P ou Q (P ∨ Q)

Vraie dès que **au moins une** est vraie (ou inclusif, pas "soit... soit").

| P | Q | P ou Q |
|---|---|---|
| V | V | V |
| V | F | V |
| F | V | V |
| F | F | F |

### Implication — P ⟹ Q ("P implique Q", "si P alors Q")

Piège classique : **fausse uniquement quand P est vraie et Q est fausse**. Dans tous les autres cas, elle est vraie — même si P est fausse ("le faux implique n'importe quoi").

| P | Q | P ⟹ Q |
|---|---|---|
| V | V | V |
| V | F | F |
| F | V | V |
| F | F | V |

Vocabulaire lié à P ⟹ Q :
- **Réciproque** (converse) : Q ⟹ P
- **Contraposée** (contrapositive) : non Q ⟹ non P — **équivalente** à P ⟹ Q (même valeur de vérité, toujours)
- La réciproque n'est PAS équivalente à l'implication de départ, en général.

### Équivalence — P ⟺ Q ("P équivaut à Q", "P si et seulement si Q")

Vraie quand P et Q ont **la même** valeur de vérité.

| P | Q | P ⟺ Q |
|---|---|---|
| V | V | V |
| V | F | F |
| F | V | F |
| F | F | V |

P ⟺ Q est vraie exactement quand (P ⟹ Q) ET (Q ⟹ P) sont vraies toutes les deux.

## 3. Lois de De Morgan (De Morgan's laws)

- non (P et Q) ⟺ (non P) ou (non Q)
- non (P ou Q) ⟺ (non P) et (non Q)
- non (P ⟹ Q) ⟺ P et (non Q)

Comment le retenir : nier un "et" donne un "ou" (et inversement), et on nie chaque proposition individuellement.

## 4. Quantificateurs (quantifiers)

- **∀** : "quel que soit" / "pour tout" (for all)
- **∃** : "il existe" (there exists) — au moins un
- **∃!** : "il existe un unique" (there exists exactly one)

Exemple : ∀x ∈ ℝ, x² ≥ 0 (pour tout réel x, x² est positif ou nul) — vraie.
Exemple : ∃x ∈ ℝ, x² = 4 (il existe un réel x tel que x² = 4) — vraie (x = 2 ou x = -2).

### Négation des propositions quantifiées

- non (∀x, P(x)) ⟺ ∃x, non P(x)
- non (∃x, P(x)) ⟺ ∀x, non P(x)

Règle : nier un ∀ donne un ∃ (et inversement), et on nie la proposition à l'intérieur.

Attention à l'ordre des quantificateurs : ∀x ∃y ... n'est PAS la même chose que ∃y ∀x ... (l'ordre change le sens).

## 5. Types de raisonnement (methods of proof)

- **Raisonnement direct** : on part de P vraie et on déduit Q par une chaîne d'implications.
- **Raisonnement par contraposée** : pour prouver P ⟹ Q, on prouve non Q ⟹ non P (équivalent, parfois plus facile).
- **Raisonnement par l'absurde** (proof by contradiction) : pour prouver P, on suppose non P et on aboutit à une contradiction.
- **Raisonnement par contre-exemple** (counterexample) : pour montrer qu'une proposition ∀x, P(x) est fausse, il suffit de trouver **un seul** x tel que P(x) est fausse.
- **Raisonnement par disjonction des cas** (case analysis) : on découpe en plusieurs cas qui couvrent toutes les possibilités, et on traite chaque cas séparément.
- **Raisonnement par récurrence** (induction) : pour prouver P(n) vraie pour tout n ≥ n₀ : (1) initialisation — P(n₀) vraie, (2) hérédité — si P(n) vraie alors P(n+1) vraie, (3) conclusion — P(n) vraie pour tout n ≥ n₀. (Vu en détail au chapitre suites numériques.)

---

# Exercices — à faire seul, puis on corrige ensemble

**1.** Parmi ces énoncés, lesquels sont des propositions ? Justifie.
a) "7 est un nombre premier"
b) "Cette ville est belle"
c) "x + 2 = 5"
d) "Il existe un réel x tel que x + 2 = 5"

**2.** Construis la table de vérité de (P et Q) ou (non P).

**3.** P = "il fait beau", Q = "je sors". Écris en français : non P, P ⟹ Q, la contraposée de P ⟹ Q, la réciproque de P ⟹ Q.

**4.** Sans table de vérité, utilise les lois de De Morgan pour simplifier : non ((non P) et Q).

**5.** Écris la négation de : ∀x ∈ ℝ, ∃y ∈ ℝ, x + y = 0.

**6.** Est-ce que P ⟹ Q et sa réciproque Q ⟹ P sont toujours équivalentes ? Donne un exemple concret (P, Q) qui le prouve ou le réfute.

**7.** Montre par contre-exemple que la proposition suivante est fausse : ∀x ∈ ℝ, x² > x.

**8.** Un exercice de raisonnement par l'absurde classique : montre que √2 n'est pas un nombre rationnel. (Indice : suppose que √2 = p/q avec p/q une fraction irréductible, et cherche la contradiction.)
