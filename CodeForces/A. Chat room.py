#https://codeforces.com/problemset/problem/58/A

word = list(input())

target = ['h','e','l','l','o']

l=0
for each in word:
    if(l<len(target) and each==target[l]):
        l+=1


if(l==len(target)):
    print("YES")
else:
    print("NO")