#https://codeforces.com/contest/1473/problem/A


tests= int(input())

for i in range (tests):

    n, d = map(int, input().split(' '))

    array = list(map(int, input().split(' ')))

    array.sort()
    max=array[-1]

    if(max>d):
        if(len(array)>1):

            if(array[0]+array[1]<=d):
                print("YES")
            else:
                print("NO")
        else:
            if(array[0]<=d):
                print("YES")
            else:
                print("NO")
    else:
        print("YES")

