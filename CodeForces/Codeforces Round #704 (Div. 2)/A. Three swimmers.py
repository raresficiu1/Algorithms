#https://codeforces.com/contest/1492/problem/A
import math
t = int(input())



for i in range(t):

    p,a,b,c = [int(j) for j in input().split(' ')]

    if(p==a or p==b or p==c):
        print(0)
    else:
        a1=(int(p/a+1))*a-p
        b1=(int(p/b+1))*b-p
        c1=(int(p/c+1))*c-p

        k=[a1,b1,c1]

        print(min(k))

