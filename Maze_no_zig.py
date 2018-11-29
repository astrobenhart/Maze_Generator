# Random Maze Generator using Depth-first Search
# http://en.wikipedia.org/wiki/Maze_generation_algorithm
# FB36 - 20130106
import random
from PIL import Image
import maze_solver
if __name__ == '__main__':
    def make_maze():
        imgx = 2100; imgy = 2970
        image = Image.new("RGB", (imgx, imgy))
        pixels = image.load()
        mx = 5; my = 6 # width and height of the maze
        maze = [[0 for x in range(mx)] for y in range(my)]
        dx = [0, 1, 0, -1]; dy = [-1, 0, 1, 0] # 4 directions to move in the maze
        color = [(0, 0, 0), (255, 255, 255)] # RGB colors of the maze
        # start the maze from a random cell
        # cx = random.randint(0, mx - 1); cy = random.randint(0, my - 1)
        # Start the maze from top left
        cx = 0; cy = 0
        maze[cy][cx] = 1; stack = [(cx, cy, 0)] # stack element: (x, y, direction)

        while len(stack) > 0:
            (cx, cy, cd) = stack[-1]
            # to prevent zigzags:
            # if changed direction in the last move then cannot change again
            if len(stack) > 2:
                if cd != stack[-2][2]: dirRange = [cd]
                else: dirRange = range(4)
            else: dirRange = range(4)

            # find a new cell to add
            nlst = [] # list of available neighbors
            for i in dirRange:
                nx = cx + dx[i]; ny = cy + dy[i]
                if nx >= 0 and nx < mx and ny >= 0 and ny < my:
                    if maze[ny][nx] == 0:
                        ctr = 0 # of occupied neighbors must be 1
                        for j in range(4):
                            ex = nx + dx[j]; ey = ny + dy[j]
                            if ex >= 0 and ex < mx and ey >= 0 and ey < my:
                                if maze[ey][ex] == 1: ctr += 1
                        if ctr == 1: nlst.append(i)

            # if 1 or more neighbors available then randomly select one and move
            if len(nlst) > 0:
                ir = nlst[random.randint(0, len(nlst) - 1)]
                cx += dx[ir]; cy += dy[ir]; maze[cy][cx] = 1
                stack.append((cx, cy, ir))
            else: stack.pop()
        print('Done')

        # import numpy as np
        # print(np.size(maze))

        # Add a black border around entire Maze and add start end points
        for i in maze:
            i.insert(0,0)
            i.append(0)
        maze.insert(0,[0]*len(maze[0]))
        maze.append([0]*len(maze[0]))
        maze[1][0] = 1
        if maze[-2][-2] == 1:
            maze[-2][-1] = 1
        else:
            maze[-2][-1] = 1
            maze[-2][-2] = 1

        print('Done again')
        # Turn maze into a list of tuples representing walls
        maze_tuple=[]
        for lists in range(len(maze)):
            for wall in range(len(maze[lists])):
                if maze[lists][wall] == 0:
                    maze_tuple.append((wall, lists))

        # start = (1, 1)
        # end = (mx, my)

        print('and again')

        # solver = maze_solver.AStar()
        # solver.init_grid(mx+2, my+2, maze_tuple, start, end)
        # fastest_path = solver.solve()

        for ky in range(imgy):
            for kx in range(imgx):
                pixels[kx, ky] = color[maze[(my+2) * ky / imgy][(mx+2) * kx / imgx]]

        image.save("Maze_" + str(mx) + "x" + str(my) + ".png", "PNG")

        return maze_tuple, mx, my

    def maze_solve(mx, my, maze_tuple):
        start = (1, 1)
        end = (mx+1, my)

        print('and again')

        solver = maze_solver.AStar()
        solver.init_grid(mx+2, my+2, maze_tuple, start, end)
        fastest_path = solver.solve()
        return fastest_path

    fastest_path = None

    while fastest_path == None:
        maze_tuple, mx, my = make_maze()
        fastest_path = maze_solve(mx, my, maze_tuple)

    fastest_path = map(list, fastest_path)
    print(fastest_path)

    fastest_path_list = [[0] * (mx+2) for i in range(my+2)]

    for walls_t in fastest_path:
        x_m = walls_t[1]
        y_m = walls_t[0]
        fastest_path_list[y_m][x_m] = 1

    for i in fastest_path_list:
        print(i)

    print('and again')

    # paint the maze
    imgx = 2100; imgy = 2970
    image = Image.new("RGB", (imgx, imgy))
    pixels = image.load()
    color = [(0, 0, 0), (255, 255, 255)]
    # for ky in range(imgy):
    #     for kx in range(imgx):
    #         pixels[kx, ky] = color[maze[(my+2) * ky / imgy][(mx+2) * kx / imgx]]
    #
    # image.save("Maze_" + str(mx) + "x" + str(my) + ".png", "PNG")


    color = [(255,255,255), (255, 0, 0)]
    for ky in range(imgy):
        for kx in range(imgx):
            pixels[kx, ky] = color[fastest_path_list[(my+2) * ky / imgy][(mx+2) * kx / imgx]]

    image.save("Maze_" + str(mx) + "x" + str(my) + "_sol.png", "PNG")

    print('finally')
