#https://codeforces.com/contest/265/problem/A


stones = list(input())

instr = list(input())

loc=stones[0]
i=0

for j in instr:
    loc = stones[i]
    if(j==loc):
        i+=1

print(i+1)
