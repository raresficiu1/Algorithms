#https://codeforces.com/problemset/problem/996/A


bank= int(input())
bills=0
while bank:

    if(bank>=100):
        aux=bank//100
        bank-=aux*100
        bills+=aux
    elif (bank >= 20):
        aux = bank //20
        bank -= aux *20
        bills += aux
    elif (bank >= 10):
        aux = bank //10
        bank -= aux *10
        bills += aux
    elif (bank >= 5):
        aux = bank //5
        bank -= aux * 5
        bills += aux
    else:
        bills+=bank
        bank=0

print(bills)