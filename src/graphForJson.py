class NodeForJson:

    def __init__(self, id: int, pos: str):
        self.id = id
        self.pos = pos

    def __repr__(self):
        return f"id: {self.id} pos: {self.pos}"


class EdgeForJson:

    def __init__(self, src: int, w: float, dest: int):
        self.src = src
        self.w = w
        self.dest = dest

    def __repr__(self):
        return f"src: {self.src} dest: {self.dest} w: {self.w}"

class GraphForJson:

    def __init__(self):
        self.Edges = []
        self.Nodes = []


    def add_edge(self, edge_src: int, edge_weight: float, edge_dest: int):
        edge_to_add = EdgeForJson(edge_src, edge_weight, edge_dest)
        self.Edges.append(edge_to_add)

    def add_node(self, node_id: int, node_pos: str = None):
        node_to_add = NodeForJson(node_id, node_pos)
        self.Nodes.append(node_to_add)

    def __repr__(self) -> str:
        return str(self.Nodes)+"\n"+str(self.Edges)


