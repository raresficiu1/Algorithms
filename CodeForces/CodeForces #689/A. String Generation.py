test = int(input())

for each in range(test):
    a,b = input().split(' ')
    contor=0
    contor1=0
    word=''
    word2=''

    for i in range(int(a)):
        if(contor<int(b)):
            word+='a'
            contor+=1
        elif (contor1%2==0 and contor1<=int(b)/2):
            word2+='b'
            contor1+=1
        elif contor1<=int(b)/2:
            word2+='c'
            contor1 += 1

    for each in word2:
        word+=each
    for each in word2:
        word+=each
    print(word)