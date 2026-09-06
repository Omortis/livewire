#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng()

# Hourly indices: 0–23
hours = np.arange(24)

# Base sinusoidal pattern: low at night (0–5), peak afternoon (14–18), dip evening
# np.sin gives -1 to 1; we shift/scale to match load range
base = 200 + 80 * np.sin((hours - 8) * np.pi / 12)  # shift peak to ~14:00

lines = ["L1", "L2", "L3", "L4", "L5"]
power_flow = np.empty((5, 24))
for i in range(5):
    # Add random noise ±20 MVA
    noise = rng.uniform(-20, 20, 24)
    power_flow[i, :] = base + noise

fig, ax = plt.subplots()
# Create the heatmap
im = ax.imshow(power_flow, cmap='viridis', aspect='auto')

# Add colorbar — this is the "legend" for the color scale
cbar = fig.colorbar(im, ax=ax)
cbar.set_label('Power Flow (MW)')

# Show all ticks and label them with the respective list entries
ax.set_xticks(range(24), labels=hours)
ax.set_yticks(range(len(lines)), labels=lines)
ax.set_xlabel("Hour")
ax.set_ylabel("Line")
ax.set_title("Hourly Power Flow Over 5 Lines (MW)")
fig.tight_layout()
plt.show()