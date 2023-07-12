import pygame

#우주선 그림
plane_img = pygame.image.load("images/player.png") #우주선
plane_img = pygame.transform.scale(plane_img, (64,64))
fire_img = pygame.image.load("images/fire.png") #충돌 효과
fire_img = pygame.transform.scale(fire_img, (64,64))



class Player:
    def __init__(self,screen):
        width, height = screen.get_size()
        self.image = [plane_img, fire_img]
        self.current_image = self.image[0]
        self.current_image = pygame.transform.scale(self.current_image, (64,64))
        self.pos = [width/2, height/2] #list 처리(순서)
        self.to = [0,0]
        self.angle = 0

    #우주선 충돌시 효과(번쩍)
    def fire(self):
        self.current_image = self.image[1]

    #우주선이 바라보는 각도 변경
    def draw(self, screen):

        if self.to == [-1,-1]:
            self.angle = 45
        elif self.to == [-1,0]:
            self.angle = 90
        elif self.to == [-1,1]:
            self.angle = 135
        elif self.to == [0,1]:
            self.angle = 180
        elif self.to == [1,1]:
            self.angle = 225
        elif self.to == [1,0]:
            self.angle = 270
        elif self.to == [1,-1]:
            self.angle = 315
        elif self.to == [0,-1]:
            self.angle = 0

        rotated = pygame.transform.rotate(self.current_image, self.angle)
        #최종 위치
        calib_pos = (
            self.pos[0] - rotated.get_size() [0]/2, 
            self.pos[1] - rotated.get_size() [1]/2
        )
        screen.blit(rotated, calib_pos)

        
    def goto(self, x, y):
        self.to[0] += x
        self.to[1] += y 

    #우주선 속도 설정
    def update(self, dt, screen):
        width, height = screen.get_size()
        self.pos[0] = (self.pos[0] + dt * self.to[0] * 0.5)
        self.pos[1] = (self.pos[1] + dt * self.to[1] * 0.5)
        #우주선 화면 이탈방지
        if self.pos[0] < 32:
            self.pos[0] = 32
        if self.pos[0] > width -32:
            self.pos[0] = width -32
        if self.pos[1] > height -32:
            self.pos[1] = height -32
        if self.pos[1] < 32:
            self.pos[1] = 32
        #대신 사용가능 코드
        # self.pos[0] = min(max(self.pos[0], 32), width-32) 
        # self.pos[1] = min(max(self.pos[1], 32), height-32)