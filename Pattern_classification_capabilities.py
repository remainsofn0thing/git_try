import numpy as np
import matplotlib.pyplot as plt;
import numpy.random as rand
N = 10
bias=5

x1 = rand.uniform(0,15,N)
x2 = x1 + [np.random.randint(15) for i in range(N)] +0.3 +bias #выше прямой
C1 = [x1, x2]
for row in C1:
    print(" | ".join([str(i) for i in row]))

x1 = rand.uniform(0,15,N)
x2 = x1 - [np.random.randint(15) for i in range(N)] - 0.3 +bias #ниже прямой
C2 = [x1, x2]
for row in C2:
    print(" | ".join([str(i) for i in row]))


xf=[0,15]
yf=[0+bias,15+bias]

w1=0.5
w3=-bias*w1
w = np.array([-w1,w1,w3])
for i in range(N):
    x = np.array([C2[0][i], C2[1][i],1])
    print(C2[0][i])
    print(C2[1][i])
    y = np.dot(w, x)
    print(y)
    if y >= 0:
        print("Класс C1")
    else:
        print("Класс C2")

plt.scatter(C1[0][:], C1[1][:], s=10, c='red')
plt.scatter(C2[0][:], C2[1][:], s=10, c='blue')
plt.plot(xf,yf)
plt.grid(True)
plt.show()