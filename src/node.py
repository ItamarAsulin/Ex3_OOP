import random


class Node:

    def __init__(self, id: int, pos: tuple = None):
        self.id = id
        if pos is None:
            x = random.uniform(35.18759, 35.21310)
            y = random.uniform(32.09965, 32.10921)
            pos = (x, y)
            self.pos = pos
        else:
            self.pos = pos
        self.tag = 0

    def __repr__(self):
        return f"id = {self.id} pos = {self.pos}"
