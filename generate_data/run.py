import random
from generate_data.args_parser import get_arguments
from generate_data.write_to_file import writeToFileForMinizinc, writeToFileForGraphsVisualizer, writeToFileAdjacentMatrix


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
        current_set = set()
        for j in range(1, N + 1):
            if random.random() > 0.75:
                current_set.add(j)
        if len(current_set) == 0:
            current_set.add(start)
        mandatory.append(current_set)

    return N, M, Q, start, end, edges, mandatory


def writeToFiles(N, file_name):
    N, M, Q, start, end, edges, mandatory = generateRandom(N)
    writeToFileForMinizinc(N, M, Q, start, end, edges, mandatory, f'{file_name}.dzn')
    writeToFileForGraphsVisualizer(N, M, edges, f'{file_name}.txt')
    writeToFileAdjacentMatrix(N, M, Q, start, end, edges, mandatory, f'{file_name}.dzn')


if __name__ == '__main__':
    N, file_name = get_arguments()
    writeToFiles(N, file_name)