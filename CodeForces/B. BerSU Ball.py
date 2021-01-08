#https://codeforces.com/problemset/problem/489/B

nr_boys=int(input())

boys= list(map(int,list(input().split(" "))))

nr_girls=int(input())

girls= list(map(int,list(input().split(" "))))

boys.sort()
girls.sort()

i=0
j=0
count=0
print(boys)
print(girls)
while(i<nr_boys and j<nr_girls):

    if(abs(int(boys[i])-int(girls[j]))<=1):
        count+=1
        j+=1
        i+=1
    elif int(boys[i])>int(girls[j]) and j<nr_girls:
        j+=1
    elif int(boys[i])<int(girls[j]) and i<nr_boys:
        i+=1
    else:
        i+=1
print(count)
