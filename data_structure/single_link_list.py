

# 设置节点
# elem 为本节点内容
# next 为本节点指向下一节点连接区域
class Node():
    def __init__(self,elem):
        self.elem=elem
        self.next=None

class SingleLinkList():
    # 单链表初始化
    # 初始化链表 设置头节点为None
    def __init__(self,node=None):
        self.__head=node
    #判断头节点是否为空，来判断链表是否为空
    def is_empty(self):
        return self.__head==None

    #计算链表长度
    def length(self):
        # 游标首先从头节点开始
        cur = self.__head
        count=0
        #开始计数节点个数
        while cur!=None:
            cur=cur.next
            count+=1
        return count
    # 遍历
    def travel(self):
        # 游标首先从头节点开始
        cur=self.__head
        while cur!=None:
            print(cur.elem,end=" ")
            cur=cur.next
        print("")

    # 在链表头部加入节点
    def add(self,item):
        # 创建节点
        node = Node(item)
        # 将头节点 放入 创建的node节点之后
        node.next=self.__head
        # 将node作为头节点
        self.__head=node
    # 在链表尾部加入节点
    def append(self,item):
        # 创建节点
        node =Node(item)
        # 判断链表是否为空
        if self.is_empty():
            # 若链表为空，则将创建的节点作为头节点
            self.__head=node
        else:
            # 若链表不为空，则将头节点作为游标的开始
            cur=self.__head
            while cur.next!=None:
                cur=cur.next
            # 将节点放入最后一个节点的下一区域
            cur.next=node

    def insert(self,pos,item):
        if pos<=0:
            self.add(item)
        elif pos>(self.length()-1):
            self.append(item)
        else:
            pre = self.__head
            count = 0
            while count<(pos-1):
                count+=1
                pre=pre.next
            # 创建需要插入的节点
            node = Node(item)
            # 将 没有插入之前的pre的节点的下一节点区域与创建节点的下一及诶单的区域联系起来
            node.next=pre.next
            # 将pre节点的下一节点区域与创建节点联系起来
            pre.next=node
    # 删除节点
    def remove(self,item):
        cur=self.__head
        pre=None
        while cur!=None:

            if cur.elem==item:
            # 若为item，则进行item的删除
                if cur == self.__head:
                    # cur的下一个节点作为头节点
                    self.__head=cur.next
                else:
                    # 将pre的下一节点的区域与cur下一节点的区域连接起来
                    pre.next=cur.next
                break
            else:
            #若不为item，则进行链表的移动
                # 实现 cur 与pre 两个游标的移动  (pre在前 cur在后)
                pre = cur
                cur=cur.next

   # 查找节点是否存在
    def search(self,item):
        cur =self.__head
        while cur!=None:
            if cur.elem==item:
                return True
            else:
                cur=cur.next
        return False
if __name__=="__main__":
    ll = SingleLinkList()
    print(ll.is_empty())
    print(ll.length())

    ll.append(1)
    print(ll.is_empty())
    print(ll.length())

    ll.append(2)
    ll.add(8)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    # 8 1 2 3 4 5 6
    ll.insert(-1, 9)  # 9 8 1 23456
    ll.travel()
    ll.insert(3, 100)  # 9 8 1 100 2 3456
    ll.travel()
    ll.insert(10, 200)  # 9 8 1 100 23456 200
    ll.travel()
    ll.remove(100)
    ll.travel()
    ll.remove(9)
    ll.travel()
    ll.remove(200)
    ll.travel()
