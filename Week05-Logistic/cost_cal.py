import math
import numpy as np

def cost_func(x1,x2):
    return 0.1+0.1*(x1) + 0.1* (x2)
def sigmoid(z):
    """ sigmoid """
    return 1 / (1 + np.exp(-z))

data = [[2,3,1],[1,4,0],[4,5,1]]

for i in data:
    if i[2] == 1:
        print(f"log sig moid: {-(math.log(sigmoid(cost_func(x1=i[0],x2=i[1]))))}")
    elif i[2] == 0:
        # print(-(math.log(1 - cost_func(x1=i[0],x2=i[1]))))
        print(f"log sig moid: {-(math.log(1 - sigmoid(cost_func(x1=i[0],x2=i[1]))))}")