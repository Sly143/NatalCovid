# Complex network model of coronavirus based on https://arxiv.org/pdf/2005.08125.pdf

from covidsimulation.simulation.layers.layer import chooseUniform, isExposed

from covidsimulation.simulation.layers.home import Home
from covidsimulation.simulation.layers.work import Work
from covidsimulation.simulation.layers.transport import Transport
from covidsimulation.simulation.layers.school import School
from covidsimulation.simulation.layers.religion import Religion
from covidsimulation.simulation.layers.random import Random

import covidsimulation.common.health_states as health_states

class Network(object):
    
    def __init__(self, p_contamination, network_params):

        self.layers = []
        self.layers.append(Home(p_contamination, network_params))
        self.layers.append(Work(p_contamination, network_params))
        self.layers.append(Transport(p_contamination, network_params))
        self.layers.append(School(p_contamination, network_params))
        self.layers.append(Religion(p_contamination, network_params))
        self.layers.append(Random(p_contamination, network_params))
    
    def fromParams(self, population):
        for layer in self.layers:
            layer.fromParams(population)

    def calculateInteractions(self, population, p_contamination):

        for agent in population:

            # Only simulate movement for infected
            if agent.health_state in health_states.infectious_states: 

                # Calculate social interactions in each of the networks
                for network in self.layers:
                    
                    # Choose agents to interact with based on network criteria
                    contacts = network.chooseContacts(agent)
                    
                    # Set health status of those exposed to virus who are susceptible
                    for i in contacts:
                        if (population[i].health_state == health_states.susceptible and isExposed(network.getPInteraction(agent), network.p_contamination)):
                                population[i].health_state = health_states.incubated
