# 这个文件是Python内建的filter()函数和sorted()函数的使用
from operator import itemgetter


# 取出list中的奇数
def is_odd(n):
    return n % 2 == 1


# 过滤空字符串
def not_empty(s):
    return s and s.strip()


# 构造从3开始的奇数序列的生成器
def odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


# 筛选器
def not_divisible(n):
    return lambda x: x % n > 0


# 通过生成器返回下一个素数(埃氏筛法)
def primes():
    yield 2
    it = odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(not_divisible(n), it)


# 筛选出回数
def is_palindrome(n):
    s = str(n)
    if s == s[::-1]:
        return n


# 获取对象的第一个域的值
def by_name():
    return itemgetter(0)


# 获取对象第二个域的值
def by_score():
    return itemgetter(1)


# 测试
print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))
print(list(filter(not_empty, ['', 'A', 'r', ' ', '8', None])))

# 打印1000以内的素数
for n in primes():
    if n < 1000:
        print(n)
    else:
        break

# 测试过滤回数:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101,
        111, 121, 131, 141, 151, 161, 171, 181, 191
]:
    print('测试成功!')
else:
    print('测试失败!')

# 测试sorted()函数按照自定义规则排序
students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print('学生名字和成绩：', tuple(students))
print('按名字排序：', list(sorted(students, key=by_name())))
print('按成绩排序：', list(sorted(students, key=by_score())))
