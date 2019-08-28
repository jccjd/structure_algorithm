class Node(object):

    def __init__(self, value=None,lchild=None, rchild=None):
        self.value = value
        self.lchild = lchild
        self.rchild = rchild

class Tree(object):

    def __init__(self):
        self.root = None

    def append(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
            return

        queue = [self.root]

        while queue:
            curnode = queue.pop(0)

            if curnode.lchild is None:
                curnode.lchild = node
                return
            else:
                queue.append(curnode.lchild)

            if curnode.rchild is None:
                curnode.rchild = node
                return
            else:
                queue.append(curnode.rchild)


    def breath_oder(self):
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            curnode = queue.pop(0)

            print(curnode.value, end=' ')
            if curnode.lchild is not None:
                queue.append(curnode.lchild)

            if curnode.rchild is not None:
                queue.append(curnode.rchild)

    def preoder(self,node):
        if node is None:
            return
        print(node.value, end=',')
        self.preoder(node.lchild)
        self.preoder(node.rchild)

    def centeroder(self, node):
        if node is None:
            return
        self.centeroder(node.lchild)
        print(node.value, end=' ')
        self.centeroder(node.rchild)
def LRU(node):
    if node is None:
        return
    LRU(node.lchild)
    LRU(node.rchild)
    print(node.value, end=" ")

def DLR_no_recursive(node):
    stack = []
    while node or stack:
        while node:
            print(node.value)
            stack.append(node)
            node = node.lchild
        node = stack.pop()
        node = node.rchild

def LDR_no_recursive(node):
    stack = []
    stack_shadow = []
    while node or stack:
        while node:
            stack.append(node)
            stack_shadow.append(node)
            node = node.lchild
        node = stack.pop()
        node = node.rchild
    return stack_shadow


def LRD_no_recursive(node):
    stack = []
    stack_reverse = []
    while node or stack:
        while node:
            stack.append(node)
            stack_reverse.append(node)
            node = node.rchild
        node = stack.pop()
        node = node.lchild
    return stack_reverse[::-1]

a = Tree()
a.append(1)
a.append(2)
a.append(3)
a.append(4)
a.append(5)
a.append(6)
a.append(7)
a.breath_oder()

DLR_no_recursive(a.root)
dlr = LDR_no_recursive(a.root)
dlr = [i.value for i in dlr]
print(dlr)
lr = LRD_no_recursive(a.root)
lrdtree = [i.value for i in lr]
print(lrdtree)