"""
集合中的元素去重
直接用set是无法保证数据的原始序列的
"""


# def dedupe(items):
#     seen = set()
#     for item in items:
#         if item not in seen:
#             yield item
#             seen.add(item)

a = [1, 5, 2, 1, 9, 1, 5, 10]
# print(list(dedupe(a)))
"""
这个方法只对序列中元素为hashable的时候管用,如果元素不可哈希
需要改变一下
"""
def dedupe2(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)
b = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
print(list(dedupe2(b, key=lambda d: (d['x'], d['y']))))
print(list(dedupe2(b, key=lambda d: d['x'])))


def dequeue(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

print(list(dequeue(a)))