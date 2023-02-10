from math import log
import numpy as np

def y_hat(x1,x2):
    return 0.1+0.1*(x1) + 0.1* (x2)
def sigmoid(z):
    """ sigmoid """
    return 1 / (1 + np.exp(-z))

data = [[2,3,1],[1,4,0],[4,5,1]]

for i in data:
    h = sigmoid(y_hat(x1=i[0],x2=i[1]))
    y = i[2]
    if y == 1:
        print(f"negative log loss: {round(-(log(h)),4)}")
    elif y == 0:
        # print(-(math.log(1 - cost_func(x1=i[0],x2=i[1]))))
        print(f"negative log loss: {round(-(log(1 - h)),4)}")