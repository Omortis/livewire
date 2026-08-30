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
import numpy as np

a = np.array([1.02, 0.98, 1.00, 1.03, 0.99])

print("a         : ", a)
print("Shape     : ", a.shape)
print("Array type: ", a.dtype)

# Output:
# a         :  [1.02 0.98 1.   1.03 0.99]
# Shape     :  (5,)
# Array type:  float64
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
import numpy as np

ybus = np.array([
                    [10, -2, -2],
                    [-2, 10, -2],
                    [-2, -2, 10]
                ])

print("ybus:\n", ybus)

is_symmetric = np.array_equal(ybus, ybus.T)
print(f"ybus is symmetrical: {is_symmetric}")

# Output:
# ybus:
#  [[10 -2 -2]
#  [-2 10 -2]
#  [-2 -2 10]]
# ybus is symmetrical: True
```

---

### Exercise 1.3: Power Calculation
Given two arrays `V = [1.0, 1.02, 0.98]` and `angle = [0, 0.1, -0.05]` (in radians), compute the complex voltage phasors `V_complex = V * exp(j * angle)`. Then compute the complex power injected at each bus if the current injection is `I = [1+0.5j, 0.8-0.2j, 1.2+0.3j]`.

*Hint: Complex power S = V × I* (where I* is the complex conjugate of current). Use `numpy.conj()`.

*Note: This is the fundamental power equation. The real part of S is active power (MW), the imaginary part is reactive power (MVAr).*

**Your Answer**:
```python
import numpy as np

np.set_printoptions(formatter={"float_kind": "{:.4f}".format})

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

# Output:
# V          :  [1.0000 1.0200 0.9800]
# V_complex  :  [1.        +0.j         1.01490425+0.10183008j 0.97877526-0.04897959j]
# I          :  [1. +0.5j 0.8-0.2j 1.2+0.3j]
# I conjugate:  [1. -0.5j 0.8+0.2j 1.2-0.3j]
# S_complex  :
#         P:  1.000       Q: -0.500
#         P:  0.792       Q:  0.284
#         P:  1.160       Q: -0.352
```

---

### Exercise 1.4: Per-Unit Conversion
You have a 2D array of power values in MW for 3 generators over 24 hours (shape: 3x24). Convert all values to per-unit using a base of 100 MVA. Use broadcasting to avoid loops.

*Note: Per-unit values make it easier to compare systems of different sizes. P_pu = P_MW / S_base.*

**Your Answer**:
```python
import numpy as np

# Generator sizes by type:
# - Base load (e.g., coal/nuclear): 100–300 MW (1.0–3.0 pu)
# - Mid-merit (e.g., combined cycle gas): 50–150 MW (0.5–1.5 pu)
# - Peaker (e.g., gas turbine): 20–80 MW (0.2–0.8 pu)

# Three generators, 24 hours each
gen1 = np.random.uniform(100, 300, 24)  # base load
gen2 = np.random.uniform(50, 150, 24)  # mid-merit
gen3 = np.random.uniform(20, 80, 24)  # peaker

P_mw = np.array([gen1, gen2, gen3])
base_power = 100.0  # MVA
P_mw_broadcast = P_mw / base_power

print("P_mw.shape:")
print(P_mw.shape)
print("P_mw:")
print(P_mw)
print("P_mw_broadcast:")
print(P_mw_broadcast)

# Output:
# P_mw.shape:
# (3, 24)
# P_mw:
# [[167.84917751 280.20353139 267.73667059 186.64391958 153.7022188
#   289.47781724 290.96574036 178.38490336 202.19967661 291.15311026
#   128.9624342  246.80319646 173.24743351 221.30893199 116.7254522
#   255.05123959 218.16659862 159.12628164 142.57995533 129.27964204
#   156.33699528 143.17831714 158.44094723 251.59558405]
#  [ 75.56905144  96.615374    61.48008959  62.05722717 126.07732877
#   149.61017672  98.22813346  97.80271333 135.90094259  58.67240927
#    51.40638345 138.32276667 110.56863237 139.41480959 118.80738337
#    62.03164749  70.65609478  69.81230448 135.18979667 110.09294692
#   148.21445533  54.71551898  81.63318452  77.74011897]
#  [ 69.33145843  64.02814783  48.48566274  49.68181071  48.30515822
#    47.96201207  24.14433988  57.91883408  75.81947373  26.42210384
#    67.04489556  27.60714879  75.72338778  22.87106616  27.56652515
#    49.64969311  68.3060724   38.37879569  56.92631364  40.85080287
#    35.57955598  49.16792295  60.06985277  40.71269285]]
# P_mw_broadcast:
# [[1.67849178 2.80203531 2.67736671 1.8664392  1.53702219 2.89477817
#   2.9096574  1.78384903 2.02199677 2.9115311  1.28962434 2.46803196
#   1.73247434 2.21308932 1.16725452 2.5505124  2.18166599 1.59126282
#   1.42579955 1.29279642 1.56336995 1.43178317 1.58440947 2.51595584]
#  [0.75569051 0.96615374 0.6148009  0.62057227 1.26077329 1.49610177
#   0.98228133 0.97802713 1.35900943 0.58672409 0.51406383 1.38322767
#   1.10568632 1.3941481  1.18807383 0.62031647 0.70656095 0.69812304
#   1.35189797 1.10092947 1.48214455 0.54715519 0.81633185 0.77740119]
#  [0.69331458 0.64028148 0.48485663 0.49681811 0.48305158 0.47962012
#   0.2414434  0.57918834 0.75819474 0.26422104 0.67044896 0.27607149
#   0.75723388 0.22871066 0.27566525 0.49649693 0.68306072 0.38378796
#   0.56926314 0.40850803 0.35579556 0.49167923 0.60069853 0.40712693]]

```

---

### Exercise 1.5: Simple DC Load Flow
In a simplified DC load flow, we ignore reactive power and voltage angles. Solve the linear system `B × θ = P` for bus angles θ, where `B` is a 3x3 susceptance matrix and `P` is the vector of real power injections.

*Note: This is the linear approximation used in market analysis and contingency screening. The solution gives voltage angles, which determine power flows.*

Use `numpy.linalg.solve`.

**Your Answer**:
```python
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

# Output:
# Solve for the bus angles θ in B x θ = P.

# B (susceptance):
# [[ 15 -10  -5]
#  [-10  20 -10]
#  [ -5 -10  15]]

# P (real power injections):
# [ 1.  -0.5 -0.5]

# Bus Angles:
# [ 0.04375 -0.01875 -0.03125]

# Verification (B @ θ):
# [ 1.  -0.5 -0.5]
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
Load a CSV file of hourly SCADA measurements (create a synthetic DataFrame with 100 rows and columns `['timestamp', 'voltage', 'power', 'frequency']`). Introduce 10 missing values at random positions. Replace missing values with the column mean and count how many values were imputed.

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
Create a DataFrame with 30 days of hourly generation data (one column per generator type: Coal, Gas, Nuclear, Wind, Solar). Compute the daily average generation for each generator and the total daily generation across all generators.

*Note: Resampling is essential for analyzing time-series data. Day-ahead markets use hourly schedules, while long-term planning uses daily/weekly averages.*

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

**Your Answer**:
```python
# Write your code here
```

---

### Exercise 2.8: Production Cost Analysis
Given three DataFrames: `generation` (hourly output by gen_id), `fuel_prices` (daily price by fuel_type), and `generator_info` (gen_id to fuel_type mapping), compute the total production cost for each day.

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
Create a base `Generator` class with attributes `gen_id`, `bus_id`, `p_max`, `p_min`, and a method `get_output()`. Create two subclasses: `ThermalGenerator` and `RenewableGenerator`. `ThermalGenerator` should have a `heat_rate` attribute and a method `get_fuel_cost()`. `RenewableGenerator` should have a `capacity_factor` attribute and override `get_output()` to consider capacity factor.

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

### Exercise 4.4: Polymorphism - Solver Interface
Create an abstract base class `PowerFlowSolver` with an abstract method `solve()`. Implement two concrete classes: `NewtonRaphsonSolver` and `GaussSeidelSolver`. Each should implement `solve()` differently. Write a function `run_solver(solver: PowerFlowSolver, system_data)` that accepts any solver type and returns the solution.

*Note: Newton-Raphson is the industry standard for load flow (fast, quadratic convergence). Gauss-Seidel is simpler but slower. Different utilities use different solvers.*

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
