#!/usr/bin/env python3

import numpy as np

ybus = np.array([
                    [10, -2, -2],
                    [-2, 10, -2],
                    [-2, -2, 10]
                ])

print("ybus:\n", ybus)

is_symmetric = np.array_equal(ybus, ybus.T)
print(f"ybus is symmetrical: {is_symmetric}")

