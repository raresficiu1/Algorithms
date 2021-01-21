#https://codeforces.com/contest/381/problem/A

t = input()

n = [int(i) for i in input().split(' ')]

d = s =0
i=0

while len(n)>0:

    if(n[0]>n[-1]):
        if (i % 2 == 0):
            s+=n[0]
        else:
            d+=n[0]
        n=n[1:]
    else:
        if (i % 2 ==0):
            s += n[-1]
        else:
            d += n[-1]
        n = n[:-1]
    i+=1
print(s,d)
