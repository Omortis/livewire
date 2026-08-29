# PyStudy — Power Engineering Python Practice

A collection of hands-on Python exercises for an experienced developer relearning electrical engineering fundamentals, specifically power system simulation concepts.

## Topics Covered

- **NumPy** — arrays, matrices, broadcasting, linear algebra for power flow
- **Pandas** — data cleaning, time series, merging, grouping for SCADA/outage data
- **Matplotlib** — load curves, heatmaps, dashboards for system visualization
- **Object-Oriented Design** — classes, inheritance, composition, observer patterns for grid components

## Getting Started

```bash
# Activate the virtual environment
source venv/bin/activate

# Install dependencies (if not already present)
pip install numpy pandas matplotlib
```

## Project Structure

- `python_homework.md` — the main exercise file (work in progress, answers inline)
- `python_homework_original.md` — the original template without answers
- `coursework.md` — the project brief and guidelines
- `ex1.py`, `ex2.py`, `ex3.py` — individual exercise scripts

## Working on Exercises

1. Open `python_homework.md`
2. Pick an exercise and write your solution in a Python script or Jupyter notebook cell
3. Paste your code into the Markdown file inline (or keep it in separate `.py` files)
4. Ask for review when ready

## Git Workflow

Work on the `numpy_exercises` branch. Do not commit to `main`.

```bash
git checkout numpy_exercises
# ... make changes ...
git add python_homework.md
git commit -m "Progress: completed exercises 1.1-1.3"
```
