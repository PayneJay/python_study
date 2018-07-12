# This is first pyhton program
a = 10
if a > 0:
    print(a)
else:
    print(-a)

print(len('好的'))
# tuple ()和数组[]类似，但是一旦初始化就不能再修改(这里指没个元素的指向不变)，
# 而数组[]可以随意修改
# tuple在定义的时候元素就得确定下来
# 数组里可以存放任意类型的元素
L = [['Apple', 'Google', 'Microsoft'], ['Java', 'Python', 'Ruby', 'PHP'],
     ['Adam', 'Bart', 'Lisa']]
# 输出元素
for l in L:
    for cell in l:
        print(cell)
        pass
    print(l)

# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖
height = 1.75
weight = 80.5
bmi = 80.5 / (1.75 * 1.75)
if bmi > 32:
    print('BMI=', bmi)
    print('严重肥胖')
elif bmi > 28:
    print('BMI=', bmi)
    print('肥胖')
elif bmi > 25:
    print('BMI=', bmi)
    print('肥胖')
elif bmi > 18.5:
    print('BMI=', bmi)
    print('肥胖')
else:
    print('BMI=', bmi)
    print('过轻')

# 求和
sum = 0
for x in range(101):
    sum = sum + x
print(sum)
