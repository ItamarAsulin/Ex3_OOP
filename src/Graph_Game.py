
import math
import sys
import os

import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
BLUE = (0, 0, 255)


class Graph_Game:

    def __init__(self, graph_algo) -> None:
        self.graphAlgo = graph_algo
        pygame.font.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode()
        self.w = int(self.screen.get_width())
        self.h = int(self.screen.get_height())
        pygame.display.set_caption("My game!")
        self.WIN = pygame.display.set_mode((self.screen.get_width() - 30, self.screen.get_height() - 70))
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        self.minX = float(sys.maxsize)
        self.maxY = float(sys.maxsize) * -1
        self.maxX = float(sys.maxsize) * -1
        self.minY = float(sys.maxsize)
        self.X_par = 0
        self.Y_par = 0

    def draw_graph(self):
        self.draw_nodes()
        self.draw_edges()

    def draw_nodes(self):
        for point in self.graphAlgo.graph.nodes.values():
            if (point.pos[0] > self.maxX):
                self.maxX = point.pos[0]
            if (point.pos[1] < self.minY):
                self.minY = point.pos[1]
            if (point.pos[0] < self.minX):
                self.minX = point.pos[0]
            if (point.pos[1] > self.maxY):
                self.maxY = point.pos[1]

        self.X_par = int(self.w) / (self.maxX - self.minX) * 0.9;
        self.Y_par = int(self.h) / (self.maxY - self.minY) * 0.8;
        for node in self.graphAlgo.graph.nodes.values():
            pygame.draw.circle(self.WIN, RED,
                               ((node.pos[0] - self.minX) * self.X_par, (node.pos[1] - self.minY) * self.Y_par), 5, 5)
            ID_FONT = pygame.font.SysFont('comicsans', 15)
            draw_text = ID_FONT.render(str(node.id), 3, BLACK)
            self.WIN.blit(draw_text, ((node.pos[0] - self.minX) * self.X_par, (node.pos[1] - self.minY) * self.Y_par))

    def draw_edges(self):
        for edge in self.graphAlgo.graph.edges.values():
            Node1 = self.graphAlgo.graph.get_node(edge.src)
            Node2 = self.graphAlgo.graph.get_node(edge.dest)
            x1 = (int)((Node1.pos[0] - self.minX) * self.X_par)
            y1 = (int)((Node1.pos[1] - self.minY) * self.Y_par)
            x2 = (int)((Node2.pos[0] - self.minX) * self.X_par)
            y2 = (int)((Node2.pos[1] - self.minY) * self.Y_par)
            pygame.draw.line(self.WIN, GREEN, (x1, y1), (x2, y2), 3)
            self.DrawArrow(x2, y2, GREEN)

    def DrawArrow(self, x, y, color, angle=0):
        def rotate(pos, angle):
            cen = (5 + x, 0 + y)
            angle *= -(math.pi / 180)
            cos_theta = math.cos(angle)
            sin_theta = math.sin(angle)
            ret = ((cos_theta * (pos[0] - cen[0]) - sin_theta * (pos[1] - cen[1])) + cen[0],
                   (sin_theta * (pos[0] - cen[0]) + cos_theta * (pos[1] - cen[1])) + cen[1])
            return ret

        p0 = rotate((0 + x, -4 + y), angle + 90)
        p1 = rotate((0 + x, 4 + y), angle + 90)
        p2 = rotate((10 + x, 0 + y), angle + 90)
        pygame.draw.polygon(self.screen, color, [p0, p1, p2])


    def play(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            self.WIN.fill((250, 250, 250))
            self.draw_graph()
            pygame.display.update()

        pygame.quit()

