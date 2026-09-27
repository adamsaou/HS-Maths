# 1ère Bac Sciences Mathématiques — Cours complet

Ce document rassemble tous les cours du programme 1BAC SM, chapitre par chapitre, dans l'ordre officiel. Mis à jour au fur et à mesure des séances.

## Sommaire

1. [Logique mathématique](#1-logique-mathématique) — ✅ fait
2. [Ensembles et applications](#2-ensembles-et-applications) — ✅ fait
3. [Généralités sur les fonctions](#3-généralités-sur-les-fonctions) — ✅ fait (résumé, à approfondir en exercices)
4. [Suites numériques](#4-suites-numériques) — ✅ fait (résumé, à approfondir en exercices)
5. [Le barycentre dans le plan](#5-le-barycentre-dans-le-plan) — ✅ fait (résumé, à approfondir en exercices)
6. [Produit scalaire dans le plan](#6-produit-scalaire-dans-le-plan-étude-analytique) — ✅ fait (résumé, à approfondir en exercices)
7. [Calcul trigonométrique](#7-calcul-trigonométrique) — ✅ fait (résumé, à approfondir en exercices)
8. [La rotation dans le plan](#8-la-rotation-dans-le-plan) — ✅ fait (résumé, à approfondir en exercices)
9. [Limite d'une fonction numérique](#9-limite-dune-fonction-numérique) — ✅ fait (résumé, à approfondir en exercices)
10. [Dérivabilité d'une fonction numérique](#10-dérivabilité-dune-fonction-numérique) — ✅ fait (résumé, à approfondir en exercices)
11. [Étude des fonctions numériques](#11-étude-des-fonctions-numériques) — ✅ fait (résumé, à approfondir en exercices)
12. [Dénombrement](#12-dénombrement) — ✅ fait (résumé, à approfondir en exercices)
13. [Arithmétique dans ℤ](#13-arithmétique-dans-ℤ) — ✅ fait (résumé, à approfondir en exercices)
14. [Vecteurs de l'espace](#14-vecteurs-de-lespace) — ✅ fait (résumé, à approfondir en exercices)
15. [Étude analytique de l'espace](#15-étude-analytique-de-lespace) — ✅ fait (résumé, à approfondir en exercices)
16. [Produit scalaire dans l'espace](#16-produit-scalaire-dans-lespace) — ✅ fait (résumé, à approfondir en exercices)
17. [Produit vectoriel dans l'espace](#17-produit-vectoriel-dans-lespace) — ✅ fait (résumé, à approfondir en exercices)

---

## 1. Logique mathématique

### 1.1 Proposition logique (proposition)

Une **proposition** est un énoncé qui a une valeur de vérité unique : soit **vraie (V)**, soit **fausse (F)**, jamais les deux, jamais aucune des deux.

Exemple : "Rabat est la capitale du Maroc" → proposition, vraie.
Contre-exemple : "Les mathématiques sont difficiles" → pas une proposition (opinion, pas de valeur de vérité fixe).

Piège : un énoncé avec une variable **non précisée et non quantifiée** (ex : "x² = 9") n'est pas une proposition — c'est une **expression ouverte**. Il faut soit préciser x, soit le quantifier (∀ ou ∃) pour obtenir une vraie proposition.

### 1.2 Connecteurs logiques (logical connectives)

On note P, Q des propositions.

**Négation (negation) — non P (¬P)**

| P | non P |
|---|---|
| V | F |
| F | V |

**Conjonction (conjunction) — P et Q (P ∧ Q)** — vraie seulement si les deux sont vraies.

| P | Q | P∧Q |
|---|---|---|
| V | V | V |
| V | F | F |
| F | V | F |
| F | F | F |

**Disjonction (disjunction) — P ou Q (P ∨ Q)** — vraie dès qu'au moins une est vraie (ou inclusif).

| P | Q | P∨Q |
|---|---|---|
| V | V | V |
| V | F | V |
| F | V | V |
| F | F | F |

**Implication — P ⟹ Q** ("si P alors Q") — fausse ⟺ P∧¬Q (P vraie et Q fausse).

| P | Q | P ⟹ Q |
|---|---|---|
| V | V | V |
| V | F | F |
| F | V | V |
| F | F | V |

Vocabulaire lié à P ⟹ Q :
- **Réciproque** (converse) : Q ⟹ P
- **Contraposée** (contrapositive) : ¬Q ⟹ ¬P — **équivalente** à P ⟹ Q
- La réciproque n'est PAS équivalente à l'implication de départ, en général.

**Équivalence — P ⟺ Q** ("P si et seulement si Q") — vraie quand P et Q ont la même valeur de vérité.

| P | Q | P ⟺ Q |
|---|---|---|
| V | V | V |
| V | F | F |
| F | V | F |
| F | F | V |

### 1.3 Lois de De Morgan (De Morgan's laws)

- ¬(P∧Q) ⟺ ¬P∨¬Q
- ¬(P∨Q) ⟺ ¬P∧¬Q
- ¬(P⟹Q) ⟺ P∧¬Q

### 1.4 Quantificateurs (quantifiers)

- **∀** : "quel que soit" / "pour tout" (for all)
- **∃** : "il existe" (there exists) — au moins un
- **∃!** : "il existe un unique" (there exists exactly one)

Négation :
- ¬(∀x, P(x)) ⟺ ∃x, ¬P(x)
- ¬(∃x, P(x)) ⟺ ∀x, ¬P(x)

Attention à l'ordre des quantificateurs : ∀x ∃y ... n'est PAS la même chose que ∃y ∀x ...

Piège : pour un "∃", il suffit d'**un seul** exemple qui marche pour que ce soit vrai — toujours vérifier les petits cas (0, 1, 2, nombres négatifs) avant de conclure "faux".

### 1.5 Types de raisonnement (methods of proof)

- **Raisonnement direct** : on part de P vraie et on déduit Q par une chaîne d'implications.
- **Raisonnement par contraposée** : pour prouver P ⟹ Q, on prouve ¬Q ⟹ ¬P.
- **Raisonnement par l'absurde** (proof by contradiction) : on suppose ¬P et on aboutit à une contradiction.
- **Raisonnement par contre-exemple** (counterexample) : pour montrer que ∀x, P(x) est fausse, un seul x où P(x) est fausse suffit.
- **Raisonnement par disjonction des cas** (case analysis) : on découpe en cas qui couvrent toutes les possibilités.
- **Raisonnement par récurrence** (induction) : (1) initialisation, (2) hérédité, (3) conclusion. (Détaillé au chapitre suites numériques.)

### Exemples rédigés (worked examples)

**Absurde** — Montrer qu'il n'existe pas de plus petit réel strictement positif.

Supposons par l'absurde qu'il existe un plus petit réel strictement positif, noté a (donc a > 0, et pour tout réel x > 0, x ≥ a).
Posons b = a/2. Comme a > 0, b > 0 aussi.
Mais b = a/2 < a.
Donc b est un réel strictement positif strictement inférieur à a, ce qui contredit le fait que a soit le plus petit.
Contradiction → l'hypothèse de départ est fausse → il n'existe pas de plus petit réel strictement positif. ∎

Structure à retenir : (1) suppose le contraire de ce qu'on veut prouver, (2) déduis une conséquence logique, (3) trouve une contradiction (avec l'hypothèse ou un fait connu), (4) conclus que l'hypothèse de départ était fausse, donc l'énoncé original est vrai.

**Contre-exemple** — Réfuter : "∀n ∈ ℕ, n² + 1 est premier."

Il suffit de trouver UN n où c'est faux.
n = 4 : 4² + 1 = 17, premier → pas un contre-exemple, on continue.
n = 3 : 3² + 1 = 10 = 2×5, pas premier → contre-exemple trouvé.
Donc l'énoncé est faux, avec n = 3 comme contre-exemple (10 n'est pas premier).

Structure : teste des petites valeurs jusqu'à en trouver une qui casse l'énoncé. Un seul suffit.

**Disjonction des cas** — Montrer que pour tout entier n, 3n² + n est pair.

Cas 1 : n pair, donc n = 2k pour un entier k.
3n² + n = 3(2k)² + 2k = 12k² + 2k = 2(6k² + k), qui est pair.

Cas 2 : n impair, donc n = 2k+1 pour un entier k.
3n² + n = 3(2k+1)² + (2k+1) = 3(4k²+4k+1) + 2k+1 = 12k² + 14k + 4 = 2(6k² + 7k + 2), qui est pair.

Dans les deux cas, 3n² + n est pair. Comme n est soit pair soit impair (jamais les deux, jamais aucun des deux), ces deux cas couvrent toutes les possibilités. ∎

Structure : découpe en cas qui couvrent TOUT (souvent pair/impair), prouve chaque cas séparément avec la même méthode (souvent direct), conclus que ça marche dans tous les cas.

**Contraposée** — Prouver : "Si 3n+1 est pair, alors n est impair."

Contraposée : "Si n est pair, alors 3n+1 est impair."
Preuve (de la contraposée) : Supposons n pair, donc n = 2k.
3n + 1 = 6k + 1 = 2(3k) + 1, qui est de la forme 2m+1, donc impair.
Par contraposée, on conclut : si 3n+1 est pair, alors n est impair. ∎

Structure : quand prouver P⟹Q directement est difficile, prouve ¬Q⟹¬P à la place (équivalent), souvent plus simple à manipuler.

---

## 2. Ensembles et applications

### 2.1 Ensembles (sets) — notions de base

- **Ensemble** : une collection d'objets, appelés **éléments**.
- **Appartenance** : x ∈ E ("x appartient à E") ; x ∉ E ("x n'appartient pas à E").
- **Ensemble vide** : ∅, ne contient aucun élément.
- **Sous-ensemble / partie** (subset) : A ⊂ E signifie que tout élément de A est aussi dans E, c'est-à-dire ∀x, x∈A ⟹ x∈E.
- **Égalité de deux ensembles** : A = B ⟺ (A⊂B ∧ B⊂A). (Technique classique pour prouver une égalité d'ensembles : montrer les deux inclusions séparément.)
- **Ensemble des parties de E**, noté P(E) : l'ensemble de TOUS les sous-ensembles de E (y compris ∅ et E lui-même). Si E a n éléments, P(E) a 2ⁿ éléments.

### 2.2 Opérations sur les ensembles

- **Intersection** (A∩B) : A∩B = {x | x∈A ∧ x∈B}
- **Union** (A∪B) : A∪B = {x | x∈A ∨ x∈B}
- **Ensembles disjoints** : A∩B = ∅ (aucun élément commun)
- **Différence** (A\B) : A\B = {x∈A | x∉B}
- **Complémentaire dans E** (si A⊂E) : noté Cₑ(A) ou Ā, = E\A = {x∈E | x∉A}
- **Produit cartésien** : E×F = {(x,y) | x∈E, y∈F} — ensemble de couples.

### 2.3 Lois de De Morgan pour les ensembles (même logique que le chapitre 1 !)

- Cₑ(A∩B) = Cₑ(A) ∪ Cₑ(B)
- Cₑ(A∪B) = Cₑ(A) ∩ Cₑ(B)
- Cₑ(Cₑ(A)) = A
- Distributivité : A∩(B∪C) = (A∩B)∪(A∩C) ; A∪(B∩C) = (A∪B)∩(A∪C)

Remarque : c'est exactement la même structure que ¬(P∧Q) ⟺ ¬P∨¬Q — juste appliquée aux ensembles au lieu des propositions. x∈Cₑ(A∩B) ⟺ ¬(x∈A ∧ x∈B) ⟺ (x∉A ∨ x∉B) (De Morgan logique) ⟺ x∈Cₑ(A)∪Cₑ(B).

### 2.4 Applications (mappings)

- **Définition** : une application f de E vers F (noté f: E→F) associe à **chaque** élément x de E un **unique** élément de F, noté f(x) (l'image de x). E = ensemble de départ, F = ensemble d'arrivée.
- Piège : pour être une application, CHAQUE élément de E doit avoir une image, et une SEULE. Si un élément n'a pas d'image, ou en a plusieurs, ce n'est pas une application.

- **Image directe d'une partie** A⊂E : f(A) = {f(x) | x∈A} ⊂ F.
- **Image réciproque d'une partie** B⊂F : f⁻¹(B) = {x∈E | f(x)∈B} ⊂ E.
  Piège important : f⁻¹(B) (image réciproque d'un ensemble) est **toujours définie**, pour n'importe quelle application — ce n'est PAS la même chose que "la fonction réciproque f⁻¹", qui elle n'existe que si f est bijective. Ne confonds pas les deux usages de f⁻¹.

- **Injectivité** : f est injective ⟺ ∀x₁,x₂∈E, f(x₁)=f(x₂) ⟹ x₁=x₂. (Éléments distincts ⟹ images distinctes.) Technique de preuve : supposer f(x₁)=f(x₂), en déduire x₁=x₂.

- **Surjectivité** : f est surjective ⟺ ∀y∈F, ∃x∈E, y=f(x). (Tout élément de F a au moins un antécédent dans E.)

- **Bijectivité** : f est bijective ⟺ (f injective) ∧ (f surjective). (Tout élément de F a EXACTEMENT un antécédent.) Si f est bijective, elle admet une application réciproque f⁻¹: F→E.

- **Composition** : si f:E→F et g:F→G, alors g∘f: E→G est définie par (g∘f)(x) = g(f(x)).

Piège classique : injective et surjective sont deux propriétés indépendantes — l'une n'implique pas l'autre en général. Une fonction peut être injective sans être surjective (et inversement).

---

## 3. Généralités sur les fonctions
*(à venir)*

## 3. Généralités sur les fonctions

### 3.1 Ensemble de définition (Df)

Une fonction f associe à chaque x un unique réel f(x). Df = l'ensemble des x pour lesquels f(x) existe (exclure ce qui annule un dénominateur, ce qui rend un radical négatif, etc.).

Exemple : f(x) = √(x-2)/(x+1). Il faut x-2≥0 ∧ x+1≠0 → x≥2 ∧ x≠-1. Comme -1∉[2,+∞[, Df = [2,+∞[.

### 3.2 Égalité de deux fonctions

f = g ⟺ (Df=Dg) ∧ (∀x∈Df, f(x)=g(x)).

### 3.3 Parité

f paire ⟺ (Df symétrique par rapport à 0) ∧ (∀x∈Df, f(-x)=f(x)) → courbe symétrique par rapport à l'axe (Oy).
f impaire ⟺ (Df symétrique) ∧ (∀x∈Df, f(-x)=-f(x)) → symétrique par rapport à O.

Piège : il FAUT vérifier que Df est symétrique par rapport à 0 en premier — si ce n'est pas le cas, la fonction n'est ni paire ni impaire, inutile de tester la formule.

### 3.4 Monotonie

f croissante sur I ⟺ ∀x1,x2∈I, x1≤x2 ⟹ f(x1)≤f(x2) (inégalité inversée pour décroissante).

Technique de preuve directe : prends x1<x2 dans I, étudie le signe de f(x1)-f(x2), ou le taux d'accroissement τ = (f(x1)-f(x2))/(x1-x2) — τ positif = croissante, négatif = décroissante.

### 3.5 Fonction bornée

Majorée : ∃M, ∀x∈Df, f(x)≤M. Minorée : ∃m, ∀x∈Df, f(x)≥m. Bornée : les deux à la fois.

### 3.6 Composée de fonctions

(g∘f)(x) = g(f(x)). Domaine : x∈Df ∧ f(x)∈Dg.

### 3.7 Fonctions usuelles — tableaux de variation à connaître par cœur

- Constante (x↦c) : ni croissante ni décroissante, tableau plat.
- Affine (x↦ax+b) : croissante si a>0, décroissante si a<0.
- Carrée (x↦x²) : décroissante sur ]-∞,0], croissante sur [0,+∞[.
- Inverse (x↦1/x) : décroissante sur ]-∞,0[ ∧ décroissante sur ]0,+∞[ — séparément. Piège : PAS décroissante sur ℝ* entier (0 n'étant pas dans le domaine, les deux moitiés ne se comparent pas directement).
- Cube (x↦x³) : strictement croissante sur ℝ tout entier, aucun extremum (contrairement à la carrée). Point d'inflexion en 0 (la courbe change de concavité mais reste croissante — piège : le tableau de variation seul ne montre PAS cette différence de forme avec une fonction affine croissante, il faut la courbe pour le voir).
- Racine carrée (x↦√x) : croissante sur [0,+∞[.
- Valeur absolue (x↦|x|) : décroissante sur ℝ⁻, croissante sur ℝ⁺ (forme en V).

**Trinôme du second degré** (f(x)=ax²+bx+c) : plus général que la fonction carrée simple — sommet en x=-b/2a (pas forcément 0), valeur au sommet f(-b/2a). Si a>0 : décroissante puis croissante, minimum au sommet. Si a<0 : croissante puis décroissante, maximum au sommet.

Tableaux de variation dessinés proprement (PDF, 10 fonctions) : voir Tableaux_de_variations.pdf.

Non inclus ici, à venir au chapitre 11 (étude des fonctions numériques) comme application : fonction homographique ((ax+b)/(cx+d)) — combine domaine de définition et monotonie, pas une fonction usuelle "de base" à ce stade.

## 4. Suites numériques

- **Suite** : fonction de ℕ vers ℝ, notée (uₙ). Génération **explicite** (uₙ=f(n)) ou **récurrente** (uₙ₊₁=f(uₙ), u₀ donné).
- **Suite arithmétique** : uₙ₊₁=uₙ+r (raison r). Terme général : uₙ=u₀+nr. Somme : S = (nombre de termes)×(premier+dernier)/2.
- **Suite géométrique** : uₙ₊₁=q×uₙ (raison q). Terme général : uₙ=u₀×qⁿ. Somme : S=u₀×(1-q^(n+1))/(1-q) si q≠1 (piège : formule invalide si q=1, alors S=(n+1)×u₀).
- **Sens de variation** : signe de uₙ₊₁-uₙ, ou (si termes strictement positifs) comparer uₙ₊₁/uₙ à 1.
- **Suite bornée** : mêmes définitions que pour les fonctions.
- **Raisonnement par récurrence** : outil principal pour les suites (revoir chapitre 1) : initialisation, hérédité, conclusion.
- **Limite d'une suite** (introduction) : convergence vers L, ou divergence vers ±∞ — formalisé au chapitre suivant sur les limites.

## 5. Le barycentre dans le plan

### 5.1 Définition et existence du barycentre

Barycentre de (A,α),(B,β) : point G tel que α×GA→ + β×GB→ = 0→ (vecteur nul).
Existence/unicité : en écrivant GA→ = A-G, l'équation devient (α+β)G=αA+βB, donc G=(αA+βB)/(α+β) — existe et unique ⟺ α+β≠0.
Cas particulier : si α=β, G = milieu de [AB] (isobarycentre).

### 5.2 Propriété vectorielle fondamentale (formule de réduction)

∀M du plan : MG→ = (α×MA→ + β×MB→) / (α+β).

C'est la formule la plus utilisée du chapitre — elle permet de remplacer une combinaison α×MA→+β×MB→ par (α+β)×MG→ dans n'importe quelle expression, ce qui simplifie énormément les calculs vectoriels et les lieux géométriques.

### 5.3 Coordonnées du barycentre

x(G) = (α×x(A) + β×x(B)) / (α+β), et de même y(G) = (α×y(A) + β×y(B)) / (α+β) — se déduit directement de 5.2 en prenant M = origine du repère.

### 5.4 Homogénéité

Multiplier tous les coefficients par un même k≠0 (kα, kβ) donne le même barycentre G.

### 5.5 Associativité (barycentre partiel)

On peut remplacer un sous-groupe de points par leur barycentre partiel (si sa somme de coefficients ≠0) sans changer le barycentre global — utile pour simplifier les problèmes à 3+ points.

### 5.6 Barycentre de n points

G tel que Σ(αᵢ×GAᵢ→) = 0→, existe ⟺ Σαᵢ≠0. Formule de réduction généralisée : MG→ = Σ(αᵢ×MAᵢ→) / Σαᵢ.

### 5.7 Applications classiques

Centre de gravité d'un triangle = isobarycentre des 3 sommets (intersection des médianes, chacune divisée 2:1 depuis le sommet).
Alignement : pour montrer que 3 points sont alignés, exprimer l'un comme barycentre des deux autres.
Lieu géométrique : pour l'ensemble des M tels que ‖α×MA→+β×MB→‖=k (norme), utiliser 5.2 pour obtenir |α+β|×MG=k, soit MG=k/|α+β| — cercle de centre G et rayon k/|α+β| (ou le point G seul si k=0).

## 6. Produit scalaire dans le plan (étude analytique)

### 6.1 Rappel : définitions du produit scalaire

Définition géométrique : u→·v→ = ‖u→‖×‖v→‖×cos(θ), θ = angle entre u→ et v→.
Définition par projection : u→·v→ = ‖u→‖×‖v→'‖ (avec signe), v→' = projeté orthogonal de v→ sur la direction de u→.
Signe : positif si angle aigu, négatif si angle obtus, nul si angle droit.

### 6.2 Expression analytique et propriétés

Repère orthonormé : u→(x,y), v→(x',y') → u→·v→ = xx'+yy'.
Propriétés : symétrie (u→·v→=v→·u→), bilinéarité (u→·(v→+w→)=u→·v→+u→·w→, (k×u→)·v→=k×(u→·v→)), u→·u→=‖u→‖².
Piège : cette formule (xx'+yy') n'est valable QUE dans un repère orthonormé — dans un repère quelconque, elle ne marche pas.

### 6.3 Norme et distance entre deux points

Norme : ‖u→‖=√(x²+y²).
Distance AB : AB = ‖AB→‖ = √((x(B)-x(A))²+(y(B)-y(A))²).

### 6.4 Orthogonalité et colinéarité (les deux conditions analytiques à connaître)

Orthogonalité : u→(x,y)⊥v→(x',y') ⟺ u→·v→=0 ⟺ xx'+yy'=0.
Colinéarité : u→(x,y) et v→(x',y') sont colinéaires ⟺ xy'-x'y=0 (déterminant nul).
Utilisation de la colinéarité : points A,B,C alignés ⟺ AB→ et AC→ colinéaires ; droites parallèles ⟺ leurs vecteurs directeurs sont colinéaires.

### 6.5 Formule d'Al-Kashi (loi des cosinus)

BC² = AB²+AC²-2×AB×AC×cos(angle en A). Généralise Pythagore (angle droit → cos=0).

### 6.6 Équation d'une droite

Via vecteur normal n→(a,b) : a(x-x0)+b(y-y0)=0, soit ax+by+c=0.
Via vecteur directeur u→(a,b) : b(x-x0)-a(y-y0)=0.
Relation : si n→(a,b) est normal à la droite, alors u→(-b,a) en est un vecteur directeur (rotation de 90°) ; coefficient directeur (pente) = b/a si a≠0.

### 6.7 Distance d'un point à une droite

Droite d'équation ax+by+c=0, point M(x(M),y(M)) : d(M,droite) = |a×x(M)+b×y(M)+c| / √(a²+b²).
Application classique : une droite est tangente à un cercle ⟺ distance du centre à la droite = rayon.

### 6.8 Équation d'un cercle

Centre Ω(a,b), rayon r : (x-a)²+(y-b)²=r². Technique pour la forme développée : compléter le carré.

### 6.9 Applications classiques

Ensemble des M tels que MA→·MB→=0 : cercle de diamètre [AB].
Tangente à un cercle en un point : perpendiculaire au rayon en ce point.

## 7. Calcul trigonométrique

### 7.1 Cercle trigonométrique et radian

Cercle trigonométrique : cercle de rayon 1, centré à l'origine, orienté (sens direct = sens anti-horaire).
Conversion : π radians = 180°. Donc radians = degrés×π/180, et degrés = radians×180/π.

### 7.2 Valeurs remarquables (à connaître par cœur)

Pour x = 0, π/6, π/4, π/3, π/2 :
cos(x) : 1, √3/2, √2/2, 1/2, 0
sin(x) : 0, 1/2, √2/2, √3/2, 1
tan(x) : 0, √3/3, 1, √3, indéfinie (cos=0)

### 7.3 Relation fondamentale et tangente

∀x, cos²(x)+sin²(x)=1. Conséquence : -1≤cos(x)≤1 ∧ -1≤sin(x)≤1.
tan(x)=sin(x)/cos(x), définie ⟺ cos(x)≠0 (donc x≠π/2+kπ). Piège : la période de tan est π, pas 2π comme cos et sin.

### 7.4 Angles associés

Opposé (-x) : cos(-x)=cos(x) [paire], sin(-x)=-sin(x) [impaire].
Supplémentaire (π-x) : cos(π-x)=-cos(x), sin(π-x)=sin(x).
Anti-supplémentaire (π+x) : cos(π+x)=-cos(x), sin(π+x)=-sin(x).
Complémentaire (π/2-x) : cos(π/2-x)=sin(x), sin(π/2-x)=cos(x).
π/2+x : cos(π/2+x)=-sin(x), sin(π/2+x)=cos(x).

### 7.5 Formules d'addition

cos(a+b)=cos(a)cos(b)-sin(a)sin(b)
cos(a-b)=cos(a)cos(b)+sin(a)sin(b)
sin(a+b)=sin(a)cos(b)+cos(a)sin(b)
sin(a-b)=sin(a)cos(b)-cos(a)sin(b)

### 7.6 Formules de duplication

cos(2a)=cos²(a)-sin²(a)=2cos²(a)-1=1-2sin²(a)
sin(2a)=2sin(a)cos(a)

### 7.7 Équations trigonométriques

cos(x)=cos(a) ⟺ (x=a+2kπ) ∨ (x=-a+2kπ), k∈ℤ
sin(x)=sin(a) ⟺ (x=a+2kπ) ∨ (x=π-a+2kπ), k∈ℤ
tan(x)=tan(a) ⟺ x=a+kπ (k∈ℤ) — une seule famille (pas deux), car tan a pour période π (pas 2π) et est injective sur chaque période.
Piège : ne jamais oublier le "+2kπ" (ou "+kπ" pour tan), et bien distinguer les deux familles de solutions pour cos/sin (signe différent sur la deuxième famille) — tan n'a qu'une seule famille.

Dessins (cercle trigonométrique complet + angles associés par symétrie) : voir Trigonometrie_dessins.pdf.

## 8. La rotation dans le plan

### 8.1 Définition

Rotation de centre Ω, angle θ : à M associe M' tel que ΩM=ΩM' et angle orienté (ΩM,ΩM')=θ (mod 2π).
θ positif = sens direct (anti-horaire, sens trigonométrique) ; θ négatif = sens indirect (horaire).
Ω est l'unique point invariant de la rotation (sauf si θ≡0 mod 2π, auquel cas c'est l'identité).

### 8.2 Écriture analytique

Repère orthonormé, rotation de centre Ω(a,b), angle θ. Image de M(x,y) : M'(x',y') avec :
x'-a = (x-a)cos(θ) - (y-b)sin(θ)
y'-b = (x-a)sin(θ) + (y-b)cos(θ)

### 8.3 Propriétés

Isométrie (conserve les distances). Conserve les angles **orientés** — c'est une différence importante avec une symétrie, qui elle inverse les angles orientés (une rotation est un "déplacement", une symétrie est un "antidéplacement").
Droite → droite (si la droite passe par Ω, son image passe aussi par Ω, tournée de θ). Cercle → cercle de même rayon (le centre image est l'image du centre par la rotation). Conserve parallélisme et orthogonalité.

### 8.4 Composée de rotations

Même centre Ω, angles θ1 et θ2 : composée = rotation de centre Ω, angle θ1+θ2.
Centres différents, angles θ1 et θ2 : si θ1+θ2 ≢ 0 (mod 2π), composée = rotation d'angle θ1+θ2 (centre à déterminer) ; si θ1+θ2 ≡ 0 (mod 2π), composée = translation.

### 8.5 Utilisation classique

Démontrer des figures (triangles équilatéraux, carrés) via rotations d'angle π/3, π/2.
Prouver qu'un triangle est équilatéral : montrer qu'une rotation d'angle π/3 (ou -π/3) envoie un sommet sur un autre.

## 9. Limite d'une fonction numérique

### 9.1 Définitions intuitives

lim(x→a) f(x) = L (finie) : f(x) se rapproche indéfiniment de L quand x se rapproche de a.
lim(x→a) f(x) = +∞ (ou -∞) : f(x) devient aussi grand (ou petit) que voulu quand x se rapproche de a.
lim(x→+∞) f(x) = L (ou ±∞) : même idée quand x devient très grand (et de même pour x→-∞).

### 9.2 Limites à gauche et à droite

lim(x→a⁻) f(x) : limite quand x tend vers a par valeurs inférieures (à gauche).
lim(x→a⁺) f(x) : limite quand x tend vers a par valeurs supérieures (à droite).
f a une limite en a ⟺ (les limites à gauche et à droite existent) ∧ (elles sont égales).
Piège classique : une fonction peut avoir des limites à gauche/droite différentes (donc pas de limite globale en ce point) — ex : 1/x en 0, limite à gauche -∞, limite à droite +∞.

### 9.3 Limites des fonctions usuelles (briques de base)

Affine, carrée, cube : limites en ±∞ = ±∞ selon le degré et le signe du coefficient dominant.
1/x : lim(x→0⁺)=+∞, lim(x→0⁻)=-∞, lim(x→±∞)=0.
√x : lim(x→+∞)=+∞, lim(x→0⁺)=0.
Ces limites de base servent à calculer des limites plus complexes par les opérations ci-dessous.

### 9.4 Opérations sur les limites

Somme : lim(f+g) = lim f + lim g (si pas de forme ∞-∞).
Produit : lim(f×g) = lim f × lim g (si pas de forme 0×∞).
Quotient : lim(f/g) = lim f / lim g (si lim g≠0, et pas de forme ∞/∞ ou 0/0).
Composée : (lim(x→a) f(x)=b) ∧ (lim(y→b) g(y)=L) ⟹ lim(x→a) g(f(x))=L.

### 9.5 Formes indéterminées et techniques de levée

4 formes classiques : "∞-∞", "0×∞", "∞/∞", "0/0".
Techniques : factoriser par le terme dominant (polynômes en ∞), multiplier par la quantité conjuguée (expressions avec racines), factoriser numérateur/dénominateur (fractions rationnelles en un point).

### 9.6 Théorèmes de comparaison

Théorème des gendarmes : (g≤f≤h près de a) ∧ (lim g=lim h=L, finie) ⟹ lim f=L.
Théorème de comparaison (limites infinies) : (f≥g près de a) ∧ (lim g=+∞) ⟹ lim f=+∞ (symétrique pour -∞).
Passage à la limite dans les inégalités : (f≤g près de a) ∧ (les deux limites existent) ⟹ lim f ≤ lim g — piège : une inégalité stricte devient large en passant à la limite.

### 9.7 Asymptotes

Horizontale : lim(x→±∞) f(x) = L (finie) → droite y=L.
Verticale : lim(x→a) f(x) = ±∞ → droite x=a.
Oblique : droite y=ax+b si lim(x→±∞) [f(x)-(ax+b)] = 0.
Méthode pratique pour trouver a et b : a = lim(x→±∞) f(x)/x, puis b = lim(x→±∞) [f(x)-ax].

### 9.8 Continuité et théorème des valeurs intermédiaires (TVI)

f continue en a ⟺ lim(x→a) f(x) = f(a) (la limite existe ∧ vaut la valeur de la fonction).
f continue sur un intervalle I : continue en chaque point de I.
TVI : f continue sur [a,b] ⟹ ∀k compris entre f(a) et f(b), ∃c∈[a,b], f(c)=k.
Corollaire très utilisé : (f continue sur [a,b]) ∧ (f(a)×f(b)<0) ⟹ ∃c∈]a,b[, f(c)=0 (existence d'une solution à f(x)=0).
Si en plus f est strictement monotone sur [a,b], cette solution c est UNIQUE (théorème de la bijection).

## 10. Dérivabilité d'une fonction numérique

### 10.1 Nombre dérivé et dérivabilité

f'(a) = lim(h→0) [f(a+h)-f(a)]/h = lim(x→a) [f(x)-f(a)]/(x-a) (deux écritures équivalentes, les deux se voient en exercice).
f est dérivable en a si cette limite existe et est finie.

### 10.2 Dérivabilité à gauche et à droite

f dérivable à gauche en a : lim(h→0⁻) [f(a+h)-f(a)]/h existe (notée f'g(a)). Dérivable à droite : idem avec h→0⁺ (notée f'd(a)).
f dérivable en a ⟺ (f dérivable à gauche en a) ∧ (f dérivable à droite en a) ∧ (f'g(a)=f'd(a)).
Exemple classique : f(x)=|x| en 0 — f'g(0)=-1, f'd(0)=1, différentes, donc f n'est PAS dérivable en 0 (point anguleux).

### 10.3 Dérivabilité et continuité

f dérivable en a ⟹ f continue en a (dérivabilité ⟹ continuité).
La réciproque est FAUSSE : une fonction peut être continue sans être dérivable — ex : |x| en 0, continue mais pas dérivable.

### 10.4 Interprétation géométrique : tangente

f'(a) = pente de la tangente à la courbe au point d'abscisse a.
Équation de la tangente : y = f'(a)(x-a) + f(a).
Cas particulier : si lim(x→a) [f(x)-f(a)]/(x-a) = ±∞, la courbe admet une tangente VERTICALE en a (droite x=a) — ex : √x en 0.

### 10.5 Dérivées usuelles

(k)'=0 (constante). (xⁿ)'=n×x^(n-1). (1/x)'=-1/x². (√x)'=1/(2√x).
(sin(x))'=cos(x). (cos(x))'=-sin(x).

### 10.6 Opérations sur les dérivées

(u+v)'=u'+v'. (k×u)'=k×u' (k constante).
(uv)'=u'v+uv'. (u/v)'=(u'v-uv')/v².
(u∘v)'=(u'∘v)×v' (règle de la chaîne).
Cas particulier très utilisé : (uⁿ)'=n×u^(n-1)×u'.

### 10.7 Dérivée, sens de variation et extremums locaux

f'≥0 sur I ⟺ f croissante sur I ; f'≤0 ⟺ décroissante.
Extremum local en a (f dérivable) : condition NÉCESSAIRE f'(a)=0, mais PAS suffisante à elle seule.
Condition suffisante : (f'(a)=0) ∧ (f' change de signe autour de a) ⟹ f admet un extremum local en a.
Piège classique : f'(a)=0 sans changement de signe ⟹ pas d'extremum (ex : x³ en 0, point d'inflexion, pas un extremum).

## 11. Étude des fonctions numériques

### 11.1 Démarche complète (méthodologie)

1. Domaine de définition Df.
2. Parité, si Df est symétrique (permet de limiter l'étude à une moitié du domaine).
3. Limites aux bornes de Df (et en tout point exclu du domaine).
4. Calcul de f' et étude de son signe.
5. Tableau de variations (signe de f', sens de variation, valeurs aux bornes/extremums).
6. Asymptotes et branches infinies.
7. Points particuliers : intersections avec les axes, quelques valeurs supplémentaires si besoin.
8. Tracé de la courbe.

### 11.2 Branches infinies (complément du chapitre 9)

Si lim(x→±∞) f(x)/x = a (fini, non nul), puis lim [f(x)-ax] = b (fini) : asymptote oblique y=ax+b.
Si lim(x→±∞) f(x)/x = ±∞ ou 0 (sans convergence du reste vers une valeur finie) : **branche parabolique** — pas d'asymptote oblique, mais la courbe s'échappe dans une direction caractéristique.

### 11.3 Application classique : la fonction homographique

f(x) = (ax+b)/(cx+d), avec c≠0 ∧ ad-bc≠0 (sinon f serait constante).
Domaine : x≠-d/c.
Forme canonique : f(x) = a/c + k/(x-x0), avec x0=-d/c, y0=a/c (k une constante liée à ad-bc).
Centre de symétrie du graphe : point Ω(x0,y0) = (-d/c, a/c) — même principe que 1/x (symétrique par rapport à l'origine), ici translaté en Ω.
Asymptotes : verticale x=-d/c, horizontale y=a/c.
Monotonie : déterminée par le signe de (ad-bc) — si ad-bc>0, f est croissante sur chaque intervalle de Df ; si ad-bc<0, f est décroissante.

## 12. Dénombrement

### 12.1 Principes de base

Cardinal d'un ensemble fini E (nombre d'éléments) : noté Card(E).
Principe multiplicatif ("et") : p étapes indépendantes avec n1,...,np choix chacune → n1×...×np résultats au total.
Principe additif ("ou") : si un choix se fait dans A OU dans B (A et B disjoints), nombre de possibilités = Card(A)+Card(B).

### 12.2 Les 4 formules (selon répétition et ordre)

p-listes (avec répétition, ordre compte) : nᵖ.
Arrangements (sans répétition, ordre compte) : A(n,p) = n!/(n-p)!.
Permutations (cas particulier : n parmi n) : n!.
Combinaisons (sans répétition, ordre ne compte pas) : C(n,p) = n!/(p!(n-p)!) = A(n,p)/p!.

Tableau de décision :
Répétition possible + ordre compte → p-liste (nᵖ).
Pas de répétition + ordre compte → arrangement (A(n,p)).
Pas de répétition + ordre ne compte pas → combinaison (C(n,p)).

### 12.3 Traduire un problème : vocabulaire des tirages

Tirage successif AVEC remise (on remet l'objet après chaque tirage, ordre compte) → p-liste.
Tirage successif SANS remise (ordre compte, pas de répétition) → arrangement.
Tirage simultané (plusieurs objets pris d'un coup, ordre ne compte pas) → combinaison.
Piège : "tirage successif sans remise" et "tirage simultané" comptent souvent le même genre de résultat final, mais utilisent des formules différentes selon que l'énoncé demande de distinguer l'ordre ou non — toujours relire attentivement ce que l'énoncé compte.

Tableau de décision dessiné (PDF) : voir Denombrement_tableau_decision.pdf.

Bonus (hors programme 1BAC, mais utile pour l'olympiade) — **combinaison avec répétition** (multichoose) : choisir p éléments parmi n types, répétition permise, ordre ne compte pas : C'(n,p) = C(n+p-1,p) = (n+p-1)!/(p!×(n-1)!). Technique "étoiles et barres" : distribuer p objets identiques dans n catégories équivaut à arranger p étoiles et (n-1) barres de séparation en ligne.

### 12.4 Propriétés et binôme de Newton

C(n,p) = C(n,n-p).
Formule de Pascal : C(n,p) = C(n-1,p-1) + C(n-1,p) (triangle de Pascal).
Binôme de Newton : (a+b)ⁿ = Σ (k=0 à n) de C(n,k)×a^(n-k)×bᵏ.

## 13. Arithmétique dans ℤ

### 13.1 Divisibilité

a|b ("a divise b") ⟺ ∃k∈ℤ, b=ka.
Propriétés : (a|b) ∧ (b|c) ⟹ a|c (transitivité). (a|b) ∧ (a|c) ⟹ a|(b+c) ∧ a|(b-c). a|b ⟹ ∀k∈ℤ, a|(kb).

### 13.2 Division euclidienne

∀a∈ℤ, ∀b∈ℕ*, ∃!(q,r), a=bq+r, 0≤r<b.

### 13.3 Nombres premiers et décomposition en facteurs premiers

Nombre premier : exactement deux diviseurs positifs (1 et lui-même). Infinité des nombres premiers (preuve par l'absurde, chapitre 1).
Test de primalité pratique : pour tester si n est premier, il suffit de vérifier qu'aucun nombre premier ≤√n ne le divise.
Théorème fondamental de l'arithmétique : tout entier n≥2 se décompose de façon UNIQUE (à l'ordre près) en produit de facteurs premiers : n = p1^a1 × p2^a2 × ... × pk^ak.
PGCD et PPCM via décomposition : PGCD = produit des facteurs premiers communs avec le plus PETIT exposant ; PPCM = produit de tous les facteurs premiers avec le plus GRAND exposant.

### 13.4 PGCD et PPCM

PGCD (algorithme d'Euclide) : PGCD(a,b)=PGCD(b, a mod b), jusqu'à reste 0.
PPCM(a,b) = (a×b)/PGCD(a,b).
a et b sont dits "premiers entre eux" si PGCD(a,b)=1.

### 13.5 Théorème de Bézout et théorème de Gauss

Bézout (cas général) : PGCD(a,b)=d ⟺ ∃u,v∈ℤ, au+bv=d.
Cas particulier très utilisé : a et b premiers entre eux ⟺ ∃u,v∈ℤ, au+bv=1.
Gauss : (a|bc) ∧ (PGCD(a,b)=1) ⟹ a|c.

### 13.6 Équations diophantiennes (application de Bézout)

Résoudre ax+by=c (x,y∈ℤ inconnues) : une solution existe ⟺ PGCD(a,b) divise c.
Méthode : trouver une solution particulière (x0,y0), puis solution générale x=x0+(b/d)t, y=y0-(a/d)t, pour t∈ℤ, où d=PGCD(a,b).

### 13.7 Congruences

a≡b (mod n) ⟺ n|(a-b) ⟺ a et b ont le même reste dans la division par n.
Opérations : (a≡b (mod n)) ∧ (c≡d (mod n)) ⟹ (a+c≡b+d (mod n)) ∧ (a×c≡b×d (mod n)) — les congruences se manipulent comme des égalités pour l'addition et la multiplication.
Piège : la DIVISION n'est pas automatiquement compatible avec les congruences (nécessite des précautions, notamment que le diviseur soit premier avec n).
Application classique : calculer le reste d'une grande puissance (ex : reste de 7¹⁰⁰ divisé par 5) en utilisant les propriétés de multiplication des congruences.

## 14. Vecteurs de l'espace

### 14.1 Vecteurs de l'espace — généralités

Un vecteur de l'espace se définit et se manipule comme un vecteur du plan (direction, sens, norme), mais dans un espace à 3 dimensions.
Somme (relation de Chasles) : AB→+BC→=AC→. Produit par un réel : k×u→.
Propriétés algébriques (associativité, commutativité, distributivité) : identiques à celles du plan (chapitres 5-6), rien de nouveau ici.

### 14.2 Vecteurs colinéaires

u→ et v→ colinéaires ⟺ (u→=0→) ∨ (∃k∈ℝ, v→=ku→).
Utilisation : A,B,C alignés ⟺ AB→ et AC→ colinéaires (même critère qu'en 2D).

### 14.3 Vecteurs coplanaires

Définition : u→,v→,w→ sont coplanaires s'il existe des représentants de ces 3 vecteurs situés dans un même plan.
Critère analytique (le plus utilisé, celui qui sert dans les exercices) : si u→ et v→ ne sont pas colinéaires, alors w→,u→,v→ coplanaires ⟺ ∃(a,b)∈ℝ², w→=au→+bv→.
Piège : ce critère suppose u→,v→ non colinéaires — sinon la notion perd son pouvoir de test (deux vecteurs colinéaires sont "coplanaires" avec n'importe quel troisième vecteur, la condition devient sans intérêt).
Utilisation : A,B,C,D coplanaires ⟺ AB→,AC→,AD→ coplanaires.

### 14.4 Base et repère de l'espace

Base de l'espace : un triplet (i→,j→,k→) de 3 vecteurs NON coplanaires.
Théorème (existence et unicité des coordonnées) : (i→,j→,k→) base ⟹ ∀u→, ∃!(x,y,z)∈ℝ³, u→=xi→+yj→+zk→. (x,y,z) = coordonnées de u→ dans cette base.
Repère de l'espace : (O,i→,j→,k→) = un point O (origine) + une base. Coordonnées d'un point M = coordonnées du vecteur OM→.
Piège : contrairement au plan, 2 vecteurs non colinéaires ne suffisent JAMAIS à tout engendrer dans l'espace — il faut 3 vecteurs non coplanaires pour former une base (un vecteur "hors du plan" formé par 2 vecteurs donnés n'est PAS une combinaison linéaire de ces 2 vecteurs).

### 14.5 Coordonnées et opérations

u→(x,y,z), v→(x',y',z') : u→+v→ a pour coordonnées (x+x', y+y', z+z') ; k×u→ a pour coordonnées (kx,ky,kz).
Coordonnées de AB→ : (x(B)-x(A), y(B)-y(A), z(B)-z(A)).
Milieu de [AB] : ((x(A)+x(B))/2, (y(A)+y(B))/2, (z(A)+z(B))/2) — extension directe du plan.
Barycentre (extension du chapitre 5) : x(G)=(α×x(A)+β×x(B))/(α+β), et de même pour y(G) et z(G).

### 14.6 Colinéarité analytique en 3D (piège important)

u→(x,y,z) et v→(x',y',z') colinéaires ⟺ ∃k∈ℝ, (x'=kx) ∧ (y'=ky) ∧ (z'=kz) — proportionnalité sur les 3 composantes.
Piège central du chapitre : contrairement au plan, où un seul déterminant (xy'-x'y=0) suffit à tester la colinéarité, en 3D il n'existe PAS de déterminant 2×2 unique qui fait ce travail — il faut vérifier la proportionnalité sur les 3 coordonnées avec le MÊME k (attention si une coordonnée est nulle : k n'est alors pas déterminé par cette composante, il faut le retrouver via une autre).

## 15. Étude analytique de l'espace

### 15.1 Équation cartésienne d'un plan

Plan P passant par A(x0,y0,z0), de vecteur normal n→(a,b,c) (n→≠0→) : M(x,y,z)∈P ⟺ n→·AM→=0 ⟺ a(x-x0)+b(y-y0)+c(z-z0)=0 ⟺ ax+by+cz+d=0, avec d=-(ax0+by0+cz0).
Réciproque : toute équation ax+by+cz+d=0 avec (a,b,c)≠(0,0,0) définit un plan de vecteur normal n→(a,b,c).
Piège : n→ n'est pas unique — tout vecteur k×n→ (k≠0) est aussi normal au même plan, donc deux équations proportionnelles (ka,kb,kc,kd) définissent le MÊME plan.

### 15.2 Représentation paramétrique d'une droite

Droite D passant par A(x0,y0,z0), de vecteur directeur u→(a,b,c) (u→≠0→) : M(x,y,z)∈D ⟺ ∃t∈ℝ, AM→=t×u→ ⟺ {x=x0+at, y=y0+bt, z=z0+ct}.
Une droite peut aussi être définie comme intersection de deux plans non parallèles (système de 2 équations cartésiennes) — un vecteur directeur s'obtient alors via le produit vectoriel des deux vecteurs normaux (vu au chapitre 17).

### 15.3 Appartenance d'un point

M∈P (équation ax+by+cz+d=0) ⟺ ses coordonnées vérifient l'équation.
M∈D (paramétrée par t) ⟺ ∃t∈ℝ tel que x=x0+at ∧ y=y0+bt ∧ z=z0+ct simultanément.
Piège : il faut un SEUL t qui marche pour les 3 coordonnées à la fois — si les 3 équations donnent des t différents, M∉D.

### 15.4 Positions relatives de deux plans

P1(n1→), P2(n2→) : P1∥P2 ⟺ n1→,n2→ colinéaires — puis confondus si un point de P1 vérifie aussi l'équation de P2, strictement parallèles sinon.
P1,P2 sécants ⟺ n1→,n2→ non colinéaires — intersection = une droite.
P1⊥P2 ⟺ n1→·n2→=0.

### 15.5 Positions relatives d'une droite et d'un plan

D(u→), P(n→) : D∥P ⟺ u→·n→=0 — puis D⊂P si un point de D vérifie l'équation de P, D strictement parallèle à P sinon.
D sécante à P ⟺ u→·n→≠0 — point d'intersection unique (substituer la paramétrisation de D dans l'équation de P, résoudre en t).
D⊥P ⟺ u→,n→ colinéaires.

### 15.6 Positions relatives de deux droites (piège central du chapitre)

D1(u1→), D2(u2→) : D1∥D2 ⟺ u1→,u2→ colinéaires — confondues si elles partagent un point, strictement parallèles sinon.
Si u1→,u2→ non colinéaires : D1,D2 sécantes (∃ un point commun) OU non coplanaires (aucun point commun).
Piège fondamental : contrairement au plan, où deux droites non parallèles sont TOUJOURS sécantes, dans l'espace deux droites non parallèles peuvent ne jamais se croiser — non coplanaires (ex : deux arêtes opposées d'un cube). Ne jamais conclure "sécantes" sans avoir vérifié l'existence réelle d'un point commun.

### 15.7 Distance d'un point à un plan

Plan ax+by+cz+d=0, point M(x(M),y(M),z(M)) : d(M,P) = |a×x(M)+b×y(M)+c×z(M)+d| / √(a²+b²+c²) — extension directe de la formule 2D (chapitre 6.7).

### 15.8 Intersection de deux plans sécants (méthode)

Résoudre le système des 2 équations cartésiennes (2 équations, 3 inconnues) : exprimer 2 variables en fonction de la 3ᵉ pour obtenir une représentation paramétrique de la droite d'intersection.

### 15.9 Application classique

Plan médiateur de [AB] : {M | MA=MB} — le plan passant par le milieu de [AB], de vecteur normal AB→.

## 16. Produit scalaire dans l'espace

### 16.1 Définitions et propriétés

Mêmes définitions qu'en 2D (chapitre 6.1) : u→·v→=‖u→‖×‖v→‖×cos(θ) (géométrique), ou via projection — rien ne change en passant à l'espace.
Propriétés : symétrie (u→·v→=v→·u→), bilinéarité (u→·(v→+w→)=u→·v→+u→·w→, (k×u→)·v→=k×(u→·v→)), u→·u→=‖u→‖².

### 16.2 Expression analytique

Repère orthonormé, u→(x,y,z), v→(x',y',z') : u→·v→ = xx'+yy'+zz'.
Piège : valable UNIQUEMENT dans un repère orthonormé (même piège qu'en 2D, chapitre 6.2).

### 16.3 Norme et distance entre deux points

‖u→‖=√(x²+y²+z²).
AB = √((x(B)-x(A))²+(y(B)-y(A))²+(z(B)-z(A))²).

### 16.4 Orthogonalité

u→⊥v→ ⟺ u→·v→=0 ⟺ xx'+yy'+zz'=0.

### 16.5 Vecteur normal à un plan (méthode analytique)

n→ normal à un plan P ⟺ n→ orthogonal à DEUX vecteurs directeurs non colinéaires de P ⟺ (n→·u→=0) ∧ (n→·v→=0), où u→,v→ dirigent P.
Piège : être orthogonal à un seul vecteur ne fige qu'un PLAN de directions possibles, pas une direction unique — il faut être orthogonal à 2 vecteurs non colinéaires pour obtenir une direction unique (la normale). C'est le miroir exact de "2 vecteurs engendrent un plan, 3 engendrent l'espace" (chapitre 14).
Méthode pratique : poser n→(a,b,c) inconnu, résoudre (n→·AB→=0) ∧ (n→·AC→=0) — 2 équations, 3 inconnues, fixer une inconnue (souvent la plus simple) pour obtenir une solution particulière.

### 16.6 Équation de sphère

Centre Ω(a,b,c), rayon r : (x-a)²+(y-b)²+(z-c)²=r². Compléter le carré pour passer à la forme développée (même technique qu'en 2D, chapitre 6.8).

### 16.7 Positions relatives sphère/plan

Sphère S(Ω,r), plan P : comparer d(Ω,P) à r.
d(Ω,P)>r : disjoints. d(Ω,P)=r : tangents (P touche S en un seul point). d(Ω,P)<r : sécants (intersection = un cercle).

### 16.8 Applications classiques

Plan tangent à une sphère en un point M0 : le plan passant par M0, de vecteur normal ΩM0→.
{M | MA→·MB→=0} : sphère de diamètre [AB] (extension directe du chapitre 6.9).

## 17. Produit vectoriel dans l'espace

### 17.1 Définition et propriétés

u→∧v→ ("produit vectoriel") : le vecteur orthogonal à u→ ET à v→, tel que (u→,v→,u→∧v→) forme une base directe, de norme ‖u→∧v→‖=‖u→‖×‖v→‖×|sin(u→,v→)| — l'aire du parallélogramme construit sur u→,v→.
Piège : u→∧v→ N'EST PAS commutatif — v→∧u→=-(u→∧v→) (antisymétrie), contrairement au produit scalaire qui lui est symétrique.
Bilinéarité : (u→+w→)∧v→=u→∧v→+w→∧v→, (k×u→)∧v→=k×(u→∧v→) — mêmes règles de distributivité que le produit scalaire, seule la commutativité change.

### 17.2 Expression analytique

u→(x,y,z), v→(x',y',z') : u→∧v→ = (yz'-zy', zx'-xz', xy'-yx').
Piège : c'est la formule la plus facile à mal recopier du programme — le pattern est cyclique (x→y→z→x), chaque composante "saute" la variable de son propre indice. Vérification rapide : calcule toujours u→∧u→ dans ta tête, ça doit donner 0→.

### 17.3 Colinéarité (raccourci du chapitre 14.6)

u→,v→ colinéaires ⟺ u→∧v→=0→ — souvent plus rapide que la vérification composante par composante du chapitre 14.6.

### 17.4 Vecteur normal à un plan (raccourci du chapitre 16.5)

Si u→,v→ dirigent un plan P (non colinéaires) : n→=u→∧v→ est automatiquement normal à P — remplace directement la résolution du système du chapitre 16.5.

### 17.5 Aires

Aire du parallélogramme construit sur u→,v→ : ‖u→∧v→‖.
Aire du triangle ABC : (1/2)×‖AB→∧AC→‖.

### 17.6 Produit mixte et coplanarité (raccourci du chapitre 14.3)

Produit mixte : [u→,v→,w→] = (u→∧v→)·w→ — un SCALAIRE (pas un vecteur, attention à ne pas le confondre avec u→∧v→).
u→,v→,w→ coplanaires ⟺ [u→,v→,w→]=0 — remplace directement la résolution en (a,b) du chapitre 14.3.

### 17.7 Volumes

Volume du parallélépipède construit sur u→,v→,w→ : |[u→,v→,w→]|.
Volume du tétraèdre ABCD : (1/6)×|[AB→,AC→,AD→]|.
