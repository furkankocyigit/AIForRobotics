#!/usr/bin/env python3

p=[0.2, 0.2, 0.2, 0.2, 0.2]
#p= [0,1,0,0,0]
world=['green', 'red', 'red', 'green', 'green']
measurement = ['red','red']
motions = [1,1]
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

def sense(p,Z):
    q=[]
    for i in range(len(p)):
        hit=(Z==world[i])
        q.append(p[i]*(hit*pHit+(1-hit)*pMiss))
    s=sum(q)
    for i in range(len(q)):
        q[i]=q[i]/s
    return q

#for k in range(len(measurement)):
#    p = sense(p,measurement[k])

def move(p,U):
    '''U=U%len(p)
    q=p[-U:]+p[:-U]'''
    q=[]
    for i in range(len(p)):
        s = pExact * p[(i-U)%len(p)]
        s = s + pOvershoot * p[(i-U-1)%len(p)]
        s = s + pUndershoot *  p[(i-U+1)%len(p)]
        q.append(s)

    return q

for k in range(len(measurement)):
    p=sense(p,measurement[k])
    p=move(p,motions[k])
print(p)
'''print(p)
print("p[-2:]",p[-2:])
print("p[-3:]",p[-3:])
print("p[:-2]",p[:-2])
print("p[:-3]",p[:-3])
print("p[2:]",p[2:])
print("p[3:]",p[3:])
print("p[:2]",p[:2])
print("p[:3]",p[:3])'''