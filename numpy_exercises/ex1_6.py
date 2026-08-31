#!/usr/bin/env python3

import numpy as np

# Line Flow Ranges
#        System Type         Typical Line Flow (MVA)  Typical Line Rating
# -----------------------------------------------------------------------
# Distribution Feeders	     1 – 10 MVA               5 - 30 MVA
# Major Transmission Lines	 100 – 1,000 MVA          100 - 1200 MVA

line_flows_mva = np.array([120, 180, 250, 480, 400, 500, 650, 1000, 1000, 1400])
line_ratings_mva = np.array([200, 300, 400, 500, 600, 750, 900, 1100, 1400, 1800])

loading_percent = (line_flows_mva / line_ratings_mva) * 100

overloaded_idx = np.where(loading_percent > 90)[0]
overloaded_pct = loading_percent[overloaded_idx]

print("Line flows   (MVA):")
print(f"\t{line_flows_mva}")
print("Line ratings (MVA):")
print(f"\t{line_ratings_mva}")
print("Line loadings:")
print(f"\t{np.round(loading_percent, decimals=2)}")
print("Indices of overloaded lines:")
print(f"\t{overloaded_idx}")
print("Overloaded percents:")
print(f"\t{np.round(overloaded_pct, decimals=2)}")
