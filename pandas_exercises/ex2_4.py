#!/usr/bin/env python3

import pandas as pd
import numpy as np

rng = np.random.default_rng()

samples = 30*24 # 30 days, 24 hours

timestamps = pd.date_range(start='2026-09-01', periods=samples, freq='h')

df = pd.DataFrame(
    {
        "coal": rng.uniform(100, 300, samples),
        "gas": rng.uniform(20, 80, samples),
        "nuclear": rng.uniform(280, 300, samples),
        "wind": rng.uniform(0, 200, samples),
        "solar": rng.uniform(0, 100, samples), # should be a half-sine wave repeated daily
    },
    index = timestamps
)

# https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#dateoffset-objects
daily_mean = df.resample("D").mean()
daily_total = df.resample("D").sum().sum(axis=1)

print(f"daily_mean:\n{daily_mean.round(2)}\n")
print(f"daily_total:\n{daily_total.round(2)}")
