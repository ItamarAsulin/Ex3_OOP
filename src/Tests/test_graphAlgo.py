from unittest import TestCase
from src.DirectedWeightedGraph.graphAlgo import *

class TestGraphAlgo(TestCase):

    def test_load_from_json_then_save_to_json(self):
        graph_algo: GraphAlgo = GraphAlgo()
        self.assertTrue(graph_algo.load_from_json("/home/itamarq/OOP_2021_1/Assignments/Ex3/data/A0.json"))
        # self.assertFalse(graph_algo.load_from_json("not a path"))
        self.assertTrue(graph_algo.save_to_json("/home/itamarq/OOP_2021_1/Assignments/Ex3/data/A0_Test.json"))
        graph_algo2: GraphAlgo= GraphAlgo()
        self.assertTrue(graph_algo2.load_from_json("/home/itamarq/OOP_2021_1/Assignments/Ex3/data/A0_Test.json"))
        for key in graph_algo.graph.nodes.keys():
            origin_node: Node = graph_algo.graph.nodes[key]
            loaded_node: Node = graph_algo2.graph.nodes[key]
            self.assertEqual(origin_node.id, loaded_node.id)
            self.assertEqual(origin_node.pos, loaded_node.pos)

    def test_is_connected(self):
        graph_algo: GraphAlgo = GraphAlgo()
        self.assertTrue(graph_algo.load_from_json("/home/itamarq/OOP_2021_1/Assignments/Ex3/data/T0.json"))
        self.assertTrue(graph_algo.is_connected())


    def test_calculate_shortest_path(self):
        self.fail()

    def test_shortest_path(self):
        self.fail()

    def test_find_min_for_tsp(self):
        self.fail()

    def test_tsp(self):
        self.fail()

    def test_find_max_value(self):
        self.fail()

    def test_center_point(self):
        self.fail()

    def test_plot_graph(self):
        self.fail()

    def test_set_all_tags(self):
        self.fail()

    def test_bfs(self):
        self.fail()
