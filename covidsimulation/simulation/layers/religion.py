from covidsimulation.simulation.layers.layer import NetworkLayer, chooseUniform

LAYER_KEY = 'religion'

class Religion(NetworkLayer):

    def __init__(self, p_contamination, network_params):
        super().__init__(LAYER_KEY, p_contamination, network_params)

        # get parameters
        self.size = self.layer_params['size']
        self.exposed_hours_per_week = self.layer_params['exposed_hours_per_week']
        self.average_num_contacts = self.layer_params['average_num_contacts']
        self.percentage_included = self.layer_params['percentage_included']

    def fromParams(self, population):

        # Create network
        # filter based on fixed percentage
        indexes = chooseUniform(len(population), int(len(population)*self.percentage_included))
        filtered_indexes = [ i for i in indexes]

        self._createConnectionPareto(
            population, 
            filtered_indexes,
            self.size[0],
            self.size[1])
            
    def getPInteraction(self, agent):
         return self._calculateInteractionProbabilityAndGroupFactor(self.exposed_hours_per_week, self.average_num_contacts, len(self.nodes[agent]))

    def chooseContacts(self, agent):
        if agent in self.nodes: 
            return chooseUniform(self.nodes[agent], self.average_num_contacts)
        # not religious
        return []
