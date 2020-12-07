l = input().split(' ')
contor=0
scores = input().split(' ')



set=0
i=0
while(i<int(l[0])):
    if(contor<int(l[1]) and int(scores[i])>0):
        contor+=1
        set=int(scores[i])
    else:
        if(contor>=int(l[1]) and int(scores[i])>0 and int(scores[i])==set):
            contor+=1
            ok=1

    i+=1

print(contor)