def ComNum(n,m):
    '''
    用递归的方法来计算 C(n,m) = n!/(m!(n-m)!)
    :param m: 
    :param n: 
    :return: 
    '''
    # C(n,m) = C(n-1,m) + C(n-1,m-1)
    # C(n,0) = C(n,n) = 1
    if m == 0 or m == n:
        return 1

    return ComNum(n-1,m) + ComNum(n-1,m-1)

m = 20
n = 30
print(ComNum(n,m))