#https://codeforces.com/contest/1481/problem/C


t =int(input())

for i in range(t):
    planks, painters = input().split(' ')
    planks=int(planks)
    initial_colors=[int(i) for i in input().split(' ')]
    solution_colors = [int(i) for i in input().split(' ')]
    painters_colors =[int(i) for i in input().split(' ')]


    final_painter=painters_colors[-1]

    colors_needed=[]

    ok=False
    for i in range(planks):
        if(initial_colors[i]!=solution_colors[i]):
            colors_needed.append([solution_colors[i],i+1])
        if(solution_colors[i]==final_painter):
            ok=True


    #print(colors_needed,painters_colors)



    painter_solution=painters_colors.copy()

    if(ok==False):
        print("NO")
    else:
        for i in range(len(colors_needed)):
            for j in range(len(painters_colors)):
                lenx=1
                try:
                    lenx=len(painter_solution[j])

                except:
                    pass
                if(colors_needed[i][0]==painters_colors[j] and lenx==1):
                    painter_solution[j]=[colors_needed[i][1],True]
                    continue

        painter_fin=''
        for each in painter_solution:
            try:
                if len(each)>1:
                    painter_fin+=str(each[0])+' '
            except:
                painter_fin+=str(planks-1)+' '

        print("YES")
        print(painter_fin[:-1])











