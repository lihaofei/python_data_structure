
class Queue():
    def __init__(self):
        self.__list=[]
    def enqueue(self,item):
        self.__list.append(item)
        # self.__list.append(0,item)
    def dequeue(self):
        return self.__list.pop(0)
        # return self.__list.pop()
    def size(self):
        return len(self.__list)

    def is_empty(self):
        return  self.__list == []

if __name__=="__main__":
    q=Queue()
    print(q.is_empty())
    q.enqueue(1)
    q.enqueue(4)
    q.enqueue(6)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())