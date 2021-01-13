#https://codeforces.com/problemset/problem/199/A


fibo=int(input())

a=0
b=1
res=1
res1=[0,1,1]

while(res<fibo):
    a=b
    b=res
    res=a+b
    res1.append(res)

res1.reverse()
res2=[]
len=0
i=0
while(fibo>=0 and len<3):
   current=res1[i]
   if(current<=fibo and len<3):
       fibo-=current
       res2.append(current)
       len+=1
   if (current <= fibo and len<3):
       fibo -= current
       res2.append(current)
       len+=1
   if (current <= fibo and len<3):
       fibo -= current
       res2.append(current)
       len+=1
   i+=1

res3=''
for each in res2:
    res3+=str(each)
    res3+=' '
print(res3[:-1])

