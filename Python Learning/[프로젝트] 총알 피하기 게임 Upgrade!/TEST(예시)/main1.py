import pygame
from player1 import Player
from bullet1 import Bullet
import random
import time

def collision(a,b):
    dist = ((a.pos[0] - b.pos[0]) ** 2 + (a.pos[1] - b.pos[1]) ** 2) ** 0.5
    if dist < 10:
        return True
    else:
        return False

pygame.init()
WIDTH, HEIGHT = 500, 400

pygame.display.set_caption("총알 피하기")

clock = pygame.time.Clock()
FPS = 60

bullets = []
for i in range(10):
    bullets.append(Bullet(0, random.random()*HEIGHT, 2 * (random.random()-0.5), 2*(random.random()-0.5)))

screen = pygame.display.set_mode((WIDTH, HEIGHT))

player = Player(screen)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

running = True
g = 0
while running:
    
    dt = clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.goto(-1,0)
            elif event.key == pygame.K_RIGHT:
                player.goto(1,0)
            elif event.key == pygame.K_UP:
                player.goto(0,-1)
            elif event.key == pygame.K_DOWN:
                player.goto(0,1)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.goto(1,0)
            elif event.key == pygame.K_RIGHT:
                player.goto(-1,0)
            elif event.key == pygame.K_UP:
                player.goto(0,1)
            elif event.key == pygame.K_DOWN:
                player.goto(0,-1)

    screen.fill((0,0,0))
    
    player.update(dt, screen)
    player.draw(screen)
    
    for b in bullets:
        b.update_and_draw(dt, screen)
        
    for b in bullets:
        if collision(player, b):
            running = False

    pygame.display.update()

