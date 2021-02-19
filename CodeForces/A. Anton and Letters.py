#https://codeforces.com/contest/443/problem/A

inputs = input()[1:-1].split(', ')

s = set()
for i in inputs:
    if(i!=''):
        s.add(i)
print(len(s))