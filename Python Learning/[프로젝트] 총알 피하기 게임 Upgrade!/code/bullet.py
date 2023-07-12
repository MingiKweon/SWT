import pygame

#총알1
class Bullet1:
    #시스템 기본값(총알)
    def __init__(self,x,y,to_x,to_y):
        self.pos = [x,y]
        self.to = [to_x,to_y]
        self.radius = 5
        self.color = (170,0,0)

    def update_and_draw(self,dt,screen):
        
        width, height = screen.get_size()
        self.pos[0] = (self.pos[0] + dt * self.to[0] * 1.5) % width
        self.pos[1] = (self.pos[1] + dt * self.to[1] * 1.5) % height

        pygame.draw.circle(screen, self.color, self.pos, self.radius)
#총알2
class Bullet2:
    def __init__(self,x,y,to_x,to_y):
        self.pos = [x,y]
        self.to = [to_x,to_y]
        self.radius = 6
        self.color = (70,150,140)

    def update_and_draw(self,dt,screen):
        
        width, height = screen.get_size()
        self.pos[0] = (self.pos[0] + dt * self.to[0] * 1.5) % width
        self.pos[1] = (self.pos[1] + dt * self.to[1] * 1.5) % height

        pygame.draw.circle(screen, self.color, self.pos, self.radius)
#총알3
class Bullet3:
    def __init__(self,x,y,to_x,to_y):
        self.pos = [x,y]
        self.to = [to_x,to_y]
        self.radius = 2
        self.color = (255,255,0)

    def update_and_draw(self,dt,screen):
        
        width, height = screen.get_size()
        self.pos[0] = (self.pos[0] + dt * self.to[0] * 1.5) % width
        self.pos[1] = (self.pos[1] + dt * self.to[1] * 1.5) % height

        pygame.draw.circle(screen, self.color, self.pos, self.radius)