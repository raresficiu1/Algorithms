#https://codeforces.com/contest/731/problem/A

word = list(input())

fin=0
start = 'a'

for i in word:
    min=30
    if(abs(ord(start)-ord(i))>26-abs(ord(start)-ord(i))):
        min=26-abs(ord(start)-ord(i))
    else:
        min=abs(ord(start)-ord(i))

    fin+=min
    start=i
print(fin)