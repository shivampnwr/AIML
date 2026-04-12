import numpy as np
scores=np.array([23,54,67,100])
print(scores==100)
scores[scores<30]=0
print(scores)