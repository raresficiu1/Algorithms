#https://codeforces.com/problemset/problem/492/B

n,l = input().split(' ')

locations= list(map(int,list(input().split(' '))))
locations.sort()

max_range=0
toCompare=locations[0]

for i in locations[1:]:
    if(i-toCompare>max_range):
        max_range= i-toCompare
    toCompare=i

max1=max_range/2
max2=locations[0]
max3=int(l)-locations[-1]
if(max1>max2 and max1>max3):
    print(max1)
elif(max2>max3):
    print(max2)
else:
    print(max3)

