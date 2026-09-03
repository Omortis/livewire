#!/usr/bin/env python3

import pandas as pd

df = pd.DataFrame({
    'contingency_id': ['C1', 'C1', 'C1', 'C2', 'C2', 'C2'],
    'line_id': ['L1', 'L2', 'L3', 'L1', 'L2', 'L3'],
    'pre_flow': [100, 200, 150, 100, 200, 150],
    'post_flow': [110, 220, 140, 105, 210, 160],
    'loading_percent': [55, 88, 70, 52.5, 84, 80]
})

max_loading_percent = df.groupby('line_id')['loading_percent'].agg("max")

print(f"max_loading_percent:\n{max_loading_percent}")
