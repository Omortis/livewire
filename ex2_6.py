#!/usr/bin/env python3

import pandas as pd

df = pd.DataFrame({
    "gen_id": ["GEN_1", "GEN_2", "GEN_3", "GEN_4", "GEN_5", 
               "GEN_6", "GEN_7", "GEN_8", "GEN_9", "GEN_10",
               "GEN_11", "GEN_12"],
    "fuel_type": ["Nuclear", "Coal", "Gas", "Wind", "Solar",
                  "Nuclear", "Coal", "Gas", "Wind", "Solar", 
                  "Coal", "Wind"],
    "capacity": [1000, 500, 400, 200, 100, 
                 2000, 1000, 800, 400, 200, 
                 650, 50]
})

report = df.groupby("fuel_type")["capacity"].agg(["sum", "mean", "count"])

print(f"input generator data:\n{df}\n")
print(f"generator fleet analysis:\n{report}")
