

def binary_search(num_list, search_key):

    left_index = 0
    right_index = len(num_list)

    while left_index<=right_index:
        mid_index = (left_index + right_index) // 2
        mid_elem = num_list[mid_index]

        if mid_elem == search_key:
            return mid_index

        if search_key > mid_elem:
            left_index = mid_index + 1
        elif search_key < mid_elem:
            right_index = mid_index - 1

    return -1

def recursive_binary_search(num_list, search_key, left_index, right_index):
    
    # left_index = 0
    # right_index = len(num_list)

    mid_index = (left_index + right_index) // 2
    mid_elem = num_list[mid_index]

    if ( mid_index >=len(num_list) or mid_index <= 0) or (left_index > right_index):
        return -1

    if mid_elem == search_key:
        return mid_index

    if search_key > mid_elem:
        left_index = mid_index + 1
    elif search_key < mid_elem:
        right_index = mid_index - 1

    return recursive_binary_search(num_list, search_key, left_index, right_index)


    
if __name__ == '__main__':
    ls=[11,12,13,14,15,16,17,18,19,20]
    res=recursive_binary_search(ls,14,0,len(ls)-1)
    print(res)
    


