#!/usr/bin/env python3


# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space


grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]]

heuristic = [[9, 8, 7, 6, 5, 4],
             [8, 7, 6, 5, 4, 3],
             [7, 6, 5, 4, 3, 2],
             [6, 5, 4, 3, 2, 1],
             [5, 4, 3, 2, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search():
    # open list elements are of the type: [g, x, y]

    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed[init[0]][init[1]] = 1

    expand = [[-1 for row in range(len(grid[0])) ] for col in range(len(grid))]
    expand[init[0]][init[1]] = 0
    action = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]

    
    x = init[0]
    y = init[1]
    g = 0
    h = heuristic[x][y]
    f = h + g
    count = 0

    open = [[f, g, h, x, y]]

    found = False       #flag that is set when search complete
    resign = False      #flag set if we can't find expand
    print('initial open list: ')
    for i in range(len(open)):
        print('    ',open[i])
    print('-----------------')

    while found is False and resign is False:
        
        #check if we still have elements on the open list
        if len(open)== 0:
            resign = True
            print('FAIL')
            print('##### Search terminated without success')
        else:
            #remove node from list
            open.sort()
            open.reverse()
            next = open.pop()
            print('take list item')
            print(next)
            x = next[3]
            y = next[4]
            g = next[1]

            expand[x][y] = count
            count += 1
            

            #check if we are done
            if x == goal[0] and y == goal[1]:
                found = True
                print(next)
                print("#### Search Succesful")
            else:
                #expand winning element and add to new list
                step = 0
                for i in range (len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    step += 1
                    if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            h2 = heuristic[x2][y2]
                            f2 = g2 + h2
                            open.append([f2, g2, h2, x2, y2])
                            print('append list item ')
                            print([f2, g2, h2, x2, y2])
                            closed[x2][y2] = 1
                            action[x2][y2] = i

                            #debug = 1
    path = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    x = goal[0]
    y = goal[1]
    path[x][y] = '*'
    debug = True
    
    while x != init[0] or y != init[1]:
        x2 = x - delta[action[x][y]][0]
        y2 = y - delta[action[x][y]][1]
        path[x2][y2] = delta_name[action[x][y]]
        x = x2
        y = y2
        debug = True
    for i in range(len(expand)):
        print(expand[i])
    for i in range(len(path)):
        print (path[i])



search()