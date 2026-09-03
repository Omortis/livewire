#!/usr/bin/env python3

import pandas as pd

gen_info = pd.DataFrame({
    "gen_id": ["GEN_1", "GEN_2", "GEN_3"],
    "fuel_type": ["Nuclear", "Gas", "Coal"],
    "heat_rate": [10.5, 7.2, 9.8]  # MMBtu per MWh
})

fuel_prices = pd.DataFrame({
    "fuel_type": ["Nuclear", "Gas", "Coal"],
    "price_per_mmbtu": [0.5, 3.5, 2.0],  # $ per MMBtu
    "date": ["2024-01-01", "2024-01-01", "2024-01-01"]
})

generation = pd.DataFrame({
    "gen_id": ["GEN_1", "GEN_1", "GEN_2", "GEN_2", "GEN_3", "GEN_3"],
    "hour": [1, 2, 1, 2, 1, 2],
    "output_mwh": [500, 520, 300, 310, 400, 410]
})

fuel_type_heat_rate_merge = gen_info.merge(generation, on="gen_id")

full_merge = fuel_type_heat_rate_merge.merge(fuel_prices, on=["fuel_type"])

full_merge["cost_per_hour"] = full_merge["output_mwh"] * full_merge["heat_rate"] * full_merge["price_per_mmbtu"]

total_system_cost = full_merge.groupby("date")["cost_per_hour"].sum()

print(f"full_merge (before grouping):\n{full_merge}\n")

print(f"total_system_cost:\n{total_system_cost}")

