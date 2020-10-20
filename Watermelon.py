#Problem Link https://codeforces.com/problemset/problem/4/A


w = int(input())
list=[]

for i in range(int(w)):
    if(i%2==0):
        list.append(i)
print(list)
answer="NO"
if(i>=1 and i<=100 and answer=="NO"):
    for i in list:
        for j in list:
            if (i+j==w):
                answer="YES"
print(answer)
