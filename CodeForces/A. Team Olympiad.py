#https://codeforces.com/contest/490/problem/A

n= input()

kids=[int(i) for i in input().split(' ')]
kidspos=kids.copy()



kids.sort()

ones = kids.count(1)
two = kids.count(2)
three= kids.count(3)

l = [ones,two,three]
teams = min(l)

ones=[]
two=[]
three=[]

i=0
while(i<len(kidspos)):
    type=kidspos[i]
    if(type==1):
        ones.append(i)
    elif(type==2):
        two.append(i)
    else:
        three.append(i)

    i+=1



fin_teams=[]
i=0
while(i<teams):
    fin_teams.append([ones[i]+1,two[i]+1,three[i]+1])
    i+=1

if(teams>0):
    print(teams)
    for i in fin_teams:
        f=''
        for j in i:
            f+=str(j)+' '
        print(f[:-1])
else:
    print(0)

