class Dequeue(object):
    """
    双端队列
    """
    def __init__(self):
        self.__list = []

    def add_front(self, item):
        self.__list.insert(0, item)

    def add_rear(self, item):
        self.__list.append(item)

    def pop_front(self):
        return self.__list.pop(0)

    def pop_rear(self):
        return self.__list.pop()

    def is_empty(self):
        return self.__list == []

    def __len__(self):
        return len(self.__list)

qu = Dequeue()
# qu.add_rear(1)
# qu.add_rear(2)
# qu.add_rear(3)
qu.add_front('A')
qu.add_front('b')
qu.add_front('c')
for _ in range(len(qu)):
    print(qu.pop_front())
