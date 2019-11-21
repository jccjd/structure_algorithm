from collections import OrderedDict
import json
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

for key in d:
    print(key, d[key])
print(json.dumps(d))

price = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# 字典排序
#  zip函数创建是是一个只能访问一次的迭代器
min_price = min(zip(price.values(), price.keys()))
sort_price = sorted(zip(price.values(), price.keys()))
print(min_price)
print(sort_price)

# 使用字典自带的函数
print(min(price, key=lambda k: price[k]))
print(max(price, key=lambda k: price[k]))

# 查找字典的相同点
a = {
    'x': 1,
    'y': 2,
    'z': 3
}
b = {
    'w': 10,
    'x': 11,
    'y': 2
}

print(a.keys() & b.keys())
print(a.keys() - b.keys())
print(a.items() & b.items())

c = {key: a[key] for key in a.keys() - {'z', 'w'}}
print(c)