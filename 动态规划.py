#走楼梯问题

# 十阶楼梯有多少中走法呢？
# 这个问题其实可以这样思考:第一种也就是考虑最简单的组合排序
# 找出所有的可能
# 第二方法 也就是递归 十阶楼梯最后一步可能是 第8阶 或者是第9阶
# 如果第 8阶楼梯有X中走法，第 9 阶楼有Y中走法 那么第十阶楼梯就有X+Y中走法
# 一直往下递归 到 一阶楼梯 有一种走法,而 二阶楼梯有两种走法 这也就是递归所
# 需要的突破口 按照这个思路我们不难得出 F(10) = F(9) + F(8)
def get_method(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return get_method(n-1) + get_method(n-2)
# print(get_method(10))
#备忘录方法
def get_method_change(n):
    #前面的不变
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        l = [1,2]
        for i in range(3,n):
            l[0],l[1] = l[1],l[1]+l[0]
        # l[1] + l[0] 就是下一个数一值 到 n-1为止
        return l[0]+l[1]
print(get_method_change(10))

# 动态规划中典型的01-背包问题 则稍微复杂一点

# 如何装能够让书包的价值最大
def backage(w,v,V):
    # 测试数据
    # 一个背包 体积 为V，
    # 费用 w = [0,60,100,120]
    # 体积 v = [0,10,20,30]
    # V = 50
    #
    n = 3 #物品的数量
    V = 50
    v = [0, 10, 20, 30]
    w = [0, 60, 100, 120]
    L = [0 for i in range(V+1) for j in range(n)]

import numpy as np

def solve(vlist,wlist,totalWeight,totalLength):
    resArr = np.zeros((totalLength+1,totalWeight+1),dtype=np.int32)
    for i in range(1,totalLength+1):
        for j in range(1,totalWeight+1):
            if wlist[i] <= j:
                resArr[i,j] = max(resArr[i-1,j-wlist[i]]+vlist[i],resArr[i-1,j])
            else:
                resArr[i,j] = resArr[i-1,j]
    print(resArr)
    return resArr[-1,-1]
# def bag(n, c, w, v):
#     """
#     测试数据：
#     n = 6  物品的数量，
#     c = 10 书包能承受的重量，
#     w = [2, 2, 3, 1, 5, 2] 每个物品的重量，
#     v = [2, 3, 1, 5, 4, 3] 每个物品的价值
#     """
#     # 置零，表示初始状态
#     value = [[0 for j in range(c + 1)] for i in range(n + 1)]
#     for i in range(1, n + 1):
#         for j in range(1, c + 1):
#             value[i][j] = value[i - 1][j]
#             # 背包总容量够放当前物体，遍历前一个状态考虑是否置换
#             if j >= w[i - 1] and value[i][j] < value[i - 1][j - w[i - 1]] + v[i - 1]:
#                 value[i][j] = value[i - 1][j - w[i - 1]] + v[i - 1]
#     for x in value:
#         print(x)
#     return value

if __name__ == '__main__':
    v = [0,6,10,12]
    w = [0,1,2,3]
    weight = 5
    n = 3
    result = solve(v,w,weight,n)
    print(result)