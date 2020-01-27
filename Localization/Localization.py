#!/usr/bin/env python3
import numpy as np

colors = [['R','G','G','R','R'],
          ['R','R','G','R','R'],
          ['R','R','G','G','R'],
          ['R','R','R','R','R']]

measurements = ['G','G','G','G','G']
motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]
sensor_right = 1.0
p_move = 1.0
sensor_wrong = 1.0 - sensor_right
p_stay = 1.0 - p_move

def localize(colors,measurements,motions,sensor_right,p_move):
    pinit = 1.0 / float(len(colors)) / float(len(colors[0]))
    p = [[pinit for row in range(len(colors[0]))] for col in range(len(colors))]
    

    return p

def show(p):
    '''rows = ['[' + ','.join(map(lambda x: '{0:.5f}'.format(x),r)) + ']' for r in p]
    print('[' + ',\n '.join(rows) + ']')'''
    for i in range(len(p)):
        print(p[i])


def sense(p,colors,measurements):

    aux = [[0.0 for row in range(len(p[0]))] for col in range(len(p))]
    s = 0.0
    for i in range(len(p)):
        for j in range(len(p[i])):
            hit = (measurements == colors[i][j])
            aux[i][j] = p[i][j]*(hit*sensor_right+(1-hit)*sensor_wrong)
            s += aux[i][j]
    for i in range(len(aux)):
        for j in range(len(p[i])):
            aux[i][j] /= s
    return aux

def move(p,motions):
    aux = [[0.0 for row in range(len(p[0]))] for col in range(len(p))]
    for i in range(len(p)):
        for j in range(len(p[i])):
            aux[i][j] = (p_move * p[(i-motions[0]) % len(p)][(j-motions[1]) % len(p[i])]) + (p_stay * p[i][j])
    return aux

'''if len(measurements) != len(motions):
    raise ValueError,"error in size of measurement/motion vector"'''

pinit = 1.0 / float(len(colors)) / float(len(colors[0]))
p = [[pinit for row in range(len(colors[0]))] for col in range(len(colors))]

for k in range(len(measurements)):
    p = move(p,motions[k])
    p = sense(p,colors,measurements[k])

show(p)

