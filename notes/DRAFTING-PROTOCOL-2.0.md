# Frozen drafting protocol — Span-Growth Note v2.0

Loose working note — never commit (notes/ stays untracked). Frozen 22 Jul 2026, submitted to Jérôme
BEFORE any LaTeX modification. Drafting starts only on his go on this protocol + plan; branch `2.0`
is already cut off `main` (= v1.2 merge, 4202e31) and pushed.

## 0. Decision being implemented

Public vehicle for the Heisenberg growth-equation closure chantier (Outcome C; report
`fermionic-matter/front-heisenberg-growth-closure-report.md`, referee PASS WITH MINOR FIXES,
all fixes applied): **SGN v2.0**, not a new note. Same repo (`admissibility/span-growth-note`),
same bib key `Beau2026sgn`, same concept DOI 10.5281/zenodo.21480521, branch `2.0`.
Proposed title (Jérôme's): *Native Span Growth from Capacity Decay and the Failure of the
Heisenberg Capacity-to-Rate Transfer*.

## 1. Frozen inputs

- SGN v1.2 tex (`tex/SpanGrowthNote.tex`, 475 lines) — the base manuscript; its Lemma
  (exact increment identity), Theorem (three-branch classification), Corollaries t1/t3, and the
  LPS/pair/beta-category remarks are the published overlap.
- The chantier protocol + closure report + recovery note (fermionic-matter/, review-complete).
- The β* transfer audit (`front-beta-star-transfer-audit.md`) for [T4]/[T5] anchors.
- Frozen corpus sources as anchored in the closure report (O4, O6, O12 03-exact-capacity, O16,
  Relaxation, CC-note incl. isometry lemma and committed `h3z_spheres.py`).
- External: Bass, Guivarc'h, LPS88, Blachère, Gurevich–Hadani (already in `external-refs.bib`);
  TO ADD: Duchin–Shapiro (arXiv:1411.4201, rational growth — needed for the two-sided sphere
  order), Coulhon–Saloff-Coste (DOI 10.4171/RMI/138, general isoperimetric lower bound —
  consistency anchor only), Pansu (DOI 10.1017/S0143385700002054, ball-volume limit). All three
  web-verified during the chantier; bibliographic data to be re-checked at drafting time.

## 2. Mandatory corrective (Jérôme's, load-bearing for v2.0)

v1.2's Theorem assumes $\sigma_c(n) = a\,n^{-\delta_c}(1+o(1))$, $a, \delta_c > 0$ POINTWISE with
real-valued weights, while $\Delta r(n) = \sigma_c(n)|S_n|$ is INTEGER-valued. For
$\delta_c > D-1$ the summand $a\kappa\,n^{D-1-\delta_c} \to 0$: a positive pointwise power law is
then unrealizable by integer increments (eventually $\Delta r \in \{0\} \cup [1,\infty)$ forces
either $\Delta r = 0$ exactly — contradicting $\sigma_c > 0$ — or a violation of the decay).
NOTE the bite: this includes the MEASURED range $3 < \delta_c < 4$ (growth branch), not only the
saturation branch. v2.0 must therefore distinguish, explicitly and with separate statements:

1. **Abstract theorem (real weights).** The three-branch classification exactly as in v1.2,
   restated for real-valued weight sequences $w_n \ge 0$ (no integrality) — proved, unchanged.
2. **Effective pre-saturation window law (integer rank) — finite two-sided bounds ONLY.** No
   asymptotic density claim (the "sparse unit increments of density $\sim a\kappa n^{D-1-\delta_c}$"
   formulation is struck: undemonstrated). The rigorous window statement is: IF on a finite window
   $m < k \le n$ the measured sequences satisfy the two-sided bounds
   $a_- k^{-\delta} \le \sigma_c(k) \le a_+ k^{-\delta}$ and
   $\kappa_- k^{D-1} \le |S_k| \le \kappa_+ k^{D-1}$, THEN
   $a_-\kappa_- \sum_{k=m+1}^{n} k^{D-1-\delta} \le r(n) - r(m) \le
   a_+\kappa_+ \sum_{k=m+1}^{n} k^{D-1-\delta}$ — an exact finite statement, compatible with
   integrality, requiring no pointwise power law and no asymptotics. The growth-branch exponent
   reading is then a property of the window bounds, nothing more.
3. **Joint $(q,n)$ limit — demoted by default.** The isometry condition $q > 2\Gamma(n(q))+1$ is
   NECESSARY but INSUFFICIENT: it controls the geometry, not the integrality of the increments.
   An acceptable construction must additionally supply either (i) an average over a growing number
   of blocks, or (ii) an amplitude $a(q)$ and a rank margin guaranteeing realizability of the
   increments along the sequence. Unless such a construction is actually produced during drafting
   (not anticipated), the joint limit is DEMOTED to the window formulation — the recommended
   default; v1.2's "equivalently in the double limit" sentence is then removed, not weakened.
4. **No asymptotic claim for measured values** without the bridge 1↔2: every numerical statement
   is window-scoped; $\delta_\infty$ stays open; the O25 bracket extrapolations are labelled
   window-law extrapolations.

## 3. Content additions (what justifies the major version)

From the closure report, calibrations included (implication chain; [T1] scoped to the two corpus
realisations; [T4] corpus-scoped "defined or derived", no impossibility claim; $\beta_{\mathrm{nat}}$
window-effective; [C] partial):

- **[T1] structured refutation** upgrading Cor t1: the contraposition
  $p \propto N \Rightarrow \sigma_c \to \text{const} > 0 \Rightarrow \delta_c = 0$ (converse
  disclaimed), for BOTH corpus realisations (bounded effective valence; span rank), plus the
  measurement-independent dimension count at fixed $q$ ($r \le q$ vs $|B_n| \to q^3$).
- **Native multiplicative coupling and the lost $p^{1/2}$**: the identity is multiplicative
  against $N^\theta$, $\theta = (D-1)/D = 3/4$ two-sided (Duchin–Shapiro + exact counts; CSC as
  consistency anchor only), window $\theta_{\mathrm{eff}} \approx 0.77$–$0.80$; conversion to a
  $p$-power requires [T1] (and would give $p^{3/4}$, not $p^{1/2}$).
- **Absence of a native BI carrier**: $N(n)$ is autonomous on the fixed graph; the O4 feedback
  loop (flux bound shaping $p(n)$) has no native carrier; $c_{\mathrm{BI}}$ constrains at most the
  rank-to-time dictionary, not the growth law.
- **[T4] failure (corpus-scoped)**, upgrading the v1.2 pair remark into a formal statement: no
  $\sigma_{\mathrm{pair}}$-carrying growth process is defined or derived in the corpus; the
  doubling has no carrier in any native growth identity.
- **[T5] exponent-coordinate failure**: $\alpha$ is defined against $p$, $\delta$ against $n$;
  $\alpha = \delta/\beta$; the identification $\alpha = \delta$ holds only in the reduced filling
  model $p(n) = n$, false natively; frozen-algebra self-consistency check
  ($1/(\alpha_R + 1 - \theta_p) = D - \delta_c$).
- **Partial O14/O15 resolution**: the $(D{-}1)$ shell factor is the boundary term, additive, never
  inside a reciprocal; constant $q$-normalisation is amplitude-only for intra-$q$ slopes; the
  inter-$q$ $\log q/\log n^*$ estimator layer is explicitly NOT reached.
- **$n$ vs $n{+}1$ estimator bias**: exact OLS inflation factors 1.13/1.10/1.08 on windows
  $[3,19]/[5,19]/[8,19]$; conditional on actual per-$q$ fit windows; value-level consequence
  ($7.44 \mapsto \approx 6.6$–$6.9$ in the papers' $n$-definition) stated as conditional.
- **Regime scoping** via the CC-note isometry lemma ($q > 2\Gamma(n)+1$): $q \ge 307$ windows
  cleanly pre-wrap; top of the O16 range ($q \gtrsim 191$) pre-wrap on $n \le 19$; small-$q$ end
  straddles (e.g. $q = 29$ wraps outright by $|B_{16}| > 29^3$).
- **Three-way separation** (discussion): native law / published conditional transfer /
  phenomenological coincidence-check — the transfer's status after Outcome C is its ceiling.

## 4. Editorial disciplines (binding)

- Current-result-only: v2.0 states its results as THE results; no chronological language, no
  narration of what v1.2 claimed; version history belongs to Zenodo release notes.
- No existing `\label` changed; surgical edits from the v1.2 tex; structure extended, not rebuilt.
- Epistemic labels on every claim (proved / structural / conditional / open); the [T1] no-go
  scoped to the two corpus realisations; no impossibility overclaim anywhere.
- No physics overclaim in title/abstract; abstract ≤ 1 page with keywords, no `\cite` in
  abstract; conceptual/interpretive dimension labelled in abstract AND conclusion (interpretive
  outlook subsection); result-first title (Jérôme's proposed title satisfies this).
- Non-reinjection: no adapted formula substituted into the $\beta^*$ relation; no claim about the
  numerical value of $\beta^*$; Remark beta-category (v1.2) retained.
- Neighbouring-literature positioning kept proportionate (working paper): growth of groups /
  isoperimetry sources properly attributed (CSC not oversold).
- Bibliography: `title = {{...}}` double braces; concept DOIs for corpus refs; external primary
  sources web-verified before deposit.

## 4b. Logged deviations from the plan (referee cycle, 22 Jul 2026)

- [T4] remains a calibrated Remark (`rem:pair`) rather than being upgraded to a formal proposition
  environment; content and corpus-scoping are per the closure report (referee F7b, accepted).
- The referee's blocking finding F1 (unit bound of the identity lemma vs the sampled multi-vector
  production observable, a v1.2-inherited inconsistency) is resolved by scoping the unit bound to the
  one-fingerprint-per-vertex object (new `rem:sampled`), a head-shell disclosure in the numerics section,
  and `sampled` qualifiers on the two $r$-based illustrations; committed data, script, figure and all
  fitted-window numbers are unchanged (conservation clause holds).
- `lem:theta` is restated in two proved parts (dyadic average via Pansu; exact enumerated-range constants)
  plus a `supported, not needed` remark for the pointwise asymptotic (referee F2).

## 5. Conservation clause

`code/span_growth_reproduce.py`, `data/` (8 npz + provenance), and
`figures/effective_exponent_crossing.pdf` are KEPT as-is unless a demonstrated necessity arises
(none anticipated: the new material is analytic; the exact sphere constants are already reproduced
by the committed code path and the CC-note enumeration). NO new numerical campaign; any new figure
must be generated by a committed script from committed data and justified during review. The
estimator-bias factors are exact arithmetic (reproducible in-text or as a ≤10-line committed
addendum to the reproduction script if the referee requires it — decision deferred to review).

## 6. Process gates (in order)

1. THIS protocol + plan reviewed by Jérôme → go.
2. Drafting on branch `2.0` (surgical edits to `tex/SpanGrowthNote.tex`), full compile cycle
   (pdflatex → bibtex → pdflatex ×2), log filtered for errors AND unresolved refs.
2b. README updated AFTER the manuscript and BEFORE the referee review, so the referee also
   controls the public summary (guard against the SGN v1.2 incident: README wording lagging the
   manuscript, caught only at v1.2).
3. Mandatory referee-style review (independent adversarial pass) on the compiled artefact AND the
   README; surgical patches; re-review of patches.
4. Present the reviewed artefact to Jérôme; EXPLICIT deposit go (the review gate and the deposit
   go are two distinct checkpoints).
5. Release via the `cosmochrony-release` skill: major bump 2.0, dry-run Version audit
   (no `version` field in zenodo.json — verified absent), deposit, PDF archived in root `pdfs/`
   only (per the 22 Jul 2026 preference: no per-paper `pdfs/`), merge into `main`, push.
6. Cascade: program registry (new version + graph if needed), SGN web pages EN+FR
   (`science/spectral/program/span-growth/`), deploy + live-verify; GitHub repo metadata
   (homepage/topics) refreshed if keywords change.

## 7. Plan of the revised note (Jérôme's 9 points → sections)

| # | Jérôme's point | v2.0 section | Base | Action |
|---|---|---|---|---|
| 1 | Native objects and regimes | §2 Setting | v1.2 §2 | EXTEND: regimes (i)/(ii)/(iii), isometry-lemma scoping, the TWO corpus realisations of $p$ (bounded effective valence; span rank) |
| 2 | Exact growth identity | §2.2 Lemma | v1.2 Lemma identity | KEEP (labels intact); add the $\Delta p/\Delta N$ reading |
| 3 | Rigorous status of the classification | §3 | v1.2 Theorem | RESTRUCTURE per sec 2 above: abstract real-weight theorem (kept) + NEW integer-rank window-law proposition + joint-limit remark (constructed or demoted) + no-asymptotic-claims caveat |
| 4 | [T1] no-go, both realisations | §4 (new) | Cor t1 | UPGRADE: contraposition chain, both realisations, fixed-$q$ dimension count; converse disclaimed |
| 5 | Native multiplicative coupling, lost $p^{1/2}$ | §5 (new, absorbs Cor t3 + Rem lps) | Cor t3 | EXTEND: $N^\theta$ coordinate, two-sided $\theta = 3/4$ + window values, BI-carrier absence |
| 6 | [T4] and [T5] failures | §6 (new, absorbs Rem pair) | Rem pair | FORMALISE: [T4] corpus-scoped statement; NEW [T5] proposition + frozen-algebra self-consistency |
| 7 | O14/O15 partial + estimator bias | §7 (new) | — | NEW: intra-$q$ resolution, inter-$q$ layer not reached; exact $(n{+}1)$ OLS factors, conditional |
| 8 | Native law / published transfer / phenomenological coincidence | §8 Consequences | v1.2 §5 | REWRITE: three-way separation; transfer status = ceiling reached |
| 9 | Calibrated conclusion + interpretation | §9 | v1.2 §6 | REWRITE: verdict-first, interpretive outlook subsection, open items ($\delta_\infty$, inter-$q$ estimator layer, joint-limit bridge if demoted) |

Title, abstract, keywords: rewritten for the new scope (title per sec 0; abstract states the
classification with its rigorous status, the transfer no-go with its scope, and the labelled
interpretive reading). Numerical illustration (v1.2 §4) kept with window-scoped wording aligned
to corrective sec 2.
