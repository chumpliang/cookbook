#!/usr/bin/env python3
# 解压序列赋值给多个变量

# eg:有一个包含N个元素的元组或者是序列，怎么将他里面的值解压后同时赋值给N个变量
tup = (4, 6)
x, y = tup
print("x=%d,y=%d" % (x, y))

data = ["name", 40, 91.1, (2018, 2, 22)]
name, shares, price, date = data
print(name, shares, price, date)
# 注：变量个数与序列元素个数不匹配产生异常

# 上述解压赋值可用在任何迭代对象上面
s = "hello"
a, b, c, d, e = s
print(a, b, c, d, e)

# 解压部分丢弃其他值，任意变量占位，然后丢弃变量
_, shares, price, _ = data
print(shares, price)
