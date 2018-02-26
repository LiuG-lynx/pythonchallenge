import math
# 题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
x = 1
while True:  # 遍历
    # math.sqrt的用法
    # >>> math.sqrt(100)  完全开平方数
    # 10.0
    # >>> math.sqrt(16)  完全开平方数
    # 4.0
    # >>> math.sqrt(20)  不完全开平方数
    # 4.47213595499958
    if math.sqrt(x+100) - int(math.sqrt(x+100)) == 0 and math.sqrt(x + 268) - \
        int(math.sqrt(x+268)):  #此步 开平方的方式取出math.sqrt(x+100) - int(math.sqrt(x+100)) ==0 这步代表符合完全开平方 不为完全平方数 开平方为小数
        print(x)
        break
    x += 1
# 优化版
#x + 100 = y*y
# x + 100 + 168 = z*z
# => z*z - y*y = 168 
# 由此可以确定y和z都在0 和 168 之间
for i in range(0,169):
    for j in range(0,169):
        if (i+j)*(i-j) == 168:
            print((i*i + j*j)/2 - 184)
