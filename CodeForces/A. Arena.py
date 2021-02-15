#https://codeforces.com/contest/1487/problem/0


t = int(input())

for i in range(t):

    n = int(input())
    m=n
    heroes=[int(i) for i in input().split(' ')]
    heroes.sort()

    ok=False
    j=1
    prim=heroes[0]
    n-=1
    while(j<m):
        if(heroes[j]==prim):
            n-=1
        else:
            break
        j+=1


    print(n)