# How to run profiling

1. Make sure you have SnakeViz installed (for visualisation): `pip install snakeviz`
2. Generate a profile (from root of project): `python -m cProfile -o covidsimulation/tests/profiling/covid_simulation.prof -m covidsimulation <args>`
3. Run the visualisation tool which will open in a browser (from root of project): `snakeviz covidsimulation/tests/profiling/covid_simulation.prof`

You can run the utility script `profile.py` to perform steps 2 and 3.