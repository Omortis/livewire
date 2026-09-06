#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng()

# Hourly indices: 0–23
hours = np.arange(24)

# Three buses with slight voltage variations around 1.0 pu
bus1 = 1.0 + rng.uniform(-0.03, 0.03, 24)
bus2 = 1.0 + rng.uniform(-0.02, 0.04, 24)
bus3 = 1.0 + rng.uniform(-0.04, 0.02, 24)

plt.plot(hours, bus1, 'b-', label="Bus 1")
plt.plot(hours, bus2, 'r--', label="Bus 2")
plt.plot(hours, bus3, 'g:', label="Bus 3")

plt.axhline(1.05, color='red', linestyle='--', alpha=0.5, label="+5% limit")
plt.axhline(0.95, color='blue', linestyle='--', alpha=0.5, label="-5% limit")

plt.xlabel("Hour")
plt.ylabel("Voltage (pu)")
plt.title("Voltage Profile Comparison")
plt.legend()
plt.grid(True)
plt.show()