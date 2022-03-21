import numpy as np

import covidsimulation.common.health_states as health_states
from covidsimulation.common.util import chooseContactsNoReplace

class Event(object):

    def __init__(self, event_params):
        self.trigger_day = event_params['day']
        self.adjust_p_contamination = None
        self.new_contacts = None

        if 'adjust_p_contamination' in event_params:
            self.adjust_p_contamination = event_params['adjust_p_contamination']
        if 'external_contacts' in event_params:
            self.new_contacts = event_params['external_contacts']

    def checkAndApply(self, current_day, sim):

        if current_day == self.trigger_day: # today is the day the intervention takes place

            # adjust p_contamination
            if self.adjust_p_contamination:
                for layer in sim.network.layers:
                    if layer.name in self.adjust_p_contamination: # if this layer designated for modification
                        # modify p_contamination for this layer
                        layer.p_contamination = self.adjust_p_contamination[layer.name]

            # simulate external contacts to the network
            if self.new_contacts:
                susceptiblePopulation = []
                # select only susceptible agents
                for i in range(len(sim.population)):
                    if sim.population[i].health_state == health_states.susceptible:
                        susceptiblePopulation.append(i)

                contacted = chooseContactsNoReplace(np.array(susceptiblePopulation), self.new_contacts)
                # choose and infected agents susceptible
                for i in contacted:
                    agent = sim.population[i]
                    if agent.health_state == health_states.susceptible:
                        agent.health_state = health_states.incubated
