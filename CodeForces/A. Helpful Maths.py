#https://codeforces.com/problemset/problem/339/A

tocalculate=input().split('+')
tocalculate.sort()
new=''
for i in tocalculate:
    new+=i
    new+='+'

print(new[:-1])