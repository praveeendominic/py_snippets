##########
#@author: Praveen Dominic
##########


def linear_search(num_list, search_key):
    for index,elem in enumerate(num_list):
        if elem == search_key:
            return index
    return -1

def binary_search(num_list, search_key):
    l = 0
    r = len(num_list)-1
    mid = 0
    
    while(l<=r):
        mid = (l+r)//2
        mid_elem = num_list[mid]
        if search_key == mid_elem:
            return mid
        
        if search_key > mid:
            l = mid + 1
        elif search_key < mid:
            r = mid - 1
        
    return -1


if __name__ == '__main__':
    num_list=[2,4,6,8,10,13,15,17,19,20]
    res = linear_search(num_list,search_key=19)
    print(res)
    
    res = binary_search(num_list,search_key=19)
    print(res)
