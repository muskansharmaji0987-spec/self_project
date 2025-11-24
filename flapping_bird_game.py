# Flapping bird Game(For entertainmnet Purpose):

import pygame
import sys
import random

pygame.init()
WIDTH,HEIGHT = 800,600
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Flappy Bird")

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (34,139,34)
BLUE = (135,206,235)
YELLOW = (255,255,0)
FONT = pygame.font.SysFont("aerial" , 32)

gravity = 0.5
bird_movement = 0
score = 0
high_score = 0
game_active = True

bird = pygame.Rect(100,HEIGHT//2,30,30)

pipe_width = 60
pipe_gap = 175
pipes = []
scored_pipes = []

def create_pipe():
    height = random.randint(100,400)
    top = pygame.Rect(WIDTH,0,pipe_width,height)
    bottom = pygame.Rect(WIDTH,height+pipe_gap , pipe_width,HEIGHT - height - pipe_gap)
    return top,bottom

SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE , 1500)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if game_active:
                    bird_movement = -10
                else:
                    bird.y = HEIGHT//2
                    bird_movement = 0
                    pipes.clear()
                    scored_pipes.clear()
                    score = 0
                    game_active = True

        if event.type == SPAWNPIPE and game_active:
            pipes.extend(create_pipe())

    if game_active:
        bird_movement += gravity
        bird.y += bird_movement

        for pipe in pipes:
            pipe.x -= 4

        pipes = [pipe for pipe in pipes if pipe.right>0]

        for pipe in pipes:
            if bird.colliderect(pipe):
                game_active = False

        if bird.top<=0 or bird.bottom>=HEIGHT:
            game_active = False

        for i in range(0,len(pipes),2):
            pipe = pipes[i]
            if pipe.right< bird.left and pipe not in scored_pipes:
                score+=1
                scored_pipes.append(pipe)
        
    WIN.fill(BLUE)

    if game_active:
        pygame.draw.rect(WIN,YELLOW,bird)
        for pipe in pipes:
            pygame.draw.rect(WIN,GREEN, pipe)

        score_text = FONT.render(f"score: {score}",True, BLACK)

        WIN.blit(score_text,(10,10))
    else:
        game_over_text = FONT.render("Game Over",True, BLACK)
        WIN.blit(game_over_text,(WIDTH//2, HEIGHT//2-60))

        restart_text = FONT.render("Press Space To Restart", True, BLACK)

        WIN.blit(restart_text,(WIDTH//2 - restart_text.get_width()//2 , HEIGHT//2))

        if score> high_score:
            high_score = score
        hs_text = FONT.render(f"High score: {high_score}", True, BLACK)
        WIN.blit(hs_text,(WIDTH//2 - hs_text.get_width()//2 , HEIGHT//2+50))
    pygame.display.update()
    clock.tick(60)



