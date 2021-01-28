# https://codeforces.com/contest/1478/problem/B
import bisect

test = int(input())
current_set = set()
set_lists = []


def pop():
    global set_lists
    for d in range(1, 10):
        lista1 = []
        current_set = set()
        for l in range(1, d * 10 + 1):
            l1 = str(l)
            for cifra in l1:
                if (cifra == str(d)):
                    lista1.append(int(l1))
        pos1 = 0
        pos2 = 0
        while (pos1 < len(lista1)):
            while (pos2 < len(lista1)):
                times = 1
                res = lista1[pos1] + lista1[pos2] * times
                while (res <= (d * 10 + 1)):
                    res = lista1[pos1] + lista1[pos2] * times
                    bisect.insort(lista1, res)
                    times += 1
                pos2 += 1
            pos1 += 1
        l = 0
        while (l < len(lista1)):
            current_set.add(lista1[l])
            l += 1
        set_lists.append(current_set)


pop()

for i in range(test):
    q, d = input().split(' ')
    nr = [int(k) for k in input().split(' ')]
    d = int(d)

    for each in nr:
        if (each >= d * 10 + 1):
            print("YES")
        elif (each in set_lists[int(d) - 1]):
            print("YES")
        else:
            print("NO")

