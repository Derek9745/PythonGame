import pygame
import time
import random

WIDTH,HEIGHT = 850, 850
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Snake Blocks")
BG = pygame.transform.scale(pygame.image.load("Python wallpaper.jpg"), (WIDTH,HEIGHT))
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 40;
PLAYER_VEL =5;





def draw(player):
    WIN.blit(BG,(0,0))

    pygame.draw.rect(WIN, "blue", player)

    pygame.display.update()




def main():
    run = True
    player = pygame.Rect(200,0, PLAYER_WIDTH,PLAYER_HEIGHT)
    stoneblock = pygame.Rect(100, 100,PLAYER_WIDTH,PLAYER_HEIGHT)
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)

        if player.y + player.height <= HEIGHT:
            player.y+=1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >=0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT]and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL
        if keys[pygame.K_DOWN] and player.y + PLAYER_VEL + player.height <= HEIGHT:
            player.y += PLAYER_VEL
        draw(player)

    pygame.quit()

if __name__== "__main__":
    main()