from covidsimulation.simulation.layers.layer import NetworkLayer, chooseUniform

LAYER_KEY = 'random'

class Random(NetworkLayer):

    def __init__(self, p_contamination, network_params):
        super().__init__(LAYER_KEY, p_contamination, network_params)

        # get parameters
        self.size = self.layer_params['size']
        exposed_hours_per_week = self.layer_params['exposed_hours_per_week']
        self.average_num_contacts = self.layer_params['average_num_contacts']

        # calculate interaction probability as it is fixed
        # group factor is 1 because random is 1-1 interaction 
        self.p_interaction = self._calculateInteractionProbability(exposed_hours_per_week, 1)

    def fromParams(self, population):

        # create network
        # no filter all members of the population included, fixed size for groups
        indexes = [i for i in range(len(population))]
        self._createConnectionsUniform(population, indexes, self.size, self.size)

    def getPInteraction(self, agent):
        return self.p_interaction

    def chooseContacts(self, agent):
        return chooseUniform(self.nodes[agent], self.average_num_contacts)