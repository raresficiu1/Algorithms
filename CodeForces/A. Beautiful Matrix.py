#https://codeforces.com/problemset/problem/263/A

lines=5

matrix=[]
for each in range(lines):
    linie=input().split(' ')
    matrix.append(linie)

coords=[]
for i in range(5):
    for j in range(5):
        if(matrix[i][j]=='1'):
            steps=abs(i-2)+abs(j-2)

print(steps)





