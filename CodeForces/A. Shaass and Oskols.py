#https://codeforces.com/contest/294/problem/A

l = input()

initial = [int(i) for i in input().split(' ')]

shots= int(input())

for i in range(shots):
    wire,pos=input().split(' ')
    wire=int(wire)-1
    pos=int(pos)



    #stanga sar jos (i-1) toate pana la pos
    jumpDown=pos-1

    # dreapta sar sus (i+1) toate dupa pos
    jumpUP = initial[wire]-pos


    if(wire-1>=0):
        initial[wire-1]+=jumpDown
    if(wire+1<len(initial)):
        initial[wire+1]+=jumpUP

    initial[wire]=0

fin=''
for i in initial:
    fin+=str(i)+' '

print(fin[:-1])
