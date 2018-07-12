# 这个文件是python返回函数和匿名函数的使用练习

# 关键字lambda表示匿名函数，冒号前的字母表示函数的参数
# 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果


# 1、将函数作为返回值，可以不用立即得到函数执行的结果，在调用的时候再真正执行
# 当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


# 闭包
#  返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量
def count():
    fs = []
    for i in range(1, 5):

        def f():
            return i * i

        fs.append(f)
    return fs


# 利用闭包返回一个计数器函数，每次调用它返回递增整数
def createCounter():
    def f():
        n = 0
        while True:
            n = n + 1
            yield n

    sun = f()

    def counter():
        return next(sun)

    return counter


# 匿名函数
print('匿名函数测试：', list(filter(lambda x: x % 2 == 1, range(1, 20))))

# 测试
print(list(range(0, 10)))
f = lazy_sum(1, 3, 5, 7, 9)
print(f)
print(calc_sum(1, 3, 5, 7, 9))
print(f())

# f1, f2, f3 = count()
# print(f1(), f2(), f3())

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
