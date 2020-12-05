import sys
#tests = int(input())
tests=1

for i in range(tests):
    nr=3 #input()
    x = map(int, input().split(" "))
    y=[]
    for each in x:
        y.append(each)

    final = 900000000000000000000
    for i in range(len(y)):
        x = y.copy()
        x.pop(i)
        max=0
        element=0
        sum=0
        for j in range(len(x)):
            diff=y[i]-x[j]
            if(diff<0):
                diff=diff*(-1)
            sum=sum+diff
            if(diff>max):
                max=diff
        potential=sum-max

        if(potential<final):
            final=potential

        print(y[i],sum,max,potential)
    print(final)



