import copy
import subprocess, os
import json
import pytest

# ========================================================================
# TESTING NOTES
#
# This is the most simple test, it will run the simulation once with the following conditions: 
# - Reduce the number of steps to reduce time to run test
# - Fix the random seed to get a deterministic outcome
# - Compare key statistics to known output values, the values are secondary as this is to catch breaking changes
#  
# We expect to change this if the number of random calls changes, or if the interface changes. 
# However, ideally the interface to this file will remain the same so changes are localised.

def test_covid_sim_basic(test_files):

    test_name = os.path.basename(__file__)
    # ========================================================================
    #				   covid_simulation call (using params)

    output_sim_dir = os.path.join(test_files.output_dir, 'results')
    output_sim_file = os.path.join(output_sim_dir, 'output.json')
    output_sim_file2 = os.path.join(output_sim_dir, 'output2.json')
    output_network_file = os.path.join(output_sim_dir, 'network.json')
    output_network_file2 = os.path.join(output_sim_dir, 'network2.json')

    command1 = ['python', '-m',
        test_files.covidsimulation, 
        '-o', output_sim_file, 
        '--o-network', output_network_file,
        '--param-files', 
        test_files.params_example,
        test_files.fixed_seed]

    runTwiceAndCheckSame(command1, output_sim_file, test_name)

    # ========================================================================
    #				   covid_simulation call (using network)
    command2 = ['python', '-m',
        test_files.covidsimulation, 
        '-o', output_sim_file2, 
        '--o-network', output_network_file2,
        '--i-network', output_network_file,
        '--param-files', 
        test_files.params_example,
        test_files.fixed_seed]

    runTwiceAndCheckSame(command2, output_sim_file2, test_name)

    # Test that the networks used in both cases are the same
    network1 = loadNetwork(output_network_file)
    network2 = loadNetwork(output_network_file2)
    assert network1 == network2

def loadNetwork(network_file):
    with open(network_file, 'r') as infile:
        return json.loads(infile.read())

def runTwiceAndCheckSame(command, output_file, test_name):
    data = runAndGetData(
        command,
        output_file,
        test_name    
    )
    expected = copy.deepcopy(data['health_states'][299])

    data = runAndGetData(
        command,
        output_file,
        test_name
    )
    values = data['health_states'][299]

    # Check run matches expected values when run again (deterministic with fixed seed)
    for i in range(len(values)):
        assert values[i] == expected[i]

def runAndGetData(command, output_file, test_name):
    result = subprocess.run(command)

    # check no error code
    assert result.returncode == 0, ('%s Failed, covid sim exited with non 0 return code' % test_name)

    # Check the output exists
    assert os.path.exists(output_file), ('%s Failed, covid sim did not produce an output' % test_name)

    # Check the data in the output is some json
    data = None
    with open(output_file, 'r') as infile:
        data = json.loads(infile.read())
    assert data is not None
        
    return data
