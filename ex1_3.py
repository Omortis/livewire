#!/usr/bin/env python3

import numpy as np

V = np.array([1.0, 1.02, 0.98])  # voltage
angle = np.array([0, 0.1, -0.05])  # radians
I = np.array([1 + 0.5j, 0.8 - 0.2j, 1.2 + 0.3j])  # current

I_conj = np.conjugate(I)

V_complex = V * np.exp(1j * angle)

S_complex = V_complex * I_conj

print("V          : ", V)
print("V_complex  : ", V_complex)
print("I          : ", I)
print("I conjugate: ", I_conj)
print("S_complex  : ")
for complex_power in S_complex:
    print(f"\tP: {complex_power.real:6.3f} \tQ: {complex_power.imag:6.3f}")
