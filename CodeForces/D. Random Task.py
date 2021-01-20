#https://codeforces.com/problemset/problem/431/D


def to_binary(n):
    i=0
    rezultat=0
    binary=[]

    while rezultat < n:
        rezultat = 2**i
        binary.append(rezultat)
        i+=1

    binary.reverse()
    mask=[]
    print(len(binary),i)
    while (i>=0):
        print(n)
        if(n<=binary[-i] and n>0):
            n-=binary[-i]
            mask.append(1)
        else:
            mask.append(0)
        i-=1
    mask.reverse()
    print(mask)
    return binary

print(to_binary(125))