# Minimal Ring Frustration Model

**First public timestamp**: 16 February 2026  
**Author**: David Schoemaker  
**X / Twitter**: [@davejing26](https://x.com/davejing26)  
**Location**: Adelaide, South Australia

## Summary

A minimal 1D ring model of N sites with states in ℤ_q, random targets, and strictly local single-site Metropolis updates under conserved modular constraint.

Key findings:
- Persistent algebraic frustration floor: E/N ∼ 1/q (effective exponent α_eff stabilizes at 1.00)
- Temperature gradients suppress the floor by 40–45% vs uniform T
- Parallel tempering outperforms annealing and greedy descent (reaches E ≤ 1 in ~18% of trials vs 9% vs 0%)
- Small 2-level nested ring proof-of-concept shows measurable floor reduction
The apparent persistent algebraic frustration floor (E/N ∼ 1/q) in the minimal modular ring model is not topological or structural. It arises solely from inefficient Metropolis dynamics using global random proposals, which become trapped far from equilibrium at large q. Local ±1 updates eliminate the floor completely — the system relaxes to near-zero energy even under forced twists or neighbor couplings — demonstrating that the residual was a dynamical artifact of the update rule, not a fundamental property of the model.
All results are reproducible from the code provided.

## Core Files

- `paper.md` — Full paper draft (markdown version)
- `ring_model.py` — Core single-site Metropolis model
- `gradient_model.py` — Temperature gradient version
- `parallel_tempering.py` — Parallel tempering implementation
- `tables/` — All result tables (markdown format)

## Reproducibility

- Python 3 + numpy, tqdm
- Seed: 42 (set in all scripts)
- 200,000 steps per trial unless otherwise noted
- 500 trials per T value in sweeps (reduced for large N/q)
  
## License

Public domain / CC0 — use freely, but please cite if used in academic work.

Contact: @davejing26 on X

Last updated: 16 February 2026
