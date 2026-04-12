import numpy as np
array= np.array([1,2,3,4,5,6,7,8,9,0])
#array[start:end:step]
print(array[1:11:2])
print(array[-1::-1])
array1= np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(array1[:,0])
print(array1[:,0:4])
print(array1[0:2,2:])