# python中的装饰器
# 在代码运行期间动态增加功能的方式，称之为“装饰器”
import time
import functools


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


# 3层嵌套
def log1(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


# 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start = time.time()
        relt = fn(*args, **kw)
        end = time.time()
        differ = end - start
        print('%s executed in %s ms' % (fn.__name__, differ))
        return relt

    return wrapper


# 把@log放到now()函数的定义处，相当于执行了语句：now = log(now)
@log1('excute->')
def now():
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


# 测试装饰器
now()


# 测试函数的执行时间
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败！')
elif s != 7986:
    print('测试失败！')
