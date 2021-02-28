#https://codeforces.com/contest/1491/problem/A

t , q = input().split(' ')

array= [int(i) for i in input().split(' ')]
k=-1
for i in array:
    if(i==1):
        k+=1


for i in range(int(q)):

    querry, pos = input().split(' ')
    querry = int(querry)
    pos = int(pos)
    pos-=1
    #print(array,querry,pos,k)

    if(querry==2 and pos<=k):
        print(1)
    elif(querry==2 and pos>k):
        print(0)
    elif(querry==1):
        if(array[pos]==1):
            k-=1
        else:
            k+=1

        array[pos]=1-array[pos]

