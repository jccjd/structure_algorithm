class Node(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList(object):

    def __init__(self):
        node = Node()
        self.root = node
        self.tail = None
        self.length = 0

    def __len__(self):
        return self.length

    def iterm_node(self):
        flagnode = self.root.next
        while flagnode is not None:
            yield flagnode
            flagnode = flagnode.next

    def __iter__(self):
        for node in self.iterm_node():
            yield node.value

    def append(self, value):
        node = Node(value)
        if self.tail is None:
            self.root.next = node
        else:
            self.tail.next = node
        self.tail = node
        self.length += 1
    # def remove(self, index):
    #     flagindex = 0
    #     prenode = self.root
    #     curnode = self.root.next
    #     while curnode is not None:
    #         if flagindex == index:
    #             prenode.next = curnode.next
    #             self.length -= 1
    #             del curnode
    #             return
    #         prenode = prenode.next
    #         curnode = curnode.next
    #         flagindex += 1
    # def find(self, index):
    #     flagindex = 0
    #     curnode = self.root.next
    #     while curnode is not None:
    #         if flagindex == index:
    #             return curnode
    #         curnode = curnode.next
    #         flagindex += 1

    def remove(self, index):
        flagindex = 0
        prenode = self.root

        if index >= 0 and index <= self.length - 1:
            for curnode in self.iterm_node():
                if flagindex == index:
                    prenode.next = curnode.next
                    self.length -= 1
                    del curnode
                prenode = prenode.next
                flagindex += 1
        else:
            raise Exception('out of range')

    def find(self, index):
        prenode = 0
        if index >= 0 and index <= self.length - 1:
            for curnode in self.iterm_node():
                if prenode == index:
                    return curnode
                prenode += 1
            return None
        else:
            raise Exception('out of range')

    def update(self, index, value):
        node = self.find(index)
        if node is not None:
            node.value = value
        else:
            raise Exception('the node is None')

    # def reverse(self):
    #     curnode = self.root.next
    #     prenode = None
    #     while curnode:
    #         curnextnode = curnode.next
    #         curnode.next = prenode
    #         if curnextnode is None:
    #             self.root.next = curnode
    #         prenode = curnode
    #         curnode = curnextnode

    def reverse(self):
        curnode = self.root.next
        prenode = None
        while curnode:
            curnnodenext = curnode.next
            curnode.next = prenode

            if curnnodenext is None:
                self.root.next = curnode

            prenode = curnode
            curnode = curnnodenext

class testLinkedlist():

    def testdate(self):
        list = LinkedList()
        list.append(1)
        list.append(2)
        list.append(3)
        return list

    def testappend(self):
        list = self.testdate()
        print('-' * 10, 'test append')
        self.printdata(list)

    def printdata(self, list):
        print('*' * 5, [i for i in list])

    def testremove(self, index):
        list = self.testdate()
        print('-' * 10, f'test remove index {index}')
        self.printdata(list)
        list.remove(index)
        self.printdata(list)

    def testfind(self, index):
        list = self.testdate()
        print('-' * 10, f'test find index {index}')
        self.printdata(list)
        print('find value:', list.find(index).value)

    def testreverse(self):
        print('-' * 10, f'test reverse')
        list = self.testdate()
        self.printdata(list)
        list.reverse()
        self.printdata(list)


test = testLinkedlist()
test.testdate()
test.testappend()
test.testremove(1)
test.testfind(0)
test.testreverse()
