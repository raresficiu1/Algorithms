#https://codeforces.com/contest/405/problem/A

t=input()
list=[int(i) for i in input().split(' ')]

list.sort()
fin=''
for i in list:
    fin+=str(i)+' '

print(fin[:-1])