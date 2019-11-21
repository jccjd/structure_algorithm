'''
查找最大或最小的N个元素
heapq nlargest() nsmallest()
'''

import heapq
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(2, nums))
print(heapq.nsmallest(2, nums))

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nlargest(2, portfolio, lambda s: s['price'])
print(cheap)

'''
如果在一个集合中找到最小的N个元素可以使用函数heap,在底层实现里面会将集合进行堆排序

'''
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
import heapq
heap = list(nums)
heapq.heapify(heap)
print(heapq.heappop(heap))
