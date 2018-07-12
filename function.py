# 函数的调用，定义和参数，递归函数的基本用法
# Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数、命名关键字参数，这5中参数都可以组合使用
# 但是参数定义顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
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


# 限制关键字参数的名字(命名关键字参数必须传入参数名）
# 命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数，没有*后面参数将被认为位置参数
def personOther(name, age, *, city='Beijing', job):
    print(name, age, city, job)


# 测试:
enroll("张三", "男", city="上海")
print('1_4sum=', calc(1, 2, 3, 4))
nums = [1, 2, 3]
print('1_3sum=', calc(*nums))
# 关键字参数测试
person('Peter', 25, city='Beijing', height='178cm', weight='65kg')

extra = {'job': 'Engineer', 'experience': '2年'}
personOther('Peter', 25, city='Shanghai', job='Programmer')
personOther('Jack', 26, job='Programmer')

# kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra
person('Peter', 25, city='Beijing', height='178cm', weight='65kg', **extra)
print('************************')

print('quadratic(2, 3, 4) =', quadratic(2, 3, 4))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
