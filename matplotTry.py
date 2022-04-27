import matplotlib.pyplot as plt
import numpy as np

arr=np.random.randint(0, 1000, 600)
arrNew=np.random.choice(arr, size=20, replace=True, p=None)
plt.hist(arrNew)