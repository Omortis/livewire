#!/usr/bin/env python3

import numpy as np

# Generator sizes by type:
# - Base load (e.g., coal/nuclear): 100–300 MW (1.0–3.0 pu)
# - Mid-merit (e.g., combined cycle gas): 50–150 MW (0.5–1.5 pu)
# - Peaker (e.g., gas turbine): 20–80 MW (0.2–0.8 pu)

# Three generators, 24 hours each
gen1 = np.random.uniform(100, 300, 24)  # base load
gen2 = np.random.uniform(50, 150, 24)  # mid-merit
gen3 = np.random.uniform(20, 80, 24)  # peaker

P_mw = np.array([gen1, gen2, gen3])
base_power = 100.0  # MVA
P_mw_broadcast = P_mw / base_power

print("P_mw.shape:")
print(P_mw.shape)
print("P_mw:")
print(P_mw)
print("P_mw_broadcast:")
print(P_mw_broadcast)
