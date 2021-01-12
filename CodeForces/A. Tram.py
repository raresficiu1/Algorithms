#https://codeforces.com/problemset/problem/116/A


stops = int(input())

inside=0
max=-1

for i in range(stops):

    a,b = input().split(' ')
    a= int(a)
    b=int(b)


    inside-=a
    inside+=b
    if(inside>max):
        max=inside

print(max)