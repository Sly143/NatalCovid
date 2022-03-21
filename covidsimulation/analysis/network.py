import json
import os, sys
import argparse
import networkx as nx
import matplotlib.pyplot as plt


class Network:
    
    def __init__(self, output_file, save, language, data):

        self.output_file = output_file
        self.save = save
        self.language = language
        self.data = data

        self.home = nx.Graph()
        self.school = nx.Graph()
        self.religion = nx.Graph()
        self.random = nx.Graph()
        self.work = nx.Graph()
        self.transport = nx.Graph()

        self.nodeColor = '#0099FF'
        self.edge_color = ['#FF0000','#006633','#666666','#CCCCCC','#FF9900','#FFFF00']
        self.nodeSize = 40
        self.edgeWidth = 2
        self.alpha = .9
        self.scale = 0.1
        self.k = 0.3 # k controls the distance between the nodes and varies between 0 and 1
        self.iterations = 20 # iterations is the number of times simulated annealing is run default k = 0.1 and iterations=50

        self.font_size = 16
        self.lines = 2
        self.columns = 3
        self.font = {'family' : 'arial',
                'weight' : 'bold',
                'size'   : self.font_size}
        plt.rc('font', **self.font)
        self.fig = plt.figure(figsize=(30.20,10.80))
        self.fig.subplots_adjust(left=0.09, bottom=0.05, right=0.9, 
            top=0.97,wspace=0.29,hspace=0.23)

    def run(self):
       
        graph = self.data
        
        for i in range(len(graph['population'])):
            if 'home' in graph['population'][i]['agent']['network'].keys():
                self.home.add_node(i)
                homeEdges = graph['population'][i]['agent']['network']['home']
                for j in homeEdges:
                    self.home.add_edge(i, j)
                for j in range(abs(len(graph['population'])-len(homeEdges))):
                    self.home.add_node(j)
            
            if 'work' in graph['population'][i]['agent']['network'].keys():
                self.work.add_node(i)
                workEdges = graph['population'][i]['agent']['network']['work']        
                for j in workEdges:
                    self.work.add_edge(i, j)
                for j in range(abs(len(graph['population'])-len(workEdges))):
                    self.work.add_node(j)

            if 'transport' in graph['population'][i]['agent']['network'].keys():
                self.transport.add_node(i)
                transportEdges = graph['population'][i]['agent']['network']['transport']
                for j in transportEdges:
                    self.transport.add_edge(i, j)
                for j in range(abs(len(graph['population'])-len(transportEdges))):
                    self.transport.add_node(j)

            if 'school' in graph['population'][i]['agent']['network'].keys():
                self.school.add_node(i)
                schoolEdges = graph['population'][i]['agent']['network']['school']
                for j in schoolEdges:
                    self.school.add_edge(i, j)
                for j in range(abs(len(graph['population'])-len(schoolEdges))):
                    self.school.add_node(j)

            if 'religion' in graph['population'][i]['agent']['network'].keys():
                self.religion.add_node(i)
                religionEdges = graph['population'][i]['agent']['network']['religion']
                for j in religionEdges:
                    self.religion.add_edge(i, j)
                for j in range(abs(len(graph['population'])-len(religionEdges))):
                    self.religion.add_node(j)
            
            if 'random' in graph['population'][i]['agent']['network'].keys():
                self.random.add_node(i)
                randomEdges = graph['population'][i]['agent']['network']['random']
                for j in randomEdges:
                    self.random.add_edge(i, j)
                for j in range(abs(len(graph['population'])-len(randomEdges))):
                    self.random.add_node(j)


        ax1 = plt.subplot2grid((self.lines, self.columns), (0, 0))
        ax1.set_title(messages[self.language]['connections of layer'] + " Home", fontname='Arial',size=self.font_size, weight="bold")
        nx.draw(self.home, node_size=self.nodeSize,
            pos=nx.spring_layout(self.home,k=self.k,iterations=self.iterations), 
            node_color=self.nodeColor, alpha=self.alpha, edge_color=self.edge_color[0], width = self.edgeWidth, scale=self.scale)

        ax2 = plt.subplot2grid((self.lines, self.columns), (0, 1))
        ax2.set_title(messages[self.language]['connections of layer'] + " Work", fontname='Arial',size=self.font_size, weight="bold")
        nx.draw(self.work, node_size=self.nodeSize,
            pos=nx.spring_layout(self.work,k=self.k+0.2,iterations=self.iterations+5),
            node_color=self.nodeColor, alpha=self.alpha-0.2, edge_color=self.edge_color[1], width = self.edgeWidth, scale=self.scale)

        ax3 = plt.subplot2grid((self.lines, self.columns), (0, 2))
        ax3.set_title(messages[self.language]['connections of layer'] + " Transport", fontname='Arial',size=self.font_size, weight="bold")
        nx.draw(self.transport, node_size=self.nodeSize, 
            pos=nx.spring_layout(self.transport,k=self.k,iterations=self.iterations),
            node_color=self.nodeColor, alpha=self.alpha, edge_color=self.edge_color[2], width = self.edgeWidth, scale=self.scale)

        ax4 = plt.subplot2grid((self.lines, self.columns), (1, 0))
        ax4.set_title(messages[self.language]['connections of layer'] + " School", fontname='Arial',size=self.font_size, weight="bold")
        nx.draw(self.school, node_size=self.nodeSize, 
            pos=nx.spring_layout(self.school,k=self.k+.3,iterations=self.iterations),
            node_color=self.nodeColor, alpha=self.alpha, edge_color=self.edge_color[3], width = self.edgeWidth, scale=self.scale)

        ax5 = plt.subplot2grid((self.lines, self.columns), (1, 1))

        ax5.set_title(messages[self.language]['connections of layer'] + " Religion", fontname='Arial',size=self.font_size, weight="bold")
        nx.draw(self.religion, node_size=self.nodeSize, 
            pos=nx.spring_layout(self.religion,k=self.k+.3,iterations=self.iterations+5),
            node_color=self.nodeColor, alpha=self.alpha, edge_color=self.edge_color[4], width = self.edgeWidth, scale=self.scale)

        ax6 = plt.subplot2grid((self.lines, self.columns), (1, 2))
        ax6.set_title(messages[self.language]['connections of layer'] + " Random", fontname='Arial',size=self.font_size, weight="bold")
        nx.draw(self.random, node_size=self.nodeSize, 
            pos=nx.spring_layout(self.random,k=self.k+.3,iterations=self.iterations),
            node_color=self.nodeColor, alpha=self.alpha, edge_color=self.edge_color[5], width = self.edgeWidth, scale=self.scale)
        
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

    default_output = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'network.png')

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
    network = Network(output_file, save, language, data)
    network.run()
    network.output()
