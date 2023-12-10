# Step 1 
In this step we will compare 2 implementations: one using the global constraint dpath (main-dpath.mzn) and one using a hand-made constraint of that type (main-adjacent-matrix.mzn).

To generate a minizinc data file with N nodes, we can use the following command.
```shell
python generate_data/run.py -N=<N> --file=<name>
```
To generate some files and then benchmark them against both implementations, we can use the fllowing command. It will output the specific times and the results in the corresponding files from the benchmark/logs.
```shell
python benchmark/run.py
```