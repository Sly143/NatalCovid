import csv, os, json

def loadData(file_name):
    with open(file_name) as infile:
        csv_reader = csv.reader(infile, delimiter=';')
        totals = []
        first_line = True
        for row in csv_reader: 
            if first_line:# skip titles
                first_line = False
                continue

            # 87th colomn is Natal
            totals.append(int(float(row[87])))
    
    return totals

def output(output_file, data):
    this_dir = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(this_dir, output_file), 'w') as outfile:
        outfile.write(json.dumps(data, indent=4))

def freeParam(scale, pathsegments):
    return {
        'scale' : scale,
        'path' : pathsegments
    }
    
def main():
    this_dir = os.path.dirname(os.path.realpath(__file__))
    confirmed = loadData(os.path.join(this_dir, 'RN_CIDADES_covid20_confirmed_SINTOMA.csv'))
    deaths = loadData(os.path.join(this_dir, 'RN_CIDADES_covid20_obitos_SINTOMA.csv'))

    data = {
        'optimiser_options' : {
            'num_simulations' : 10, # how many simulations to run per individual evaluation
            'number_optimisation_steps' : 50, # how many iterations of the optimisation algorithm to run 
            'population_size' : 10, # in population based optimisation methods, how many individuals to use
            'agent_factor' : 10, # number of agents may be scaled down to descrease simulation time, this is how much to scale the model numbers by to bring into the range of actual population
            'max_contacts_per_day' : 100 # maximum value for 'external_contacts' and 'initial_infected'
        },
        'confirmed' : confirmed,
        'deaths' : deaths
    }
    output('real_data.json', data)
    # for how long the simulation should be run
    sim = {
        'sim' : {
            'days' : len(confirmed)
        }
    }
    output('days.json', sim)
    # create free parameters format
    free_params = {}
    free_params['initial_p_contamination'] = freeParam(1.0, ['epidemy', 'p_contamination'])
    free_params['initial_infected'] = freeParam(100, ['epidemy', 'initial_infected'])
    for i in range(3): # how many events to use as input parameters
        param_key = 'event_'+str(i)
        free_params[param_key+'_day'] = freeParam(len(confirmed), ['events', param_key, 'day'])
        free_params[param_key+'_external_contacts'] = freeParam(100, ['events', param_key, 'external_contacts'])

        adjust_p_contamination = ['events', param_key, 'adjust_p_contamination']
        free_params[param_key+'_religion'] = freeParam(1.0, adjust_p_contamination+['religion'])
        free_params[param_key+'_school'] = freeParam(1.0, adjust_p_contamination+['school'])
        free_params[param_key+'_transport'] = freeParam(1.0, adjust_p_contamination+['transport'])
        free_params[param_key+'_work'] = freeParam(1.0, adjust_p_contamination+['work'])
        free_params[param_key+'_home'] = freeParam(1.0, adjust_p_contamination+['home'])
        free_params[param_key+'_random'] = freeParam(1.0, adjust_p_contamination+['random'])
    output('free_params.json', free_params)
        
if __name__ == '__main__':
    main()
