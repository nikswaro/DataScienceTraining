#print('Congratulations on running this script!!')


"""def mean(num_list):
    return sum(num_list) / len(num_list)

def add_five(num_list):
    return [n + 5 for n in num_list]

def main():
    print("Testing mean function")
    n_list = [34, 44, 23, 46, 12, 24]
    correct_mean = 30.5
    assert(mean(n_list) == correct_mean)

    print("Testing add_five function")
    correct_list = [39, 49, 28, 51, 17, 29]
    assert(add_five(n_list) == correct_list)

    print("All tests passed!")

if __name__ == '__main__':
    main()
"""
import numpy as np
import pandas as pd
x = np.array([1, 2, 3, 4, 5])
Y = np.array([[1,2,3],[4,5,6],[7,8,9], [10,11,12]])
print('x = ', x)
x_shape = x.shape
print(x_shape[0])
print('y = ', Y)
y_shape = Y.shape
print(y_shape[0])

# Using the Built-in functions you learned about in the
# previous lesson, create a 4 x 4 ndarray that only
# contains consecutive even numbers from 2 to 32 (inclusive)
z = np.arange(2,33,2).reshape(4,4)
print(z)