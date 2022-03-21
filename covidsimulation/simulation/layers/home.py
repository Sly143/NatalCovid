import numpy as np
import copy

from covidsimulation.simulation.layers.layer import NetworkLayer

LAYER_KEY = 'home'

class Home(NetworkLayer):

    def __init__(self, p_contamination, network_params):
        super().__init__(LAYER_KEY, p_contamination, network_params)

        # get parameters
        self.size = self.layer_params['size']
        exposed_hours_per_week = self.layer_params['exposed_hours_per_week']
        self.p_family_size = self.layer_params['p_family_size']

        # calculate interaction probability as it is fixed
        # group factor is one because every member of the group is contacted 
        self.p_interaction = self._calculateInteractionProbability(exposed_hours_per_week, 1)

    def fromParams(self, population):

        # Create network
        # no filter all population used
        indexes = [ i for i in range(len(population))]
        self._createConnections(
            population,
            indexes,
            self.size[0],
            self.size[1],
            self._choosePFamily
        )

    def getPInteraction(self, agent):
        return self.p_interaction

    def chooseContacts(self, agent):
        # contact everyone at home
        return self.nodes[agent]

    def _choosePFamily(self, group_sizes):
        return np.random.choice(group_sizes, p=self.p_family_size)


