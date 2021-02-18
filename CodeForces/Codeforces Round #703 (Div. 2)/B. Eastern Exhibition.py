#https://codeforces.com/contest/1486/problem/B

#TLE

t = int(input())

for i in range(t):

    n= int(input())

    points=[]
    x=0
    y=0
    for j in range(n):
        point = [int(i) for i in input().split(' ')]
        points.append(point)
        if(point[0]>x):
            x=point[0]
        if(point[1]>y):
            y=point[1]


    min_distance=9999999999
    nr=0
    for xi in range(x+1):
        for yj in range(y+1):
            distance=0
            for point in points:
                distance+= abs(xi-point[0])+abs(yj-point[1])
                #print(xi,point[0],'    ',yj,point[1],'    ',distance,min_distance)
            if(distance<min_distance):
                nr=0
                min_distance=distance
            if(distance==min_distance):
                nr+=1


    print(nr)

