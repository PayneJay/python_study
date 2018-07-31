# 这是文件是Python高级特性迭代的使用练习
import time


# 求最大值，最小值
def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    else:
        min = L[0]
        max = L[0]
        tickes = time.time()
        print('当前时间戳：', tickes)
        for num in L:
            if num > max:
                max = num
            if num < min:
                min = num

        print('耗时：', time.time() - tickes)
        return (min, max)


# 这个函数主要是去除集合L中的非字符串，并将字符串转为小写输出
def filterNum(L):
    return [s.lower() for s in L if isinstance(s, str)]


# 求斐波拉契数列(普通函数)
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


# 求斐波拉契数列(generator函数)
def fibGenerator(max):
    n, a, b = 0, 0, 1
    while n < max:
        a, b = b, a + b
        n = n + 1
        yield b
    return 'done'


# 杨辉三角
def triangles():
    ls = [1]
    while True:
        yield ls
        ls = [1] + [ls[i] + ls[i + 1] for i in range(len(ls) - 1)] + [1]


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

# 测试:
L2 = filterNum(['Hello', 'World', 18, 'Apple', None])
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('filterNum 测试通过!')
else:
    print('filterNum 测试失败!')

# 测试
fib(10)
print(fibGenerator(10))
for n in fibGenerator(10):
    print(n)

print('*****************杨辉三角*******************')
# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4,
                                                      1], [1, 5, 10, 10, 5, 1],
               [1, 6, 15, 20, 15, 6, 1], [1, 7, 21, 35, 35, 21, 7,
                                          1], [1, 8, 28, 56, 70, 56, 28, 8, 1],
               [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]]:
    print('测试通过!')
else:
    print('测试失败!')
