import numpy as np
rng=np.random.default_rng()
array=np.array([1,3,4,5,6])
rng.shuffle(array)
print(array)
# random in string
fruits=np.array(["apple","mango","guava","pineapple"])
fruit=rng.choice(fruits)
print(fruit)
