#!/usr/bin/env python3

import numpy as np

class Transformer:
    """Represents an electrical voltage transformer."""

    def __init__(
        self,
        id: str,
        impedance: complex,
        tap_ratio: float = 1.0
    ):
        """Initialize a new Transformer instance.

        :param tap_ratio: The tap ratio changes the voltage transformation ratio.
        :param impedance: The input impedance for the transformer.
        """

        self._id = id
        self._tap_ratio = tap_ratio
        self._impedance = impedance

    @property
    def impedance(self) -> complex:
        """Read-only transformer impedance."""
        return self._impedance

    @property
    def tap_ratio(self) -> float:
        return self._tap_ratio

    def set_tap_ratio(self, value: float):
        if not (0.9 <= value <= 1.1):
            raise ValueError(f"0.9 <= tap ratio <= 1.1, got {value}")
        self._tap_ratio = value

# Example usage:
if __name__ == "__main__":

    transformer = Transformer(id="OptimusPrime", impedance=0.01+0.08j, tap_ratio=1.0)

    try:
        transformer.impedance = 0.02 + 0.1j
    except AttributeError:
        print("Correctly raised AttributeError (impedance is read-only)")

    try:
        transformer.tap_ratio = 0.95
    except AttributeError:
        print("Correctly raised AttributeError (tap_ratio is read-only)")

    transformer.set_tap_ratio(0.95)

