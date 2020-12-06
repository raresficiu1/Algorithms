#problem https://codeforces.com/contest/1081/problem/H

tests = int(input())
#tests=1


for i in range(tests):
    #nrA , nrB = "9 14".split(" ")
    nrA, nrB = input().split(" ")
    trainsA=[]
    trainsB=[]
    '''for each in "2 7 16 28 33 57 59 86 99".split(" "):
        trainsA.append(int(each))
    for each in "3 9 14 19 25 26 28 35 41 59 85 87 99 100".split(" "):'''
        #trainsB.append(int(each))
    trainsA=input().split(" ")
    trainsB=input().split(" ")

    contor=0
    for each1 in trainsA:
        for each2 in trainsB:
            if(each1==each2):
                contor+=1
    print(contor)


