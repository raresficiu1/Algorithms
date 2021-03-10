#https://codeforces.com/contest/1496/problem/B
import math
t = int(input())

for i in range(t):
    n,k = input().split(' ')
    k=int(k)
    string = [int(j) for j in input().split(' ')]
    x = set()
    current=0
    max1=0

    for j in range(len(string)):
        if(string[j]==current):
            current+=1
        if(string[j]>max1):
            max1=string[j]
        x.add(string[j])

    #print(x,current,max1,len(x))
    #stop=-1
    for j in range(k):
        val = math.ceil((current+max1)/2)
        #print(val,current,max1)
        if(val==current):
            current+=1
            while(current in x):
                    current+=1
        if(val>max1):
            max1=val

        """if(stop==-1):
            stop=val
        elif(stop==val):
            break"""
        x.add(val)
        #print(val)
    print(len(x))


