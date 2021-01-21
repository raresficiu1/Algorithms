#https://codeforces.com/contest/677/problem/A


n,h = [int(i) for i in input().split(' ')]

a = [int(i) for i in input().split(' ')]


width=0

for i in a:
    if(i>h):
        width+=2
    else:
        width+=1

print(width)