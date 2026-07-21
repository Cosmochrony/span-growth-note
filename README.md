# Capacity Decay Determines Span-Growth Universality on Heisenberg Graphs

**A Three-Branch Classification, and the Substrate Dependence of the Cascade-Exponent Law**

Cosmochrony working paper (spectral admissibility sub-programme).
Cite via the Zenodo concept DOI: [10.5281/zenodo.21480521](https://doi.org/10.5281/zenodo.21480521).

## Result

On the breadth-first cascade of the Heisenberg Cayley graph, the cumulative fingerprint span $r(n)$ obeys the
exact increment identity $\Delta r(n) = \sigma_c(n)\,|S_n|$, where $\sigma_c(n) \sim a\,n^{-\delta_c}$ is the
measured block capacity and $|S_n| \sim \kappa\,n^{D-1}$ the exact BFS sphere, with homogeneous dimension
$D = 4$ (Bass--Guivarc'h).
Asymptotic summation yields a complete three-branch classification depending only on $(\delta_c, D)$:

- $\delta_c < D$: polynomial span growth $r(n) \sim n^{D-\delta_c}$ (growth branch,
  $\beta_{\mathrm{Heis}} = D - \delta_c$);
- $\delta_c = D$: logarithmic growth $r(n) \sim \log n$ (marginal branch);
- $\delta_c > D$: saturation $r_\infty - r(n) \sim n^{-(\delta_c - D)}$ (strictly for $\delta_c > D$).

Two analytic corollaries delimit the expander-derived cascade-exponent law
$\beta = 1/(\delta + \tfrac{1}{2})$:

1. **No valence--exploration proportionality**: $r(n)/|B_n| \to 0$ for every $\delta_c > 0$ — the closure
   hypothesis of the LPS growth equation does not transpose to this substrate.
2. **No uniform square-root frontier**: since $r(n) \le |B_n|$, any uniform constant in
   $\Delta r \le c\,\sigma_c\sqrt{r}$ must exceed $|S_n|/\sqrt{|B_n|} \asymp n^{D/2-1}$, which diverges for
   every polynomial growth dimension $D > 2$.

The additive $\tfrac{1}{2}$ of the cascade-exponent law is thereby identified as expander-specific; the
Heisenberg capacity-to-growth map on the growth branch is $\beta_{\mathrm{Heis}} = D - \delta_c$.
The window-effective exponents of the production data ($q \le 211$) sit near the marginal boundary
$\delta_c \approx D$ — recorded as an observation about window-effective exponents, with the asymptotic
branch left open.
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
