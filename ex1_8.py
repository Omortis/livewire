#!/usr/bin/env python3

import numpy as np

rng = np.random.default_rng()

μ = 200  # MW
σ = 30  # MW

scenarios = 10000
zones = 5
zone_loads = rng.normal(μ, σ, (scenarios, zones))
scenario_totals = np.sum(zone_loads, axis=1)
zone_total_mean = np.mean(scenario_totals)
zone_total_std_dev = np.std(scenario_totals)
total_load_gt_1100_prob = np.sum(scenario_totals > 1100) / 10000

print(f"Total system load mean       : {zone_total_mean:.3f} MW")
print(f"Total system load std dev    : {zone_total_std_dev:.3f} MW")
print(f"Prob for total load > 1100 MW: {total_load_gt_1100_prob:.3f}")
