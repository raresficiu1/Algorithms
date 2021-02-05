#https://codeforces.com/contest/1481/problem/0


t = int(input())

for i in range(t):

    lx , ly = input().split(' ')
    lx=int(lx)
    ly = int(ly)

    UP=0
    DOWN=0
    RIGHT=0
    LEFT=0

    orders = input()

    for i in orders:
        if i == 'U':
            UP+=1
        elif i=='D':
            DOWN+=1
        elif i=='R':
            RIGHT+=1
        else:
            LEFT+=1

    condy=False
    condx=False

    #print(UP,DOWN,ly)
    if(ly>0 and ly<=UP):
        condy=True
    elif(ly<0 and abs(ly)<=DOWN):
        condy=True
    elif(ly==0):
        condy=True



    #print(RIGHT,LEFT,lx)

    if (lx > 0 and lx <= RIGHT):
        condx = True
    elif (lx < 0 and abs(lx) <= LEFT):
        condx = True
    elif (lx == 0):
        condx = True

    if(condy==True and condx==True):
        print('YES')
    else:
        print("NO")

