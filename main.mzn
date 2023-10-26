int: N; %number of nodes
int: M; %number of directed edges
int: Q; %number of constraints 
int: start; %starting point of path
int: end; %ending point of path

array[1..N,1..N] of int: mat; %adjacent matrix
array[1..Q] of set of int: mandatory; %list of mandatory sets

var 1..M+1: L; %the lenght of the path
array[1..M+1] of var 0..N: path; %the target path

%first and last element constraint
constraint path[1]==start /\ path[L]==end;

%valid vertexes for the path
constraint forall(i in 1..N)(if i<=L then path[i]>=1 else path[i]==0 endif);

%edge between every consecutive pair of elements
constraint forall(i in 1..L-1)(mat[path[i],path[i+1]]!=-1);

%verify constraints of mandatory vertex
constraint forall(i in 1..Q)(exists([if path[j] in mandatory[i] then true else false endif | j in 1..L]));

solve minimize sum(i in 1..L-1)(mat[path[i],path[i+1]]);

output[show(sum(i in 1..L-1)(mat[path[i],path[i+1]])), "\n", show(L-1), "\n", show(path)];