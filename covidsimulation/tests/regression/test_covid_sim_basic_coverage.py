import os, sys
import pytest

from covidsimulation.__main__ import main

# ========================================================================
# TESTING NOTES
#
# similar to the basic but doesn't generate a subprocess so we can get code coverage metrics...
# - Also removed test params so that more simulation is run (therefore more code covered)
# - Uses the intervention params to increas coverage
# - Also uses the network 

def test_covid_sim_basic_coverage(test_files):

    test_name = os.path.basename(__file__)

    output_sim_file = os.path.join(test_files.output_dir, 'results', 'output.json')
    output_network_file = os.path.join(test_files.output_dir, 'results', 'network.json')

    old_args = sys.argv
    sys.argv = [
        'covid_simulation.py',
        '-o',
        output_sim_file,
        '--o-network',
        output_network_file,
        '--param-files',
        test_files.params_example,
        test_files.fixed_seed
    ]
    main()
    sys.argv = old_args
        
    assert (os.path.exists(output_sim_file)), ('%s Failed, covid sim did not produce an output' % test_name)
    assert (os.path.exists(output_network_file)), ('%s Failed, covid sim did not produce an output network' % test_name)

    old_args = sys.argv
    sys.argv = [
        'covid_simulation.py',
        '-o',
        output_sim_file,
        '--i-network',
        output_network_file,
        '--param-files',
        test_files.params_example,
        test_files.fixed_seed
    ]
    main()
    sys.argv = old_args





