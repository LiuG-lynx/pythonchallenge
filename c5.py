# 题目：输入三个整数x,y,z，请把这三个数由小到大输出。
x = int(input('x'))
y = int(input('y'))
z = int(input('z'))
# python拥有最简洁的置换
if x > y:
    x, y = y, x
if x > z:
    x, z = z, x
if y > z:
    y, z = z, y

print(x, y, z)
