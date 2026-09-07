#!/usr/bin/env python3

from ex4_1 import Bus
from ex4_2 import ThermalGenerator

class Line:
    def __init__(
            self, 
            line_id: str | int, 
            from_bus: str | int, 
            to_bus: str | int, 
            flow_mw: float, 
            rating_mva: float
        ):
        self.line_id = line_id
        self.from_bus = from_bus    # Bus ID at one end
        self.to_bus = to_bus        # Bus ID at the other end
        self.flow_mw = flow_mw      # Current power flow
        self.rating_mva = rating_mva  # Thermal limit

    def is_overloaded(self) -> bool:
        """Check if line flow exceeds its rating."""
        return abs(self.flow_mw) > self.rating_mva

    def __repr__(self) -> str:
        return f"Line({self.line_id!r}, {self.from_bus}→{self.to_bus}, flow={self.flow_mw} MW)"
    
class PowerSystem:
    def __init__(self):
        self.buses = []
        self.generators = []
        self.lines = []

    # Busses
    # -----------------------------------------------------------------
    def add_bus(self, bus: Bus):
        self.buses.append(bus)
    
    def remove_bus(self, bus_id: str | int):
        self.buses = [b for b in self.buses if b.bus_id != bus_id]
    
    def total_load(self) -> float:
        return sum(bus.load_mw for bus in self.buses)

    # Generators
    # -----------------------------------------------------------------
    def add_generator(self, generator: ThermalGenerator):
        self.generators.append(generator)

    def remove_generator(self, gen_id: int | str):
        self.generators = [g for g in self.generators if g.gen_id != gen_id ]

    def total_generation(self) -> float:
        return sum(gen.get_output() for gen in self.generators)

    # Lines
    # -----------------------------------------------------------------
    def add_line(self, line: Line):
        self.lines.append(line)

    def remove_line(self, line_id: str | int):
        self.lines = [l for l in self.lines if l.line_id != line_id]

if __name__ == "__main__":

    # Create bus objects
    bus1 = Bus(bus_id=101, voltage=1.02, angle=-0.5, load_mw=50.0)
    bus2 = Bus(bus_id=102, voltage=1.04, angle=-0.4, load_mw=60.0)
    bus3 = Bus(bus_id=103, voltage=1.06, angle=-0.3, load_mw=70.0)
    bus4 = Bus(bus_id=104, voltage=1.08, angle=-0.2, load_mw=80.0)

    # Create generator objects
    gen1 = ThermalGenerator(bus_id=101, gen_id="gen1", p_max=1.0, p_min=0.0, heat_rate=7.2)
    gen2 = ThermalGenerator(bus_id=102, gen_id="gen2", p_max=1.1, p_min=0.1, heat_rate=7.3)
    gen3 = ThermalGenerator(bus_id=103, gen_id="gen3", p_max=1.2, p_min=0.2, heat_rate=7.4)
    gen4 = ThermalGenerator(bus_id=104, gen_id="gen4", p_max=1.3, p_min=0.3, heat_rate=7.5)

    # Create line objects
    line1 = Line(line_id=101, from_bus=101, to_bus=102, flow_mw=50.0, rating_mva=100)
    line2 = Line(line_id=102, from_bus=102, to_bus=103, flow_mw=55.0, rating_mva=90)
    line3 = Line(line_id=103, from_bus=103, to_bus=104, flow_mw=60.0, rating_mva=80)
    line4 = Line(line_id=104, from_bus=104, to_bus=101, flow_mw=65.0, rating_mva=70)

    power_system = PowerSystem()

    power_system.add_bus(bus1)
    power_system.add_bus(bus2)
    power_system.add_bus(bus3)
    power_system.add_bus(bus4)

    power_system.add_generator(gen1)
    power_system.add_generator(gen2)
    power_system.add_generator(gen3)
    power_system.add_generator(gen4)

    power_system.add_line(line1)
    power_system.add_line(line2)
    power_system.add_line(line3)
    power_system.add_line(line4)

    print(f"Total load: {power_system.total_load()} MW")
    print("Removing bus1.")
    power_system.remove_bus(101)
    print(f"Total load: {power_system.total_load()} MW")

    print(f"Total generation: {power_system.total_generation()} MW")
    print("Removing gen1")
    power_system.remove_generator("gen1")
    print(f"Total generation: {power_system.total_generation()} MW")
