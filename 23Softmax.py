'''
Softmax Activation Function Implementation (easy)

Write a Python function that computes the softmax activation for a given list of scores. 
The function should return the softmax values as a list, each rounded to four decimal places.

Example:
        input: scores = [1, 2, 3]
        output: [0.0900, 0.2447, 0.6652]
        reasoning: The softmax function converts a list of values into a probability distribution. 
        The probabilities are proportional to the exponential of each element divided by the sum of the exponentials of all elements in the list.

import math

def softmax(scores: list[float]) -> list[float]:
	# Your code here
	return probabilities
'''

import math
def softmax(scores: list[float]) -> list[float]:
    # 在计算sum_exp_scores时，如果 exp_scores中的值非常大，它们的和可能会超出浮点数的表示范围，导致数值溢出。为了避免这个问题，通常从每个指数值中减去最大的指数值，然后再求和。
    max_score = max(scores) 
    exp_scores = [math.exp(score - max_score) for score in scores]
    sum_exp_scores = sum(exp_scores)
    probabilities = [round(score / sum_exp_scores, 4) for score in exp_scores]
    return probabilities

print(softmax([1, 2, 3]))

'''
Softmax函数常用于机器学习和深度学习中，将一个含任意实数的向量转换成另一个实数向量，新向量的每个元素值在0到1之间，且所有元素值的总和为1。这使得softmax函数成为多类分类问题中输出层的激活函数的理想选择。
'''