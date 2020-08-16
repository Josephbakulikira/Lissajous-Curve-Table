import pygame
class Curve:
    def __init__(self, color):
        self.points = []
        self.color = color
        self.current = [0,0]
    def set_point_x(self, x):
        self.current[0] = x
    def set_point_y(self, y):
        self.current[1] = y
    def update_points(self):

        self.points.append( ( int(self.current[0]), self.current[1]) )

    def draw(self, screen):
        for i in range(len(self.points)):
            if i >0:
                pygame.draw.line(screen, self.color, self.points[i-1], self.points[i], 2)
        pygame.draw.circle(screen, (200, 200,200), (int(self.current[0]), int(self.current[1])), 5)
        self.current = [0,0]
