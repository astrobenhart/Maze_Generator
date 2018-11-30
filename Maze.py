import random
from PIL import Image
import maze_solver
if __name__ == '__main__':
    def make_maze(imgx, imgy, mx, my):
        # imgx = 1000; imgy = 1000
        image = Image.new("RGB", (imgx, imgy))
        pixels = image.load()
        # mx = 30; my = 30 # width and height of the maze
        maze = [[0 for x in range(mx)] for y in range(my)]
        dx = [0, 1, 0, -1]; dy = [-1, 0, 1, 0] # 4 directions to move in the maze
        color = [(0, 0, 0), (255, 255, 255)] # RGB colors of the maze
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

        # Add border to the maze and add gaps for start and end
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

        # Turn maze into a list of tuples representing walls for solver
        maze_tuple=[]
        for lists in range(len(maze)):
            for wall in range(len(maze[lists])):
                if maze[lists][wall] == 0:
                    maze_tuple.append((wall, lists))
        print('and again')

        # save a PNG of the maze
        for ky in range(imgy):
            for kx in range(imgx):
                pixels[kx, ky] = color[maze[(my+2) * ky / imgy][(mx+2) * kx / imgx]]

        image.save("Maze_" + str(mx) + "x" + str(my) + ".png", "PNG")

        return maze_tuple, mx+2, my+2, imgx, imgy

    def maze_solve(imgx = 1000, imgy = 1000, mx = 30, my = 30):
        maze_tuple, mx, my, imgx, imgy = make_maze(imgx, imgy, mx, my)
        start = (0, 1)
        end = (mx, my)

        print('and again')

        solver = maze_solver.AStar()
        solver.init_grid(mx+2, my+2, maze_tuple, start, end)
        fastest_path = solver.solve()
        # return fastest_path
        if fastest_path == None:
            while fastest_path == None:
                maze_tuple, mx, my, imgx, imgy = make_maze()
                fastest_path = maze_solve(mx, my, maze_tuple)

        fastest_path = map(list, fastest_path)

        # Turn tuple solution into list like maze walls
        fastest_path_list = [[0] * (mx+2) for i in range(my+2)]
        for walls_t in fastest_path:
            x_m = walls_t[1]
            y_m = walls_t[0]
            #print((x_m, y_m))
            fastest_path_list[x_m][y_m] = 1

        print('and again')

        # Save solution to PNG with transperant background
        image = Image.new("RGBA", (imgx, imgy))
        pixels = image.load()
        color = [(255,255,255,0), (255, 0, 0,255)]
        for ky in range(imgy):
            for kx in range(imgx):
                pixels[kx, ky] = color[fastest_path_list[(my) * ky / imgy][(mx) * kx / imgx]]

        image.save("Maze_" + str(mx-2) + "x" + str(my-2) + "_sol.png", "PNG")

        # Merge maze and solution and save as new PNG
        background = Image.open("Maze_" + str(mx-2) + "x" + str(my-2) + ".png")
        foreground = Image.open("Maze_" + str(mx-2) + "x" + str(my-2) + "_sol.png")
        background.paste(foreground, (0, 0), foreground)
        background.save("Maze_" + str(mx-2) + "x" + str(my-2) + "_solution.png")

        print('finally')

maze_solve()
