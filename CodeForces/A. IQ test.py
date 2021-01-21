#https://codeforces.com/problemset/problem/25/A

nr= int(input())
n=[int(i) for i in input().split(' ')]
even=0
odd=0

for i in n:
    if(i%2==0):
        even+=1
    else:
        odd+=1

if(odd>even):
    for i in range(len(n)):
        if(n[i]%2==0):
            print(i+1)
            break
else:
    for i in range(len(n)):
        if(n[i]%2==1):
            print(i+1)
            break

