#https://codeforces.com/problemset/problem/778/A
#BRUTE FORCE time limit exceeded

initial = list(input())

target= list(input())

a= [int(i) for i in input().split(' ')]
a_index=[]
k=0

for i in range(len(a)):
    a_index.append([initial[i],False,k])
    k+=1


def create_current(a):
    b=[]
    for i in a:
       if(i[1]==False):
           b.append(i[0])
    return b


def verify(a,b):
    k=0
    k1=len(b)-1
    for i in a:
        if(k<=k1 and i==b[k]):
            k+=1
    if(k==k1+1):
        return True

    return False



i=0
ok=True

while(i<len(a) and ok==True):
    #presupun ca trebuie sa ma opresc
    ok=False

    #updatez indexul
    a_index[a[i]-1][1]=True
    #print(a_index)

    a_current = create_current(a_index)

    #print(create_current(a_index),target,verify(a_current,target),i)

    #acum verific daca targetul e inclus in a current si daca e inclus fac ok = true altfel opresc

    if(len(a_current)>len(target)):
        if verify(a_current,target):
            ok=True
        else:
            ok=False
            break
    elif(len(a_current)==len(target)):
        if verify(a_current,target)==False:
            i-=1
            ok=False
        else:
            ok=False

    i+=1

print(i)
