import os, json
from covidsimulation.simulation.covid_simulation import COVIDSimulation

# In order for multiprocessing to work this has to be in a separate file to __main__
def output(output_file, data):
    '''
    Create output data file and output to specified output file, if the output already contains data then the new data will be appended to the data file
    '''
    # check directory exists and create if not
    if (not os.path.exists(os.path.dirname(output_file))) and (os.path.dirname(output_file) != ""):
        os.makedirs(os.path.dirname(output_file))
    
    # output data
    with open(output_file, 'w') as outfile:
        outfile.write(json.dumps(data, indent=4))

def run(params, from_network=None):

    sim = COVIDSimulation(params, from_network=from_network)
    return sim.run()

def runAndOutput(params, network_input_file, output_file, network_output_file, use_full_agent_state=False):
    # Run simulation
    sim = COVIDSimulation(params, use_full_agent_state, from_network=network_input_file)
    data = sim.run()

    # Output result
    output(output_file, data.serialiseOutput())
    if network_output_file is not None: # network output requested
        output(network_output_file, data.serialiseNetwork(sim))
