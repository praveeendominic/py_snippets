

def add(num_list):
    sum=0
    for i in num_list:
        sum=sum+i
    return sum

def add_rec(n):
    if n==1:
        return 1
   
    return n + add_rec(n-1)


if __name__=='__main__':
    ls=[1,2,3,4,5]
    res=add_rec(5)
    print(res)
