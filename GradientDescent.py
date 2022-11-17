# -*- coding: utf-8 -*-
"""
Gradient Descent Algorithm
"""

import numpy as np
def gradientFunction(x):
    return 2*x + 6

def gradientDescent (start, gradient, learnRate, maxIteration, total=0.01):
    steps = [start]
    X = start
    
    for i in range(maxIteration):
        diff = learnRate * gradient(X)
        if np.abs(diff) < total:
            break
        X = X - diff
        steps.append(X)
    return steps, learnRate, X, len(steps)
history, learnRate, result, steps = gradientDescent(10, gradientFunction, 0.03, 23)

print("\nSteps in Gradient Descent: ", history)
print("\nLearning rate is: ", learnRate)
print("\nNumber of steps required to reach Local Minima: ", steps)
