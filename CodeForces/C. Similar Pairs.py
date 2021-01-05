words = int(input())

for each in range(words):

    word = input()
    word2=list(word)
    word1=''
    if(len(word2)>10):
        word1+=word2[0]+str(len(word2)-2)+word2[-1]
    else:
        word1=word

    print(word1)