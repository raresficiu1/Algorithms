#https://codeforces.com/contest/1486/problem/0


t = int(input())

for i in range(t):

    n = input()

    a = [int(i) for i in input().split(' ')]



    ramas=0
    ok=True
    for j in range(len(a)):
        if(a[j] + ramas < j):
            ok=False
            break
        elif(a[j]+ramas>=j):
            ramas-=j-a[j]

        elif(a[j]>j):
            ramas+=a[j]-j
    if(ok==True):
        print("YES")
    else:
        print("NO")









