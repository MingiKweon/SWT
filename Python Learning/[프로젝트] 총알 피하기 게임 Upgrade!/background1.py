import pygame

pygame.init()

WIDTH = 400
HEIGHT = 400

pygame.display.set_caption("TEST")

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FPS = 120

back1 = pygame.image.load("")
back1 = pygame.transform.scale(,(100,100))

running = True
while running:
    dt = clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.display.update()