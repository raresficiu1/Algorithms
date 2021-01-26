#https://codeforces.com/contest/431/problem/A


a = [int(i) for i in input().split(' ')]

k= [int(i) for i in list(input())]
fin=0
for i in k:
    fin+=a[i-1]

print(fin)