
def insertion_sort(list):

    for j in range(1,len(list)):
        key=list[j]

        i=j-1

        while(i>=0 and list[i]>key):
            list[i+1] = list[i]
            i-=1
        list[i+1]=key

    return list

def merge_sort(list):
    if len(list) > 1:
        mid = len(list) // 2
        L = list[:mid]
        R = list[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        #print(L,R)
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                list[k] = L[i]
                i += 1
            else:
                list[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            list[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            list[k] = R[j]
            j += 1
            k += 1

        print(list)
        #return list

list = [5 ,2 ,4 ,6 ,1, 3]
merge_sort(list)
#print(insertion_sort(list))
#print(merge_sort(list))


