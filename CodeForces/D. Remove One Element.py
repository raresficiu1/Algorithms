# https://codeforces.com/problemset/problem/1272/D


drop = input()

elements = input().split(' ')
# elements=[6, 5, 4, 3, 2, 4, 3,5]
ri = []
li = []
for i in range(len(elements)):
    ri.append(1)
    li.append(1)
max1 = 1
for i in range(1, len(elements)):
    if (int(elements[i]) > int(elements[i - 1])):
        li[i] = li[i - 1] + 1
        if li[i] > max1:
            max1 = li[i]
    if (int(elements[-i]) > int(elements[-i - 1])):
        ri[-i - 1] = ri[-i] + 1


for i in range(len(elements) - 2):
    if (int(elements[i]) < int(elements[i + 2])):
        if (li[i] + ri[i + 2] > max1):
            max1 = li[i] + ri[i + 2]

print(max1)
