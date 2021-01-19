#https://codeforces.com/contest/1474/problem/B



tests = int(input())
d=[]
max=0
for i in range(tests):

    o = int(input())
    d.append(o)
    if(o>max):
        max=o


solFound=False
start=1
primes=[]


while solFound==False:
    found=False
    if start > 1:
        for i in range(2, start):
            if (start % i) == 0:
                break
        else:
            primes.append(start)
            found=True
    start+=1

    if(found==True):
        for i in range(len(primes)):
            for j in range(1,len(primes)):
                if(primes[j]-primes[i]>=max):
                    solFound=True


for i in range(len(d)):
    found==False
    for j in range(len(primes)):
        if(primes[j]>=1+d[i]):
            for k in range(1, len(primes)):
                if (primes[k] - primes[j] >= d[i] ):
                    print(primes[k]*primes[j])
                    found=True
                    break
            if(found==True):
                break