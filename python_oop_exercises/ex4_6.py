#!/usr/bin/env python3

from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, measurement_name: str, value: float) -> None:
        """Called by the SCADA subject when a measurement changes."""
        pass

class SCADA:
    """Holds system measurements and notifies observers when values change."""
    
    def __init__(self):
        self._measurements = {}
        self._observers = []
    
    def register_observer(self, observer: Observer) -> None:
        self._observers.append(observer)
    
    def unregister_observer(self, observer: Observer) -> None:
        self._observers.remove(observer)
    
    def update_measurement(self, name: str, value: float) -> None:
        self._measurements[name] = value
        self._notify_observers(name, value)
    
    def _notify_observers(self, name: str, value: float) -> None:
        for observer in self._observers:
            observer.update(name, value)

class VoltageAlarm(Observer):
    """Triggers when voltage is outside acceptable range."""
    
    def __init__(self, bus_id: str | int, min_v: float = 0.95, max_v: float = 1.05):
        self.bus_id = bus_id
        self.min_v = min_v
        self.max_v = max_v
    
    def update(self, measurement_name: str, value: float) -> None:
        # Only react to measurements for this specific bus
        if measurement_name == f"bus_{self.bus_id}_voltage":
            if value < self.min_v or value > self.max_v:
                print(f"ALARM: Bus {self.bus_id} voltage {value:.3f} pu out of range "
                      f"({self.min_v}-{self.max_v})")

class LineFlowAlarm(Observer):
    """Triggers when line flow exceeds thermal rating."""
    
    def __init__(self, line_id: str | int, rating_mva: float, threshold: float = 0.9):
        self.line_id = line_id
        self.rating_mva = rating_mva
        self.threshold = threshold
    
    def update(self, measurement_name: str, value: float) -> None:
        # Only react to measurements for this specific line
        if measurement_name == f"line_{self.line_id}_flow":
            limit = self.rating_mva * self.threshold
            if abs(value) > limit:
                print(f"ALARM: Line {self.line_id} flow {value:.1f} MVA exceeds "
                      f"{self.threshold*100:.0f}% of rating ({limit:.1f} MVA)")

# Example usage:
if __name__ == "__main__":
    scada = SCADA()
    
    # Register alarms
    scada.register_observer(VoltageAlarm(101))
    scada.register_observer(LineFlowAlarm(201, rating_mva=100.0))
    
    # Simulate measurements
    scada.update_measurement("bus_101_voltage", 1.02)   # OK
    scada.update_measurement("bus_101_voltage", 1.08)   # Triggers alarm
    scada.update_measurement("line_201_flow", 85.0)     # OK (below 90%)
    scada.update_measurement("line_201_flow", 95.0)     # Triggers alarm