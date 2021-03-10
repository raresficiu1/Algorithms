#https://codeforces.com/contest/1496/problem/0


t = int(input())

for i in range(t):

    n, k = input().split(' ')
    k=int(k)
    n=int(n)
    elem= list(input())
    elem2= elem.copy()
    elem2.reverse()

    if(k==0):
        print('YES')
    else:
        if(n%2==1):
            if(elem[:k] == elem2[:k]):
                print("YES")
            else:
                print("NO")
        else:
            if(n-2*k > 1):
                if (elem[:k] == elem2[:k]):
                    print("YES")
                else:
                    print("NO")
            else:
                print("NO")

