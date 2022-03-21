import numpy as np
import matplotlib.pyplot as plt
import json
import argparse
import os, sys

import covidsimulation.common.health_states as health_states

class Graph:

    def __init__(self, output_file, save, language, data):
        self.output_file = output_file
        self.save = save
        self.language = language
        self.data = data

        font_size = 16
        self.lines = 4
        self.columns = 2
        self.font = {'family' : 'arial',
                'weight' : 'bold',
                'size'   : font_size}
        plt.rc('font', **self.font)
        self.fig = plt.figure(figsize=(30.20,10.80))
        self.fig.subplots_adjust(left=0.05, bottom=0.03, 
            right=0.99, top=0.97,wspace=0.14,hspace=0.26)

    def makeAxes(self, x, y, data, ylabel):
        ax = plt.subplot2grid((self.lines, self.columns), (x, y))
        plt.plot(data)

        ax.set_xlim([0,len(data)])
        ax.set_ylabel(messages[self.language][ylabel])
        ax.set_xlabel(messages[self.language]['days'])
        #ax.set_yscale('log')
        #ax.set_ylim((10**1,10**7))
        ax.get_xaxis().set_tick_params(which='minor', size=0, width=0)

        return ax

    def run(self):

        health_states_data = np.array(self.data['health_states'])
            
        #               Infections
        infected_states = [health_states.incubated] + health_states.infectious_states
        infected = np.sum(health_states_data[:,infected_states], axis=1)
        ax1 = self.makeAxes(0,0, infected, 'infected')

        #               Accumulated snapshot
        most_states = health_states.infectious_states + [health_states.dead, health_states.incubated]
        most_data = np.sum(health_states_data[:,most_states], axis=1)
        ax2 = self.makeAxes(0,1, most_data, 'positives_accumulated')

        #               Deaths by day
        deaths_per_day = health_states_data[1:,health_states.dead] - health_states_data[:-1,health_states.dead] # This is magic?
        ax3 = self.makeAxes(1,0, deaths_per_day, 'deaths_per_day')
        ax3.set_yscale('linear')
        ax3.set_ylim(0, np.max(deaths_per_day))

        #               Death accumulated
        deaths = np.sum(health_states_data[:,[health_states.dead]], axis=1)
        ax4 = self.makeAxes(1,1, deaths, 'deaths_accumulated')

        poptotal = sum(health_states_data[0])
        percentages = 100 * most_data / poptotal
        ax6 = self.makeAxes(2,1, percentages, 'percentage_infected')
        ax6.set_yscale('linear')
        ax6.set_ylim((0, 100))

        #               ICU 
        icu_usage = health_states_data[:,health_states.ICU] 
        ax7 = self.makeAxes(3,0, icu_usage, 'icu')
        ax7.plot([0,300],[317,317],'--r',label=messages[language]['icus'])
        ax7.plot([0,300],[648,648],'--k',label=messages[language]['respirators'])
        ax7.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

    def output(self):
        if self.save:

            # check directory exists and create if not
            if (not os.path.exists(os.path.dirname(output_file))) and (os.path.dirname(output_file) != ""):
                os.makedirs(os.path.dirname(output_file))

            self.fig.savefig(output_file, format='png', dpi=300)
        else: 
            plt.show()

def validLanguage(string):
    if string not in messages: # not a supported language
        raise argparse.ArgumentTypeError('%s is not one of the supported languages %s' % (string, messages.keys()))
    return string

def parseArgs():

    default_output = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'graph.png')

    parser = argparse.ArgumentParser(description='Graph utility for Covid Simulation')

    parser.add_argument('--no-save', help='if set, this will NOT save output as an image', dest='save', action='store_false')
    parser.add_argument('--save', help='if set, this will save output as an image (default)', dest='save', action='store_true', default=True)
    parser.add_argument('-o', help='output file name if save requested', default=default_output)
    parser.add_argument('--language', help='set the language used for output', type=validLanguage, default='english')
    parser.add_argument('rest', nargs=argparse.REMAINDER) # file specified last

    # parse arguments
    args = parser.parse_args()

    # check for funny business
    if len(args.rest) != 1:
        print('Expected one unamed argument specifying the data file to analyse, got %s' % args.rest)
        exit(1)

    with open(args.rest[0], 'r') as infile:
        j = json.loads(infile.read())

    return (args.o, args.save, args.language, j)

if __name__ == '__main__':
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'translate_language.json'), 'r', encoding='utf8') as json_file: # convert to messages.json and make it common
        messages = json.load(json_file)

    output_file, save, language, data = parseArgs()
    g = Graph(output_file, save, language, data)
    g.run()
    g.output()
