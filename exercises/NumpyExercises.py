import numpy as np
import os
import time
import operator


a=np.arange(45).reshape(3,3,5)


print(a)
print(a.shape)
print(a.ndim)
print(a.itemsize)
print(a.size)
b=np.array([6,7,8])
print(b)
print(b.dtype)
c=np.array([6.4,6.7,7.8])
print(c.dtype)


b = np.array([(1.5,2,3), (4,5,6)])


mete=np.zeros( (3,4) )

print(20*"--")
print(mete)
aaa=np.arange( 10, 30, 5 )
print(aaa)


x = np.linspace( 0, 2*np.pi, 100 )        # useful to evaluate function at lots of points
f = np.sin(x)
print(f)

print(a<5)

print(a.sum())


d = np.arange(12).reshape(3,4)
print(d)

print(d.sum(axis=0))                     # sum of each column




print(100*"-")
print("Exercise1 part:")

sizeofArray=int(input("please enter the size n>>>>"))
list1=list(range(sizeofArray))
list2=list(range(sizeofArray))
list3=np.arange(sizeofArray)
list4=np.arange(sizeofArray)

t1=time.time()
list12=list(map(operator.add, list1,list2))
t2=time.time()
list34=list3+list4
t3=time.time()


print("time for list:",t2-t1)
print(list12)
print("time for numpy list",t3-t2)
print(list34)





