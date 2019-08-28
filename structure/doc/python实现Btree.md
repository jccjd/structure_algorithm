---
title: python实现单链表

date: 2019-8-27

tags: 
    - python
    - structure

category
    - structure

---

### python实现Btree
二叉树其实和双链表的结构很像，数据结构书里一般说链表是特殊的树，就是将一颗二叉树一条线下去只有左子节点或只有右子节点，当然最好还是看书详细了解
一下这里只做简单的实现。

### 构造节点
树节点的构造需要一个值存value,一个左子节点`lchild`，一个右子节点`rchild`，如下这是个很简单的结构，直接可以看代码

    class Node(object):
        def __init__(self, value=None, lchild=None, rchild=None):
            self.value = value
            self.lchild = lchild
            self.rchild = rchild
    

### append & 遍历树
然后开始对这棵树增加节点，显然应该首先需要`new`一个节点，在初始化的时候定义了一个`self.root = None`，那么在第一次添加节点的时候，根据这个
标志，将第一个增加的节点作为`树的根`，假设为: `1`

当增加第二个节点的时候，情况就有点复杂了。首先要判断`root`节点的`lchild`是否为空，显然第一次添
加是为空的，假设第二个节点为: `2`

第三次添加时`rchild`也是空，这个也很容易加上,假设为: `3`

但当第四次要往上加节点的时候，就有问题了，往哪加啊，没地方加了，在加的话需要去遍历树，往最下面
一层的最左边的节点开始增加，也就是加到二节点的左子节点，

那么树怎么遍历呢，这里引入了队列，用一个列表来模拟一个队列，我们将`self.root`放到队列中,要遍历的时候就将这个节点弹出，然后输出，第一个节点
`self.root`在来判断`root`节点是否有左子节点,和右子节点(刚才我们加了两个元素在跟节点下所以一定是有的)
如果有将其加入到队列中，**注意**这个顺序一定是`先左子节点`后`右子节点的`，这个时候队列里有两个节点`[2, 3]`(这里放的是节点，输出时输出节点的
值，这里用`2,3`代替一下)
当再次弹出的时候就是弹出第二个节点输出也就是`2`，然后判断`2`是否有`lchild` or `rchild` 这里显然没有，然后去弹出`3`节点去输出值为3，依然判
是否有`lchild` or `rchild`，这时队列为空了这个树也遍历完了，那么我们增加的约束条件就是当队空时退出循环。
    
        def breadth_order(self):
            queue = [self.root]
    
            while queue:
                curnode = queue.pop(0)
                print(curnode.value)
                if curnode.lchild is not None:
                    queue.append(curnode.lchild)
    
                if curnode.rchild is not None:
                    queue.append(curnode.rchild)

那么可以遍历了，就可以添加节点了，在遍历的时候不做输出了，如果当前节点的`lchild`或`rchild`为空时，这正是我们想要的直接加上去即可，如果不为空
则像上面遍历的一样将当前节点存到队列当中，下一轮弹出的时候在为其做判断，直到队列中没有元素的时候停止循环。还是有点绕的。

     def append(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:

            curnode = queue.pop(0)
            if curnode.lchild is  None:
                curnode.lchild = node
                return
            else:
                queue.append(curnode.lchild)
                

            if curnode.rchild is None:
                curnode.rchild = node
                return
            else:
                queue.append(curnode.rchild)

### 广度优先搜素
上面的遍历其实就是二叉树的广度优先搜索，可以看到在增加元素的时候用到了，所以显然，当用广度优先搜索的时候，就是将树的元素按照增加的顺序遍历了一遍
(为了文档的完整这里还是贴一下代码)
    
           def breadth_order(self):
            queue = [self.root]
    
            while queue:
                curnode = queue.pop(0)
                print(curnode.value)
                if curnode.lchild is not None:
                    queue.append(curnode.lchild)
    
                if curnode.rchild is not None:
                    queue.append(curnode.rchild)

### 深度优先搜索
深度优先有三种方式，先序遍历(DLR),中序遍历(LDR)，后序遍历(LRD)，然后分别的实现有非递归实现，和递归实现，递归实现代码简单，原理怎么说呢，看
个人理解吧，其实就算理解不了，还是能写出来的,这里直接给出代码，注意一点这里传入的值 node 是根结点，下面会给出测试代码
    
    # 先序遍历
    def DLR_recursion(self, node):
        if node is None:
            return
        print(node.value, end=' ')
        self.DLR_recursion(node.lchild)
        self.DLR_recursion(node.rchild)
        
    # 中序遍历
    def LDR_recursion(self, node):
        if node is None:
            return
        self.LDR_recursion(node.lchild)
        print(node.value, end=' ')

        self.LDR_recursion(node.rchild)
        
    # 后序遍历
    def LRD_recursion(self, node):
        if node is None:
            return
        self.DLR_recursion(node.lchild)
        self.DLR_recursion(node.rchild)
        print(node.value, end=' ')
#### DLR-非递归遍历
非递归的先序遍历，其实现过程和深度优先遍历很相似，这里用到了栈去存取每个结点，可以参考深度优先的实现方式，用列表来模拟栈，这里的退出循环的条件是
当前节点和栈同时为空，带着空栈和根节点进入循环，然后遍历节点。

> 假设一棵二叉树顺序存入`1-7`
    
                    1
                  /   \
                 2     3
               /  \   /  \
              4    5 6    7
              
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


遍历第一个节点`1` 输出当前节点的值`1`，将当前节点压栈，当前节点左子节点`2` 成为当前节点，直到将左子节点遍历完，

    这时得到打印`[1, 2, 4]` 压入栈中的节点也是`[1, 2, 4]`，跳出小循环
    弹出元素4,4的右子节点为空构不成进入小循环的条件       stack: [1, 2]
    弹出2, 2的右子节点为5进入小循环,                    stack: [1]
    将5压入栈中,5无子节点跳出循环                       stack: [1, 5]  print: `[1, 2, 4, 5]`
    弹出5,5的右子节点为空进入不了小循环,                 stack: [1]
    弹出1，该节点存在左子节点3,进入循环将3压入栈中        stack: [3]     print: `[1, 2, 4, 5, 3]`，
    3也有左子节点6,输出6将6后在压入栈中，                stack: [3 ,6]  print: `[1, 2, 4, 5, 3, 6]` 
    6无左子节点出循环，弹出6,6无子节点，                 stack: [3]
    弹出3,3存在右子节点7,7进入循环输入7,                 stack: [7]     print: `[1, 2, 4, 5, 3, 6, 7]`
    7无子结点跳出循环再弹出7，此时栈空，7无右子节点,结点也为空，跳出大循环，遍历结束。

过程就是这么个过程，主要就是借助一个栈，进行节点的交换，根据先序遍历的规则来选择输出的时机。

