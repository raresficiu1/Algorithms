#https://codeforces.com/problemset/problem/118/A


string= list(input())
cuvant=''
vocale = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
for letter in string:
    esteVocala=False
    for vocala in vocale:
        if(letter==vocala):
            esteVocala=True
    if(esteVocala==False):
        if(letter.isupper()):
            cuvant+='.'
            cuvant+=letter.lower()
        else:
            cuvant += '.'
            cuvant += letter

print(cuvant)