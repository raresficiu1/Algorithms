#https://codeforces.com/contest/1490/problem/C


def cubes():
    sieve = []
    for i in range(1, 10001):
            result = i ** 3
            sieve.append(result)
            sieve1.add(result)
    return sieve

sieve1=set()
sieve = cubes()



t=int(input())
for i in range(t):
    x=int(input())
    ok = False

    for i in sieve:
        if (x-i in sieve1):
            ok=True
            break

    if ok == True:
        print("YES")
    else:
        print("NO")
