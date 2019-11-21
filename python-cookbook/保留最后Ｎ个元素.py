''''
问题：　在迭代操作或者其他操作时，怎么只保留最后有限
几个元素的历史记录
解决方案：
    使用　collections.deque
'''

from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


if __name__ == '__main__':
    with open('test.txt') as f:
        f_line = []
        f_pre = None
        for line, prevlines in search(f, 'python', 5):
            f_line.append(line)
            f_pre = prevlines


