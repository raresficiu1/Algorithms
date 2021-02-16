#https://codeforces.com/contest/1490/problem/0

t =int(input())

for i in range(t):

    n = int(input())
    a=[int(i) for i in input().split(' ')]


    contor=0
    j=0
    while(j<n-1):
        mare =max(a[j],a[j+1])
        mic=min(a[j],a[j+1])
        while((mare/mic) > 2):
            k=1
            mic*=2
            contor+=1
        j+=1
    print(contor)
