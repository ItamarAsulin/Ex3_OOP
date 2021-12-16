import json
from abc import ABC
from typing import List
from queue import PriorityQueue
from GraphInterface import GraphInterface
from diGraph import DiGraph
from graphForJson import *


class GraphAlgo(GraphInterface):

    def __init__(self, graph: DiGraph = DiGraph()):
        self.graph = graph
        self.map_dist = {}
        self.map_prev = {}

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        loaded_graph = DiGraph()
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
                node_pos = (x,y)
                node_pos = node_pos
                loaded_graph.add_node(node_id, node_pos)

        for edge in edges:
            src = int(edge["src"])
            weight = float(edge["w"])
            dest = int(edge["dest"])
            loaded_graph.add_edge(src, dest, weight)

        self.graph = loaded_graph
        return True

    def save_to_json(self, file_name: str) -> bool:
        json_graph = GraphForJson()
        for node in self.graph.nodes.values():
            json_graph.add_node(node.id, str(node.pos))

        for edge in self.graph.edges.values():
            json_graph.add_edge(edge.src, edge.w, edge.dest)

        with open(file_name, 'w') as f:
            json.dump(self.graph.__dict__, f)


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
            path.append(self.map_prev[prev_node])
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
