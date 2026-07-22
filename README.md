# Native Span Growth from Capacity Decay and the Failure of the Heisenberg Capacity-to-Rate Transfer

**A Three-Branch Classification with Its Rigorous Status, and the Substrate No-Go for the Expander-Derived
Cascade-Exponent Law**

Cosmochrony working paper (spectral admissibility sub-programme).
Cite via the Zenodo concept DOI: [10.5281/zenodo.21480521](https://doi.org/10.5281/zenodo.21480521).

## Result

On the breadth-first cascade of the Heisenberg Cayley graph, the cumulative fingerprint span $r(n)$ obeys the
exact increment identity $\Delta r(n) = \sigma_c(n)\,|S_n|$, where $\sigma_c(n)$ is the measured block
capacity and $|S_n|$ the exact BFS sphere, with homogeneous dimension $D = 4$ (Bass--Guivarc'h).
For real-valued weight sequences with power-law decay $\sigma_c(n) \sim a\,n^{-\delta_c}$, summation yields a
complete three-branch classification depending only on $(\delta_c, D)$:

- $\delta_c < D$: polynomial span growth $r(n) \sim n^{D-\delta_c}$ (growth branch,
  $\beta_{\mathrm{Heis}} = D - \delta_c$);
- $\delta_c = D$: logarithmic growth $r(n) \sim \log n$ (marginal branch);
- $\delta_c > D$: saturation $r_\infty - r(n) \sim n^{-(\delta_c - D)}$ (strictly for $\delta_c > D$).

Because the measured increments are integers, the pointwise power-law hypothesis is unrealizable whenever
$\delta_c > D - 1$ --- a range that includes the measured windows --- and the classification reaches the
measured rank only through an exact finite-window formulation with two-sided bounds
($a_\pm$, $\kappa_\pm$ sandwiching $r(n) - r(m)$ by $\sum k^{D-1-\delta_c}$).
Every numerical exponent statement is window-scoped, and no joint large-$q$ limit is claimed.

The expander-derived conversion law $\beta = 1/(\delta + \tfrac{1}{2})$ does not transfer to the substrate on
which the capacities are measured.
The no-go has three independent legs, each scoped to the constructions the corpus defines:

1. **No valence--exploration proportionality**: proportionality forces a vanishing capacity exponent, and it
   fails for both native realisations of the LPS valence --- outright at fixed $q$ by the dimension count
   $r(n) \le q$ against $|B_n| \to q^3$.
2. **No square-root frontier, no native flux carrier**: the native frontier is a power of the explored
   volume, $|S_n| \asymp |B_n|^{3/4}$ (two-sided), not of the achieved span; no uniform constant restores
   the $\sqrt{r}$ form for $D > 2$, and the bounded-flux constant $c_{\mathrm{BI}}$ has no native carrier
   because the explored volume is autonomous on a fixed graph.
3. **Pair and coordinate obstructions**: no native growth process carrying
   $\sigma_{\mathrm{pair}} = \sigma_c \sigma_{q-c}$ is defined or derived in the corpus, and the exponent
   coordinates of the conversion law ($\alpha$ against valence, $\delta$ against shell index) coincide only
   in the reduced filling model $p(n) = n$, which fails natively.

The separation-of-variables algebra itself is coordinate-honest: with the native inputs it returns the
growth-branch map $\beta_{\mathrm{Heis}} = D - \delta_c$.
On the block-level side, the shell-growth factor $D - 1$ is the native boundary term (additive, never inside
a reciprocal), intra-window slopes are invariant under constant normalisations, and fitting against the
shifted logarithm $\log(n{+}1)$ inflates exponents by a computable 8--13% on the production windows; the
inter-$q$ estimator layer is left untouched.
The window-effective exponents of the production data make contact near $q = 211$ and separate strictly for
$q \ge 307$: the contact is a transitional crossing, with the asymptotic value of $\delta_c$, and hence the
asymptotic branch, left open.
The polynomial span exponent is explicitly distinguished from the exponential per-shell rate carried by
$\beta^*$ in the projected-Yukawa mass factorisation.

## Repository layout

- `tex/` — LaTeX source (`SpanGrowthNote.tex`) and bibliographies
- `code/` — `span_growth_reproduce.py`, the single reproduction script
- `data/` — compact copies of the block-level observables actually used (frozen windows and per-checkpoint
  provenance in `data/provenance.json`; about 47 kB total)
- `figures/` — `effective_exponent_crossing.pdf`, produced by the script (PDF only)
- `compile.sh` — full compile cycle (`pdflatex -> bibtex -> pdflatex x2`) into `out/` (generated, git-ignored)
- `zenodo.json` — publication metadata (concept DOI)

## Reproducing the numerical results

From the repository root, with `numpy` and `matplotlib` installed:

```bash
python code/span_growth_reproduce.py
```

This recomputes the exact spheres of $\mathrm{Heis}_3(\mathbb{Z})$, every window-effective exponent of the
paper's table (with the bootstrap standard errors of the $q \ge 307$ rows reproduced exactly under the
documented seed), the 27 window-shift and knee-trimming robustness variants, the $\log(n{+}1)$ convention
check, and regenerates `figures/effective_exponent_crossing.pdf`.

## Context

Web page: <https://cosmochrony.org/science/spectral/program/span-growth/>.
Part of the Cosmochrony research programme; see the programme registry for the full dependency structure.
