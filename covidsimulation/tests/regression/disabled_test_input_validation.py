import subprocess, os, shutil
import json
import pytest

# ========================================================================
# TESTING NOTES
#
# This test will verify if the minimum parameters are passing on input
# The minimum parameters are: age_range, mobility_events, city_structure, 
# seed, days, initial_infected
#
# Note, it doesn't check if the output makes any sense, you need to check this manually!


def test_input_validation_nomobility(test_files):

    test_name = os.path.basename(__file__)

    # ========================================================================
    #             covid_simulation call
    output_sim_dir = os.path.join(test_files.output_dir, 'results')
    output_sim_file = os.path.join(output_sim_dir, 'output.json')

    result = subprocess.run(['python', '-m',
        test_files.covidsimulation, 
        '-o', output_sim_file, 
        '--param-files', 
        test_files.smallcity_params, 
        test_files.epidemy_params, 
        test_files.sim_params, 
        test_files.test_params], stdout=subprocess.PIPE)

    # ========================================================================
    #                 Tests
    assert (not (result.returncode == 0)), ('%s Failed, validation returned success error code when it should have raised an error' % test_name)
    
    console_log = result.stdout.decode("utf-8")
    assert "Error! The parameter [mobility_events] are missing" in console_log, ('%s Failed, mobility_events should have been identified as missing' % test_name)

def test_input_validation_nocity(test_files):

    test_name = os.path.basename(__file__)

    # ========================================================================
    #             covid_simulation call
    output_sim_dir = os.path.join(test_files.output_dir, 'results')
    output_sim_file = os.path.join(output_sim_dir, 'output.json')

    result = subprocess.run(['python', '-m',
        test_files.covidsimulation, 
        '-o', output_sim_file, 
        '--param-files', 
        test_files.mobility_params, 
        test_files.epidemy_params, 
        test_files.sim_params, 
        test_files.test_params], stdout=subprocess.PIPE)

    assert (not (result.returncode == 0)), ('%s Failed, validation returned success error code when it should have raised an error' % test_name)
    
    console_log = result.stdout.decode("utf-8")
    assert "Error! The parameter [city_structure] are missing" in console_log, ('%s Failed, mobility_events should have been identified as missing' % test_name)

def test_input_validation_noOParam(test_files):

    test_name = os.path.basename(__file__)

    output_sim_directory = os.path.join(test_files.project_path, 'covidsimulation', 'analysis', 'sim_results')
    output_sim_file = os.path.join(output_sim_directory, 'output.json')
    output_sim_file_rename = os.path.join(output_sim_directory, 'outputTemp.json')
    
    os.rename(output_sim_file, output_sim_file_rename)

    result = subprocess.run(['python', '-m',
        test_files.covidsimulation,
        '--param-files',
        test_files.smallcity_params,
        test_files.mobility_params, 
        test_files.epidemy_params, 
        test_files.sim_params, 
        test_files.test_params])

    assert (result.returncode == 0), ('%s Failed, expected 0 but return code was not 0' % test_name)
    assert (os.path.exists(output_sim_file)), ('%s Failed, covid sim did not produce an output' % test_name)

    os.remove(output_sim_file)
    os.rename(output_sim_file_rename, output_sim_file)
    