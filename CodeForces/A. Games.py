#https://codeforces.com/contest/268/problem/A

teams= int(input())

pairs=[]
count=0
for i in range(teams):

    h,a=input().split(' ')


    for j in pairs:
        if(j[0]==a):
            count+=1
        if(j[1]==h):
            count+=1

    pairs.append([h, a])

print(count)