import random
from args_parser import get_arguments
from write_to_file import writeToFileForMinizinc, writeToFileForGraphsVisualizer


def generateRandom(N):
    M = 0
    edges = []
    Q = random.randint(1, N)
    start = 1
    end = N

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i == j:
                continue
            if random.random() > 0.5:
                edges.append((i, j, random.randint(0, 10)))
                M += 1

    mandatory = []
    for i in range(Q):
        mandatory.append({random.randint(1, N)})

    return N, M, Q, start, end, edges, mandatory


if __name__ == '__main__':
    N, file_name = get_arguments()
    N, M, Q, start, end, edges, mandatory = generateRandom(N)
    writeToFileForMinizinc(N, M, Q, start, end, edges, mandatory, f'{file_name}.dzn')
    writeToFileForGraphsVisualizer(N, M, edges, f'{file_name}.txt')