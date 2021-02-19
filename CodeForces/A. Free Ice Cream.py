#https://codeforces.com/contest/686/problem/A


n,x = input().split(' ')
n=int(n)
x=int(x)
count=0
for i in range(n):

    order = input().split(' ')
    type = order[0]
    nr=int(order[1])

    if (type == '-'):
        if(nr<=x):
            x-=nr
        else:
            count+=1
    else:
        x+=nr

print(x,count)