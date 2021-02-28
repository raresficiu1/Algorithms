
def solve(v):
    lungime=len(v)
    if(lungime>0):
        max1 = max(v)
        pos1 = v.index(max1)
        remaining=solve(v[:pos1])
        return v[pos1:] + remaining

    else:
        return ['a']
t =int(input())

for i in range(t):

    n=input()
    v=[int(j) for j in input().split(' ')]


    v=solve(v)[:-1]
    fin=''
    for j in v:
        fin+=str(j)+' '
    print(fin[:-1])
