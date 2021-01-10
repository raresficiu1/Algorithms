#https://codeforces.com/problemset/problem/1092/B

n=int(input())

students = list(map(int,input().split(' ')))

students.sort()


i=1
count=0
while i<n:
    count+=abs(students[i-1]-students[i])
    i+=2
print(count)