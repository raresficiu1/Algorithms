#https://codeforces.com/contest/1487/problem/B
import math
t = int(input())

for t in range(t):
    n,k = input().split(' ')
    n=int(n)
    k=int(k)


    if(n%2==0):
        if(k%n==0):
            print(n)
        else:
            print(k%n)
    else:
        r=k%n
        if(r==0):
            r=n

        ajutor=int((k-1)/int(n/2))

        r = (r+ajutor) % n
        if(r==0):
            r=n
        print(r)


