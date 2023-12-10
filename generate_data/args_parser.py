import argparse

def get_arguments():
    parser = argparse.ArgumentParser(description='Script with named arguments N and file.')

    parser.add_argument('-N', type=int, help='Value for N', required=True)
    parser.add_argument('--file', type=str, help='File name', required=True)

    args = parser.parse_args()

    N_value = args.N
    file_value = args.file

    return N_value, file_value