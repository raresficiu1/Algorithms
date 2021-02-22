
f = open(r"C:\Users\Rares\OneDrive\Desktop\iot_PC.txt",'r')

count=0
word='NO_PI_EVALUATION'
current=0
linec=0

for line in f:
    current=0
    for letter in line:
        if(letter==word[current]):
            current+=1

        if(current>=len(word)):
            #print(line)
            current=0
            count+=1
            break




    linec+=1


print(count,linec,count/linec*100)