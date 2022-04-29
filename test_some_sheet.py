import numpy as np
import numpy.random as rand
n,m=10,10
a=[[i * j for j in range(m)] for i in range(n)]
for row in a:
    print(' '.join([str(elem) for elem in row]))

mas=rand.random(5)
print("|".join([str(i) for i in mas]))
mas_iter=iter(mas)
for i in enumerate(mas_iter):
    print(next(mas_iter))



