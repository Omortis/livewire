#!/usr/bin/env python3

import numpy as np

rng = np.random.default_rng()

μ = 500  # MW
σ = 100
# 8760 hours = 365 days × 24 hours
hours = 365 * 24

# hourly load demand (MW)
s_mw = rng.normal(μ, σ, hours)

print(f"Sample count   : {s_mw.size:8}")
print(f"Mean           : {np.mean(s_mw):8.2f}")
print(f"Std Dev        : {np.std(s_mw):8.2f}")
print(f"Minimum        : {np.min(s_mw):8.2f}")
print(f"Maximum        : {np.max(s_mw):8.2f}")
print(f"95th percentile: {np.percentile(s_mw, 95):8.2f}")
print(f"Hours > 700 MW : {np.sum(s_mw > 700):8}")
