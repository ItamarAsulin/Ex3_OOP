import random


class Node:

    def __init__(self, id: int, pos: tuple = None):
        self.id = id
        if pos == None:
            x=random.randint(35,36)
            y = random.randint(32, 33)
            pos=(x,y)
            self.pos=pos
        else:
            self.pos = pos
        self.tag = 0

    def __repr__(self):
        return f"id = {self.id} pos = {self.pos}"