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
        self.Xscale = (WIN_WIDTH) // width//2
        self.Yscale = (WIN_HEIGHT) // height//2
        self.matrix = [[0 for x in range(width * 2)] for x in range(height * 2)]
        self.visited = []

    def Generate(self):
        self.Recursively_Make([0, 0])

    def available(self, x, y):
        pass

    def Recursively_Make(self, CurrentPos):
        while True:
            self.Draw(CurrentPos)
            self.visited.append(CurrentPos)
            x, y = CurrentPos[0], CurrentPos[1]
            print(CurrentPos)
            self.matrix[x][y] = 1

            rand = [[x - 2, y], [x + 2, y], [x, y - 2], [x, y + 2]]
            [tx, ty] = random.choice(rand)
            while [tx, ty] in self.visited or tx < 0 or ty >= len(self.matrix) or ty < 0 or tx >= len(self.matrix[0]):
                rand = [x for x in rand if x != [tx, ty]]
                if len(rand) <= 0:
                    return
                [tx, ty] = random.choice(rand)
            else:
                rand = [x for x in rand if x != [tx, ty]]
                self.visited.append([tx, ty])
                self.matrix[tx][ty] = 1
                self.matrix[(x + tx) // 2][(y + ty) // 2] = 1
                self.Recursively_Make([tx, ty])

    def Draw(self, CurrentPos):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        #pygame.time.Clock().tick(30)
        WINDOW.fill(WALL_COLOR)
        for y in range(len(self.matrix)):
            for x in range(len(self.matrix[0])):
                if self.matrix[x][y] == 1:
                    pygame.draw.rect(WINDOW, PATH_COLOR, (self.Xscale * x, self.Yscale * y, self.Xscale, self.Yscale))

        pygame.draw.rect(WINDOW, GREEN,
                         (self.Xscale * CurrentPos[0], self.Yscale * CurrentPos[1], self.Xscale * 2, self.Yscale * 2))

        pygame.display.update()


def main():
    run = True
    FPS = 10
    clock = pygame.time.Clock()

    maze = Maze(40, 40)

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        maze.Generate()


main()
