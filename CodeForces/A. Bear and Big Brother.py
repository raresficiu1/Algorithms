#https://codeforces.com/problemset/problem/791/A

a,b = input().split(' ')

a =int(a)
b= int(b)

count=0
while (a<=b):
    a=a*3
    b=b*2
    count+=1
print(count)