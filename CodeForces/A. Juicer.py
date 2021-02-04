#https://codeforces.com/contest/709/problem/A


n,b,d = input().split(' ')

size=int(b)
refill=int(d)

second = [int(i) for i in input().split(' ')]
sum1=0
sum2=0
count=0
for i in second:
    if(i<=size):
        sum1+=i
        sum2+=i

    if(sum2>refill):
        sum2=0
        count+=1

'''if(sum1>0):
    if(sum1%refill==0):
        print(sum1//refill-1)
    else:
        print(sum1//refill)'''


print(count)