def writeToFileForMinizinc(N, M, Q, start, end, edges, mandatory, file_name):
    output_file = "generate_data/data/dpath/{}".format(file_name)
    with open(output_file, "w") as file:
        file.write("N = {};\n".format(N))
        file.write("E = {};\n".format(M))
        file.write("Q = {};\n".format(Q))
        file.write("from = {};\n".format([e[0] for e in edges]))
        file.write("to = {};\n".format([e[1] for e in edges]))
        file.write("weights = {};\n".format([e[2] for e in edges]))
        file.write("mandatory = {};\n".format(mandatory))
        file.write("S = {};\n".format(start))
        file.write("T = {};\n".format(end))


def writeToFileForGraphsVisualizer(N, M, edges, file_name):
    output_file = "generate_data/data/graph-visualization/{}".format(file_name)
    with open(output_file, "w") as file:
        for edge in edges:
            file.write("{} {} {}\n".format(edge[0], edge[1], edge[2]))


def writeToFileAdjacentMatrix(N, M, Q, start, end, edges, mandatory, file_name):
    mat = [[-1 for _ in range(N)] for _ in range(N)]
    for edge in edges:
        mat[edge[0] - 1][edge[1] - 1] = edge[2]
    ouptut_file = "generate_data/data/adjacent-matrix/{}".format(file_name)
    with open(ouptut_file, "w") as file:
        file.write("N = {};\n".format(N))
        file.write("M = {};\n".format(M))
        file.write("Q = {};\n".format(Q))
        file.write("start = {};\n".format(start))
        file.write("end = {};\n".format(end))
        file.write("mat = [|")
        for row in mat:
            file.write("{}|".format(row).replace("[", "").replace("]", ""))
        file.write("];\n")
        file.write("mandatory = {};\n".format(mandatory))