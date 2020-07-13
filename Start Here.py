import pygame
import mazegen

WIN_WIDTH, WIN_HEIGHT = 800, 600

WINDOW = pygame.display.set_mode(WIN_WIDTH, WIN_HEIGHT)
pygame.display.set_caption("Maze Generator And Solver")

# Color Pallete
WALL_COLOR = [0,0,0]
PATH_COLOR = [255,255,255]


def main():
	m = mazegen.Generate_Maze(50,50)

