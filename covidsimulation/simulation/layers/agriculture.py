import numpy as np

from covidsimulation.simulation.layers.layer import NetworkLayer, chooseUniform

LAYER_KEY = 'agriculture'

class Agriculture(NetworkLayer):

    def __init__(self, p_contamination, network_params):
        super().__init__(LAYER_KEY, p_contamination, network_params)

        # get parameters
        self.size = self.layer_params['size']
        self.exposed_hours_per_week = self.layer_params['exposed_hours_per_week']
        self.average_num_contacts = self.layer_params['average_num_contacts']
        self.included_groups = self.layer_params['included_groups']
        self.percentage_included = self.layer_params['percentage_included']
        
    def fromParams(self, population):

        # Create network
        # filter based on age groups
        filtered_indexes = [ i for i in range(len(population)) if self.included_groups[population[i].age_group]]

        self._createConnectionsUniformByProbability(
            population,
            filtered_indexes, 
            self.size[0],
            self.size[1],
            self.percentage_included)

    def getPInteraction(self, agent):
        return self._calculateInteractionProbabilityAndGroupFactor(self.exposed_hours_per_week, self.average_num_contacts, len(self.nodes[agent]))

    def chooseContacts(self, agent):
        if agent in self.nodes: 
            return chooseUniform(self.nodes[agent], self.average_num_contacts)
        # not of working age
        return []
