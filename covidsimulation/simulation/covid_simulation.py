import numpy as np
from numba import jit

from covidsimulation.simulation.data_collector import DataCollector
from covidsimulation.simulation.agent import Agent
from covidsimulation.simulation.network import Network
from covidsimulation.simulation.events import Event

import covidsimulation.common.health_states as health_states

@jit(nopython=True)
def setNumbaSeed(seed): # pragma: no cover
    '''
    To have deterministic runs you need to set the seed of numpy and numba
    '''
    np.random.seed(seed) 

class COVIDSimulation:

    def __init__(self, params, use_full_agent_state=False, from_network=None):
        
        #  full agents state
        self.use_full_agent_state = use_full_agent_state
        
        # sim params
        sim_params = params['sim']
        self.seed = sim_params['seed']
        self.days = sim_params['days']

        # if requested, fix the random seed (parts of initialisation are stochastic e.g. outcomes, ages, network)
        if self.seed is not None:
            np.random.seed(self.seed)
            setNumbaSeed(self.seed)

        # epidemy params
        epidemy_params = params['epidemy']
        self.p_contamination = epidemy_params['p_contamination']
        self.t_incubation = epidemy_params['t_incubation']
        self.t_discharge = epidemy_params['t_discharge']
        self.t_hospital = epidemy_params['t_hospital']
        self.initial_infected = epidemy_params['initial_infected']

        # intervention params
        self.events = []
        if 'events' in params: # check optional parameter exists 
            event_params = params['events']
            self.events = [ Event(event_params[event]) for event in event_params ]

        # population params
        population_params = params['population']
        self.population_total = population_params['population_total']

        self.network = Network(self.p_contamination, population_params['network'])
        # argsO_
        # TODO check if already exist another network
        if from_network is None: # no premade network specified
            # outcome distribution params
            outcome_distributions = population_params['outcome_distributions']
            self.age_range = outcome_distributions['age_range']
            ages = np.random.choice(
                    len(outcome_distributions['age_distribution']),
                    size=self.population_total,
                    p=outcome_distributions['age_distribution'])

            incubation_times = np.random.lognormal(
                self.t_incubation[0],
                self.t_incubation[1], 
                size=self.population_total)

            health_outcomes = self._assignHealthOutcomes(
                ages, 
                outcome_distributions)

            # network params and population
            self.population = self._createPopulation(
                ages,
                health_outcomes,
                incubation_times)

            # initialise/generate network from parameters
            self.network.fromParams(self.population)

        else: # premade network specified
            
            self.age_range = from_network['age_range']
            self.population = []
            for entry in from_network['population']:
                agent_entry = entry['agent']

                # create agent
                if self.use_full_agent_state and 'days_exposed' in agent_entry:
                    agent = Agent(
                        agent_entry['age_group'],
                        agent_entry['health_outcome'],
                        agent_entry['incubation_time'],
                        agent_entry['days_exposed'],
                        agent_entry['days_with_symptoms'],
                        agent_entry['health_state'],
                    )
                else:
                    agent = Agent(
                        agent_entry['age_group'],
                        agent_entry['health_outcome'],
                        agent_entry['incubation_time'],
                    )
                self.population.append(agent)

                # add agent to network
                for layer_entry in agent_entry['network']:
                    for layer in self.network.layers: # TODO convert to dict to make this cleaner
                        if layer_entry == layer.name:
                            layer.nodes[agent] = np.array(agent_entry['network'][layer_entry]) # type compatability with numba, TODO anyway to simplify this?

        # choose individuals to start with the disease, set health state
        initial_infected = np.random.choice(self.population, self.initial_infected, replace=False)
        for agent in initial_infected:
            agent.health_state = health_states.incubated

    def runUntilFirstConfirmed(self, limit=100):
        '''
        Used to initialise the state of the simulation to the first confirmed case, which is when real data begins to be relevant

        to avoid simulating forever if the virus does not spread sufficiently, a threshold is placed 
        '''
        steps = 0
        first_case = False
        while (not first_case) and steps < limit: 

            # Meet people in the same population and between populations
            self.network.calculateInteractions(self.population, self.p_contamination)

            for agent in self.population:
                # Update disease state machine for each agent
                agent.cycleDisease(self)

                if agent.confirmed_case:
                    first_case = True
                    break
            
            steps += 1
        
        return steps
        
    def run(self):

        # Start data tracking
        data = DataCollector(self.days) 

        # Run simulation
        for current_day in range(self.days):
            
            # determine if any event triggers occur
            for event in self.events:
                event.checkAndApply(current_day+1, self)
            
            # Meet people in the same population and between populations
            self.network.calculateInteractions(self.population, self.p_contamination)

            for agent in self.population:
                # Update disease state machine for each agent
                agent.cycleDisease(self)

            # Store data for this day
            data.collect(self.population)

        return data

    def _assignHealthOutcomes(self, ages, outcome_params):
        data_health_outcomes = np.zeros(self.population_total)

        for i in range(len(outcome_params['age_range'])):
            # Get probability distribution of health outcomes for this age group
            pp = np.zeros((6))  # Every round, create a empty array of length = 6
            pp[0] = outcome_params['p_asymptomatic'][i]
            pp[1] = outcome_params['p_symptomaticLight'][i]
            pp[2] = outcome_params['p_symptomaticMedium'][i]
            pp[5] = outcome_params['p_dead'][i]
            pp[3] = outcome_params['p_hospital'][i] - pp[5]
            pp[4] = outcome_params['p_ICU'][i] - pp[3] - pp[5]
            if (pp[4] < 0): # TODO can this happen, can we clarify the above or make it something we check is true in the parameters instead?
                pp[4] = 0.0

            # randomly assign a health outcome to all the population in this age category
            match_age = ages == i
            data_health_outcomes[match_age] = np.random.choice(health_states.health_outcomes, size=np.sum(match_age), p=pp)
        
        return data_health_outcomes

    def _createPopulation(self, ages, outcomes, incubations):

        population = []

        # create agents
        for i in range(self.population_total):
            population.append(
                Agent(ages[i], 
                    outcomes[i], 
                    incubations[i]))

        return population
    

