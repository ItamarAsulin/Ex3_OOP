from matplotlib import pyplot as plt
# from src.api.GraphAlgoInterface import GraphInterface
# from src.DirectedWeightedGraph.graphAlgo import GraphAlgo
from src.DirectedWeightedGraph.graphAlgoFile import *


class PlotGraph:

    def __init__(self, graph_algo):
        self.nodes_x = []
        self.nodes_y = []
        self.arrows = []
        for node in graph_algo.graph.nodes.values():
            current_x = node.pos[0]
            current_y = node.pos[1]
            self.nodes_x.append(current_x)
            self.nodes_y.append(current_y)

        for edge in graph_algo.graph.edges.values():
            src_x = graph_algo.graph.nodes[edge.src].pos[0]
            src_y = graph_algo.graph.nodes[edge.src].pos[1]

    def draw_graph(self):
        plt.plot(self.nodes_x, self.nodes_y, 'ro')
        plt.show()
