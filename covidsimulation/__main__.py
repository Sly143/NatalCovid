import json
import jsonmerge

import argparse
import os
from multiprocessing import Pool

import covidsimulation.run

def buildJSONfromArgs():
    '''
    Creates JSON object from passed arguments
    '''
    # Specify how to interpret command line arguments
    default_output = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'analysis', 'sim_results', 'output.json') 

    parser = argparse.ArgumentParser(description="Covid agent simulation tool")

    parser.add_argument('-o', help='output file path for data', default=default_output)
    parser.add_argument('--o-network', help='output file path for complex network')
    parser.add_argument('--full-agents', action='store_true', help='If set along with output network, includes agents current state in the network description')
    parser.add_argument('--i-network', help='a JSON network description file')
    parser.add_argument('--param-files', nargs='+', help='a list of JSON parameter files, files will overwrite parameters in order passed')
    parser.add_argument('--multi-run', help='How many simulations to run', type=int, default=1)

    # parse arguments
    args = parser.parse_args()

    # load json files and merge into single representation
    params = None
    for param_file in args.param_files:
        with open(param_file, 'r') as infile:
            j = json.loads(infile.read())
            params = jsonmerge.merge(params, j)
    # validating args
    validateJSON(params)

    # load input network if specified
    input_network = None
    if args.i_network:
        with open(args.i_network) as infile:
            input_network = json.loads(infile.read())

    # format argument list for simulations
    number_of_sims = args.multi_run
    # get output files for each run
    output_files = generateFileParameters(args.o, number_of_sims)
    if args.o_network:
        network_output_files = generateFileParameters(args.o_network, number_of_sims)
    else:
        network_output_files = [None] * number_of_sims # else create empty arguments

    # format of simulation arguments
    arguments = []
    for i in range(number_of_sims):
        arguments.append((params, input_network, output_files[i], network_output_files[i], args.full_agents))
    return arguments
 
def validateJSON(params):
    '''
    Converts JSON into internal variables

    May be preferable in future not to convert the model, but just to use it directly
    '''
    minimum_params = ['population', 'epidemy', 'sim']

    for i in minimum_params:
        if i not in params.keys():
            print("\nError! The parameter [{}] are missing!".format(i))
            print("The minimum parameters are: {}".format(minimum_params))
            print("The current parameters are: {}".format(list(params.keys())))
            exit(1)

def generateFileParameters(output_file, number_of_sims):
    
    output_files = []

    if number_of_sims > 1:
        file_path = output_file.split('.')
        file_path.insert(1, '')
        for i in range(number_of_sims):
            file_path[1] = str(i) + '.'
            output_files.append(''.join(file_path)) 

    else :
        output_files.append(output_file)

    return output_files

def main():
    # Load in parameters from passed arguments
    arguments = buildJSONfromArgs()

    # Run the simulation as many times as requested
    with Pool() as pool:
        pool.starmap(covidsimulation.run.runAndOutput, arguments)

if __name__ == '__main__':
    main()