#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 函数的调用，定义和参数，递归函数的基本用法
import math


# 求一元二次方程的根
def quadratic(a, b, c):
    pass
    drt = power(b) - (4 * a * c)
    if drt < 0:
        print('没有实数根')
    elif drt == 0:
        x = (-b / 2 * a * c)
        return x
    else:
        x1 = (-b + math.sqrt(drt)) / (2 * a)
        x2 = (-b - math.sqrt(drt)) / (2 * a)
        return x1, x2


# 求x的n次方,默认求平方
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


# 参数不按顺序传递测试
def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


# 可变参数求和
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + power(n)
        pass
    return sum


# 关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


# 测试:
enroll("张三", "男", city="上海")
print('1_4sum=', calc(1, 2, 3, 4))
nums = [1, 2, 3]
print('1_3sum=', calc(*nums))
print('************************')

print('quadratic(2, 3, 4) =', quadratic(2, 3, 4))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
