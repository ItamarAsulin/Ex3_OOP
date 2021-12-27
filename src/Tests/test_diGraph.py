from unittest import TestCase
from src.diGraph import *


def generate_connected_graph() -> DiGraph:
    graph_to_return: DiGraph = DiGraph()
    for i in range(0, 10):
        graph_to_return.add_node(i)

    for i in range(0, 10):
        for j in range(0, 10):
            if i != j:
                graph_to_return.add_edge(i, j, 1)

    return graph_to_return


class TestDiGraph(TestCase):

    def test_v_size(self):
        my_graph: DiGraph = generate_connected_graph()
        self.assertEqual(10, my_graph.v_size())

    def test_e_size(self):
        my_graph: DiGraph = generate_connected_graph()
        self.assertEqual(90, my_graph.e_size())

    def test_get_all_v(self):
        my_graph: DiGraph = generate_connected_graph()
        dict_to_test = my_graph.nodes
        self.assertIs(dict_to_test, my_graph.get_all_v())

    def test_all_in_edges_of_node(self):
        my_graph: DiGraph = generate_connected_graph()
        dict_to_test = my_graph.in_edges[0]
        self.assertIs(dict_to_test, my_graph.all_in_edges_of_node(0))

    def test_all_out_edges_of_node(self):
        my_graph: DiGraph = generate_connected_graph()
        dict_to_test = my_graph.out_edges[0]
        self.assertIs(dict_to_test, my_graph.all_out_edges_of_node(0))

    def test_get_mc(self):
        my_graph: DiGraph = generate_connected_graph()
        self.assertEqual(100, my_graph.get_mc())

    def test_add_edge(self):
        my_graph: DiGraph = generate_connected_graph()
        self.assertTrue(my_graph.add_edge(1,1,1))
        self.assertEqual(91, my_graph.e_size())

    def test_add_node(self):
        my_graph: DiGraph = generate_connected_graph()
        self.assertTrue(my_graph.add_node(11))
        self.assertEqual(11, my_graph.v_size())

    def test_remove_node(self):
        my_graph: DiGraph = generate_connected_graph()
        self.assertTrue(my_graph.remove_node(0))
        self.assertFalse(my_graph.remove_node(11))
        self.assertEqual(9, my_graph.v_size())

    def test_remove_edge(self):
        my_graph: DiGraph = generate_connected_graph()
        self.assertTrue(my_graph.remove_edge(0,1))
        self.assertFalse(my_graph.remove_edge(0,11))
        self.assertEqual(89, my_graph.e_size())

    def test_set_all_tags(self):
        my_graph: DiGraph = generate_connected_graph()
        my_graph.set_all_tags(3)
        for node in my_graph.nodes.values():
            self.assertEqual(3, node.tag)
