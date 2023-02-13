import matplotlib.pyplot as plt
import numpy as np

mat = np.array([
    [2,34],[4,45],[5,65],[6,123],[9,67]]
)

a,b = np.split(mat,2,axis=1)

plt.scatter(a, b)
plt.show()