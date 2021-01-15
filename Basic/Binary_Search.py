

def binary_search(element, the_list):

    L=0
    R=len(the_list)-1

    while L<=R:
        m=(L+R)//2
        if(the_list[m]<element):
            L=m+1
        elif the_list[m]>element:
            R=m-1
        else:
            return m
    return False


list= [1,2,3,5,6,7,8,9]
print(binary_search(5,list))