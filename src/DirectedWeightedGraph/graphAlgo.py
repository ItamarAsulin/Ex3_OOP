import json
from typing import List
from queue import PriorityQueue
from queue import Queue
from src.api.GraphInterface import GraphInterface
from src.DirectedWeightedGraph.diGraph import *
from src.GraphForJson.graphForJson import *
from src.api import GraphAlgoInterface


class GraphAlgo(GraphAlgoInterface.GraphAlgoInterface):

    def __init__(self, graph: DiGraph = DiGraph()):
        self.graph: DiGraph = graph
        self.inverted: DiGraph = graph.invert_graph()
        self.map_dist = {}
        self.map_prev = {}

    def __repr__(self) -> str:
        return str(self.graph)

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        loaded_graph: DiGraph = DiGraph()
        with open(file_name, "r") as f:
            graph_from_json = json.load(f)
        nodes = graph_from_json.get("Nodes")
        edges = graph_from_json.get("Edges")
        for node in nodes:
            if len(node) == 1:
                node_id = int(node["id"])
                loaded_graph.add_node(node_id)
            else:
                node_id = int(node["id"])
                pos_str = str(node["pos"]).split(',')
                x = float(pos_str[0])
                y = float(pos_str[1])
                node_pos = (x, y)
                node_pos = node_pos
                loaded_graph.add_node(node_id, node_pos)

        for edge in edges:
            src = int(edge["src"])
            weight = float(edge["w"])
            dest = int(edge["dest"])
            loaded_graph.add_edge(src, dest, weight)

        self.graph = loaded_graph
        self.inverted = loaded_graph.invert_graph()
        return True

    def save_to_json(self, file_name: str) -> bool:
        json_graph = GraphForJson()
        for edge in self.graph.edges.values():
            json_graph.add_edge(edge.src, edge.w, edge.dest)
        for node in self.graph.nodes.values():
            node_x = node.pos[0]
            node_y = node.pos[1]
            node_z = 0.0
            json_node_pos = f"{node_x},{node_y},{node_z}"
            json_graph.add_node(node.id, json_node_pos)

        with open(file_name, 'w') as f:
            json.dump(json_graph, default=lambda l: l.__dict__, fp=f, indent=4)
            return True

    def is_connected(self):
        # is_connected_normal: bool = self.__is_connected(self.graph)
        # self.invert_graph()
        # is_connected_inverted: bool = self.__is_connected()
        # self.invert_graph()
        normal_graph = self.graph
        inverted_graph = self.inverted
        return self.__is_connected(normal_graph) and self.__is_connected(inverted_graph)

    def calculate_shortest_path(self, src_id: int):
        self.map_dist.clear()
        self.map_prev.clear()
        for node_id in self.graph.nodes.keys():
            self.map_dist[node_id] = float('inf')

        self.map_prev[src_id] = -1
        queue = PriorityQueue()
        queue.put(src_id)
        self.map_dist[src_id] = 0.0
        while not queue.empty():
            current_node = queue.get()
            for neighbor_id, edge in self.graph.all_out_edges_of_node(current_node).items():
                total_weight = self.map_dist[current_node] + edge.w
                if total_weight < self.map_dist[neighbor_id]:
                    self.map_dist[neighbor_id] = total_weight
                    self.map_prev[neighbor_id] = current_node
                    queue.put(neighbor_id)

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if id1 not in self.graph.nodes.keys() or id2 not in self.graph.nodes.keys():
            return -1, []

        if id1 in self.graph.nodes.keys() and id1 == id2:
            path = List
            path.append(id1)
            return 0.0, path

        self.calculate_shortest_path(id1)
        if id2 not in self.map_prev.keys():
            return float('inf'), []

        dist = float(self.map_dist[id2])
        path = list()
        prev_node = self.map_prev.get(id2)
        while prev_node != -1:
            path.append(prev_node)
            prev_node = self.map_prev[prev_node]
        return dist, path

    def find_min_for_tsp(self, unvisited: set):
        min_dist_node = -1
        min_dist = float('inf')
        for node_id in unvisited:
            current_dist = self.map_dist[node_id]
            if current_dist < min_dist:
                min_dist = current_dist
                min_dist_node = node_id

        if min_dist_node == -1:
            return unvisited.pop()
        return min_dist_node

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        if len(node_lst) == 0:
            return [], -1

        if len(node_lst) == 1:
            return node_lst, 0
        total_dist = 0.0
        path = list()
        unvisited = set()
        for node_id in node_lst:
            unvisited.add(node_id)
        current_node_id = unvisited.pop()
        while len(unvisited) != 0:
            unvisited.remove(current_node_id)
            self.calculate_shortest_path(current_node_id)
            next_node = self.find_min_for_tsp()
            path_from_current_to_next: list = self.shortest_path(current_node_id, next_node)[1]
            path.append(path_from_current_to_next[0])
            if path_from_current_to_next[0] in unvisited:
                unvisited.remove(path_from_current_to_next[0])
            for i in range(1, len(path_from_current_to_next)):
                node_id = path_from_current_to_next[i]
                if node_id in unvisited:
                    unvisited.remove(node_id)
                path.append(node_id)
            total_dist += self.map_dist[next_node]
            current_node_id = next_node

        return path, total_dist

    def find_max_value(self) -> float:
        max_value = 0.0
        for dist in self.map_dist.values():
            if dist > max_value:
                max_value = dist
        return max_value

    def centerPoint(self) -> (int, float):
        key_of_center = -1
        min_max_dist = float('inf')
        for node_id in self.graph.nodes.keys():
            self.calculate_shortest_path(node_id)
            current_max_value = self.find_max_value()
            if current_max_value < min_max_dist:
                min_max_dist = current_max_value
                key_of_center = node_id
        if key_of_center == -1:
            return self.graph.nodes.get(0), float('inf')

        return key_of_center, min_max_dist

    def plot_graph(self) -> None:
        return


    @staticmethod
    def BFS(graph, node):
        queue: Queue = Queue()
        queue.put(node)
        node.tag = 1
        while not queue.empty():
            current_node: node = queue.get()
            for edge in graph.all_out_edges_of_node(current_node.id).values():
                dest_node_id = edge.dest
                node_to_set = graph.nodes[dest_node_id]
                if node_to_set.tag == 0:
                    node_to_set.tag = 1
                    assert isinstance(node_to_set, Node)
                    queue.put(node_to_set)

    def __is_connected(self, graph: DiGraph):
        graph.set_all_tags(0)
        random_key, random_value = graph.nodes.popitem()
        node_first: Node = random_value
        graph.nodes[random_key] = random_value
        self.BFS(graph, node_first)
        for node in graph.nodes.values():
            if node.tag == 0:
                return False

        return True
