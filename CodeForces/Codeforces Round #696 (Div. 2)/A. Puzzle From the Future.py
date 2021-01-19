#https://codeforces.com/contest/1474/problem/0


tests = int(input())

for i in range(tests):


    ln=int(input())

    b = [int(i) for i in list(input())]

    if(b[0]==1):
        previous=2
    else:
        previous=1
    a='1'
    for i in range(1,len(b)):
        if(previous==2 and b[i]==1):
            a+=str(0)
            previous=1

        elif previous == 2 and b[i]==0:
            a+=str(1)
            previous=b[i]+1
        elif previous==1 and b[i]==0:
            a+=str(0)
            previous=0
        else:
            a+=str(1)
            previous = b[i] + 1



        #print(previous)
    print(a)




