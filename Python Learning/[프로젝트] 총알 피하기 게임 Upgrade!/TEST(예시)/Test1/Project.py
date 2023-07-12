import pygame

WIDTH, HEIGHT = 700, 800

screen_size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(screen_size)

image1 = pygame.image.load("test1.png")
image1 = pygame.transform.scale(image1,(300,300))
image2 = pygame.image.load("test2.png")
image2 = pygame.transform.scale(image2,(300,300))

pygame.init()

class Enemy():
    def __init__(self):
        self.images = [image1, image2]
        self.current_image = self.images[0]


enemy = Enemy()
gameloop_count = 0

running = True
while running:
    for event in pygame.event.get():
        # gameloop_count += 1
        screen.blit(enemy.current_image, (WIDTH/2, HEIGHT/2))
        # print(gameloop_count, ":", event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # screen.fill((0,0,0))
            enemy.current_image = enemy.images[1]
        if event.type == pygame.KEYUP:
            enemy.current_image = enemy.images[0]

    pygame.display.update()