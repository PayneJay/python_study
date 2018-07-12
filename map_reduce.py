# 这是python高阶函数的用法的练习测试文件
from functools import reduce
import math


# Python内建了map()和reduce()函数。
def f(x):
    return x * x


def sum(a, b):
    return a + b


def quadrature(a, b):
    return a * b


def normalize(name):
    return name.capitalize()


def prod(L):
    return reduce(quadrature, L)


def str2float(s):
    s = s.split('.', 1)

    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        digits = {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9
        }
        return digits[s]

    print(reduce(fn, map(char2num, s[0])))
    print(reduce(fn, map(char2num, s[1])) * math.pow(0.1, len(s[1])))
    return reduce(fn, map(
        char2num,
        s[0])) + reduce(fn, map(char2num, s[1])) * math.pow(0.1, len(s[1]))


# 测试
# map()函数接收两个参数，一个是函数，一个是Iterable
print(list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
print(reduce(sum, [1, 2, 3, 4, 5]))

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

# 求积测试
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

# 字符串转浮点数测试
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
