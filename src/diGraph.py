from GraphInterface import GraphInterface


class Node:

    def __init__(self, id: int, pos: tuple = (0, 0)):
        self.id = id
        self.pos = pos

    def __repr__(self):
        return f"id = {self.id} pos = {self.pos}"


class Edge:

    def __init__(self, src: int, dest: int, w: float):
        self.src = src
        self.dest = dest
        self.w = w

    def __repr__(self):
        return f"src = {self.src} dest = {self.dest} weight = {self.w}"


class DiGraph(GraphInterface):

    def __init__(self, nodes={}, edges={}, in_edges={}, out_edges={}):
        self.nodes = nodes
        self.edges = edges
        self.out_edges = in_edges
        self.in_edges = out_edges
        self.mc = 0
        self.num_of_nodes = 0
        self.num_of_edges = 0

    def v_size(self) -> int:
        return self.num_of_nodes

    def e_size(self) -> int:
        return self.num_of_edges

    def get_all_v(self) -> dict:
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.in_edges[id1]

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.out_edges[id1]

    def get_mc(self) -> int:
        return self.mc

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

    def remove_node(self, node_id: int) -> bool:
        if node_id not in self.nodes.keys():
            return False
        else:
            del self.nodes[node_id]
            del self.out_edges[node_id]
            del self.in_edges[node_id]
            self.num_of_nodes -= 1
            self.mc += 1
            return True

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

    def __repr__(self):
        return f"nodes: {self.nodes.values().__repr__()} edges: {self.edges.values().__repr__()}"

