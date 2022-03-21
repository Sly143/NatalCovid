import os
import subprocess

def profile():
    project_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..', '..') 
    covidsimulation = 'covidsimulation'

    parameter_dir = os.path.join(project_path, 'covidsimulation', 'data', 'params') 
    params_scabinietal = os.path.join(parameter_dir, 'tests', 'params_ScabiniEtAl.json')

    real_outcomes_dir = os.path.join(project_path, 'covidsimulation', 'data', 'real_outcomes')
    days = os.path.join(real_outcomes_dir, 'days.json')
    free_params = os.path.join(real_outcomes_dir, 'free_params.json')

    output_dir = os.path.dirname(os.path.realpath(__file__))
    profile_output = os.path.join(output_dir, 'covid_simulation.prof')

    # TODO how do I make this work with packages
    result = subprocess.run([
        'python', '-m', 'cProfile', '-o', profile_output, 
        '-m', 
        covidsimulation, 
        '--multi-run', 
        '16', 
        '--param-files', 
        params_scabinietal,
        days,
        free_params])

    if not (result.returncode == 0):
        print('covid simulation exited with non zero exit code, stopping profiling')
        exit(1)

    subprocess.run(['snakeviz', profile_output])
    # wont exit, interupt when done with the visualisation


if __name__ == '__main__':
    profile()