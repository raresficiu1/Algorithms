#https://codeforces.com/problemset/problem/69/A

nr=int(input())
x=0
y=0
z=0
for i in range(nr):
    x1,y1,z1=input().split(" ")

    x+=int(x1)
    y+=int(y1)
    z+=int(z1)
if(x==y and y==z and z==0):
    print("YES")
else:
    print("NO")