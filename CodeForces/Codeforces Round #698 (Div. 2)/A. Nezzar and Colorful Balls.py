#https://codeforces.com/contest/1478/problem/0


n = int(input())

for i in range(n):

    x = input()

    l = [int(k) for k in input().split(' ')]

    count=1
    maxi=1
    actual=l[0]

    for j in l[1:]:
        if(j==actual):
            count+=1
            if(count>maxi):
                maxi=count
        else:
            actual=j
            count=1
    print(maxi)
