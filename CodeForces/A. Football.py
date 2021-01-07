#https://codeforces.com/problemset/problem/96/A


inm=list(input())

count=1
previous=inm[0]
for i in inm[1:]:
    if i == previous:
        count+=1
    else:
        count=1

    if (count>=7):
        print("YES")
        break
    previous=i
if count<7:
    print("NO")