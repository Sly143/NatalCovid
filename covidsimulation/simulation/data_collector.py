import numpy as np
import covidsimulation.common.health_states as health_states
import covidsimulation.common.layers as layers

def countHealthStates(population):
    '''
    returns the number of people in each health state as a list
    '''
    count_states = [0] * (health_states.NUM_INTERNAL_STATES)
    for p in population:
        count_states[p.health_state] += 1
    return count_states

def countHealth_stateStats(population):
    '''
    returns the count of health state by each people
    '''
    for p in population:
        p.health_stateStats[p.health_state] += 1

def countConfirmedCases(population):
    '''
    returns the number of people who have been confirmed to have the virus
    '''
    total = 0
    for p in population:
        if p.confirmed_case:
            total += 1
    return total

def countInfectedByLayer(population):
    '''
    returns the number of people infected in each layers as a list
    '''
    count_states = [0] * (layers.NUM_INTERNAL_STATES)
    for p in population:
        count_states[p.dayInfected] += 1
    return count_states


class DataCollector(object):

    def __init__(self, days):
        self.health_states = []
        self.confirmed_cases = []
        self.infectedByLayer = []
        self.health_stateStats = []


    def collect(self, population):
        '''
        Stores population statistics for the current day
        '''
        self.health_states.append(countHealthStates(population))
        self.confirmed_cases.append(countConfirmedCases(population))
        self.infectedByLayer.append(countInfectedByLayer(population))
        
        # self.health_stateStats.append(countHealth_stateStats(population))

    def serialiseOutput(self):
        '''
        Converts the object representation to a dictionary object to be output
        '''
        data = {
            'health_states' : self.health_states
        }
        return data

    def serialiseNetwork(self, sim):
        '''
        Coverts object representation of agents and network into an output format
        '''
        age_range = sim.age_range
        population = []
        for agent in sim.population:
    
            # get agents network connections
            network = {}
            for layer in sim.network.layers:
                if agent in layer.nodes: # if agent present in this layer
                    network[layer.name] = layer.nodes[agent].tolist()

            # combine network with agent properties
            if sim.use_full_agent_state:
                agent = {
                    'age_group' : int(agent.age_group), # numpy type cannot be serialised
                    'health_outcome' : agent.health_outcome,
                    'incubation_time' : agent.incubation_time,
                    'days_exposed': agent.days_exposed,
                    'days_with_symptoms':agent.days_with_symptoms,
                    'health_state':agent.health_state,
                    'health_stateStats':agent.health_stateStats,
                    'neighborhood' : agent.neighborhood,
                    'agentLayers' : agent.agentLayers,
                    'getInfectedInLayer': agent.getInfectedInLayer,
                    'infectedByLayer': agent.dayInfected,
                    'network' : network
                }
            else:
                agent = {
                    'age_group' : int(agent.age_group), # numpy type cannot be serialised
                    'health_outcome' : agent.health_outcome,
                    'incubation_time' : agent.incubation_time,
                    'neighborhood' : agent.neighborhood,
                    'agentLayers' : agent.agentLayers,
                    'getInfectedInLayer': agent.getInfectedInLayer,
                    'infectedByLayer': agent.dayInfected,
                    'health_stateStats':agent.health_stateStats,
                    'network' : network
                }
            # add to output data
            population.append({ 'agent' : agent })

        # output age range and population
        data = {
            'age_range' : age_range,
            'population' : population
        }
        return data

    def getConfirmedCases(self):
        '''
        The number of tested and confirmed cases accumulated for each day
        '''
        return self.confirmed_cases
 
    def getInfectedByLayerCases(self):
        '''
        The number of infected by each layer; for each day
        '''
        return self.infectedByLayer
    
    
    def getHealthStateStats(self):
        '''
        The agents each health state number of days
        '''
        return self.health_stateStats

    def getDeaths(self):
        return [ day[health_states.dead] for day in self.health_states]
