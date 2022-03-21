# pytest protected name do not change

import pytest
import os, shutil

class RegressionTestUtil:

    def __init__(self):
        
        self.project_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..', '..') 
        self.output_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'results')

        self.covidsimulation = 'covidsimulation'
        self.graph = 'covidsimulation.analysis.graph'

        parameter_dir = os.path.join(self.project_path, 'covidsimulation', 'data', 'params') 
        self.params_example = os.path.join(parameter_dir, 'tests', 'params_example.json')
        self.params_scabinietal = os.path.join(parameter_dir, 'tests', 'params_ScabiniEtAl.json')
        self.fixed_seed = os.path.join(parameter_dir, 'tests', 'fixed_seed.json')

    def ensure_output_clean(self):
        if os.path.exists(self.output_dir):
            shutil.rmtree(self.output_dir)

@pytest.fixture()
def test_files():

    # Setup
    test_files_container = RegressionTestUtil()
    test_files_container.ensure_output_clean()

    # Resource
    yield test_files_container

    # Teardown
    test_files_container.ensure_output_clean()

    