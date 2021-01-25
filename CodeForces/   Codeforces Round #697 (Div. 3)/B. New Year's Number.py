#https://codeforces.com/contest/1475/problem/B

nr1=0
nr2=0

tests = int(input())
tests1=[]
values=set()
max=100000000

for i in range(tests):
    nr = int(input())


    n=nr/2020
    r=nr%2020

    if(n-r)>=0:
        print("YES")
    else:
        print("NO")