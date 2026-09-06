#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

fuel_types = ["Nuclear", "Coal", "Gas", "Wind", "Solar"]
capacity = [1000, 500, 400, 200, 100]

fig, ax = plt.subplots()

ax.barh(fuel_types, capacity, align='center')
ax.yaxis.set_inverted(True)  # arrange data from top to bottom
ax.set_xlabel('Capacity (MW)')
ax.set_title('Capacity By Fuel Type')

for i, cap in enumerate(capacity):
    ax.text(cap + 20, i, f"{cap} MW", va='center', ha='left')

plt.show()