'''
Feature Scaling Implementation (easy)

Write a Python function that performs feature scaling on a dataset using both standardization and min-max normalization. The function should take a 2D NumPy array as input, where each row represents a data sample and each column represents a feature. It should return two 2D NumPy arrays: one scaled by standardization and one by min-max normalization. Make sure all results are rounded to the nearest 4th decimal.

Example:
        input: data = np.array([[1, 2], [3, 4], [5, 6]])
        output: ([[-1.2247, -1.2247], [0.0, 0.0], [1.2247, 1.2247]], [[0.0, 0.0], [0.5, 0.5], [1.0, 1.0]])
        reasoning: Standardization rescales the feature to have a mean of 0 and a standard deviation of 1.
        Min-max normalization rescales the feature to a range of [0, 1], where the minimum feature value
        maps to 0 and the maximum to 1.

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	# Your code here
	return standardized_data, normalized_data
'''

import numpy as np

def feature_scaling(data):
    # Standardization
    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0)
    standardized_data = (data - mean) / np.where(std == 0, 1, std)

    # Min-Max Normalization
    min_val = np.min(data, axis=0)
    max_val = np.max(data, axis=0)
    normalized_data = (data - min_val) / (max_val - min_val)
    
    return np.round(standardized_data,4).tolist(), np.round(normalized_data,4).tolist()

data = np.array([[1, 2], [3, 4], [5, 6]])
print(feature_scaling(data))

'''
两种常见的特征缩放方法：标准化（Standardization）和最小-最大归一化（Min-Max Normalization）
'''