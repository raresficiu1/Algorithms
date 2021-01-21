#https://codeforces.com/contest/344/problem/A

i= int(input())
prim=input()

count=1
for j in range(1,i):
    input1=input()
    if(input1!=prim):
        prim=input1
        count+=1

print(count)

