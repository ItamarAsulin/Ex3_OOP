import math
import sys

import pygame, os
from graphAlgo import GraphAlgo

from diGraph import *


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
BLUE = (0, 0, 255)

class Graph_Game:

    def __init__(self,graphAlgo:GraphAlgo) -> None:
        self.graphAlgo=graphAlgo
        pygame.font.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode()
        self.w=int(self.screen.get_width())
        self.h=int(self.screen.get_height())
        pygame.display.set_caption("My game!")
        self.WIN=pygame.display.set_mode((self.screen.get_width()-30,self.screen.get_height()-70))
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        self.minX=float(sys.maxsize)
        self.maxY=float(sys.maxsize)*-1
        self.maxX=float(sys.maxsize)*-1
        self.minY=float(sys.maxsize)
        self.X_par=0
        self.Y_par=0

    def main_menu_buttons(self):
        self.menu_rect = pygame.Rect([10, 10], [100, 30])
        self.quit_rect = pygame.Rect([120, 10], [100, 30])
        rect_button_color = CYAN
        menu = "MENU"
        quit="QUIT"
        font = pygame.font.SysFont('impact', 32)  # Here's the font we'll use to render text
        pygame.draw.rect(self.WIN, rect_button_color, self.menu_rect)
        rect_clicks_surf = font.render(menu, True, BLACK)
        self.WIN.blit(rect_clicks_surf, [self.menu_rect.topleft[0]+10, self.menu_rect.topleft[1]-5])
        pygame.draw.rect(self.WIN, rect_button_color, self.quit_rect)
        rect_clicks_surf = font.render(quit, True, BLACK)
        self.WIN.blit(rect_clicks_surf, [self.quit_rect.topleft[0]+10, self.quit_rect.topleft[1]-5])

    def menu_buttons(self):
        self.actions_rect = pygame.Rect([10, 10], [100, 30])
        self.algorithm_rect = pygame.Rect([40, 40], [100, 30])
        rect_button_color = CYAN
        actions = "Actions on graph"
        algo="Algorithms on graph"
        font = pygame.font.SysFont('impact', 32)
        pygame.draw.rect(self.WIN, rect_button_color, self.actions_rect)
        rect_clicks_surf = font.render(actions, True, BLACK)
        self.WIN.blit(rect_clicks_surf, [self.actions_rect.topleft[0]+10, self.menu_rect.topleft[1]-5])
        pygame.draw.rect(self.WIN, rect_button_color, self.algorithm_rect)
        rect_clicks_surf = font.render(algo, True, BLACK)
        self.WIN.blit(rect_clicks_surf, [self.algorithm_rect.topleft[0]+10, self.algorithm_rect.topleft[1]-5])


    def draw_graph(self):
        self.draw_nodes()
        self.draw_edges()

    def draw_nodes(self):
        for point in self.graphAlgo.graph.nodes.values():
             if (point.pos[0]>self.maxX):
                self.maxX=point.pos[0]
             if (point.pos[1]<self.minY):
                self.minY=point.pos[1]
             if (point.pos[0]<self.minX):
                self.minX=point.pos[0]
             if (point.pos[1]>self.maxY):
                self.maxY=point.pos[1]

        self.X_par=int(self.w)/(self.maxX-self.minX)*0.9;
        self.Y_par=int(self.h)/(self.maxY-self.minY)*0.8;
        for node in self.graphAlgo.graph.nodes.values():
            pygame.draw.circle(self.WIN, RED, ((node.pos[0]-self.minX)*self.X_par,(node.pos[1]-self.minY)*self.Y_par) ,5, 5)
            ID_FONT = pygame.font.SysFont('comicsans', 15)
            draw_text = ID_FONT.render(str(node.id), 3, BLACK)
            self.WIN.blit(draw_text, ((node.pos[0]-self.minX)*self.X_par,(node.pos[1]-self.minY)*self.Y_par))

    def draw_edges(self):
        for edge in self.graphAlgo.graph.edges.values():
            Node1=self.graphAlgo.graph.get_node(edge.src)
            Node2=self.graphAlgo.graph.get_node(edge.dest)
            x1=(int) ((Node1.pos[0]-self.minX)*self.X_par)
            y1=(int) ((Node1.pos[1]-self.minY)*self.Y_par)
            x2=(int) ((Node2.pos[0]-self.minX)*self.X_par)
            y2=(int) ((Node2.pos[1]-self.minY)*self.Y_par)
            pygame.draw.line(self.WIN,GREEN,(x1,y1),(x2,y2),3)
            self.DrawArrow(x2,y2,GREEN)

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

    # def draw_shortest_path(self):


    def play(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.quit_rect.collidepoint(mouse_pos):
                        run = False
                        # pygame.quit()
                    if self.menu_rect.collidepoint(mouse_pos):
                        self.menu_buttons()
            self.WIN.fill((250, 250, 250))
            self.draw_graph()
            self.main_menu_buttons()
            # self.menu_buttons()
            pygame.display.update()

        pygame.quit()




if __name__ == "__main__":
    g = GraphAlgo()
    g.load_from_json(r"C:\Users\shira\Desktop\Ex3_OOP-main\Ex3_OOP-main\data\A3.json")
    game=Graph_Game(g)
    game.play()