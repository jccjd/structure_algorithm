#   现在有一个包含 N 个元素的元组或者是序列，怎样将它里面的值解压后同时赋值给 N 个变量
p = (4, 5)
x, y = p

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
# 丢弃一部分值
_, shares, price, _ = data

