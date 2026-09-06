#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng()

# Hourly indices: 0–23
hours = np.arange(24)

# Base sinusoidal pattern: low at night (0–5), peak afternoon (14–18), dip evening
# np.sin gives -1 to 1; we shift/scale to match load range
base = 200 + 80 * np.sin((hours - 8) * np.pi / 12)  # shift peak to ~14:00

# Add random noise ±20 MW
noise = rng.uniform(-20, 20, 24)
load_data = base + noise

# Ensure no negative values
load_data = np.maximum(load_data, 50)

plt.plot(hours, load_data, label="load_data")
plt.plot(hours, base, linestyle='--', alpha=0.7, label="ideal pattern")
plt.ylabel("Load (MW)")
plt.xlabel("Hour")
plt.title("Daily Load Profile")
plt.grid(True)
plt.legend()
plt.show()