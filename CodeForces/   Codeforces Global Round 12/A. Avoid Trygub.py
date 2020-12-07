
tests =int(input())



for i in range(tests):

    drop = input()

    word = list(input())
    # pt fiecare litera din cuvant
    #print(word)
    gasit=0

    word.sort()
    word1=''
    for each in word:
        word1+=each
    print(word1)