

### 单链表
链表嘛就是链接而成的一张表，由于在存储数据的时候，不见得分配的内存就是连续的，链表能将那些在物理上不连续
的空间给利用起来，其数据结构就是，将一块地址空间拆分来用，一部分存放数据，一部分，放指针，指针指向下个
数据，每增加一个元素都让最后一个元素的指针指向该元素，然后就能将这些数据串起来了，当然这些描述并不是很精准，具体定义还是书上比较精确。然后开始Python去实现这个简单的数据结构

### Node类
首先定义一个Node类，有两个值，一个`value` 用来存放数据的，一个next用来指向下一个元素的
初始化为None, 很简单的一个结构
    
    class Node(object):
        def __init__(self, value=None, next=None):
            self.value = value
            self.next = next

### LinkedList
开始实现链表，首先对一个链表进行初始化，确认一个根结点，下面还定义了一个 `tailnode` 用来表示尾节点，这个尾节点
一开始是指向None的，如果增加元素就将该节点指向新元素，
    
    class LinkedList(object):
        def __init__(self):
            node = Node()
            self.root = node
            self.tailnode = None
            self.lenght = 0
 
### append
初始化完root节点后，就可以增加节点然后串成一张表了,
    
    def append(self, value):
        node = Node(value)
        if self.tailnode is None:
            self.root.next = node
        else:
            self.tailnode.next = node
        self.tailnode = node
        self.lenght += 1
        
每次增加节点肯定是需要新节点的，在初始化的时候，尾节点是指向`None`的，所以
如果`self.tailnode is None` 说明该链表只有root节点还没有增加节点，那么
这时候只要将root节点的Next指向新节点`self.root.next = node`即可，每次增加节点，尾节点都移向新节点`self.tailnode = node`,最后长度加加，

第二次增加节点的时候，尾节点已经不为空了，尾节点已经是一个真实的节点，然后将尾节点的next指向新节点，`self.tailnode.next = node`, 再将尾节点标志给这个新节点。在增加的话依然执行该操作。那么这就是增加节点的过程

### remove
能增当然也应该能删除，删除有两种思路，是根据索引位置删除还是根据值删除，下面的实现是根据位置的删除,
    
    def remove(self, index):
        prenode = self.root
        curnode = self.root.next
        flagindex = 0
        while curnode is not None:
            if flagindex == index:
                prenode.next = curnode.next
                self.length -= 1
                del curnode
                return
            prenode = prenode.next
            curnode = curnode.next
            flagindex += 1
传统的单链表删除操作就是使用两个结点一前一后，当后一个节点遍历到目标时，用前一个节点去指向后一节点的next，然后del 目标节点。大概思路是这样的。

上面的代码定义了，一个前驱节点 `prenode = self.root`,一开始是指向root的，然后当前节点是第一个节点`curnode = self.root.next`，是有值的,
还有一个游标`flagindex` 

然后从第一个节点开始遍历，通过 `flagindex` 和`index`比较判断是否是需要删除的节点，是则删除，否则让`prenode` 和`curnode`向前走，直到找到为止
这里当然要对index进行校验，后面会加上。
### find
查找比较简单遍历链表即可,这里依然根据索引去查找
    
    def find(self, index):
        flagindex = 0
        curnode = self.node.next
        while curnode is not None:
            if flagindex == index:
                return curnode.value
            curnode = curnode.next
            flagindex += 1
可以看到这里跟remove 很相似，我们可能需要一些工具函数，比如遍历链表，得到链表的长度
### 遍历链表
    
    def iterm_node(self):
        flagnode = self.root.next
        while flagnode is not None:
            yield flagnode
            flagnode = flagnode.next

    def __iter__(self):
        for node in self.iterm_node():
            yield node.value
    def __len__(self):
        return self.length
        
这里用了生成器将结果转为一个node生成器对象，节省空间，随用随取,然后重写了`__iter__`可以直接遍历值
那么上面的删除和查找就可以这样写了
    
    def remove(self, index):
        flagindex = 0
        prenode = self.root

        if index >= 0 and index <= self.length - 1:
            for node in self.iterm_node():
                if flagindex == index:
                    prenode.next = node.next
                    self.length -= 1
                    del node
                prenode = prenode.next
                flagindex += 1
        else:
            raise Exception('out of range')

    def find(self, index):
        prenode = 0
        if index >= 0 and index <= self.length - 1:
            for curnode in self.iterm_node():
                if flagindex == index:
                    return curnode
                flagindex += 1
            return None
        else:
            raise Exception('out of range')
上面的代码加上了边界的判定，然后直接去遍历节点的生成器，来得到当前节点，`prenode`在每次
遍历时跟随，直至找到节点，然后进行删除或者输出操作。
### update
在对数据进行更新，那么这个操作就比较简单了，直接找到节点，然后更新值即可

    def update(self, index, value):
        node = self.find(index)
        if node is not None:
            node.value = value
        else:
            raise Exception('the node is None')
### reverse
反转一个链表，这个还是有点复杂的，大概思想是，需要一个`hepenode=None` 从第一个
有值节点`curnode = self.root.next`开始遍历，将遍历到的节点的`next`指向`hepenode`,这时的`hepenode`为`None` 然后`hepenode = curnode`,`curnnode`继续向后走 `curnode = curnode.next`


    
    def reverse(self):
        curnode = self.root.next
        helpnode = None
        
        while curnode:
            curnodenext = curnode.next
            
            curnode.next = helpnode
            if curnodenext is None:
                self.root.next= curnode
            
            helpnode = curnode
            curnode = curnodenext
在`helpnode` 和`curnode`之间交换时需要一个中介`curnodenext`,

先将`curnode`的下一个节点存到`curnodenext`中，

然后再将`curnode.next`指向`helpnode`, 


`curnode` 赋值给`helpnode`，

把存在`curnodenext`的节点在赋值给`curnode`,

直到`curnodenext`为`None`时`root`指向`curnode`，

这样就将一个链表给反转了， 还是比较复杂的，


