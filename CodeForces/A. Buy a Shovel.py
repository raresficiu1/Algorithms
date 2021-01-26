#https://codeforces.com/contest/732/problem/A


r,k = input().split(' ')
r_n=int(r)
ok= False
count=0

while(ok==False):
    r=str(r)
    if(r[-1]=='0'):
        ok=True
    if(r[-1]==k):
        ok=True
    r=int(r)+r_n
    count+=1

print(count)
