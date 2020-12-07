#https://codeforces.com/problemset/problem/231/A


problems=int(input())
count=0

for each in range(problems):
    line= list(input().split(' '))
    sum=0
    for each in line:
        sum += int(each)

    if(sum>=2):
        count+=1
print(count)