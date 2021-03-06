import math
import numpy as np
from numba import jit

@jit(nopython=True)
def chooseUniform(a, size): # pragma: no cover (can't analyse numba functions)
    return np.random.choice(a, size, replace=False)

@jit(nopython=True)
def isExposed(p_interaction, p_contamination): # pragma: no cover (can't analyse numba functions)
    p_threshold = p_interaction * p_contamination
    return np.random.random() < p_threshold

def choosePareto(group_sizes):
    # because group_sizes is a list of sizes in order
    min_group_size = group_sizes[0]
    max_group_size = group_sizes[-1]
    alpha = math.log(5, 4) # power law

    while True:
        group_size = int(np.random.pareto(a=alpha)+min_group_size) 
        if group_size <= max_group_size:
            break
    return group_size

# base class used by specific network layers, TODO better way to enforce this?
class NetworkLayer(object):

    def __init__(self, name, p_contamination, network_params):
        '''
        the following must exist for the interaction algorithm to work
        '''
        self.nodes = {}
        self.name = name
        self.p_contamination = p_contamination
        self.layer_params = network_params[self.name]

    def fromParams(self, population):  # pragma: no cover (implemented in subclass)
        '''
        Should generate the network layer based on the agents and the network parameters
        '''
        return 

    def chooseContacts(self, agent):  # pragma: no cover (implemented in subclass)
        '''
        Should return a list of the agents that have been contacted this timestep 
        '''
        return []
    
    def getPInteraction(self, agent): # pragma: no cover (implemented in subclass)
        '''
        Should return the probability for close interaction with this agent
        '''
        return 0

    def _calculateInteractionProbability(self, exposed_hours, group_factor):
        '''
        num_hours / num hours per week * likelihood of interaction

        can be used by implementing classes to set p_interaction, or an alternative could be used.
        '''
        return (exposed_hours / 168.0) * group_factor 

    def _calculateInteractionProbabilityAndGroupFactor(self, exposed_hours, number_of_contacts, number_of_connections):
        '''
        group factor calculated as the proportion of number of contacts to the overall group size (calculated from the number of connections)
        '''
        size_of_group = number_of_connections + 1 # add self to group
        group_factor = number_of_contacts / size_of_group
        return self._calculateInteractionProbability(exposed_hours, group_factor)

    def _createConnectionsUniform(self, population, filtered_indexes, min_group_size, max_group_size):
        self._createConnections(population, filtered_indexes, min_group_size, max_group_size, np.random.choice)

    def _createConnectionPareto(self, population, filtered_indexes, min_group_size, max_group_size):
        self._createConnections(population, filtered_indexes, min_group_size, max_group_size, choosePareto)

    def _createConnections(self, population, filtered_indexes, min_group_size, max_group_size, size_distribution_func):

        # range of network sizes
        group_sizes = range(min_group_size, max_group_size + 1) # inclusive stop
        
        # randomise the indexes so connections aren't always local
        np.random.shuffle(filtered_indexes)

        # while still have agents to assign
        number_assigned = 0
        while number_assigned != len(filtered_indexes): 

            # Choose group size
            group_size = size_distribution_func(group_sizes)
            # make sure there are enough people to fill the minimum group size
            # TODO this can make a large group at the end bigger than max... not sure if there is something better to do here
            if number_assigned + group_size > len(filtered_indexes) - min_group_size: 
                group_size = len(filtered_indexes) - number_assigned # make sure we have enough people to create this family size

            # Create group from unassigned people
            # TODO simple selection based on order of population, more complex selection is computationally intensive
            for i in range(group_size):
                # get agent for key to nodes
                agent = population[filtered_indexes[number_assigned+i]]
                self.nodes[agent] = []

                # Add everyone who isn't me to my connection
                for j in range(group_size):
                    if i != j:
                        self.nodes[agent].append(filtered_indexes[number_assigned+j])

                self.nodes[agent] = np.array(self.nodes[agent]) # numba type compliance

            # update number assigned
            number_assigned += group_size
