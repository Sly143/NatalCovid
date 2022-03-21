# requires pyswarms, pyyaml
import pyswarms as ps
import numpy as np

from covidsimulation.analysis.optimisation.basic_optimiser import BasicOptimiser

class PSO(BasicOptimiser):

    def __init__(self, sim_params, free_params, real_data):
        super().__init__(sim_params, free_params, real_data)

    def run(self):
        # Set-up hyperparameters
        options = {
            'c1': 0.5, 
            'c2': 0.3, 
            'w':0.9
        }

        x_max = np.ones(self.number_of_dimensions)
        x_min = np.zeros(self.number_of_dimension)
        bounds = (x_min, x_max)

        # Perform optimization
        optimizer = ps.single.GlobalBestPSO(n_particles=self.population_size, dimensions=self.number_of_dimension, options=options, bounds=bounds)
        cost, pos = optimizer.optimize(self.step, iters=self.number_optimisation_steps)

        return pos

    def step(self, positions):
        mses = []
        for pos in positions:
            self._setFreeParams(pos)

            _, _, mse = self._simulate()
            mses.append(mse)
            
        return mses