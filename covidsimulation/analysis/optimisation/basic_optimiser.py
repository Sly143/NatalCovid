from multiprocessing import Pool
import os, copy

import matplotlib.pyplot as plt
import numpy as np
import jsonmerge, json

from covidsimulation.run import run

def MSE(actual, data):
    total = 0
    for i in range(len(actual)):
        total += (actual[i] - data[i]) ** 2
    return total

class BasicOptimiser(object) :

    def __init__(self, sim_params, free_params, real_data):
        self.actual_confirmed = real_data['confirmed']
        self.actual_deaths = real_data['deaths']

        self.sim_params = sim_params
        self.free_params = free_params
        self.free_params_sim_format = self._createSimFormatParams()
        
        options = real_data['optimiser_options']
        self.num_simulations = options['num_simulations'] 
        self.number_optimisation_steps = options['number_optimisation_steps']
        self.population_size = options['population_size']
        self.agent_factor = options['agent_factor']

        self.number_of_dimensions = len(self.free_params)
    
    def run(self):
        '''
        Implemented by subclasses, will perform the full optimisation process 

        MUST return the best free params found before exiting so the correct solution is output
        '''
        error = np.Infinity # TODO need sensible thresholds
        steps = 0

        best_MSE = np.Infinity
        best_values = None

        while error > 100000 and steps < self.number_optimisation_steps:

            # the basic optimisation is.... random!
            # perform optimisation step (randomly select values for the parameters)
            random_vector = np.random.random(self.number_of_dimensions)

            # set the parameters back into simulation format
            self.setFreeParams(random_vector)

            # run the simulation
            _, _, step_mse = self._simulate()

            # check to see if this is better than the previous best
            if step_mse < best_MSE:
                best_MSE = step_mse
                best_values = copy.deepcopy(random_vector)

            print(steps)
            steps += 1

        # set best free parameters as "answer"
        return best_values
        
    def output(self, best_values):  
        # re run best setting
        self.setFreeParams(best_values)
        average_confirmed, average_deaths, mse = self._simulate()

        # visualise the data
        self._visualise(average_confirmed, average_deaths)
        print("MSE : %d" % mse)

        # output the parameters
        with open('output_free_params.json', 'w') as outfile:
            outfile.write(json.dumps(self.free_params_sim_format, indent=4))

    def _createSimFormatParams(self):

        sim_format_free_params = {}
        for key in self.free_params:

            path = sim_format_free_params
            for i, path_segment in enumerate(self.free_params[key]['path']):

                if i == len(self.free_params[key]['path']) - 1:
                    path[path_segment] = self.free_params[key]['scale']
                    self.free_params[key]['type'] = type(self.free_params[key]['scale'])

                elif path_segment not in path:
                    path[path_segment] = {} 
                
                path = path[path_segment]
        return sim_format_free_params

    def setFreeParams(self, vector):
        '''
        vector of floats [0, 1] which are converted to the parameter format used by the simulation
        '''
        # make sure vector is valid
        for i in range(len(vector)):
            if vector[i] < 0:
                vector[i] = 0.0 # all values must be positive
            if vector[i] > 1:
                vector[i] = 1.0 # all values must be less than 1 (some variables encode probabilities)

        for i, key in enumerate(self.free_params):

            path = self.free_params_sim_format
            for j, path_segment in enumerate(self.free_params[key]['path']):

                if j == len(self.free_params[key]['path']) - 1:  
                    value = self.free_params[key]['scale'] * vector[i]
                    path[path_segment] = self.free_params[key]['type'](value)
                else:
                    path = path[path_segment]

    def _simulate(self): 
        '''
        convienience function, calls the simulation num_runs times using the current setting of sim/free params. it then averages the data from the runs and returns the averaged data and mean squared error
        '''
        # construct arguments
        self.sim_params = jsonmerge.merge(self.sim_params, self.free_params_sim_format)
        arguments = [(self.sim_params,)] * self.num_simulations

        # run simulations
        with Pool() as pool:
            returns = pool.starmap(run, arguments)

        # average data and calculate error
        average_confirmed, average_deaths = self._average_data(returns)
        # mse = MSE(self.actual_confirmed, average_confirmed) + MSE(self.actual_deaths, average_deaths)
        mse = MSE(self.actual_deaths, average_deaths)
        return average_confirmed, average_deaths, mse

    def _average_data(self, data):

        num_days = len(data[0].getConfirmedCases())

        average_confirmed = [0] * num_days
        average_deaths = [0] * num_days

        # get totals     
        for run in data:
            confirmed = run.getConfirmedCases()
            deaths = run.getDeaths()

            for day in range(num_days):
                average_confirmed[day] += confirmed[day]
                average_deaths[day] += deaths[day]

        # divide by number of runs to get average
        for day in range(len(confirmed)):
            average_confirmed[day] = (average_confirmed[day] / self.num_simulations) * self.agent_factor # scale results to population level
            average_deaths[day] = (average_deaths[day] / self.num_simulations) * self.agent_factor # scale results to population level

        return average_confirmed, average_deaths

    def _plotData(self, ax, data, actual, ylabel):
        ax.set_xlim([0,len(data)])

        ax.set_ylabel(ylabel) # TODO make it use "messages.json"
        ax.set_xlabel('days')

        days = range(len(data))
        ax.plot(days, data)
        ax.plot(days, actual)

    def _visualise(self, average_confirmed, average_deaths):
        fig, (ax1, ax2) = plt.subplots(1, 2)
        # self._plotData(ax1, average_confirmed, self.actual_confirmed, 'confirmed')
        self._plotData(ax2, average_deaths, self.actual_deaths, 'deaths')

        fig.savefig('output.png', format='png', dpi=300)




            