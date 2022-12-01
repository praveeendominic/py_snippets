




def linear_search(num_list, search_key):
    for index,elem in enumerate(num_list):
        if elem == search_key:
            return index
    return -1



if __name__ == '__main__':
    num_list=[2,4,6,8,10,13,15,17,19,20]
    res = linear_search(num_list,search_key=19)
    print(res)

