import sys
#tests = int(input())
tests=1


def solve(string, value,stop):

    print(string,value,stop) # pt verificare
    newstring=[]

    #oprire cand e gol stringul
    if(len(string)>0):
        #directia in care trebuie toate mutate
        actualsteps = string[0] - value
        steps = actualsteps
        #print(actualsteps)
        if(actualsteps!=0):
            if(steps<0):
                steps*=-1

            for each in string:
                newstring.append(each-actualsteps)

            if (steps < stop):
                return steps + solve(newstring[1:], value, stop)
            else:
                return stop + 1
        else:
            return steps+solve(string[1:],value,stop)
    else:
        return 0


for i in range(tests):
    #nr=input()
    x = map(int, input().split(" "))
    y=[]
    miny=9999999999999
    maxy=-999999999999
    for each in x:
        if(each>maxy):
            maxy=each
        if(each<miny):
            miny=each
        y.append(each)
    #unique_values=create_space_search(miny,maxy)


    #print(unique_values)
    if(miny==maxy):
        minim=0
    else:
        minim = 999999999999999999999999
    unique_values=set(y)
    unique_values=list(unique_values)

    print(unique_values)
    index = None
    #pt fiecare posibilitate [['X', 4, 3, 2, 4, 1], [1, 'X', 3, 2, 4, 1], [1, 4, 'X', 2, 4, 1], [1, 4, 3, 'X', 4, 1], [1, 4, 3, 2, 'X', 1], [1, 4, 3, 2, 4, 'X']]
    for i in range(len(y)):
        k=y.copy()

        for each in unique_values: #incerc cel mai scurt drum pt fiecare cifra
            k[i] = each
            for each1 in unique_values:
                #print("trying ", k, each1)
                minimaux=solve(k,each1,minim)
                if(minimaux<minim):
                    minim=minimaux



    print(minim)