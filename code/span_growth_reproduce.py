"""Reproduce every numerical result and the figure of the Span-Growth Note.

Run from the repository root:

    python code/span_growth_reproduce.py

Inputs:  data/q{29,61,101,151,211,307,401,601}_blocks.npz (compact block-level observables;
         provenance and frozen windows in data/provenance.json).
Outputs: all numbers quoted in the note (printed), and
         figures/effective_exponent_crossing.pdf (the only figure format is PDF).

Conventions: log-log fits against log n (the note's convention); the campaign's log(n+1)
variant is reported for the robustness check. Only exponents are used, never amplitudes.
Bootstrap: 2000 resamples over conjugate pair-blocks, seed 20260721 (the frozen-audit seed).
"""

import json
import os
from collections import deque

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

DATA = os.path.join(os.path.dirname(__file__), "..", "data")
FIGS = os.path.join(os.path.dirname(__file__), "..", "figures")
PRIMES = (29, 61, 101, 151, 211, 307, 401, 601)
NBOOT = 2000
SEED = 20260721


def exact_spheres(nmax=22):
    """Exact BFS of Heis_3(Z), generators {X^+-1, Y^+-1} (CC-note convention)."""
    dist = {(0, 0, 0): 0}
    frontier = deque([(0, 0, 0)])
    s = [1]
    while len(s) <= nmax:
        nxt = deque()
        for (a, b, g) in frontier:
            for v in ((a + 1, b, g), (a - 1, b, g), (a, b + 1, g + a), (a, b - 1, g - a)):
                if v not in dist:
                    dist[v] = len(s)
                    nxt.append(v)
        s.append(len(nxt))
        frontier = nxt
    return np.array(s, dtype=float)


def loglog_slope(x, y):
    return np.polyfit(np.log(x), np.log(y), 1)[0]


def window_fits(d, n0, n1, use_np1=False):
    """(delta_c_eff, D_eff, beta_r_eff) on [n0, n1] from a compact data file."""
    ns = d["ns"].astype(float)
    S = d["shell_sizes"].astype(float)
    sig = np.nanmean(d["sigma_c_mean"], axis=0)
    r = np.cumsum(sig * S)
    N = np.cumsum(S)
    w = (ns >= n0) & (ns <= n1)
    x = ns[w] + 1.0 if use_np1 else ns[w]
    return (-loglog_slope(x, sig[w]), loglog_slope(x, N[w]), loglog_slope(x, r[w]))


def bootstrap_se(d, n0, n1, rng):
    """Bootstrap SE of delta_c_eff over pair-blocks."""
    ns = d["ns"].astype(float)
    S = d["shell_sizes"].astype(float)
    sig = d["sigma_c_mean"]
    K = sig.shape[0]
    w = (ns >= n0) & (ns <= n1)
    ln = np.log(ns[w])
    boots = np.empty(NBOOT)
    for b in range(NBOOT):
        m = np.nanmean(sig[rng.integers(0, K, K)], axis=0)
        boots[b] = -np.polyfit(ln, np.log(m[w]), 1)[0]
    return boots.std(ddof=1)


def main():
    # Part A: exact substrate facts
    s = exact_spheres(22)
    B = np.cumsum(s)
    ns = np.arange(23)
    tail = slice(10, 23)
    print("=== exact spheres of Heis_3(Z) ===")
    print(f"s_22 = {int(s[22])}   |B_22| = {int(B[22])}   (published: 16934, 99689)")
    print(f"|S_n| ~ n^{loglog_slope(ns[tail], s[tail]):.2f}   |B_n| ~ n^{loglog_slope(ns[tail], B[tail]):.2f}"
          f"   (published: 3.10, 3.99)")
    print(f"isoperimetric n*(|S_n|/|B_n|) in "
          f"[{(ns[tail]*s[tail]/B[tail]).min():.2f}, {(ns[tail]*s[tail]/B[tail]).max():.2f}]  (~3.5/n)")
    print(f"no-go factor |S_n|/sqrt(|B_n|) ~ n^{loglog_slope(ns[tail], s[tail]/np.sqrt(B[tail])):.2f}"
          f"   (published: 1.11)")

    # Part B: window-effective exponents (the note's table) + bootstrap SEs.
    # The note quotes bootstrap SEs for q >= 307; they are reproduced EXACTLY by consuming a
    # dedicated rng (seed 20260721) in the frozen-audit order 307, 401, 601. The remaining
    # primes get figure-only error bars from an independent stream (seed 20260722).
    rng_pub = np.random.default_rng(SEED)
    rng_fig = np.random.default_rng(SEED + 1)
    rows, ses = {}, {}
    loaded = {q: np.load(os.path.join(DATA, f"q{q}_blocks.npz")) for q in PRIMES}
    for q in (307, 401, 601):
        d = loaded[q]
        ses[q] = bootstrap_se(d, int(d["n0"]), int(d["n1"]), rng_pub)
    print("\n=== window-effective exponents (table of the note) ===")
    for q in PRIMES:
        d = loaded[q]
        n0, n1 = int(d["n0"]), int(d["n1"])
        dc, De, br = window_fits(d, n0, n1)
        if q not in ses:
            ses[q] = bootstrap_se(d, n0, n1, rng_fig)
        rows[q] = (n0, n1, dc, De, br)
        tag = "" if q < 307 else "   [SE as published]"
        print(f"q={q:>3} [{n0},{n1}]  delta_c_eff = {dc:6.3f} +/- {ses[q]:.3f}   D_eff = {De:5.3f}"
              f"   beta_r_eff = {br:5.3f}   gap = {dc - De:+.3f}{tag}")

    # Part C: robustness — 27 window/knee variants and the log(n+1) convention
    print("\n=== robustness (q >= 307): window shifts, knee trimming, log(n+1) ===")
    all_neg = True
    for q in (307, 401, 601):
        d = np.load(os.path.join(DATA, f"q{q}_blocks.npz"))
        n0, n1 = int(d["n0"]), int(d["n1"])
        gaps = []
        for a in (n0 - 1, n0, n0 + 1):
            for b in (n1 - 2, n1 - 1, n1):
                if b - a < 4 or a < 2:
                    continue
                dc, De, _ = window_fits(d, a, b)
                gaps.append(dc - De)
        dc1, De1, _ = window_fits(d, n0, n1, use_np1=True)
        all_neg &= all(g < 0 for g in gaps)
        print(f"q={q}: {sum(g < 0 for g in gaps)}/{len(gaps)} variants negative, "
              f"range [{min(gaps):+.3f}, {max(gaps):+.3f}];  log(n+1) gap = {dc1 - De1:+.3f}")
    print(f"sign stable across all variants: {'YES' if all_neg else 'NO'}")

    # Figure: two panels
    qs = np.array(PRIMES, dtype=float)
    dcs = np.array([rows[q][2] for q in PRIMES])
    Des = np.array([rows[q][3] for q in PRIMES])
    errs = np.array([ses[q] for q in PRIMES])
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.2, 3.6))
    ax1.errorbar(qs, dcs, yerr=errs, fmt="o-", capsize=3, label=r"$\delta_c^{\mathrm{eff}}$")
    ax1.plot(qs, Des, "s--", label=r"$D_{\mathrm{eff}}$")
    ax1.axvline(211, color="grey", lw=0.8, ls=":")
    ax1.set_xscale("log")
    ax1.set_xlabel(r"$q$")
    ax1.set_ylabel("window-effective exponent")
    ax1.legend(frameon=False)
    ax1.set_title("(a) contact near $q=211$")
    ax2.errorbar(qs, dcs - Des, yerr=errs, fmt="o-", capsize=3, color="C3")
    ax2.axhline(0.0, color="k", lw=0.8)
    ax2.axvline(211, color="grey", lw=0.8, ls=":")
    ax2.set_xscale("log")
    ax2.set_xlabel(r"$q$")
    ax2.set_ylabel(r"$\delta_c^{\mathrm{eff}} - D_{\mathrm{eff}}$")
    ax2.set_title("(b) transitional crossing, then separation")
    fig.tight_layout()
    out = os.path.join(FIGS, "effective_exponent_crossing.pdf")
    fig.savefig(out)
    print(f"\nfigure written: {os.path.relpath(out)}")


if __name__ == "__main__":
    main()
