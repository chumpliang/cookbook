#!/usr/bin/env python3
# 保留最后N个元素

# 在迭代操作或者其他操作的时候，怎样保留最后有限几个元素的历史记录？

# 使用collections.deque模块->内建集合模块，有许多集合类

from collections import deque

# print(help(deque)) 查询类函数功能函数help()


def search(lines, pattern, history=5):
    privious_lines = deque(maxlen=history)  # 定义一个history的list
    for line in lines:
        if pattern in lines:
            yield line, privious_lines
        privious_lines.append(line)

# deque类功能函数 该类是一种队列的数据结构。
q=deque()
q.append(1)
q.append(2)
q.append(3)
q.appendleft(4)
print(q)
print(q.popleft())


if __name__ == '__main__':
    with open(r'../cookbook/somefile.txt') as f:  # 使用with语句直接处理异常
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end=" ")
                print(line, end=" ")
                print('-'*20)
