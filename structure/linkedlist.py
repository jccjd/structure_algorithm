class Node(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class LinkedList(object):

    def __init__(self):
        node = Node()
        self.root = node
        self.taile = None
        self.length = 0

    def append(self, value):
        node = Node(value)
        if self.taile is None:
            self.root = node
        else:
            self.taile = node
        self.taile = node
        self.length += 1

    def iter_node(self):
        flag_node = self.root
        while flag_node.next is not None:
            yield flag_node
            flag_node = flag_node.next
        yield flag_node
    def __iter__(self):
        for node in self.iter_node():
            yield node.value

a = LinkedList()
a.append(1)
a.append(1)
a.append(1)
for node in a.iter_node():
    print(node.value)


