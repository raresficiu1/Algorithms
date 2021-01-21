
word = input()
l=0
h=0
for i in word:
    if (i.islower()):
        l+=1
    else:
        h+=1
if(l>=h):
    print(word.lower())
else:
    print(word.upper())
