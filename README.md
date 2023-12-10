# Manadatory Vertex Constraint

## Step 1 
In this step, we will compare 2 implementations: [one](https://github.com/Mihai-Eduard/mandatory-vertex-constraint/blob/main/main-dpath.mzn) using the global constraint, and [one](https://github.com/Mihai-Eduard/mandatory-vertex-constraint/blob/main/main-adjacent-matrix.mzn) using a hand-made constraint of that type.

We can use the following command to generate a minizinc data file with N nodes. You are required to choose the number of nodes of the graph and the file name.
``` shell
python generate_data/run.py -N=<N> --file=<name>
```
We can use the following command to generate some files and benchmark them against both implementations. It will output the specific times and the results in the corresponding files from the benchmark/logs. You are required to choose the number of nodes of the graph and the timeout.
``` shell
python benchmark/run.py -N=<N> --timeout=<time(sec)>
```
