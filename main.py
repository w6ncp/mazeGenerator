from graphics import Window
from maze import Maze
import sys
    

def main():
    num_rows = 20
    num_cols = 36
    margin = 50
    screen_x = 1920
    screen_y = 1080
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows

    seed = 9662742662472669

    sys.setrecursionlimit(10000)
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, seed)
    print("maze created")
    is_solvable = maze.solve()
    maze._animate()
    if not is_solvable:
        print("maze can not be solved!")
    else:
        print("maze solved!")

    win.wait_for_close()

main()