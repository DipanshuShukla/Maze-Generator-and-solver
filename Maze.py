import pygame
import random

WIN_WIDTH, WIN_HEIGHT = 800, 800

WINDOW = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Maze Generator And Solver")

# Color Palette
WALL_COLOR = [0, 0, 0]
PATH_COLOR = [255, 255, 255]
GREEN = [0, 255, 0]


class Maze:
    def __init__(self, width):
        height = width
        self.matrix = [[0 for x in range(height * 2)] for x in range(width * 2)]
        self.visited = []
        self.Xscale = (WIN_WIDTH) // (len(self.matrix))
        self.Yscale = (WIN_HEIGHT) // (len(self.matrix[0]))

    def Generate(self):
        self.Recursively_Make([0, 0])
        return

    def available(self, x, y):
        pass

    def Recursively_Make(self, CurrentPos):
        while True:
            self.Draw()
            pygame.draw.rect(WINDOW, GREEN,
                             (self.Xscale * CurrentPos[1] + self.Xscale // 2,
                              self.Yscale * CurrentPos[0] + self.Yscale // 2, self.Xscale * 2,
                              self.Yscale * 2))
            pygame.display.update()
            self.visited.append(CurrentPos)
            x, y = CurrentPos[0], CurrentPos[1]
            self.matrix[y][x] = 1

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
                self.matrix[ty][tx] = 1
                self.matrix[(y + ty) // 2][(x + tx) // 2] = 1
                self.Recursively_Make([tx, ty])

    def Draw(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        WINDOW.fill(WALL_COLOR)
        for y in range(len(self.matrix[0])):
            for x in range(len(self.matrix)):
                if self.matrix[x][y] == 1:
                    pygame.draw.rect(WINDOW, PATH_COLOR, (
                        self.Xscale * x + self.Xscale // 2, self.Yscale * y + self.Yscale // 2, self.Xscale,
                        self.Yscale))
        pygame.display.update()


def main():
    run = True
    FPS = 10
    clock = pygame.time.Clock()

    maze = Maze(40)

    while run:
        #clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            maze.Generate()
        maze.Draw()




main()
