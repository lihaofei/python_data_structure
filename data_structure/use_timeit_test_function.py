# this demo  is  use timeit
from timeit import Timer

def function():
    list_func=[]
    for i in range(10000):
        list_func.append(i)


time=Timer("function","from __main__ import function ")
# 10000是指该代码运行10000遍求得均值时间
print("function use time is",time.timeit(10000))
