import numpy as np
# for integers
# seed is used to reproduce the same outcome
rng=np.random.default_rng(seed=1)
print(rng.integers(low=1,high=7))
print(rng.integers(low=1,high=7,size=(3,2)))
# for floating point number
np.random.seed(seed=2)
print(np.random.uniform(1,2,size=(2,3)))
