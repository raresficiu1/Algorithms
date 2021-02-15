#https://codeforces.com/contest/1485/problem/0
import math

t = int(input())

for i in range(t):

    a,b=input().split(' ')
    a=float(a)
    b=float(b)


    if(a>b):
        if (b==1):
            max_nr_steps = a
        else:
            max_nr_steps = math.log(a,b)+1
        print(max_nr_steps)
        x=max_nr_steps
        fac=2
        while(fac<=x):
            nou=math.log(a,(b+fac))+fac
            print(nou)
            if(nou<max_nr_steps):
                max_nr_steps=nou
                x=max_nr_steps
            fac+=1

        frac, whole = math.modf(max_nr_steps)
        if(frac>0.999):
            print(math.ceil(max_nr_steps)-1)
        else:
            print(math.ceil(max_nr_steps))

    elif(a==b):
        print(2)
    else:
        print(1)



