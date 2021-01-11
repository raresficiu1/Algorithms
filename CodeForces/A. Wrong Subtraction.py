#https://codeforces.com/problemset/problem/977/A


n, times = input().split(' ')
n= int(n)
times= int(times)

while (times>0):
    rest=n%10
    if(rest>0):
        if(times>rest):
            times-=rest
            n-=rest
        else:
            n-=times
            times=0
    else:
        n=n/10
        times-=1
print(int(n))


