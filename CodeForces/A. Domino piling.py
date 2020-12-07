#https://codeforces.com/problemset/problem/50/A
import math

sides = input().split(' ')
n=int(sides[0])
m=int(sides[1])

print(math.floor(n*m/2))