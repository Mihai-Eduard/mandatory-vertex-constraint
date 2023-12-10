include "path.mzn";

int: N;
int: E;
int: Q;
array[1..E] of int: from;
array[1..E] of int: to;
array[1..E] of int: weights;
array[1..Q] of set of int: mandatory;

int: S;
int: T;

array [1..N] of var bool: ns;
array [1..E] of var bool: es;

constraint dpath(N, E, from, to, S, T, ns, es);

function var int: get_path_weight(array[1..E] of var bool: es, array[1..E] of int: weights) 
    = sum(i in 1..E)(if(es[i] == true) then weights[i] else 0 endif);

predicate set_satisifed(set of int: required_nodes, array[1..N] of var bool: ns)
    = exists(node in required_nodes)(ns[node]);

constraint forall(i in 1..Q)(set_satisifed(mandatory[i], ns));

solve minimize(get_path_weight(es, weights));

output["The nodes considered are: ", show(ns), "\n", 
        "The edges considered are: ", show(es), "\n",
        "The total cost is: ", show(get_path_weight(es, weights))];