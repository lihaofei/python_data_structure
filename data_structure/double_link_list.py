class Node():
    def __init__(self,elem):
        self.elem=elem
        self.next=None
        self.prev=None
class DoubleLinkList():
    def __init__(self,node=None):
        self.__head=node
    def is_empty(self):
        return self.__head==None
    def length(self):
        cur = self.__head
        count=0
        while cur!=None:
            count+=1
            cur=cur.next
        return count

    def travel(self):
        cur = self.__head
        while cur!=None:
            print(cur.elem,end=" ")
            cur=cur.next
        print(" ")


    def add(self,item):
        node =Node(item)
        node.next = self.__head
        self.__head= node
        node.next.prev=node

    def append(self,item):
        node = Node(item)
        if self.is_empty()
            self.__head=node
        else:
            cur =self.__head
            while cur!=None:
                cur=cur.next
            cur.next=node
            node.pre=cur

    def insert(self,pos,item):
        if pos<=0:
            self.add(item)
        elif pos>(self.length()-1):
            self.append(item)
        else:
            cur=self.__head
            count=0
            while count<pos:
                count+=1
                cur=cur.next
            node=Node(item)
            node.next=cur
            cur.next=node.prev
            cur.prev.next=node
            cur.prev = node

    def remove(self,item):
        cur = self.__head
        while cur!=None:
            if cur.elem==item:
                if cur==self.__head:
                    self.__head=cur.next
                    if cur.next:
                        # 判断链表是否只有一个结点
                        cur.next.prev=None

                else:
                    cur.prev.next=cur.next
                    if cur.next:
                        # 判断链表是否只有一个结点
                        cur.next.prev = cur.prev
                break

            else:
                cur = cur.next

    def search(self,item):
        cur=self.__head
        while cur!=None:
            if cur.elem==item:
                return True
            else:
                cur=cur.next
        return False

if __name__=="__main__":
    pass
