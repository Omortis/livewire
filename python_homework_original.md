# Python Homework Exercises

> **Instructions**: Complete the exercises below. For each exercise, write your solution in a Python script or Jupyter notebook cell. When you are ready, share your code and I will review it.
>
> **Note**: These exercises assume you are proficient in Python but may be rusty on electrical engineering concepts. Each section includes brief explanations to help you relearn the domain as you go.

---

## Introduction: Power Systems Basics

**Per-Unit System**: Power engineers normalize values to a common base to simplify calculations. For example, 105 MVA on a 100 MVA base is 1.05 per-unit (pu).

**AC Power**: Unlike DC, AC power has both real (P, measured in MW) and reactive (Q, measured in MVAr) components. Apparent power (S, measured in MVA) is the vector sum: S = P + jQ.

**Voltage Phasor**: An AC voltage is described by magnitude (|V|) and angle (δ). In complex form: V = |V|∠δ = |V|e^(jδ).

**Admittance (Y)**: The reciprocal of impedance (Z). Y = G + jB, where G is conductance and B is susceptance. In power systems, lines are mostly inductive, so B is negative.

**Load Flow Analysis**: The process of calculating steady-state voltages and power flows in a power system. It solves the nonlinear equation: Y_bus × V = I.

---

## 1. NumPy

### Exercise 1.1: Voltage Magnitude Array
Create a 1D NumPy array representing voltage magnitudes (in per-unit) at 5 buses: `[1.02, 0.98, 1.00, 1.03, 0.99]`. Print the array, its shape, and its data type.

*Note: In power systems, "per-unit" means normalized to a base value (e.g., 100 kV). A value of 1.0 means the voltage is exactly at the nominal level.*

**Your Answer**:
```python
#!/usr/bin/env python3

import numpy as np

a = np.array([1.02, 0.98, 1.00, 1.03, 0.99])

print("a         : ", a)
print("Shape     : ", a.shape)
print("Array type: ", a.dtype)

```

---

### Exercise 1.2: Building a Simple Matrix
Create a 3x3 matrix representing a simplified Y-bus (admittance matrix) where:
- Diagonal elements are 10 (representing self-admittance)
- Off-diagonal elements are -2 (representing mutual admittance between connected buses)

Print the matrix and verify it is symmetric.

*Note: Y-bus is the fundamental matrix used in power system analysis. Each row/column represents a bus, and the values describe how electricity can flow between buses.*

**Your Answer**:
```python
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

```

---

### Exercise 1.3: Power Calculation
Given two arrays `V = [1.0, 1.02, 0.98]` and `angle = [0, 0.1, -0.05]` (in radians), compute the complex voltage phasors `V_complex = V * exp(j * angle)`. Then compute the complex power injected at each bus if the current injection is `I = [1+0.5j, 0.8-0.2j, 1.2+0.3j]`.

*Hint: Complex power S = V × I* (where I* is the complex conjugate of current). Use `numpy.conj()`.

*Note: This is the fundamental power equation. The real part of S is active power (MW), the imaginary part is reactive power (MVAr).*

**Your Answer**:
```python
# Write your code here
```

---

### Exercise 1.4: Per-Unit Conversion
You have a 2D array of power values in MW for 3 generators over 24 hours (shape: 3x24). Convert all values to per-unit using a base of 100 MVA. Use broadcasting to avoid loops.

*Note: Per-unit values make it easier to compare systems of different sizes. P_pu = P_MW / S_base.*

**Your Answer**:
```python
# Write your code here
```

---

### Exercise 1.5: Simple DC Load Flow
In a simplified DC load flow, we ignore reactive power and voltage angles. Solve the linear system `B × θ = P` for bus angles θ, where `B` is a 3x3 susceptance matrix and `P` is the vector of real power injections.

*Note: This is the linear approximation used in market analysis and contingency screening. The solution gives voltage angles, which determine power flows.*

Use `numpy.linalg.solve`.

**Your Answer**:
```python
# Write your code here
```

---

### Exercise 1.6: Overloaded Line Detection
Given a 1D array of line flows (in MVA) and a 1D array of corresponding line ratings, find the indices of all lines that are operating above 90% of their rating. Return both the indices and the actual overload percentages.

*Note: Transmission lines have thermal limits. Operating above rating can cause the line to sag and potentially touch trees/ground.*

**Your Answer**:
```python
# Write your code here
```

---

### Exercise 1.7: Load Profile Statistics
Generate a 8760-element array representing hourly load demand (MW) for a year using a normal distribution with mean 500 and standard deviation 100. Compute the mean, standard deviation, minimum, maximum, and the 95th percentile. Also find how many hours the load exceeds 700 MW.

*Note: 8760 hours = 365 days × 24 hours. Load forecasting is a major task in power system planning.*

**Your Answer**:
```python
# Write your code here
```

---

### Exercise 1.8: Monte Carlo Load Uncertainty
Simulate 10,000 scenarios of total system load where each of 5 zones has a mean load of 200 MW and a standard deviation of 30 MW. Compute the mean and standard deviation of the total system load across all scenarios. Also compute the probability that the total load exceeds 1100 MW.

*Note: Monte Carlo simulation is used for probabilistic load flow and reliability assessment. It helps utilities plan for uncertainty.*

**Your Answer**:
```python
# Write your code here
```

---

## 2. Pandas

### Exercise 2.1: Generator DataFrame
Create a DataFrame with columns `['bus_id', 'gen_id', 'p_max', 'p_min', 'fuel_type', 'cost_per_mwh']` and populate it with 5 rows of realistic generator data (e.g., Coal, Gas, Nuclear, Wind, Solar).

*Note: Generator data (called "unit commitment data") is used in economic dispatch to decide which generators to run.*

**Your Answer**:
```python
# Write your code here
```

---

### Exercise 2.2: Cleaning Missing Measurements
Create a synthetic DataFrame with 100 rows and columns `['timestamp', 'voltage', 'power', 'frequency']` using realistic ranges. Introduce 10 missing values at random positions. Replace missing values with the column mean and count how many values were imputed.

*Note: SCADA (Supervisory Control and Data Acquisition) systems collect real-time measurements from substations. Missing data is common due to communication issues.*

**Your Answer**:
```python
# Write your code here
```

---

### Exercise 2.3: Peak Demand Filtering
Given a DataFrame of hourly load data with columns `['hour', 'load_mw']`, find all rows where the load is above the 90th percentile and return the top 10 highest load hours.

*Note: Peak demand determines how much generation capacity must be available. Utilities plan for the highest expected load plus a reserve margin.*

**Your Answer**:
```python
# Write your code here
```

---

### Exercise 2.4: Time Series Resampling
Create a DataFrame with 30 days of **hourly** generation data (one column per generator type: Coal, Gas, Nuclear, Wind, Solar). This gives you 720 rows (30 days × 24 hours). The index should be a DatetimeIndex with hourly timestamps.

Then perform two resampling operations:
1. **Daily average** for each generator — use `df.resample('D').mean()` to get the average generation per day for each generator type
2. **Total daily generation** across all generators — use `df.resample('D').sum().sum(axis=1)` to get the total system generation for each day

*Why resampling?* Power system data is collected at high frequency (hourly or 5-minute intervals from SCADA systems). But day-ahead electricity markets use daily schedules, and monthly/quarterly planning reports need daily or weekly summaries. Resampling is the standard tool for aggregating high-frequency time-series data to the resolution needed for the analysis at hand. It's also critical for aligning data with different time granularities — e.g., merging hourly generation data with daily fuel price data.

**Your Answer**:
```python
# Write your code here
```

---

### Exercise 2.5: Merging Outage Data
You have two DataFrames: one with generator information (`gen_id`, `fuel_type`, `capacity`) and one with scheduled outages (`gen_id`, `start_date`, `end_date`, `outage_mw`). Merge them and compute the total outage MW by fuel type.

*Note: Scheduled outages are planned maintenance. System operators must ensure enough generation remains available during outages.*

**Your Answer**:
```python
# Write your code here
```

---

### Exercise 2.6: Capacity by Fuel Type
Given a DataFrame of generators with columns `['gen_id', 'fuel_type', 'capacity']`, group by fuel type and compute total capacity, average capacity, and count of generators.

*Note: This is the "generator fleet" analysis. The capacity mix (how much coal vs gas vs renewables) determines system reliability and emissions.*

**Your Answer**:
```python
# Write your code here
```

---

### Exercise 2.7: Contingency Results Analysis
You have a DataFrame of contingency analysis results with columns `['contingency_id', 'line_id', 'pre_flow', 'post_flow', 'loading_percent']`. Find the maximum `loading_percent` for each line across all contingencies.

*Note: Contingency analysis simulates "what if" scenarios (e.g., what if a line trips). NERC standards require utilities to analyze single contingencies.*

*What the columns mean:*
- **`pre_flow`** = power flow on the line under normal operating conditions (before any contingency)
- **`post_flow`** = power flow on the line after a simulated contingency (e.g., another line tripped, causing power to reroute through this line)
- **`loading_percent`** = how loaded the line is after the contingency, as a percentage of its thermal rating

*The goal:* Identify the worst-case loading for each line across all possible single contingencies. This tells operators which lines are most vulnerable to overload if another part of the network fails.*

**Your Answer**:
```python
# Write your code here
```

---

### Exercise 2.8: Production Cost Analysis
Given three DataFrames: `generation` (hourly output by gen_id), `fuel_prices` (daily price by fuel_type), and `generator_info` (gen_id, fuel_type, and heat_rate in MMBtu/MWh), compute the total production cost for each day.

*Note: Production cost = generation (MWh) × fuel price ($/MMBtu) × heat rate (MMBtu/MWh). This is the core of economic dispatch.*

**Your Answer**:
```python
# Write your code here
```

---

## 3. Matplotlib

### Exercise 3.1: Daily Load Curve
Plot a daily load curve (24 hours) from a given array of load values. Add proper labels for the x-axis ("Hour"), y-axis ("Load (MW)"), and title ("Daily Load Profile"). Include a grid.

*Note: Load curves show the typical pattern: low at night, ramping up in morning, peak in afternoon/evening.*

**Your Answer**:
```python
# Write your code here
```

---

### Exercise 3.2: Voltage Profile Comparison
Create a plot showing voltage profiles for 3 different buses over 24 hours. Use different line styles/colors and include a legend. All buses should be plotted on the same axes.

*Note: Voltage should stay within ±5% of nominal (0.95 to 1.05 pu). This plot helps identify buses with voltage problems.*

**Your Answer**:
```python
# Write your code here
```

---

### Exercise 3.3: Generation vs Demand Scatter
Create a scatter plot of generation (MW) vs demand (MW) for 1000 hourly points. Color the points by time of day (e.g., morning, afternoon, evening, night). Add a diagonal line representing generation = demand.

*Note: In a balanced system, generation equals demand. This plot shows how well the system is balanced.*

**Your Answer**:
```python
# Write your code here
```

---

### Exercise 3.4: Capacity by Fuel Type Bar Chart
Create a horizontal bar chart showing total installed capacity by fuel type. Add data labels at the end of each bar showing the capacity in MW.

*Note: The "capacity mix" determines grid reliability and environmental impact. Many regions are shifting from coal to renewables.*

**Your Answer**:
```python
# Write your code here
```

---

### Exercise 3.5: Line Flow Heatmap
Create a heatmap showing power flow on 5 lines over 24 hours. Use a colorbar to indicate flow magnitude in MW. Add labels for lines and hours.

*Note: Heatmaps are great for identifying patterns. You might see certain lines are always heavily loaded during peak hours.*

**Your Answer**:
```python
# Write your code here
```

---

### Exercise 3.6: System Status Dashboard
Create a single figure with multiple chart types: a line plot for total generation, a bar chart for fuel mix, and a scatter plot for price vs demand. Arrange them in a grid layout and add a main title.

*Note: Control room operators use dashboards like this to monitor the system in real-time.*

**Your Answer**:
```python
# Write your code here
```

---

## 4. Object-Oriented Concepts

### Exercise 4.1: Bus Class
Create a `Bus` class with attributes `bus_id`, `voltage`, `angle`, and `load_mw`. Include methods to update the voltage and angle, and a method to return the complex voltage representation.

*Note: A "bus" in power systems is a node in the network where equipment connects (generators, loads, transformers). Think of it as a substation.*

**Your Answer**:
```python
# Write your code here
```

---

### Exercise 4.2: Generator Inheritance
Create a base `Generator` class with attributes `gen_id`, `bus_id`, `p_max`, `p_min`, and a method `get_output()`. Create two subclasses: `ThermalGenerator` and `RenewableGenerator`.

- `ThermalGenerator` should have a `heat_rate` attribute (MMBtu/MWh) and a method `get_fuel_cost(fuel_price_per_mmbtu: float)` that returns the fuel cost in dollars per hour: `get_output() * heat_rate * fuel_price_per_mmbtu`.
- `RenewableGenerator` should have a `capacity_factor` attribute (0.0 to 1.0) and override `get_output()` to return `p_max * capacity_factor`.

*Note: Thermal generators (coal, gas, nuclear) convert fuel to electricity. Renewables (wind, solar) depend on weather. Capacity factor is the actual output divided by maximum possible output.*

**Your Answer**:
```python
# Write your code here
```

---

### Exercise 4.3: Encapsulation - Power System Component
Create a `Transformer` class that encapsulates its tap ratio and impedance. The tap ratio should only be adjustable through a method `set_tap_ratio(new_ratio)` that validates the ratio is between 0.9 and 1.1. The impedance should be read-only after initialization.

*Note: Transformers have adjustable taps to control voltage. The tap ratio changes the voltage transformation ratio. Typical range is ±10%.*

**Your Answer**:
```python
# Write your code here
```

---

### Exercise 4.4: Polymorphism - Data Source Adapter Interface
Create an abstract base class `PowerSystemDataSource` with an abstract method `read_measurements()`. Implement two concrete classes: `ScadaCsvAdapter` (reads CSV with columns `timestamp,bus_id,voltage_pu,power_mw`) and `Iec61850JsonAdapter` (reads JSON with nested structure). Write a function `ingest_data(source: PowerSystemDataSource)` that accepts any adapter type and returns a normalized `pandas.DataFrame` with columns `['timestamp', 'bus_id', 'voltage_pu', 'power_mw']`.

*Note: Power system data arrives in many formats — SCADA CSV exports, IEC 61850 JSON payloads, CIM/XML files, DNP3 binary streams. An ETL pipeline normalizes these disparate formats into a canonical schema before analytics and storage.*

**Sample data files:**

`scada_sample.csv`:
```csv
timestamp,bus_id,voltage_pu,power_mw
2024-01-01T00:00,1,1.02,50.5
2024-01-01T00:00,2,0.98,120.0
2024-01-01T01:00,1,1.01,48.0
2024-01-01T01:00,2,0.97,115.0
```

`iec61850_sample.json`:
```json
{
  "measurements": [
    {"timestamp": "2024-01-01T00:00", "busId": 1, "voltage": 1.02, "power": 50.5},
    {"timestamp": "2024-01-01T00:00", "busId": 2, "voltage": 0.98, "power": 120.0},
    {"timestamp": "2024-01-01T01:00", "busId": 1, "voltage": 1.01, "power": 48.0},
    {"timestamp": "2024-01-01T01:00", "busId": 2, "voltage": 0.97, "power": 115.0}
  ]
}
```

**Your Answer**:
```python
# Write your code here
```

---

### Exercise 4.5: Composition - Power System
Create a `PowerSystem` class that contains lists of `Bus`, `Generator`, and `Line` objects. Implement methods to add components, remove components, and calculate the total system load and total generation. The class should delegate to the component classes rather than storing duplicate data.

*Note: This is the "has-a" relationship. A power system has buses, generators, and lines. Composition is preferred over inheritance for this.*

**Your Answer**:
```python
# Write your code here
```

---

### Exercise 4.6: Observer Pattern for SCADA
Implement the Observer pattern for a SCADA monitoring system. Create a `SCADA` subject that holds system measurements. Create `Alarm` observers that trigger when voltage or line flow exceeds thresholds. Demonstrate registering observers, updating measurements, and handling alarms.

*Note: SCADA systems monitor thousands of points. When a value exceeds a threshold, alarms notify operators to take action.*

**Your Answer**:
```python
# Write your code here
```

---

## Submission Notes

- Save your completed exercises as a Python script or Jupyter notebook.
- When you are ready for review, copy the code for the exercises you want me to check and paste it into the chat.
- I will review your solutions for correctness, efficiency, and style.
- If you get stuck on the electrical engineering concepts, ask! I can explain the theory behind any exercise.

## Additional Resources

- **Power Systems Basics**: "Power System Analysis and Design" by Glover, Sarma, and Overbye
- **Python for Power Systems**: Check out the `pypsa` and `pandapower` open-source libraries
- **Industry Standards**: NERC (North American Electric Reliability Corporation) sets reliability standards
