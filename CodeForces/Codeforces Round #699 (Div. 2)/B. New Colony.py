#https://codeforces.com/contest/1481/problem/B


t = int(input())

for i in range(t):

    n,k = input().split(' ')

    k= int(k)
    n=int(n)

    provisiory=[int(i) for i in input().split(' ')]
    #for each stone
    for x in range(k):
        curr=0;
        for j in range(n-1):
            if(provisiory[j]>=provisiory[j+1]):
                curr+=1
            else:
                provisiory[j]+=1
                break
        if(curr==n-1):
            break
    curr+=1
    if(curr==n):
        curr=-1

    print(curr)



