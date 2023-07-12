#모듈 가져오기
import pygame 
from player import Player
from bullet import Bullet1, Bullet2, Bullet3
from background import Background
import random
from math import sqrt
import time

#pygame 시작
pygame.init()

#배경음악 설정
pygame.mixer.Channel(0).play(pygame.mixer.Sound("sounds/bgm.wav")) #배경음악

#시작시간 저장
start_time = time.time()

#게임화면 크기
WIDTH, HEIGHT = 700, 700

#게임 프로그램 제목(상단에 표시)
pygame.display.set_caption("총알 피하기")

#게임 시스템 설정값
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FPS = 120
Health = 70

#클래스 불러오기
player = Player(screen)
background = Background(screen)

#충돌 시 작동하는 함수 설정
def collision(a,b):
    #global 변수 불러오기
    global Health
    
    #우주선과 총알의 거리
    dist = sqrt((a.pos[0] - b.pos[0]) ** 2 + (a.pos[1] - b.pos[1]) ** 2)
    #조건
    if dist < 10:
        #충돌 시 번쩍이는 효과
        player.fire()
        #충돌 시 효과음
        pygame.mixer.Channel(1).play(pygame.mixer.Sound("sounds/break_sound.mp3"))
        #체력 감소
        Health -= 2
        if Health == 0:
            return True
        else:
            return False
    else:
        return False

#글씨 화면출력 함수
def draw_text(txt,size,pos,color,screen):
    font = pygame.font.Font('freesansbold.ttf',size)
    r = font.render(txt,True,color)
    screen.blit(r,pos)

#총알 개수
bullets = []
for i in range(1):
    bullets.append(Bullet1(0,random.random()*HEIGHT,random.random()-0.5, random.random()-0.5))
    bullets.append(Bullet2(0,random.random()*HEIGHT,random.random()-0.5, random.random()-0.5))
    bullets.append(Bullet3(0,random.random()*HEIGHT,random.random()-0.5, random.random()-0.5))


time_for_adding_bullets = 0

gameover = False
#점수 변수(엔드화면에서 출력)
score = 0
running = True

#게임실행
while running:
    current_time = time.time()
    dt = clock.tick(FPS) #Frame Per Second #이거 다시..
    
    for event in pygame.event.get():
        #충돌 - 게임종료
        if event.type == pygame.QUIT:
            running = False
        #우주선 이동
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.goto(-1,0)
                background.goto(-1,0)
            elif event.key == pygame.K_RIGHT:
                player.goto(1,0)
                background.goto(1,0)

            elif event.key == pygame.K_UP:
                player.goto(0,-1)
                background.goto(0,-1)

            elif event.key == pygame.K_DOWN:
                player.goto(0,1) #화면 왼쪽 위가 (0,0) 기준
                background.goto(0,1)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.goto(1,0)
                background.goto(1,0)

            elif event.key == pygame.K_RIGHT:
                player.goto(-1,0)
                background.goto(-1,0)

            elif event.key == pygame.K_UP:
                player.goto(0,1)
                background.goto(0,1)

            elif event.key == pygame.K_DOWN:
                player.goto(0,-1)
                background.goto(0,-1)

    #배경그림 이동(우주선 이동에 따라)
    background.update(dt,screen)
    #사용자가 보는 화면을 둘러싼 주위 그림8개 출력
    screen.blit(background.image1, (background.pos1[0], background.pos1[1]))
    screen.blit(background.image2, (background.pos2[0], background.pos2[1]))
    screen.blit(background.image3, (background.pos3[0], background.pos3[1]))
    screen.blit(background.image4, (background.pos4[0], background.pos4[1]))
    screen.blit(background.image2, (background.pos5[0], background.pos5[1]))
    screen.blit(background.image3, (background.pos6[0], background.pos6[1]))
    screen.blit(background.image4, (background.pos7[0], background.pos7[1]))
    screen.blit(background.image4, (background.pos8[0], background.pos8[1]))
    screen.blit(background.image4, (background.pos9[0], background.pos9[1]))
    #우주선 출력
    player.update(dt,screen)
    player.draw(screen) #134, 135 순서대로 실행
    #총알 출력
    for b in bullets:
        b.update_and_draw(dt,screen)
    
    #엔드화면 출력값
    if gameover:

        score = time.time() - start_time
        draw_text("GAME OVER", 50, (WIDTH/2 -147.5, HEIGHT/2 - 50), (255,255,255), screen)
        txt = "Time: {:.1f}, Bullets: {}".format(score, len(bullets))
        draw_text(txt, 15, (WIDTH/2 - 63, HEIGHT/2 + 50), (255,255,255), screen)


    else:
        txt1 = "Time: {:.1f}, Bullets: {}, Health: {}".format(time.time()-start_time, len(bullets), Health)
        txt2 = "HP: "+"ㅁ"*Health
        draw_text(txt1, 16, (10,10), (255,255,255), screen)
        draw_text(txt2, 10, (player.pos[0] - 90, player.pos[1] - 70), (255,255,255), screen)
        draw_text(txt2, 13, (10, 27), (255, 0 ,0), screen)

    pygame.display.update()

    if gameover:
        
        time.sleep(1.5)
        running = False
    elif not gameover:
        for b in bullets:
            if collision(player,b):
                    gameover = True
                
        
        time_for_adding_bullets += dt
        if time_for_adding_bullets >= 1000:
            bullets.append(Bullet1(random.random()*WIDTH,random.random()*HEIGHT,random.random()-0.5, random.random()-0.5))
            bullets.append(Bullet2(random.random()*WIDTH,random.random()*HEIGHT,random.random()-0.5, random.random()-0.5))
            bullets.append(Bullet3(random.random()*WIDTH,random.random()*HEIGHT,random.random()-0.5, random.random()-0.5))
            time_for_adding_bullets -= 1000