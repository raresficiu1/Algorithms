#https://codeforces.com/contest/339/problem/A


inputs = [int(i) for i in input().split('+')]

inputs.sort()
fin=''
for i in inputs:
    fin+=str(i)+'+'

print(fin[:-1])

