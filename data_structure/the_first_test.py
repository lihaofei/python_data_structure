# if a+b+c=1000,且a^2+b^2=c^2(a,b,c 为自然数)，如何求出所有a，b，c可能的组合？
# the first method
import time
# start_time=time.time()
# for a in range(0,1001):
#     for b in range(0,1001):
#         for c in range(0,1001):
#             if (a*a+b*b==c*c)&(a+b+c==1000):
#                 print("a=%d,b=%d,c=%d\r\n"%(a,b,c))
# end_time=time.time()
# print("time=%d\r\n"%(end_time-start_time))

# the second method
start_time=time.time()
for a in range(0,1001):
    for b in range(0,1001):
        c=1000-a-b
        if(a*a+b*b==c*c):
            print("a=%d,b=%d,c=%d\r\n" % (a, b, c))
end_time=time.time()
print("time=%f\r\n"%(end_time-start_time))
