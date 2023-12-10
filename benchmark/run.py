import subprocess
import time
import sys
import os

from args_parser import get_arguments

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from generate_data.run import writeToFiles


def run_minizinc_with_timeout(main_file, input_file, timeout):
    command_to_run = ['minizinc', main_file, input_file, '--time-limit', f'{timeout}000']
    process = subprocess.Popen(command_to_run, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process_output = {'stdout': None, 'stderr': None, 'returncode': None}

    start_time = time.time()
    process_output['stdout'], process_output['stderr'] = process.communicate()
    end_time = time.time()

    process_output['returncode'] = process.returncode

    log_file = "benchmark/logs/{}/{}".format(main_file.removesuffix('.mzn').removeprefix('main-'), input_file.split('/')[-1].removesuffix('.dzn') + '.log')
    with open(log_file, 'w') as file:
        file.write('{}\n'.format(process_output['stdout'].decode('utf-8')))
        file.write('{}\n'.format(process_output['stderr'].decode('utf-8')))
        file.write('{}\n'.format(process_output['returncode']))
        file.write('{}\n'.format(end_time - start_time))

    return process_output


def benchmark(N, timeout):
    for i in range(1, 11):
        file_name = f'N_{N}_{i}'
        writeToFiles(N, file_name)
        run_minizinc_with_timeout('main-dpath.mzn', f'generate_data/data/dpath/{file_name}.dzn', timeout)
        run_minizinc_with_timeout('main-adjacent-matrix.mzn', f'generate_data/data/adjacent-matrix/{file_name}.dzn', timeout)
        print(f'Finished N = {N} : {i}/10')


if __name__ == '__main__':
    N, timeout = get_arguments()
    benchmark(N, timeout)