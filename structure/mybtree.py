class Node(object):
    def __init__(self, value=None, lchild=None, rchild=None):
        self.value = value
        self.lchild = lchild
        self.rchild = rchild


class Btree(object):
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

    def breadth_order(self):
        queue = [self.root]

        while queue:
            curnode = queue.pop(0)
            print(curnode.value, end=' ')
            if curnode.lchild is not None:
                queue.append(curnode.lchild)

            if curnode.rchild is not None:
                queue.append(curnode.rchild)

    def DLR_recursion(self, node):
        if node is None:
            return
        print(node.value, end=' ')
        self.DLR_recursion(node.lchild)
        self.DLR_recursion(node.rchild)

    def LDR_recursion(self, node):
        if node is None:
            return
        self.LDR_recursion(node.lchild)
        print(node.value, end=' ')
        self.LDR_recursion(node.rchild)

    def LRD_recursion(self, node):
        if node is None:
            return
        self.LRD_recursion(node.lchild)
        self.LRD_recursion(node.rchild)
        print(node.value, end=' ')

    def DLR_no_recursive(self):
        stack = []
        curnode = self.root
        while curnode or stack:
            while curnode:
                print(curnode.value, end=' ')
                stack.append(curnode)
                curnode = curnode.lchild
            curnode = stack.pop()
            curnode = curnode.rchild

    def LDR_no_recursive(self):
        stack = []
        curnode = self.root
        # stack_shadow = []
        while  curnode or stack:
            while curnode:
                stack.append(curnode)
                curnode = curnode.lchild
            curnode = stack.pop()
            # stack_shadow.append(curnode)
            print(curnode.value, end=' ')
            curnode = curnode.rchild

    def LRD_no_recursive(self):
        stack = []
        stack_shadow = []
        curnode = self.root
        while curnode or stack:
            while curnode:
                stack.append(curnode)
                stack_shadow.append(curnode)
                curnode = curnode.rchild
            curnode = stack.pop()
            curnode = curnode.lchild
        return stack_shadow[::-1]

tree = Btree()
tree.append(1)
tree.append(2)
tree.append(3)
tree.append(4)
tree.append(5)
tree.append(6)
tree.append(7)

tree.breadth_order()
print('广度优先')

tree.DLR_recursion(tree.root)
print("先序遍历-递归")

tree.DLR_no_recursive()
print("先序遍历-非递归")

tree.LDR_recursion(tree.root)
print("中序遍历-递归")

tree.LDR_no_recursive()

print("中序遍历-非递归")

tree.LRD_recursion(tree.root)
print("后序遍历-递归")
lrdnode = tree.LRD_no_recursive()

for i in lrdnode:
    print(i.value, end=' ')
print("后序遍历-非递归")

