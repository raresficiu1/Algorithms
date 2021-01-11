#https://codeforces.com/problemset/problem/749/A

nr = int(input())


par = False
n=nr%2
k=nr//2

if (n==0):
    par = True

if par:
    print(k)
    rasp=''
    for i in range(k):
        rasp+='2'
else:
    print(k)
    rasp='3'
    for i in range(k-1):
        rasp+='2'

final=''
for each in rasp:
    final+=each
    final+=' '
print(final[:-1])