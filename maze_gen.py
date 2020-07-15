import random, sys, pygame

pygame.font.init()

WIN_WIDTH, WIN_HEIGHT = 1000, 600

WINDOW = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Maze Generator And Solver")

BUTTON_SIZE = [(WIN_WIDTH - WIN_HEIGHT) // 1.3, WIN_HEIGHT // 10]

# Color Palette
WALL_COLOR = [0, 139, 139]
PATH_COLOR = [175, 234, 220]
TEXT_0 = [0, 139, 139]
GREEN = [0, 255, 0]

# Fonts
TITLE_FONT = pygame.font.SysFont("comicsans", 80)
LABEL_FONT = pygame.font.SysFont("comicsans", 20)




class Maze:
    def __init__(self, width):
        self.width = width
        self.height = width
        sys.setrecursionlimit(width * self.height)
        self.matrix = [[1 for x in range(self.height * 2)] for x in range(self.width * 2)]
        self.visited = []
        self.Xscale = (WIN_HEIGHT) // (len(self.matrix))
        self.Yscale = (WIN_HEIGHT) // (len(self.matrix[0]))

    def Generate_Recursively(self):
        self.matrix = [[1 for x in range(self.height * 2)] for x in range(self.width * 2)]
        self.Recursively_Make([0, 0])
        return

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
            self.matrix[y][x] = 0

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
                self.matrix[ty][tx] = 0
                self.matrix[(y + ty) // 2][(x + tx) // 2] = 0
                self.Recursively_Make([tx, ty])

    def Draw(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        WINDOW.fill(WALL_COLOR)
        for y in range(len(self.matrix[0])):
            for x in range(len(self.matrix)):
                if self.matrix[x][y] == 0:
                    pygame.draw.rect(WINDOW, PATH_COLOR, (
                        self.Xscale * x + self.Xscale // 2, self.Yscale * y + self.Yscale // 2, self.Xscale,
                        self.Yscale))
        pygame.draw.rect(WINDOW, PATH_COLOR, (WIN_HEIGHT, 0, WIN_WIDTH-WIN_HEIGHT, WIN_HEIGHT))

        text = TITLE_FONT.render("Create Maze", 1, TEXT_0)
        WINDOW.blit(text, (WIN_WIDTH - (WIN_WIDTH - WIN_HEIGHT) // 2 - text.get_width() // 2,
                           WIN_WIDTH // ((WIN_WIDTH - WIN_HEIGHT) // 2) + text.get_height()))

        pygame.display.update()