#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng()

# Hourly indices: 0–23
hours = np.arange(1000)

# Same daily sinusoid, repeating every 24 hours
daily_cycle = np.sin((hours % 24 - 8) * np.pi / 12)

# Base demand: 500 MW average, ±100 MW daily swing, plus random noise
demand = 500 + 100 * daily_cycle + rng.normal(0, 20, 1000)

# Generation tracks demand closely (grid must balance), small random imbalance
generation = demand + rng.normal(0, 10, 1000)

# Time-of-day category for coloring
time_of_day = np.where(
    (hours % 24 < 6), "Night",
    np.where((hours % 24 < 12), "Morning",
    np.where((hours % 24 < 18), "Afternoon", "Evening"))
)

plt.plot([demand.min(), demand.max()], [demand.min(), demand.max()], 'k--', label="gen = demand")

for tod, color in [("Morning", "orange"), ("Afternoon", "red"), ("Evening", "blue"), ("Night", "gray")]:
    mask = time_of_day == tod
    plt.scatter(demand[mask], generation[mask], c=color, label=tod, alpha=0.5, s=10)


plt.xlabel("Power Demand (MW)")
plt.ylabel("Power Generation (MW)")
plt.title("Generation vs Demand")
plt.legend()
plt.grid(True)
plt.show()