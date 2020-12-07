#https://codeforces.com/problemset/problem/112/A

cuvant1=list(input())
cuvant2=list(input())

ok=0
for i in range(len(cuvant1)):
    litera1=cuvant1[i].lower()
    litera2=cuvant2[i].lower()

    if(litera1>litera2):
        ok=1
        break

    else:
        if(litera1==litera2):
            pass
        else:
            ok=-1
            break


print(ok)

