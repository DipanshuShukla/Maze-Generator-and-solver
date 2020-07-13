import pygame
import random

WIN_WIDTH, WIN_HEIGHT = 800, 600

WINDOW = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Maze Generator And Solver")

# Color Palette
WALL_COLOR = [0, 0, 0]
PATH_COLOR = [255, 255, 255]
GREEN = [0, 255, 0]


class Maze:
    def __init__(self, width, height):
        self.visited = []
        self.Xscale = WIN_WIDTH // (width // 2)
        self.Yscale = WIN_HEIGHT // (height // 2)
        self.matrix = [[0 for x in range(width * 2)] for x in range(height * 2)]

    def Generate(self):
        self.Recursively_Make([0,0])

    def available(self, x, y):
        avl = []
        print(self.visited)
        if x-2 > 0 and [x-2, y] not in self.visited:
            avl.append([-2, 0, -1, 0])
        if x + 2 < len(self.matrix[0]) and [x-2, y] not in self.visited:
            avl.append([2, 0, 1, 0])
        if y-2 > 0 and [x, y-2] not in self.visited:
            avl.append([0, -2, 0, -1])
        if y + 2 < len(self.matrix) and [x, y+2] not in self.visited:
            avl.append([0, 2, 0, 1])
        return avl

    def Recursively_Make(self, CurrentPos):
        self.Draw(CurrentPos)
        self.visited.append(CurrentPos)
        self.matrix[CurrentPos[0]][CurrentPos[1]] = 1
        available = self.available(CurrentPos[0], CurrentPos[1])
        if len(available) == 0:
            return
        else:
            while True:
                move = random.choice(available)
                self.matrix[CurrentPos[0] + move[2]][CurrentPos[1] + move[3]] = 1
                CurrentPos = [CurrentPos[0] + move[0], CurrentPos[1] + move[1]]
                self.Recursively_Make(CurrentPos)

    def Draw(self,CurrentPos):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        pygame.time.Clock().tick(30)
        WINDOW.fill(WALL_COLOR)
        for y in range(len(self.matrix)):
            for x in range(len(self.matrix[0])):
                if self.matrix[x][y] == 1:
                    pygame.draw.rect(WINDOW, PATH_COLOR, (self.Xscale*x, self.Yscale*y, self.Xscale,self.Yscale))

        pygame.draw.rect(WINDOW, GREEN, (self.Xscale * CurrentPos[0], self.Yscale * CurrentPos[1], self.Xscale, self.Yscale))
        
        pygame.display.update()


def main():
    run = True
    FPS = 10
    clock = pygame.time.Clock()

    maze = Maze(50,50)

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        maze.Generate()

main()