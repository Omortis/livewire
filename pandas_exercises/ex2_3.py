#!/usr/bin/env python3

import pandas as pd
import numpy as np

rng = np.random.default_rng()

df = pd.DataFrame({"hour": range(100), "load_mw": rng.normal(500, 100, 100)})

threshold_90_percent = df["load_mw"].quantile(0.90)
high_load = df[df["load_mw"] > threshold_90_percent]
top_10 = df.nlargest(10, "load_mw")

print(f"90th percentile load value: {threshold_90_percent:.2f}")
print(f"Rows above the 90th percentile:\n{high_load}")
print(f"Top 10 loads:\n{top_10}")
