'''
Calculate Covariance Matrix (medium)
Write a Python function that calculates the covariance matrix from a list of vectors. Assume that the input list represents a dataset where each vector is a feature, and vectors are of equal length.

Example:
        input: vectors = [[1, 2, 3], [4, 5, 6]]
        output: [[1.0, 1.0], [1.0, 1.0]]
        reasoning: The dataset has two features with three observations each. The covariance between each pair of features (including covariance with itself) is calculated and returned as a 2x2 matrix.

def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	return covariance_matrix        
'''
def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    n_features = len(vectors)
    n_observations = len(vectors[0])
    covariance_matrix = [[0 for _ in range(n_features)] for _ in range(n_features)] #创建了一个n_features x n_features的二维列表，所有元素都被初始化为0。

    means = [sum(feature) / n_observations for feature in vectors]

    for i in range(n_features):
        for j in range(i, n_features):
            covariance = sum((vectors[i][k] - means[i]) * (vectors[j][k] - means[j]) for k in range(n_observations)) / (n_observations - 1)
            covariance_matrix[i][j] = covariance_matrix[j][i] = covariance

    return covariance_matrix

print(calculate_covariance_matrix([[1, 2, 3], [4, 5, 6]]))

'''
Covariance Matrix（协方差矩阵）是统计学中一个非常重要的概念，它用于量化多个变量之间的线性关系。
矩阵的对角线元素表示各个变量的方差。
非对角线元素表示两个不同变量之间的协方差。
     - 正值表示正相关：当一个变量的值高于其均值时，另一个变量的值也倾向于高于其均值。
     - 负值表示负相关：当一个变量的值高于其均值时，另一个变量的值倾向于低于其均值。
     - 接近零的值表示没有明显的线性关系。
在传统机器学习中，协方差矩阵用于特征选择和降维。
'''