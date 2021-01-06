#https://codeforces.com/problemset/problem/266/A

throw=input()

imp=list(input())

i=1
count=0
while(i<len(imp)):
    if(imp[i]==imp[i-1]):
        count+=1
    i+=1
print(count)



