import argparse

def get_arguments():
    parser = argparse.ArgumentParser(description='Script with named arguments N and timeout.')

    parser.add_argument('-N', type=int, help='Value for N', required=True)
    parser.add_argument('--timeout', type=int, help='Timeout in seconds', required=True)

    args = parser.parse_args()

    N_value = args.N
    timeout_value = args.timeout

    return N_value, timeout_value