# pytest protected name do not change

import pytest, json, os

from covidsimulation.simulation.agent import Agent
from covidsimulation.simulation.covid_simulation import COVIDSimulation

import covidsimulation.common.health_states as health_states

@pytest.fixture()
def population():

    # Setup
    # TODO better initialisation of test population values
    population = []
    population.append(Agent(0, health_states.asymptomatic, 5))
    population.append(Agent(0, health_states.symptomaticLight, 5))
    population.append(Agent(0, health_states.symptomaticMedium, 5))
    population.append(Agent(0, health_states.hospital, 5))
    population.append(Agent(0, health_states.ICU, 5))

    # Resource
    yield population

    # Teardown

@pytest.fixture()
def sim():

    # TODO this is bad but we need to make the agent interface not require the simulation object to improve it
    project_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..', '..')
    parameter_dir = os.path.join(project_path, 'covidsimulation', 'data', 'params') 
    params_example = os.path.join(parameter_dir, 'tests', 'params_example.json') 
    with open(params_example, 'r') as infile:
        j = json.loads(infile.read())
    sim = COVIDSimulation(j) 

    yield sim
