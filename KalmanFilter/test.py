#!/usr/bin/env python3
from math import * 
value= [[0,1,2],[3,4,5],[6,7,8]]
value = [[0 for row in range(len(value))] for col in range(len(value[0]))]
print(value)

a= [[1,2,3],
    [1,2,3]]
b= [[1,2,3],
    [1,2,3]]

c = a+b
open=[[2,4,1],[8,0,0],[3,0,1]]
open.sort()
print('sort: ',open)
open.reverse()
print('reverse: ',open)
next = open.pop()
print('next: ',next)
next = open.pop()
print('next: ',next)

furkan = [[0 for row in range(len(b[0]))] for col in range(len(b))]
print("furkan:",furkan)
