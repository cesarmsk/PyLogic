import sys
from functions import *
import utils



#matriz layout: maze.txt
maze_file = open('maze.txt' , 'r')
lines = maze_file.read().splitlines()
maze = []
output = sys.stdout
output.write('\nMatriz:\n')
output.write('=======\n')

i = 0
for line in lines:
    splitted_line = line.split(' ')
    maze.append([])
    output.write(line + '\n')
    for elem in splitted_line:
        if utils.is_number(elem):
            maze[i].append(int(elem))
        else:
            maze[i].append(elem)
        
    i += 1
    

output.write('\nShortest Path:\n')
output.write('==============\n')

maze_costs_file = open('maze_costs.txt' , 'r')
maze_costs = [ map(int,line.split(' ')) for line in maze_costs_file ]

Robot_position = Robot_start_position(maze)
exit_position = exit_position(maze)
routes = fill_routes(maze, maze_costs, exit_position[0], exit_position[1])

maze_available_positions = available_positions(maze)
escape(maze, maze_costs, Robot_position, exit_position, maze_available_positions, routes)
