import random

def writeToFile(N, M, Q, start, end, mat, mandatory, file_name):
    output_file = "generated_data/{}".format(file_name)
    with open(output_file, "w") as file:
        file.write("N = {};\n".format(N))
        file.write("M = {};\n".format(M))
        file.write("Q = {};\n".format(Q))
        file.write("start = {};\n".format(start))
        file.write("end = {};\n".format(end))
        file.write("mat = {};\n".format(mat).replace("], [", "|").replace("[[", "[|").replace("]]", "|]"))
        file.write("mandatory = {};\n".format(mandatory))


def generateRandom(Nmin, Nmax):
    N = random.randint(Nmin, Nmax)
    M = 0
    Q = random.randint(1, N)
    start = random.randint(1, N)
    end = random.randint(1, N)

    mat = [[-1 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j:
                mat[i][j] = random.randint(-1, 10)
                if mat[i][j] != -1:
                    M += 1

    mandatory = []
    for i in range(Q):
        mandatory.append({random.randint(1, N)})

    return N, M, Q, start, end, mat, mandatory


if __name__ == '__main__':
    N, M, Q, start, end, mat, mandatory = generateRandom(5, 5)
    writeToFile(N, M, Q, start, end, mat, mandatory, "data1.dzn")
