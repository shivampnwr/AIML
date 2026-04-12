''' numpy functions'''
import numpy as np
# a=np.zeros((2,3))
# b=np.ones((3,3))
# c=np.arange(1,11,2)
# print(a)
# print(b)
# print(c)
''' mathematical function'''
# a=np.array([0,np.pi/2,np.pi])
# print(np.sin(a))
# print(np.cos (a))
# b=np.array([4,8,81])
# print(np.sqrt(b))
# print(np.exp(b))
'''sorting '''
# data=[('name','S10'),('year',int),('cgpa',float)]
# value=[('ajay','2005','4.3'),
#        ('arambh','2000','9.9'),
#        ('aaplaksh','2008','3.3')]
# a=np.array(value,data)
# print(np.sort(a))
'''datatype'''
# a=np.array([[1,2,3],[4,5,6]])
# print(a.dtype)
# b=np.array([1.2,3.4,4])
# print(b.dtype)
# c=a.T
# print(c)
'''check list is empty'''
# a=[1]
# if a:
#     print("list is not empty")
# else:
#     print("list is empty")
# if not a:
#     print("list is empty")
# else: print("list is not empty")
'''product of all number of list'''
# a=[1,2,3,4]
# import math
# res=math.prod(a)
# print(res)
# res=1
# for i in a:
#     res=res*i
# print(res)
'''multply of matrix in single line'''
# array=[1,2,3,4]
# arr=[2,3,4,5]
# print(np.dot(array,arr))
'''size function'''
# a=([1,2,3],[3,4,5])
# print("total size:",np.size(a))
# print("row size:",np.size(a,0))
# print("column size:",np.size(a,axis=1))
'''eye function'''
print(np.eye(10,dtype =int))
# gives an identity matrix
'''empty function:returns an empty array of a given shape. does not initilaize the values so we use fill to initialize the values'''
a=np.empty((3,3))
a.fill(1)
print(a)



