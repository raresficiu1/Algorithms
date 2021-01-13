# https://codeforces.com/contest/1470/problem/A
#WRONG
tests = int(input())

for i in range(tests):
    n, m = input().split(' ')
    friends=list(input().split(' '))
    gifts = list(input().split(' '))
    #gifts_taken=[]
    #for i in range(int(m)):
    #   gifts_taken.append(0)
    friends.sort(reverse=True)
    sum=0
    current=0
    for each in friends:
        min=9999999999999999999
        if(current<int(m)):
            min = int(gifts[current])
            current += 1

        if(min>int(gifts[int(each)-1])):
            min=int(gifts[int(each)-1])
        sum+=min

    print(sum)

''' for j in range(int(each)):
            if(gifts_taken[j]==0 and ok==False):
                ok=True
                gifts_taken[j]=1
                sum+=int(gifts[j])
'''