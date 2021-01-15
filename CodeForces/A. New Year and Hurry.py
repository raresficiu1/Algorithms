#https://codeforces.com/problemset/problem/750/A

n,k=[int(i) for i in input().split(' ')]

time_left = 240-k

sums=[i*5 for i in range(1,n+1)]
previous=0
sums1=[]
for i in sums:
    sums1.append(i+previous)
    previous+=i




i=0
while (i<n and sums1[i]<=time_left) and time_left>0:
    i+=1

print(i)

