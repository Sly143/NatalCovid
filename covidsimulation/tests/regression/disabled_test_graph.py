
import subprocess, os
import json
import pytest

# ========================================================================
# TESTING NOTES
#
# This test is to ensure that the output analysis (graph creation) actually produces 
# some output when you run it. It will detect problems with the interface between sim and graph.
#
# Note, it doesn't check if the graph makes any sense, you need to check this manually!

def test_graph(test_files):

    test_name = os.path.basename(__file__)

    # ========================================================================
    #				   covid_simulation call
    output_sim_dir = os.path.join(test_files.output_dir, 'sim_results')
    output_sim_file = os.path.join(output_sim_dir, 'output.json')

    result = subprocess.run(['python', '-m', 
        test_files.covidsimulation, 
        '-o', output_sim_file, 
        '--param-files', 
        test_files.smallcity_params, 
        test_files.epidemy_params, 
        test_files.mobility_params, 
        test_files.sim_params])

    # Check the simulation ran
    assert result.returncode == 0, ('%s Failed, covid sim exited with non 0 return code' % test_name)
    assert os.path.exists(output_sim_file), ('%s Failed, covid sim did not produce an output' % test_name)

    # ========================================================================
    #                 Graph Call 
    output_graph_dir = os.path.join(test_files.output_dir, 'graph')
    output_graph_file = os.path.join(output_graph_dir, 'graph.png')

    result = subprocess.run(['python', '-m',
        test_files.graph, 
        '-o', output_graph_file, 
        output_sim_file])

    assert result.returncode == 0, ('%s Failed, graph exited with non 0 return code' % test_name)
    assert os.path.exists(output_graph_file), ('%s Failed, graph did not produce an output' % test_name)



