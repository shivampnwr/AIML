import numpy as np
arr1=np.array([[1],[2],[3],[4]])
arr2=np.array([[5,6,7,8]])
print(arr1.ndim)
print(arr1.shape)
print(arr1.shape)
print(arr1*arr2)
print(arr2.reshape(2,2))
arr3=(arr2.shape)
print(np.zeros(arr3))
# multiplication table from 1 to 10 using broadcasting
a=np.array([1,2,3,4,5,6,7,8,9,10])
b=np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
print("\t multiplication table\n")
print(a*b)


