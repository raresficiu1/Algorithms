#https://codeforces.com/contest/1475/problem/A


test = int(input())

for i in range(test):

    nr = int(input())
    ok=False
    while nr>1 and ok==False:
        if(nr%2==1):
            ok=True
        else:
            nr=nr/2

    if(ok==False):
        print("NO")
    else:
        print("YES")




