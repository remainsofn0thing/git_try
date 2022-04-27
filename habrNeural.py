import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import math

# симпатичная сетка на белом фоне
# (без нее русские подписи -> кракозябры)
sns.set(style='whitegrid', font_scale=1.8)
# точки - признаки (одно измерение)
X1 = np.array([1, 2, 6, 8, 10])
# метки классов (правильные ответы)
y = np.array([-1, -1, 1, 1, 1])

# ось Ф=0
plt.plot(X1, np.zeros(len(X1)), color='black', lw=2)

# обучающие точки на оси Ф=0
plt.scatter(X1[y==1], np.full(len(X1[y==1]), 0), color='blue', marker='o', s=300,
        label=u'объект x (1 признак): класс-1 (y=1)')
plt.scatter(X1[y==-1], np.full(len(X1[y==-1]), 0), color='red', marker='s', s=300,
        label=u'объект x (1 признак): класс-2 (y=-1)')

plt.xlabel(u'X1 (единственный признак)')
plt.ylabel(u'Ф (активация)')

plt.show()

# не будет работать, если включен seaborn
#plt.rcParams.update({'font.size': 16})