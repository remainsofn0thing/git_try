from datetime import datetime

import numpy as np
from main import *

length=1000
weightToTry=np.linspace(-10,10,length)
costs=np.zeros(length)

startTime=datetime.now()
for i in range(length):
    NN.W1[0,0]=weightToTry[i]
    yHat=NN.forward(X)
    costs[i]=0.5*sum((y-yHat)**2)
endTime=datetime.now()

timeElapsed=endTime-startTime
print(timeElapsed.seconds,timeElapsed.microseconds)

