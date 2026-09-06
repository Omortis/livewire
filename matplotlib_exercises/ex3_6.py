#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng()

# Hourly indices: 0–23
hours = np.arange(24)

fig, axes = plt.subplots(2, 2)

# Generate 5 generator types
coal = rng.uniform(100, 300, 24)
gas = rng.uniform(50, 150, 24)
nuclear = rng.uniform(280, 300, 24)
wind = rng.uniform(0, 200, 24)
solar = rng.uniform(0, 100, 24)
total_gen = coal + gas + nuclear + wind + solar

axes[0, 0].plot(hours, total_gen)

axes[0, 0].set_xlabel("Hour")
axes[0, 0].set_ylabel("Load (MW)")
axes[0, 0].set_title("Load")

fuel_types = ["Nuclear", "Coal", "Gas", "Wind", "Solar"]
capacity = [1000, 500, 400, 200, 100]

axes[0, 1].barh(fuel_types, capacity, align='center')
axes[0, 1].yaxis.set_inverted(True)  # arrange data from top to bottom
axes[0, 1].set_xlabel('Capacity (MW)')
axes[0, 1].set_title('Capacity By Fuel Type')

scatter_hours = np.arange(1000)

# Same daily sinusoid, repeating every 24 hours
daily_cycle = np.sin((scatter_hours % 24 - 8) * np.pi / 12)

# Base demand: 500 MW average, ±100 MW daily swing, plus random noise
demand = 500 + 100 * daily_cycle + rng.normal(0, 20, 1000)

# Generation tracks demand closely (grid must balance), small random imbalance
generation = demand + rng.normal(0, 10, 1000)

# Time-of-day category for coloring
time_of_day = np.where(
    (scatter_hours % 24 < 6), "Night",
    np.where((scatter_hours % 24 < 12), "Morning",
    np.where((scatter_hours % 24 < 18), "Afternoon", "Evening"))
)

price = 20 + 0.05 * demand + rng.normal(0, 5, 1000)
# At 500 MW demand → ~$45/MWh
# At 700 MW demand → ~$55/MWh

for tod, color in [("Morning", "orange"), ("Afternoon", "red"), ("Evening", "blue"), ("Night", "gray")]:
    mask = time_of_day == tod
    axes[1, 0].scatter(demand[mask], price[mask], c=color, label=tod, alpha=0.5, s=10)


axes[1, 0].set_xlabel("Demand (MW)")
axes[1, 0].set_ylabel("Price ($/MWh)")
axes[1, 0].set_title("Price vs Demand")
axes[1, 0].grid(True)

axes[1, 1].axis('off')

fig.suptitle("System Status")
fig.tight_layout()

plt.show()