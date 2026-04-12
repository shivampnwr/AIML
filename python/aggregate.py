import numpy as np
array=np.array([[1,2,3,4],
               [5,6,7,8]])
# print(array.shape)
print(np.sum(array))
print(np.mean(array))
print(np.median(array))
print(np.var(array))
print(np.std(array))
print(np.max(array))
print(np.min(array))
print(np.argmin(array)) # returns the index of the minimum value
print(np.argmax(array)) # returns the index of the maximum value
print(np.sum(array,axis=0))
print(np.sum(array,axis=1))
