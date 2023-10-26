import pygame
import time
import random
import sys

WIDTH,HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()

PLAYER_VEL =5
FPS = 60

class Grid:
    def draw_grid(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = ([[0 for j in range(self.num_cols)] for i in range(self.num_rows)])
        self.colors = self.get_cell_colors()
    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end = " ")
            print()

    def get_cell_colors(self):
        dark_grey = (26,31,40)
        green = (47,230,23)
        red = (232,18,18)
        orange = (226,116,17)
        yellow = (237,234,4)
        purple = (116,0,247)
        cyan = (21,204,209)
        blue = (13,64,216)

        return [dark_grey,green,red,orange,yellow, purple,cyan,blue]

    def draw(self):

def main():
    run = True
    while run:
        clock.tick(FPS)
        pygame.display.update
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


if __name__== "__main__":
    main()