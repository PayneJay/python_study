#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Student(object):
    count = 0

    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender
        Student.count += 1

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        if gender == 'male' or 'female':
            self.__gender = gender
        else:
            raise ValueError('bad gender!')

    def __call__(self):
        print('My name is %s' % self.name)


class Animal(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Animal.count += 1


# 测试：
bart = Student('Bart', 'male')
print(bart())
print('before', bart.get_gender())
if bart.get_gender() != 'male':
    print('测试失败！')
else:
    bart.set_gender('female')
    print('after:', bart.get_gender())
    if bart.get_gender() != 'female':
        print('测试失败！')
    else:
        print('测试成功！')

# 测试:
if Animal.count != 0:
    print('测试失败!')
else:
    bart = Animal('Husky')
    if Animal.count != 1:
        print('测试失败!')
    else:
        lisa = Animal('ibetan Mastiff')
        if Animal.count != 2:
            print('测试失败!')
        else:
            print('Animals:', Animal.count)
            print('测试通过!')
