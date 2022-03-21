# requires deap
from deap import base, creator, tools, algorithms, cma

import numpy as np

from covidsimulation.analysis.optimisation.basic_optimiser import BasicOptimiser

class EA(BasicOptimiser):

    def __init__(self, sim_params, free_params, real_data):
        super().__init__(sim_params, free_params, real_data)

        creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
        creator.create("Individual", list, fitness=creator.FitnessMin)

        self.toolbox = base.Toolbox()
        self.toolbox.register("evaluate", self.evaluate)

        strategy = cma.Strategy(
            centroid=[0.5]*self.number_of_dimensions, # Where the individuals start
            sigma=0.2, # 1/5th of domain [0, 1]
            lambda_=self.population_size # population number?
            )
        self.toolbox.register("generate", strategy.generate, creator.Individual)
        self.toolbox.register("update", strategy.update)

    def run(self):  

        hof = tools.HallOfFame(1)

        algorithms.eaGenerateUpdate(self.toolbox, 
                    ngen=self.number_optimisation_steps, 
                    halloffame=hof)

        return hof[0]

    def evaluate(self, individual):
        self.setFreeParams(individual)
        _, _, mse = self._simulate()
        return mse,