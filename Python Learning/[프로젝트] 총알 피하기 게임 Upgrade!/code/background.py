import pygame

#배경그림 설정값
screen = pygame.display.set_mode((700, 700))
bg_image1 = pygame.image.load("images/bg.jpg")
bg_image1 = pygame.transform.scale(bg_image1, (700,700))
bg_image2 = pygame.transform.flip(bg_image1, True, False)
bg_image3 = pygame.transform.flip(bg_image1, False, True) #처음그림 대칭시킨 그림
bg_image4 = pygame.transform.flip(bg_image1, True, True)

class Background:
    def __init__(self,screen):
        width, height = screen.get_size()
        self.image1 = bg_image1
        self.image2 = bg_image2
        self.image3 = bg_image3
        self.image4 = bg_image4

        self.pos1 = [0, 0]
        self.pos2 = [width, 0]
        self.pos3 = [0, height]
        self.pos4 = [width, height]
        self.pos5 = [-width, 0]
        self.pos6 = [0, -height]
        self.pos7 = [-width, -height]
        self.pos8 = [width, -height]
        self.pos9 = [-width, height]
    
        self.to = [0,0]
    #배경 이동
    def goto(self, x, y):
        self.to[0] += x
        self.to[1] += y 

    #배경 이동속도 제어
    def update(self, dt, screen):
        width, height = screen.get_size()
        self.pos1[0] = (self.pos1[0] + dt * self.to[0] * 0.05)
        self.pos1[1] = (self.pos1[1] + dt * self.to[1] * 0.05)

        self.pos2[0] = (self.pos2[0] + dt * self.to[0] * 0.05)
        self.pos2[1] = (self.pos2[1] + dt * self.to[1] * 0.05)

        self.pos3[0] = (self.pos3[0] + dt * self.to[0] * 0.05)
        self.pos3[1] = (self.pos3[1] + dt * self.to[1] * 0.05)

        self.pos4[0] = (self.pos4[0] + dt * self.to[0] * 0.05)
        self.pos4[1] = (self.pos4[1] + dt * self.to[1] * 0.05)

        self.pos5[0] = (self.pos5[0] + dt * self.to[0] * 0.05)
        self.pos5[1] = (self.pos5[1] + dt * self.to[1] * 0.05)

        self.pos6[0] = (self.pos6[0] + dt * self.to[0] * 0.05)
        self.pos6[1] = (self.pos6[1] + dt * self.to[1] * 0.05)

        self.pos7[0] = (self.pos7[0] + dt * self.to[0] * 0.05)
        self.pos7[1] = (self.pos7[1] + dt * self.to[1] * 0.05)

        self.pos8[0] = (self.pos8[0] + dt * self.to[0] * 0.05)
        self.pos8[1] = (self.pos8[1] + dt * self.to[1] * 0.05)

        self.pos9[0] = (self.pos9[0] + dt * self.to[0] * 0.05)
        self.pos9[1] = (self.pos9[1] + dt * self.to[1] * 0.05)