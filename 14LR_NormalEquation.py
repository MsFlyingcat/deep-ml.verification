''''
Linear Regression Using Normal Equation (easy)
Write a Python function that performs linear regression using the normal equation. The function should take a matrix X (features) and a vector y (target) as input, and return the coefficients of the linear regression model. Round your answer to four decimal places, -0.0 is a valid result for rounding a very small number.

Example:
        input: X = [[1, 1], [1, 2], [1, 3]], y = [1, 2, 3]
        output: [0.0, 1.0]
        reasoning: The linear model is y = 0.0 + 1.0*x, perfectly fitting the input data.

import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	# Your code here, make sure to round
	return theta
'''

import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    X = np.array(X)
    y = np.array(y).reshape(-1, 1)
    X_transpose = X.T
    theta = np.linalg.inv(X_transpose.dot(X)).dot(X_transpose).dot(y)
    theta = np.round(theta, 4).flatten().tolist()
    return theta

print(linear_regression_normal_equation([[1, 1], [1, 2], [1, 3]], [1, 2, 3]))