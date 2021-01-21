

nr = int(input())



bits=[]
current=2**32

while(nr>0 and current>=1):
    print(nr,current)
    if(nr>=current):
        bits.append(1)
        current//=2
        nr= int(nr)-int(current)
    else:
        current//=2
        bits.append(0)

print(bits, len(bits))