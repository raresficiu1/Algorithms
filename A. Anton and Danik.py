#https://codeforces.com/contest/734/problem/A


nr= input()

string=input()

d=0
a=0
for i in string:
    if i=='D':
        d+=1
    else:
        a+=1
if(d>a):
    print("Danik")
elif(d<a):
    print('Anton')
else:
    print('Friendship')