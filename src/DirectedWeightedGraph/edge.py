class Edge:

    def __init__(self, src: int, dest: int, w: float):
        self.src = src
        self.dest = dest
        self.w = w

    def __repr__(self):
        return f"src = {self.src} dest = {self.dest} weight = {self.w}"