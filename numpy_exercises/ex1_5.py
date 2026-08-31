#!/usr/bin/env python3

import numpy as np

# The B matrix (susceptance):
#   - A simplified version of the Y-bus from Exercise 1.2
#   - Diagonal = sum of line susceptances connected to that bus
#   - Off-diagonal = negative of the line susceptance between those buses
#
# For a 3-bus system with lines 1-2, 2-3, and 1-3:

B = np.array([[15, -10, -5], [-10, 20, -10], [-5, -10, 15]])

# The P vector (power injections):
#   - Positive = generation supplying power
#   - Negative = load consuming power
#   - Sum of all P must equal zero (conservation of energy)
#
# Bus 1 generates 100 MW, Buses 2&3 each consume 50 MW:

P = np.array([1.0, -0.5, -0.5])

# Solve for the bus angles θ in B × θ = P

θ = np.linalg.solve(B, P)

print("Solve for the bus angles θ in B x θ = P.\n")
print("B (susceptance):")
print(B)
print("\nP (real power injections):")
print(P)
print("\nBus Angles:")
print(θ)
print("\nVerification (B @ θ):")
print(B @ θ)
