#https://codeforces.com/contest/1490/problem/D


t = int(input())
def calculate_depth(a,count):
    max_value=max(a)
    max_index=a.index(max_value)

    left=a[0:max_index]
    right=a[max_index+1:]

    res_left=[]
    res_right=[]
    center=count

    if(len(left)>0):
        res_left = calculate_depth(left,count+1)

    if(len(right)>0):
        res_right= calculate_depth(right,count+1)

    final=[]
    for each in res_left:
        final.append(each)
    final.append(center)
    for each in res_right:
        final.append(each)
    return final




for i in range(t):
    n= input()
    a=[int(i) for i in input().split(' ')]
    fin=calculate_depth(a,0)
    sx=''
    for each in fin:
        sx+=str(each)+' '
    print(sx[:-1])

