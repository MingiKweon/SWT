import pygame

class Player:
    def __init__(self, screen):
        width, height = screen.get_size()
        self.image = pygame.image.load("pack.png")
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.pos = [width/2, height/2]
        self.to = [0,0]
        self.angle = 0
        
    def draw(self, screen):
        
        if self.to == [-1,-1]:
            self.angel = 45
        elif self.to == [-1,0]:
            self.angel = 90
        elif self.to == [-1,1]:
            self.angel = 135
        elif self.to == [0,1]:
            self.angel = 180
        elif self.to == [1,1]:
            self.angel = -135
        elif self.to == [1,0]:
            self.angel = -90
        elif self.to == [1,-1]:
            self.angel = -45
        elif self.to == [0,-1]:
            self.angel = 0
            
        rotated = pygame.transform.rotate(self.image, self.angle)
        
        
        calib_pos = (
            self.pos[0] - self.image.get_size()[0]/2,
            self.pos[1] - self.image.get_size()[1]/2
        )
        screen.blit(rotated, calib_pos)
       
    def goto(self, x, y):
        self.to[0] += x
        self.to[1] += y
       
        
    def update(self, dt, screen):
        width, height = screen.get_size()
        self.pos[0] = (self.pos[0] + dt * self.to[0] * 0.5) 
        self.pos[1] = (self.pos[1] + dt * self.to[1] * 0.5)
        
        self.pos[0] = min(width-16, max(16, self.pos[0]))
        self.pos[1] = min(height-16, max(16, self.pos[1]))