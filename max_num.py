#求从顶部到底部和的最大值

#多进行了几次递归
import  time
def test_time(func):
    def  wrapper(list,i,j,n,*args):
        start = time.time()
        func(list,i,j,n)
        end = time.time()
        print(end-start)
    return  wrapper
@test_time
def play():
    print("playing games")
#@test_time
d = {}
def max_num(list1,i,j,n):
    if (i,j) in d:
        return d[(i,j)]
    if i == n:
        return list1[i][j]
    else:
        left = max_num(list1,i+1,j,n)
        d[(i+1,j)]=left
        right = max_num(list1,i+1,j+1,n)
        d[(i+1,j+1)] = right
    return max(left,right) + list1[i][j]
array = [[7],[3,8],[8,1,0],[2,7,4,4],[4,5,2,6,5]]
# start = time.time()
print(max_num(array,0,0,len(array)-1))
# end = time.time()
# print('运行 的时间为:',end-start)
# play()
# 将算法进行优化

