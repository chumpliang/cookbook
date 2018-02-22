#!/usr/bin/env python3

# 1.2解压可迭代对象赋值给多个变量

# eg:若一个可迭代对象的元素超过变量个数时，会抛出ValueError.z怎么样才能
# 从这个可迭代对象中解压出N个元素来

# *表达式的作用

# 算出去掉第一个和最后一个分数的平均成绩


grades = [10, 20, 30, 40, 50, 60]


def drop_first_last(grades):
    first, *middle, last = grades  # middle 类型为list
    return sum(middle)/len(middle)


print(drop_first_last(grades))


# 比如一个公司有6个月的销售数据，想取最近一个月的
sale_data = [220, 330, 550, 280, 600, 510]

*five_m, last_m = sale_data
print("最近一个月的销售额：%d" % last_m)


# 星号表达式在迭代元素为可变长元组的序列时的作用

records = [
    ('foo', 1, 2), ('bar', "hello"), ('foo', 3, 4)
]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


# 遍历访问
for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)


# 解压一些元素后丢弃他们，使用废弃变量
record =('name',20,)