#!/usr/bin/env python
###############################################################################
# Random search
###############################################################################
import argparse
from cec2013.cec2013 import *
import numpy as np

def main(passed_args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('--budget_multiplier', type=float, default=1, help="Multiplier for budget to control execution time")
    opt = parser.parse_args(passed_args)

    # Demonstration of using how_many_goptima function
    for i in range(1, 21):
        # Create function
        f = CEC2013(i)
        dim = f.get_dimension()

        # Create population of position vectors
        pop_size = int(f.get_maxfes()*opt.budget_multiplier)
        X = np.zeros((pop_size, dim))
        ub = np.zeros(dim)
        lb = np.zeros(dim)
        # Get lower, upper bounds
        for k in range(dim):
            ub[k] = f.get_ubound(k)
            lb[k] = f.get_lbound(k)

        # Create population within bounds
        fitness = np.zeros(pop_size)
        for j in range(pop_size):
            X[j] = lb + (ub - lb) * np.random.rand(1, dim)
			print(j)
            fitness[j] = f.evaluate(X[j])

        # Calculate how many global optima are in the population
        accuracy = 0.001
        count, seeds = how_many_goptima(X, f, accuracy)
        print(f"In the current population there exist {count} global optimizers.")
        print(f"Global optimizers: {seeds}")

if __name__ == "__main__":
    #TODO load algorithm
    main()
