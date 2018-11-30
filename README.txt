This project was to try and code a maze maker and solver. Runs in python 3.

The solver is the same code as found here (https://www.laurentluce.com/posts/solving-mazes-using-python-simple-recursivity-and-a-search/). This is a brilliant blog post with a ton of good info, diagrams, and code walkthroughs for maze solving.

the maze maker way originally the no Zigzag version of the code here (http://code.activestate.com/recipes/578356-random-maze-generator/) that I modified to include the solver.

It works pretty well. There are definitely faster solvers out there but this was just a test so I'm happy with how it performs.

### NOTE ###
## This Requires PIL, so if you have Tensorflow installed you will have to make another python environment, if you are using anaconda this is easy, otherwise, google away.

Running Maze.py will produce a PNG maze, solution, and maze+solution.

If you want to change the map shape or output PNG resolution just use maze_solve(imgx, imgy, mx, my), where imgx and imgy are number of pixels in x and y in the PNG, respectively. mx and my are the number of columns and rows in the maze, respectively.
I was going to make this run via command line, but I'm lazy. Feel free to make it so, also the maze maker should be object wise, but again, lazy.

Hope you enjoy
Let me know if you have any comments or questions.
Thanks,
