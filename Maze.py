from maze_gen import *


if __name__ == "__main__":
    maze = Maze(60)
    maze.Generate_Recursively()
    while True:
        maze.Draw()
