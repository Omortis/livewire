#!/usr/bin/env python3

import pandas as pd
import numpy as np

rng = np.random.default_rng()

# Using data similar to previous exercises
df_gen = pd.DataFrame({
    'gen_id': ['GEN_1', 'GEN_2', 'GEN_3', 'GEN_4', 'GEN_5'],
    'fuel_type': ['Nuclear', 'Coal', 'Gas', 'Wind', 'Solar'],
    'capacity': [1000, 500, 400, 200, 100]
})

df_outage = pd.DataFrame({
    'gen_id': ['GEN_1', 'GEN_2', 'GEN_3', 'GEN_1', 'GEN_4'],
    'start_date': ['2024-01-01', '2024-02-15', '2024-03-10', '2024-06-01', '2024-04-20'],
    'end_date': ['2024-01-15', '2024-02-20', '2024-03-12', '2024-06-10', '2024-04-25'],
    'outage_mw': [1000, 500, 400, 1000, 200]
})

merged = df_gen.merge(df_outage, on="gen_id")
merged_summed = merged.groupby("fuel_type")["outage_mw"].sum()

print(f"df_gen:\n{df_gen}")
print(f"df_outage:\n{df_outage}")
print(f"merged:\n{merged}")
print(f"merged_summed:\n{merged_summed}")
