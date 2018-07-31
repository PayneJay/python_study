#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Screen(object):
    __slots__ = ('width', 'height')

    @property
    def resolution(self):
        return self.width * self.height


# 定制类
class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a

    def __getitem__(self, n):
        if isinstance(n, int):  # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):  # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


# 测试:
s = Screen()
s.width = 1024
s.height = 768
# s.weight = 1
print('width =', s.width)
print('height =', s.height)
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')

print(Student('Michael'))

for n in Fib():
    print(n)

f = Fib()
print('输出前5个：', f[0:5])
print('输出前12个：', f[:12])
print('按步长3输出前20个：', f[:20:3])
for n in range(10):
    print(f[n])
