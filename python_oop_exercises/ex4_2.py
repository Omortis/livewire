#!/usr/bin/env python3

import numpy as np

class Generator:
    """Represents an electrical power generation system."""

    def __init__(
        self,
        bus_id: int | str,
        gen_id: int | str,
        p_max: float,
        p_min: float
    ):
        """Initialize a new Generator instance.

        :param bus_id: Unique identifier for the bus (e.g., integer index or name)
        :param gen_id: Unique identifier for a specific generator
        :param p_max: Maximum power the generator can provide
        :param p_min: Minimum power the generator can provide
        """
        self.bus_id = bus_id
        self.gen_id = gen_id
        self.p_max = p_max
        self.p_min = p_min

    def get_output(self) -> float:
        """Return the output for this generator. Not implemented in base class."""
        raise NotImplementedError(
             "Subclasses must implement this method"
         )
    def __repr__(self) -> str:
        """Return a string representation of the Generator for debugging."""
        return (
            f"Generator(bus_id={self.bus_id!r}, gen_id={self.gen_id}, "
            f"p_max={self.p_max}, p_min={self.p_min})"
        )

class ThermalGenerator(Generator):
    """Represents a Thermal Generator.
    
    :param heat_rate: Fuel consumed in MMBtu to produce one MWh of electricity (MMBtu/MWh).
    """

    def __init__(
        self,
        bus_id: int | str,
        gen_id: int | str,
        p_max: float,
        p_min: float,
        heat_rate: float
    ):
        super().__init__(bus_id, gen_id, p_max, p_min)
        self.heat_rate = heat_rate

    def get_output(self) -> float:
        return self.p_max

    def get_fuel_cost(self, fuel_price_per_mmbtu: float) -> float:
        return self.get_output() * self.heat_rate * fuel_price_per_mmbtu

    def __repr__(self) -> str:
        """Return a string representation of the ThermalGenerator for debugging."""
        return (
            f"ThermalGenerator(bus_id={self.bus_id!r}, gen_id={self.gen_id}, "
            f"p_max={self.p_max}, p_min={self.p_min}, heat_rate={self.heat_rate})"
        )
    
class RenewableGenerator(Generator):
    """Represents a Renewable Generator (solar, wind, etc).
    
    :param capacity_factor: Long-term average ratio of actual 
    energy output to maximum possible output (0.0 to 1.0), 
    accounting for weather and downtime.
    """

    def __init__(
        self,
        bus_id: int | str,
        gen_id: int | str,
        p_max: float,
        p_min: float,
        capacity_factor: float
    ):
        super().__init__(bus_id, gen_id, p_max, p_min)
        if capacity_factor < 0.0 or capacity_factor > 1.0:
            raise ValueError("0.0 <= capacity_factor <= 1.0: value out of range:", capacity_factor)
        self.capacity_factor = capacity_factor


    def get_output(self) -> float:
        return self.p_max * self.capacity_factor

    def __repr__(self) -> str:
        """Return a string representation of the RenewableGenerator for debugging."""
        return (
            f"RenewableGenerator(bus_id={self.bus_id!r}, gen_id={self.gen_id}, "
            f"p_max={self.p_max}, p_min={self.p_min}, capacity_factor={self.capacity_factor})"
        )
    
# Example usage:
if __name__ == "__main__":
    gen1 = Generator(bus_id=101, gen_id="gen1", p_max=1.0, p_min=0.0)

    try:
        output = gen1.get_output()
    except NotImplementedError:
        print("Correctly raised NotImplementedError")

    thermal = ThermalGenerator("GEN_1", 1, 500, 100, heat_rate=7.2)
    print(f"{thermal.get_output()} MW")
    print(f"${thermal.get_fuel_cost(3.5):,.0f}/hour")

    try:
        renewable = RenewableGenerator("GEN_2", 2, 200, 0, capacity_factor=1.35)
    except ValueError:
        print("Correctly raised ValueError (capacity_factor > 1.0)")

    try:
        renewable = RenewableGenerator("GEN_2", 2, 200, 0, capacity_factor=-0.35)
    except ValueError:
        print("Correctly raised ValueError (capacity_factor < 0.0)")

    renewable = RenewableGenerator("GEN_2", 2, 200, 0, capacity_factor=0.35)
    print(f"{renewable.get_output()} MW")