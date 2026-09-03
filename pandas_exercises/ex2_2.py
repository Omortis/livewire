#!/usr/bin/env python3

import pandas as pd
import numpy as np

rng = np.random.default_rng()

# 1. Generate 100 hourly timestamps
timestamps = pd.date_range(start="2024-01-01", periods=100, freq="h")

# 2. Synthetic SCADA data
df = pd.DataFrame(
    {
        "timestamp": timestamps,
        "voltage": rng.uniform(0.95, 1.05, 100),
        "power": rng.uniform(100, 500, 100),
        "frequency": rng.uniform(59.9, 60.1, 100),
    }
)

# Pick 10 random row indices and 10 random column indices (numeric columns only: 1,2,3)
random_rows = rng.integers(0, 100, 10)
random_cols = rng.choice([1, 2, 3], 10)  # column indices

# Introduce NaNs and record WHERE they went
nan_locations = list(zip(random_rows, random_cols))
for r, c in nan_locations:
    df.iloc[r, c] = np.nan

# Now fill and report
df_filled = df.fillna(df.mean(numeric_only=True))
print(f"Number of NaNs imputed: {len(nan_locations)}")
print("Cells imputed:")
for r, c in nan_locations:
    col_name = df_filled.columns[c]
    imputed_value = df_filled.iloc[r, c]
    print(f"  Row {r}, Column '{col_name}', imputed value: {imputed_value:.3f}")
