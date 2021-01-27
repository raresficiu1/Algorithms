#https://codeforces.com/contest/9/problem/A


a,b = input().split(' ')
a=int(a)
b=int(b)
max=a

if(a<b):
    max=b

total=6
outcomes=total-max+1

if(outcomes==6):
    print('1/1')
elif outcomes==5:
    print('5/6')
elif outcomes==4:
    print('2/3')
elif(outcomes==3):
    print('1/2')
elif(outcomes==2):
    print('1/3')
else:
    print('1/6')



