from unittest import TestCase
from src.graphAlgoFile import *


def create_graph(size: int, graph: DiGraph):
    for i in range(0, size):
        graph.add_node(i)


graph_algo_test2: GraphAlgo = GraphAlgo()
graph_algo: GraphAlgo = GraphAlgo()
g1: DiGraph = DiGraph()
create_graph(10, g1)
g1.add_edge(0, 1, 0.5)
g1.add_edge(0, 2, 2.5)
g1.add_edge(2, 3, 1.98)
g1.add_edge(1, 4, 8.3)
g1.add_edge(4, 6, 4.1)
g1.add_edge(8, 6, 2.4)
g1.add_edge(5, 6, 3.1)
g1.add_edge(6, 5, 3.1)
g1.add_edge(7, 8, 1.8)
g1.add_edge(3, 8, 9.6)
g1.add_edge(1, 5, 5.6)
graph_algo = GraphAlgo()


class TestGraphAlgo(TestCase):

    def test_load_from_json_then_save_to_json(self):
        self.assertTrue(graph_algo.load_from_json("../data/A0.json"))
        self.assertFalse(graph_algo.load_from_json("not a path"))
        self.assertTrue(graph_algo.save_to_json("../data/A0_Test.json"))
        graph_algo2: GraphAlgo = GraphAlgo()
        self.assertTrue(graph_algo2.load_from_json("../data/A0_Test.json"))
        self.assertFalse(graph_algo2.save_to_json('/home/1'))
        for key in graph_algo.graph.nodes.keys():
            origin_node: Node = graph_algo.graph.nodes[key]
            loaded_node: Node = graph_algo2.graph.nodes[key]
            self.assertEqual(origin_node.id, loaded_node.id)
            self.assertEqual(origin_node.pos, loaded_node.pos)

    def test_is_connected(self):
        graph_algo.load_from_json("../data/A0.json")
        self.assertTrue(graph_algo.is_connected())
        self.assertTrue(graph_algo.load_from_json("../data/A5_edited"))
        self.assertFalse(graph_algo.is_connected())

    def test_shortest_path(self):
        graph_algo_test: GraphAlgo = GraphAlgo()
        graph_algo_test.graph = g1
        self.assertEqual(5.6, graph_algo_test.shortest_path(1, 5)[0])
        self.assertEqual(0.5, graph_algo_test.shortest_path(0, 1)[0])
        self.assertEqual(4.48, graph_algo_test.shortest_path(0, 3)[0])
        self.assertEqual(7.300000000000001, graph_algo_test.shortest_path(7, 5)[0])
        self.assertEqual(float('inf'), graph_algo_test.shortest_path(8, 3)[0])
        self.assertEqual(0.0, graph_algo_test.shortest_path(2, 2)[0])
        self.assertEqual(float('inf'), graph_algo_test.shortest_path(20, 20)[0])
        self.assertEqual(float('inf'), graph_algo_test.shortest_path(0, 20)[0])

    def test_tsp(self):
        pass

    def test_center_point(self):
        graph_algo_test2 = GraphAlgo()
        graph_algo_test2.load_from_json("../data/A0.json")
        self.assertEqual(7, graph_algo_test2.centerPoint()[0])
        self.assertEqual(6.806805834715163, graph_algo_test2.centerPoint()[1])

        graph_algo_test3 = GraphAlgo()
        graph_algo_test3.load_from_json("../data/A1.json")
        self.assertEqual(8, graph_algo_test3.centerPoint()[0])
        self.assertEqual(9.925289024973141, graph_algo_test3.centerPoint()[1])

        graph_algo_test2.load_from_json("../data/A2.json")
        self.assertEqual(0, graph_algo_test2.centerPoint()[0])
        self.assertEqual(7.819910602212574, graph_algo_test2.centerPoint()[1])

        graph_algo_test2.load_from_json("../data/A3.json")
        self.assertEqual(2, graph_algo_test2.centerPoint()[0])
        self.assertEqual(8.182236568942237, graph_algo_test2.centerPoint()[1])

        graph_algo_test2.load_from_json("../data/A4.json")
        self.assertEqual(6, graph_algo_test2.centerPoint()[0])
        self.assertEqual(8.071366078651435, graph_algo_test2.centerPoint()[1])

        graph_algo_test2.load_from_json("../data/A5.json")
        self.assertEqual(40, graph_algo_test2.centerPoint()[0])
        self.assertEqual(9.291743173960954, graph_algo_test2.centerPoint()[1])

    def test_plot_graph(self):
        graph_algo_to_plot_check: GraphAlgo = GraphAlgo()
        graph_algo_to_plot_check.load_from_json("../data/A3.json")
        graph_algo_to_plot_check.plot_graph()
