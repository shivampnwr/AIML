import numpy as np
array=np.array(['a','b','c'])
print(array)
print(array.shape)
array1=np.array('a')
print(array1)
print(array1.shape)
array2=np.array([[['a','b','c'],['d','e','f'],['d','e','f']]
                 ,[['d','e','f'],['d','e','f'],['d','e','f']]
                 ,[['d','e','f'],['d','e','f'],['d','e','f']]])
print(array2[0][0][0])
print(array2[0,1,1])
print(array2.shape)  # return the dimension of array
word=array2[0,0,1]+array2[0,0,0]+array2[0,1,1]
print(word)