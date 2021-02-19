#https://codeforces.com/contest/770/problem/A


n,k = [int(i) for i in input().split(' ')]

def generate_letters(nr):
    letters=[]
    for i in range(97,97+nr):
        letters.append(chr(i))
    return letters

letters=generate_letters(k)


c=0
fin=''
for i in range(n):
    if (c >= k):
        c = 0
    current = letters[c]
    fin += current
    c+=1
print(fin)