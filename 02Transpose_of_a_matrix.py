'''
Transpose of a Matrix (easy)

Write a Python function that computes the transpose of a given matrix.

Example:
        input: a = [[1,2,3],[4,5,6]]
        output: [[1,4],[2,5],[3,6]]
        reasoning: The transpose of a matrix is obtained by flipping rows and columns.
 
def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
	return b
'''

def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    return [list(i) for i in zip(*a)]

#定义一个list, 使用方括号[]是创建列表的首选方法，因为它更简洁。list()函数通常用于将其他可迭代对象（如元组、集合或字符串）转换为列表。如list(“hello”)返回['h', 'e', 'l', 'l', 'o']
a = [[1,2,3],[4,5,6]] 
print(transpose_matrix(a))

'''
zip()将对象中对应的元素打包成一组组元组，然后返回由这些元组组成的zip对象（在Python 3中，zip()返回的是一个迭代器）。
zip(*a)的作用是将a中的每个子元素（如列表或元组）作为参数“解包”(Unpacking)后传递给zip函数。意味着如果a是一个可迭代对象（如列表、元组等），其元素本身也是可迭代对象（比如列表的列表、元组的元组等），那么*a会将a中的元素解包成独立的参数，然后这些参数被传递给zip函数。
'''