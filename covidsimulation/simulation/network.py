# Complex network model of coronavirus based on https://arxiv.org/pdf/2005.08125.pdf

from covidsimulation.simulation.layers.layer import chooseUniform, isExposed

from covidsimulation.simulation.layers.home import Home
from covidsimulation.simulation.layers.transport import Transport
from covidsimulation.simulation.layers.random import Random
from covidsimulation.simulation.layers.ufrn import Ufrn

# Religion layers
from covidsimulation.simulation.layers.catholic import Catholic
from covidsimulation.simulation.layers.evangelic import Evangelic

# Work layers
from covidsimulation.simulation.layers.agriculture import Agriculture
from covidsimulation.simulation.layers.industry import Industry
from covidsimulation.simulation.layers.construction import Construction
from covidsimulation.simulation.layers.commerce import Commerce
from covidsimulation.simulation.layers.services import Services

# School layers
from covidsimulation.simulation.layers.school_KindergartenPublic import School_KindergartenPublic
from covidsimulation.simulation.layers.school_KindergartenPrivate import School_KindergartenPrivate
from covidsimulation.simulation.layers.school_ElementaryPublic import School_ElementaryPublic
from covidsimulation.simulation.layers.school_ElementaryPrivate import School_ElementaryPrivate
from covidsimulation.simulation.layers.professional_EducationPublic import Professional_EducationPublic
from covidsimulation.simulation.layers.professional_EducationPrivate import Professional_EducationPrivate

import covidsimulation.common.health_states as health_states
import covidsimulation.common.layers as layerList

class Network(object):
    
    def __init__(self, p_contamination, network_params):

        self.layers = []
        self.layers.append(Home(p_contamination, network_params))
        self.layers.append(Transport(p_contamination, network_params))
        self.layers.append(Random(p_contamination, network_params))
        
        # Religion layers
        self.layers.append(Catholic(p_contamination, network_params))
        self.layers.append(Evangelic(p_contamination, network_params))

        # Work layers
        self.layers.append(Agriculture(p_contamination, network_params))
        self.layers.append(Industry(p_contamination, network_params))
        self.layers.append(Construction(p_contamination, network_params))
        self.layers.append(Commerce(p_contamination, network_params))
        self.layers.append(Services(p_contamination, network_params))

        # Schools layers
        self.layers.append(Ufrn(p_contamination, network_params))
        self.layers.append(School_KindergartenPublic(p_contamination, network_params))
        self.layers.append(School_KindergartenPrivate(p_contamination, network_params))
        self.layers.append(School_ElementaryPublic(p_contamination, network_params))
        self.layers.append(School_ElementaryPrivate(p_contamination, network_params))
        self.layers.append(Professional_EducationPublic(p_contamination, network_params))
        self.layers.append(Professional_EducationPrivate(p_contamination, network_params))
        
    def fromParams(self, population):
        for layer in self.layers:
            layer.fromParams(population)

    def calculateInteractions(self, population, p_contamination, sameNeighborhoodProbabilityInteraction):

        for agent in population:

            # Only simulate movement for infected
            if agent.contaminated:
                # Calculate social interactions in each of the networks
                for network in self.layers:
                    # Choose agents to interact with based on network criteria
                    contacts = network.chooseContacts(agent)
                    for i in contacts:
                        # Verify if agents are from the same neighborhood
                        if population[i].neighborhood == agent.neighborhood:
                            pInteraction = network.getPInteraction(agent) * sameNeighborhoodProbabilityInteraction
                        else:
                            pInteraction = network.getPInteraction(agent)
                        # Set health status of those exposed to virus who are susceptible
                        if (population[i].health_state == health_states.susceptible and 
                            isExposed(pInteraction, network.p_contamination)):
                                population[i].health_state = health_states.incubated
                                population[i].getInfectedInLayer = network.name
                                population[i].dayInfected = layerList.layers.index(network.name)
