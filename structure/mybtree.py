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
        print(node.value, end=' -')
        self.centeroder(node.rchild)

a = Tree()
a.append(1)
a.append(2)
a.append(3)
a.append(4)
a.breath_oder()
a.preoder(a.root)
a.centeroder(a.root)