"""filtering refers to the process ofselecting elements from an array
that matches the given condition"""
import numpy as np
ages=np.array([[12,22,44,67,19],
               [56,34,18,23,12]])
teenagers=ages[ages<18]
adults=ages[(ages>=18) & (ages<60)]
senior=ages[ages>60]
even=ages[ages%2==0]
print(teenagers)
print(adults)
print(senior)
print(even)
# where function is used to preserve the original
#  shape of the array but it is slower
grownup=np.where(ages>18,ages,0)
print(grownup)