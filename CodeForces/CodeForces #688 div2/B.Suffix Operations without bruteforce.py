import sys
tests = int(input())

for i in range(tests):
    nr = input()
    x = map(int, input().split(" "))
    y=[]
    miny=9999999999999
    maxy=-999999999999
    for each in x:
        if (each > maxy):
            maxy = each
        if (each < miny):
            miny = each
        y.append(each)
    if(miny!=maxy):
        max1 = 0
        sum = 0
        max12 = abs(y[1] - y[0])
        rsdmax = abs(y[-1] - y[-2])
        for i in range(2, len(y)):
            max1 = max(abs(y[i] - y[i - 1]) + abs(y[i - 1] - y[i - 2]) - abs(y[i] - y[i - 2]), max1)
            sum += abs(y[i] - y[i - 1])

        max1 = max(max1, abs(y[2]-y[1]), rsdmax)
        sum = sum + max12 -max1

        print(sum)
    else:
        print(0)