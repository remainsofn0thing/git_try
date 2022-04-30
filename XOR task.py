import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def act(x):
    return 0 if x <= 0 else 1

def go(C):
    x = np.array([C[0], C[1], 1])
    w1 = [1, 1, -1.5]
    w2 = [1, 1, -0.5]
    w_hidden = np.array([w1, w2])
    w_out = np.array([-1, 1, -0.5])

    sum = np.dot(w_hidden, x)
    out = [act(x) for x in sum]
    out.append(1)
    out = np.array(out)

    sum = np.dot(w_out, out)
    y = act(sum)
    return y

C1 = [(1,0), (0,1)]
C2 = [(0,0), (1,1)]

xf1,xf2=[1,-1],[2,-1]
yf1,yf2=[-1,2],[-1,3.25]

fig, ax = plt.subplots()

#  Устанавливаем интервал основных и
#  вспомогательных делений:
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))

#  Добавляем линии основной сетки:
ax.grid(which='major',color = 'k')

#  Включаем видимость вспомогательных делений:
#ax.minorticks_on()

#  Теперь можем отдельно задавать внешний вид
#  вспомогательной сетки:
ax.grid(which='minor',color = 'gray',linestyle = ':')

fig.set_figwidth(14)
fig.set_figheight(10)

plt.plot(xf1,yf1)
plt.plot(xf2,yf2)
plt.scatter(C2[1][0], C2[1][1], s=50, c='blue')#coordinates(x,y) s=radius(shape) ,c=color
plt.scatter(C1[1][0], C1[1][1], s=50, c='red')
plt.scatter(C2[0][0], C2[0][1], s=50, c='blue')#coordinates(x,y) s=radius(shape) ,c=color
plt.scatter(C1[0][0], C1[0][1], s=50, c='red')
plt.grid(True)
plt.show()

print( go(C1[0]), go(C1[1]) )
print( go(C2[0]), go(C2[1]) )
