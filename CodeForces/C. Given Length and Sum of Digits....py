#https://codeforces.com/problemset/problem/489/C

m,s = input().split(' ')
m=int(m)
s=int(s)
def create_high(m,sum):
    nr=''
    i=9
    while sum>0 and m>0:
       if(sum>=i and m>0):
           nr+=str(i)
           m-=1
           sum-=i
       else:
           i-=1
    while m>0:
        nr+=str(0)
        m-=1
    return nr
def create_initial_low(m):
    nr=''
    if(m>0):
        nr+='1'
        m-=1
        while m:
            nr+='0'
            m-=1
        return nr
    else:
        return nr

def create_low(m,sum):
    nr=create_initial_low(m)

    if(len(nr)>1):
        if((len(nr)-1)*9>=sum):
            sum=sum-1

        pos=len(nr)-1
        nr=list(nr)
        i=9
        set=0
        while sum > 0:
            if (sum >= i):
                nr[pos] = i
                sum -= i
                set=1
            else:
                i -= 1
            if(set==1):
                pos-=1
                set=0
                i=9
        return nr
    else:
        if(sum<=9):
            nr=str(sum)
    return nr

if(m*9>=s):
    high=create_high(m ,s)
    s1=0
    for each in list(high):
        s1+=int(each)
    s2=0
    low = create_low(m ,s)
    low1=''
    for each in list(low):
        s2+=int(each)
        low1+=str(each)
    if(s1==s2):
        print(low1,high)
    else:
        print(-1,-1)
else:
    print(-1,-1)