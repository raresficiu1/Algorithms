#https://codeforces.com/contest/1473/problem/B

import math
tests = int(input())

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

for i in range(tests):
    word1= input()
    word2= input()
    lword1=len(word1)
    lword2=len(word2)

    k= lcm(lword1,lword2)

    word1=(k//lword1)*word1
    word2 = (k // lword2) * word2

    if(word1==word2):
        print(word1)
    else:
        print(-1)