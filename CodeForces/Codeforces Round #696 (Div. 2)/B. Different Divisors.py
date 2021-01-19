#https://codeforces.com/contest/1474/problem/B



tests = int(input())
d=[]
max=0

#O(n)
for i in range(tests):
    o = int(input())
    d.append(o)
    if(o>max):
        max=o

solFound=False
start=1
primes=[]


#O(n**2)
def primes_sieve1():
    limitn = 1000000
    primes = dict()
    for i in range(2, limitn): primes[i] = True

    for i in primes:
        factors = range(i,limitn,i)
        for f in factors[1:]:
            primes[f] = False
    return [i for i in primes if primes[i]==True]




'''while solFound==False:
    found=False
    if start >= 1:
        for i in range(2, start):
            if (start % i) == 0:
                break
        else:
            primes.append(start)
            found=True


    if(found==True):
        for i in range(len(primes)):
            for j in range(1,len(primes)):
                if(primes[j]-primes[i]>=max):
                    solFound=True
    start += 1'''

primes=primes_sieve1()

print(len(primes))
found=0
#O(n**3)
for i in range(len(d)):
    found=False
    for j in range(len(primes)):
        if(primes[j]>=1+d[i]):
            for k in range(1, len(primes)):
                if (primes[k] - primes[j] >= d[i]):
                    print(primes[k]*primes[j])
                    found=True
                    break
            if(found==True):
                break
