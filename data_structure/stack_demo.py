
class Stack():
    def __init__(self):
        self.__list=[]

    def push(self,item):
        self.__list.append(item)

    def pop(self):
        return self.__list.pop()

    def size(self):
        return len(self.__list)

    def is_empty(self):
        return self.__list==[]


    def peek(self):
        return self.__list[-1]

if __name__=="__main__":
    s=Stack()
    s.push(1)
    s.push(3)
    s.push(4)
    print(s.pop())
    print(s.pop())
