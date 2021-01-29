#https://codeforces.com/contest/1476/problem/0
import math

tests =int(input())


for i in range(tests):

    n,k = input().split(' ')

    n=int(n)
    k=int(k)


    if(n<k):
        print(math.ceil(k / n))
    elif n==k or n%k==0:
        print(1)
    else:
        print(2)

