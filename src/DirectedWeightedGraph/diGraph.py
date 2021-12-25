import random

from src.DirectedWeightedGraph.edge import Edge
from src.DirectedWeightedGraph.node import Node
from src.api.GraphInterface import GraphInterface


class DiGraph(GraphInterface):

    def __init__(self, nodes={}, edges={}, in_edges={}, out_edges={}):
        self.nodes = nodes
        self.edges = edges
        self.out_edges = in_edges
        self.in_edges = out_edges
        self.mc = 0
        self.num_of_nodes = 0
        self.num_of_edges = 0
    """
    this method returns the number of nodes in the graph.
    """
    def v_size(self) -> int:
        return self.num_of_nodes

    """
    this method returns the number of edges in the graph.
    """
    def e_size(self) -> int:
        return self.num_of_edges

    """
    this method returns a dictionary of all the graph's nodes
    """
    def get_all_v(self) -> dict:
        return self.nodes

    """
    this method returns a dictionary representing all the in edges of the given node.
    """
    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.in_edges[id1]

    """
    this method returns a dictionary representing all the out edges of the given node.
    """
    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.out_edges[id1]

    """
    this method returns the graph's mods count.
    """
    def get_mc(self) -> int:
        return self.mc

    """
    this method adds the given edge to the graph.
    """
    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        edge_key = (id1, id2)
        if edge_key in self.edges.keys():
            return False
        else:
            edge_to_add = Edge(id1, id2, weight)
            self.edges[edge_key] = edge_to_add
            self.out_edges[id1][id2] = edge_to_add
            self.in_edges[id2][id1] = edge_to_add
            self.mc += 1
            self.num_of_edges += 1
            return True

    """
    this method adds the given node to the graph.
    """
    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self.nodes.keys():
            return False
        else:
            node_to_add = Node(node_id, pos)
            self.nodes[node_id] = node_to_add
            self.in_edges[node_id] = {}
            self.out_edges[node_id] = {}
            self.mc += 1
            self.num_of_nodes += 1
            return True

    """
    this method removes the given nodes from the graph.
    """
    def remove_node(self, node_id: int) -> bool:
        if node_id not in self.nodes.keys():
            return False
        else:
            del self.nodes[node_id]
            del self.out_edges[node_id]
            del self.in_edges[node_id]
            keys_to_remove = []
            for key, edge in self.edges.items():
                edge_src = key[0]
                edge_dest = key[1]
                if edge_src == node_id or edge_dest == node_id:
                    keys_to_remove.append(key)

            for key in keys_to_remove:
                del self.edges[key]
                edge_src = key[0]
                edge_dest = key[1]
                if edge_dest == node_id:
                    del self.out_edges[edge_src][edge_dest]
            self.num_of_nodes -= 1
            self.mc += 1
            return True

    """
    this method removes the given edge from the graph.
    """
    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        edge_key = (node_id1, node_id2)
        if edge_key not in self.edges.keys():
            return False
        else:
            del self.edges[edge_key]
            del self.out_edges[node_id1][node_id2]
            del self.in_edges[node_id2][node_id1]
            self.num_of_edges -= 1
            self.mc += 1
            return True

    """
    this method sets all the graph's nodes tags to thew given tag.
    """
    def set_all_tags(self, tag: int):
        for node in self.nodes.values():
            node.tag = tag

    def __repr__(self):
        return f"nodes: {self.nodes.values().__repr__()} edges: {self.edges.values().__repr__()}"

    """
    this method returns the node relevant to the given key.
    """
    def get_node(self, key):
        return self.nodes[key]