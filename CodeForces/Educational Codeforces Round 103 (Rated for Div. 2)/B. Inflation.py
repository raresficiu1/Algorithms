#https://codeforces.com/contest/1476/problem/B
import math

t = int(input())

for i in range(t):
    n,k=input().split(' ')

    k=int(k)

    p= [int(j) for j in input().split(' ')]
    change_track=0
    actual=p[0]
    j=1
    change=True
    while(change==True):
        change=False
        j=1
        actual=p[0]
        while(j<len(p)):
            sus=p[j]
            if(sus/actual > k/100):
                x=math.ceil(sus*100/k - actual)
                p[0]+=x
                change_track+=x
                change=True
                break
            actual+=sus

            j+=1
    print(change_track)