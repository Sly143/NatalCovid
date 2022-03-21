import json, argparse

import jsonmerge

from covidsimulation.analysis.optimisation.basic_optimiser import BasicOptimiser
from covidsimulation.analysis.optimisation.pso import PSO
from covidsimulation.analysis.optimisation.ea import EA

'''
These are the keys used in the command line interface to determine which strategy to use, first in the list is the default
'''
EA_MODE = 'EA'
PSO_MODE = 'PSO'
opt_choices = [EA_MODE, PSO_MODE]

def parseArgs():

    parser = argparse.ArgumentParser(description='Optimisation utility for Covid Simulation')

    parser.add_argument('--param-files', nargs='+', help='a list of JSON parameter files, files will overwrite parameters in order passed')
    parser.add_argument('--free-params', help='a file path containing the simulation parameters to be optimised')
    parser.add_argument('--mode', help='which optimisation strategy should be used', choices=opt_choices, default=opt_choices[0])
    parser.add_argument('rest', nargs=argparse.REMAINDER) # file specified last

    # parse arguments
    args = parser.parse_args()

    # get simulation parameters
    params = None
    for param_file in args.param_files:
        with open(param_file, 'r') as infile:
            j = json.loads(infile.read())
            params = jsonmerge.merge(params, j)
    
    # get free parameters
    with open(args.free_params) as infile:
        free_params = json.loads(infile.read()) 

    # check for funny business
    if len(args.rest) != 1:
        print('Expected one unamed argument specifying the data file to analyse, got %s' % args.rest)
        exit(1)

    with open(args.rest[0], 'r') as infile:
        real_data = json.loads(infile.read())

    # create optimiser depending on mode
    if args.mode == EA_MODE:
        return EA(params, free_params, real_data)
    elif args.mode == PSO_MODE:
        return PSO(params, free_params, real_data)
    else:
        print("Error: invalid optimisation mode requested %s" % args.mode)
        exit(1)

def main():
    # run optimiser and output best solution
    opt = parseArgs()
    best_values = opt.run()
    opt.output(best_values)

if __name__ == '__main__':
    main()