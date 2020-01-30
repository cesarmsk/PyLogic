

import sys

from random import randint



#################

# function: available_positions

# params: maze (array)

# objective: given a maze, returns all available positions

#################

def available_positions(maze):

    positions = []

    for row in range(len(maze)):

        for col in range(len(maze[row])):

            if maze[row][col] != 0:

                positions.append((row, col))



    return positions



#################

# function: possible_back_moves

# params: maze (array), current_row (int), current_col (int)

# objective: given a position of a maze, returns an array with possible reverse moves

#################

def possible_back_moves(maze, current_row, current_col):

    possible = []

    next_row = current_row - 1

    next_col = current_col - 1

    if (next_row >= 0 and maze[next_row][current_col] != 0):

        possible.append((next_row, current_col))



    if (next_col >= 0 and maze[current_row][next_col] != 0):

        possible.append((current_row, next_col))



    return possible



#################

# function: add_route

# params: origin (tuple), destination (tuple), cost (int), routes (dict)

# objective: creates or updates the cost of an origin position to next position (destination)

#################

def add_route(origin, destination, cost, routes):

    if origin in routes:

        routes[origin][destination] = cost

    else:

        routes[origin] = { destination: cost }



#################

# function: fill_routes

# params: maze (array), maze_costs (array), current_row (int), current_col (int)

# objective: recursive function that returns an dict with all positions and its costs to end

#################

def fill_routes(maze, maze_costs, current_row, current_col, last_cost = 0, last_position = (), routes = {}):

    cost = maze_costs[current_row][current_col] + last_cost
    add_route((current_row, current_col), last_position, cost, routes)
    current_position = (current_row, current_col)

    for position in possible_back_moves(maze, current_row, current_col):

        fill_routes(maze, maze_costs, position[0], position[1], cost, current_position, routes)



    return routes



#################

# function: geneRobote_position

# params: available_positions (array)

# objective: given an array with available positions, returns a random available position

#################

def geneRobote_position(available_positions):

    drawn_position = available_positions[randint(0, len(available_positions)-1)]

    return drawn_position



#################

# function: put_cat

# params: maze_costs (array), position (tuple)

# objective: just updates the cost of the given position

#################

def put_cat(maze_costs, position):

    maze_costs[position[0]][position[1]] = float('inf')



#################

# function: go_Robot

# params: position (tuple), routes (dict)

# objective: returns the next minimum position, from the given position

#################

def go_Robot(position, routes):

    minimum = float('inf')

    next_route = None

    
    for route in routes[(position[0], position[1])]:

        route_cost = routes[(position[0], position[1])][route]

        if route_cost < minimum:

            minimum = route_cost

            next_route = route



    return next_route



#################

# function: Robot_start_position

# params: maze (array)

# objective: returns the start position of the maze

#################

def Robot_start_position(maze):

    i = 0

    for row in maze:

        j = 0

        for elem in row:

            if elem == 'S':

                return (i, j)

            j += 1

        i += 1



#################

# function: exit_position

# params: maze (array)

# objective: returns the exit position of the maze >> 9

#################

def exit_position(maze):

    i = 0

    for row in maze:

        j = 0

        for elem in row:

            if elem == 9:

                return (i, j)

            j += 1

        i += 1



#################

# function: escape

# params: maze (array), maze_costs (array), Robot_position (tuple), exit_position (tuple), available_positions (array), routes (dict)

# objective: uses all other functions, tries to reaches the exit position

# throws a cat before to walk with the Robot

# if no restrictions, walk with Robot

#################

def escape(maze, maze_costs, Robot_position, exit_position, available_positions, routes, output = sys.stdout):

    while Robot_position != exit_position:

        #updates the routes

        routes = fill_routes(maze, maze_costs, exit_position[0], exit_position[1])



        #tries to walk with Robot

        Robot_position = go_Robot(Robot_position, routes)



        #there's no way to go

        if Robot_position is None:

            output.write("There's no way to Robot\n")

            break

        else:

            output.write("Robot goes to " + `Robot_position` + "\n")



