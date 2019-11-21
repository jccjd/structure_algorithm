d = {
    'a': [1, 2, 3],
    'b': [4, 5],
}
e = {
    'a': {1, 2, 3},
    'b': {4, 5}
}
from collections import defaultdict

d = defaultdict(list)

d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
b = {}
b.setdefault('a', []).append(1)
b.setdefault('a', []).append(2)
b.setdefault('a', []).append(2)
b.setdefault('b', []).append(4)

print(d)
print(b)

'''
自己创建多值字典
'''
mydict = {}
for key, value in e:
    if key not in mydict:
        mydict[key] = []
    mydict[key].append(value)
