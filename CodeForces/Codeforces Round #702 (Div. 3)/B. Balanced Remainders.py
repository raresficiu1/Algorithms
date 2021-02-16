#https://codeforces.com/contest/1490/problem/B

t = int(input())

def check_solution(x,fin):
    if(x[0]!=fin):
        return False
    elif(x[1]!=fin):
        return False
    elif(x[2]!=fin):
        return False
    else:
        return True


for i in range(t):

    n = int(input())
    fin=n/3

    a = [int(i) for i in input().split(' ')]

    x=[]
    count=[0,0,0]
    for j in a:
        aux = j%3
        count[aux]+=1
        x.append(aux)
    #print(a,x,count)
    moves= 0
    change=True
    if(change==True):
        change=False
        if(count[2]<fin):
            moves+=fin-count[2]
            count[1]-=fin-count[2]
            count[2]=fin
            change=True
        if(count[1]<fin):
            change=True
            moves += fin - count[1]
            count[0] -= fin - count[1]
            count[1] = fin
        if(count[0]<fin):
            moves += fin - count[0]
            count[2] -= fin - count[0]
            count[0] = fin
            change=True
    print(int(moves))

