#https://codeforces.com/contest/427/problem/A


n= int(input())
events = [int(i) for i in input().split(' ')]
k=0
freep=0
for i in events:
    if(i>=0):
        freep+=i
    else:
        if(freep>0):
            freep-=1
        else:
            k+=1
print(k)
