#https://codeforces.com/problemset/problem/282/A

nrOperations = int(input())

x=0

for i in range(nrOperations):
    rand=list(input())
    if(rand[0]=='X'):
        if(rand[1]=='+'):
            x += 1
        else:
            x-=1
    else:
        if(rand[0]=='+'):
            x+=1
        else:
            x-=1
print(x)

