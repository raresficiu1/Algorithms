#https://codeforces.com/problemset/problem/1/A

import math
data= input().split(' ')

n=int(data[0])
m=int(data[1])
a=int(data[2])

count=0
sum1=0

n=math.ceil(n/a)*a
m=math.ceil(m/a)*a

sum1=int(n*m/a**2)

print(sum1)
