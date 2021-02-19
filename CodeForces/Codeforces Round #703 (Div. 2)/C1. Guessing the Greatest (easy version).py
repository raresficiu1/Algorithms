#https://codeforces.com/contest/1486/problem/C1

import sys

def solve(l,r):
    if(l!=r):
        center = int((l + r) / 2)
        print('? ',l,' ',r)
        second_max=int(input())
        sys.stdout.flush()
        max1=-1
        dreapta=False

        #caut dreapta
        if(second_max>center):
            print(' ? ', center, ' ', r)
            max1 = int(input())
            sys.stdout.flush()
            if(max1!=second_max):
                dreapta=False
            else:
                dreapta=True
        #caut stanga
        else:
            print('? ', l, ' ', center)
            max1 = int(input())
            sys.stdout.flush()
            if (max1 != second_max):
                dreapta = True
            else:
                dreapta=False
        if (abs(l - r) <= 1 and max1==second_max):
            if(l==max1):
                return (r)
            else:
                return (l)
        else:
            if(dreapta==True):
                return(solve(center,r))
            else:
                return(solve(l,center))
n = int(input())

print('! ',solve(1,n))




