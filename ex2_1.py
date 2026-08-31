#!/usr/bin/env python3

import pandas as pd

# These are ballpark realistic for a simplified system. Nuclear is cheap
# but inflexible, coal is mid-cost, gas is expensive but flexible, wind/solar
# have near-zero marginal cost.

df = pd.DataFrame(  
    {
        "bus_id": [1, 2, 3, 4, 5],
        "gen_id": ["GEN_1", "GEN_2", "GEN_3", "GEN_4", "GEN_5"],
        "p_max": [1000, 500, 400, 200, 100],
        "p_min": [500, 100, 50, 0, 0],
        "fuel_type": ["Nuclear", "Coal", "Gas", "Wind", "Solar"],
        "cost_per_mwh": [25.00, 35.00, 45.00, 0.00, 0.00],
    }
)

print(df.to_string(float_format=lambda x: f"{x:.2f}"))
