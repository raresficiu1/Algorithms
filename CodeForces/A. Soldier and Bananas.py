#https://codeforces.com/problemset/problem/546/A

k,n,w = input().split(' ')

#k = cost of the first banana
#n = cati $ are
#w = cate banane trebuie

cumparate=1
cost=int(k)

while cumparate<int(w):
    cumparate += 1
    cost+=cumparate*int(k)
if(cost-int(n)>=0):
    print(cost-int(n))
else:
    print(0)