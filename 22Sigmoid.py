'''
Sigmoid Activation Function Understanding (easy)

Write a Python function that computes the output of the sigmoid activation function given an input value z. The function should return the output rounded to four decimal places.

Example:
        input: z = 0
        output: 0.5
        reasoning: The sigmoid function is defined as σ(z) = 1 / (1 + exp(-z)). For z = 0, exp(-0) = 1, hence the output is 1 / (1 + 1) = 0.5.

import math

def sigmoid(z: float) -> float:
	#Your code here
	return result
'''

import math
def sigmoid(z: float) -> float:
   return round(1 / (1 + math.exp(-z)) , 4)

print(sigmoid(0))

'''
Sigmoid函数的图形是一条S形曲线，称为sigmoid曲线。当x值很大时，函数趋近于1；当x值很小（或为负数）时，函数趋近于0。
e是自然对数的底数，约等于2.71828.
'''