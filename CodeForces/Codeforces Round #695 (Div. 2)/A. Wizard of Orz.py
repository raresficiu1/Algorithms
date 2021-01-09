#https://codeforces.com/contest/1467/problem/0

tests=int(input())


for each in range(tests):

    panels=int(input())

    i=9

    final=''
    loc=0

    if(panels==1):
        print(9)
    elif(panels==2):
        print(98)
    else:
        final = '98'
        while(loc<panels-2):
            final+=str(i%10)
            i+=1
            loc+=1
        print(final)