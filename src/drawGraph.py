from graphAlgoFile import GraphAlgo
from sys import argv
from Graph_Game import Graph_Game

if __name__ == '__main__':
    algo_graph: GraphAlgo = GraphAlgo()
    algo_graph.load_from_json(argv[1])
    draw_graph:Graph_Game = Graph_Game(algo_graph)
    draw_graph.play()