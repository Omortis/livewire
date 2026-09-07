#!/usr/bin/env python3

import numpy as np

class Bus:
    """Represents an electrical power system bus bar."""

    def __init__(
        self,
        bus_id: int | str,
        voltage: float,
        angle: float,
        load_mw: float,
    ):
        """Initialize a new Bus instance.

        :param bus_id: Unique identifier for the bus (e.g., integer index or name)
        :param voltage: Voltage magnitude (typically in per-unit or kV)
        :param angle: Voltage phase angle (typically in degrees or radians)
        :param load_mw: Real power load connected to the bus in megawatts (MW)
        """
        self.bus_id = bus_id
        self.voltage = voltage
        self.angle = angle
        self.load_mw = load_mw

    def update_voltage(self, new_voltage: float) -> None:
        """Update the voltage magnitude of the bus.

        :param new_voltage: The updated voltage value
        """
        self.voltage = new_voltage

    def update_angle(self, new_angle: float) -> None:
        """Update the voltage phase angle of the bus.

        :param new_angle: The updated phase angle value
        """
        self.angle = new_angle

    def get_complex_voltage(self) -> complex:
        """Return the complex voltage phasor as a complex number."""
        return self.voltage * np.exp(1j * self.angle)

    def __repr__(self) -> str:
        """Return a string representation for debugging."""
        return (
            f"Bus(bus_id={self.bus_id!r}, voltage={self.voltage}, "
            f"angle={self.angle}, load_mw={self.load_mw})"
        )


# Example usage:
if __name__ == "__main__":
    # Create a bus object
    bus1 = Bus(bus_id=101, voltage=1.02, angle=-0.5, load_mw=50.0)
    print("Initial State: ", bus1)
    complex_voltage: complex = bus1.get_complex_voltage()
    print("Complex voltage (rect): ", complex_voltage)
    print(f"Complex voltage (polar): {bus1.voltage}exp({bus1.angle})")

    # Update voltage and angle
    bus1.update_voltage(1.05)
    bus1.update_angle(-0.8)

    print("Updated State:", bus1)
    complex_voltage: complex = bus1.get_complex_voltage()
    print("Complex voltage (rect): ", complex_voltage)
    print(f"Complex voltage (polar): {bus1.voltage}exp({bus1.angle})")
