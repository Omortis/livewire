# LiveWire — Power Systems Programming Practice

A multi-language exercise set for experienced developers building skills in power system engineering. Covers data analysis, system integration, and domain modeling across Python, Java, and Kotlin.

## Mission

Relearn electrical engineering fundamentals (power flow, SCADA, contingency analysis, economic dispatch) through hands-on programming exercises. The target domain is day-to-day analysis and integration work at a power engineering firm.

## Tracks

### Python (Data Analysis)
- **NumPy** — arrays, matrices, broadcasting, linear algebra for power flow
- **Pandas** — data cleaning, time series, merging, grouping for SCADA/outage data
- **Matplotlib** — load curves, heatmaps, dashboards for system visualization
- **Object-Oriented Design** — classes, inheritance, composition, observer patterns for grid components

### Java (System Integration)
- **NIO / File I/O** — log analysis, CSV/JSON ETL pipelines
- **Collections & Generics** — equipment registries, filtering, type-safe data structures
- **Interfaces & Polymorphism** — solver abstractions, middleware patterns
- **Maven** — dependency management, build tooling

### Kotlin (Modern JVM)
- **Data Classes & Null Safety** — SCADA measurement modeling with explicit missing data handling
- **Collection DSL** — concise load profiling and time-series transformations
- **Coroutines** — async SCADA polling and concurrent data source integration
- **Sealed Classes** — exhaustive protocol state machines (message types, function codes)
- **Gradle (Kotlin DSL)** — build tooling

## Domain Context

Exercises are grounded in power system simulation methodologies:
- **Load flow analysis** — DC/AC power flow, voltage angles, Y-bus matrices
- **Contingency analysis** — N-1 criteria, line overload detection, post-contingency flows
- **Production cost modeling** — economic dispatch, fuel cost calculations, unit commitment data
- **SCADA integration** — time-series data, missing value imputation, alarm thresholds
- **IEC 61850 / CIM** — substation automation protocols, Common Information Model data exchange

## Getting Started

### Python
```bash
source venv/bin/activate
pip install numpy pandas matplotlib
```

### Java (Maven)
```bash
# Per-exercise project
cd java/exercise_01
mvn compile exec:java -Dexec.mainClass="com.example.App"
```

### Kotlin (Gradle)
```bash
# Per-exercise project
cd kotlin/exercise_01
gradle run
```

## Project Structure

- `python_homework.md` — Python exercise file (work in progress, answers inline)
- `python_homework_original.md` — Python template without answers
- `java_kotlin_homework.md` — Java and Kotlin exercise file
- `java_kotlin_coursework.md` — Java/Kotlin project brief and guidelines
- `coursework.md` — Original project brief
- `ex1.py`, `ex2.py`, `ex3.py` — Individual Python exercise scripts
- `README.md` — This file

## Working on Exercises

1. Open the relevant `.md` file for your track
2. Pick an exercise and write your solution in a standalone script or CLI application
3. Paste your code into the Markdown file inline (or keep it in separate source files)
4. Ask for review when ready

## Git Workflow

All work happens on feature branches. Do not commit directly to `main`.

```bash
# Python
git checkout pandas_exercises
# ... make changes ...
git add python_homework.md
git commit -m "Progress: completed exercises 2.5-2.8"

# Java/Kotlin
git checkout java_kotlin_exercises
# ... make changes ...
git add java_kotlin_homework.md
git commit -m "Completed Java exercises 1.1-1.3"
```

## Target Platforms

- macOS (primary development environment)
- FreeBSD (secondary, where OS-specific decisions arise)
- Java 17+ LTS (conservative enterprise target for power utilities)
- Python 3.10+
- Kotlin 2.x
