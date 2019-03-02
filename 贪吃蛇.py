# 输入n
# 输入如下
#如 输入 4
# 10 11  12 1
# 9  16  13 2
# 8  15  14 3
# 7  6   5  4
# a[0][3] = 1 a[1][3] = 2 a[2][3] = 3 a[3][3] = 4
# a[3][2] = 5 a[3][1] = 6 a[3][0] =7
# a[2][0] = 8 a[1][0] = 9 a[0][0] = 10
# a[0][1] = 11 a[0][2] = 12
# a[1][2] = 13 a[2][2] = 14
# a[2][1] = 15
# a[1][1] = 16
s = int(input("请输入整数:"))
l = [[0 for _ in range(s) ] for k in range(s)]
m = s-1
n = 0
num = 1
while num<=s**2:
    print("in loop")
    while n<m and l[n+1][m] == 0: #向下  行递增
        print("再循环1")
        l[n][m] = num
        num+=1
        n+=1
    while m>0 and l[n][m-1] ==0 : #想做 列递减
        print("in loop 2")
        l[n][m] = num
        m-=1
        num+=1
    while n>0 and l[n-1][m] == 0:
        print("in loop 3")
        l[n][m] = num
        n-=1
        num+=1
    while m>=n and l[n][m+1] == 0 :
        l[n][m] = num
        m+=1
        num+=1
    while n==m  and l[m][n] == 0:
        l[n][m] = num
        num+=1
        n +=1
for i in l :
    print("%2s"%i)
