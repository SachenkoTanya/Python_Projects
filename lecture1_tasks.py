import numpy as np

# Create a 1D array of numbers from 0 to 9 (Level 1)

# array = np.arange(10)
# print(array)

# Replace all odd numbers in arr with -1 without changing arr (Level 2)
"""
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
new_arr = np.where(arr % 2 == 1, -1, arr)
print(arr)
print(new_arr)
"""

# Stack the arrays a and b horizontally (Level 2)
"""
a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)

result = np.hstack((a, b))

print(result)
"""

# Select the rows of iris_2d that does not have any nan value(Level 3)
"""
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])

mask = np.isnan(iris_2d).any(axis=1)
iris_2d_no_nan = iris_2d[~mask]

print(iris_2d_no_nan)
"""

# Find the duplicate entries (2nd occurrence onwards) in the given numpy array and mark them as True. First time occurrences should be False (Level 3)
"""
np.random.seed(100)
a = np.random.randint(0, 5, 10)
print('Array: ', a)

_, indices = np.unique(a, return_inverse=True)
mask = np.zeros_like(a, dtype=bool)
mask[indices >= 1] = True

print('Duplicate mask: ', mask)
"""

# Compute the moving average of window size 3, for the given 1D array (Level 3)
"""
np.random.seed(100)
Z = np.random.randint(10, size=10)

moving_avg = np.convolve(Z, np.ones(3)/3, mode='valid')

print("Original array:", Z)
print("Moving average array:", moving_avg)

"""

# From the given 1d array arr, generate a 2d matrix using strides, with a window length of 4 and strides of 2, like [[0,1,2,3], [2,3,4,5], [4,5,6,7]..] (Level 4)

"""
arr = np.arange(15)
n = 4
s = 2
output_shape = ((arr.size - n) // s + 1, n)
strides = arr.strides + (arr.strides[-1],)

output = np.lib.stride_tricks.as_strided(arr, shape=output_shape, strides=strides)
"""

# Find all the peaks in a 1D numpy array a. Peaks are points surrounded by smaller values on both sides(Level 4)
def find_peaks(arr):
    peaks = []
    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            peaks.append(i)
    return peaks


a = np.array([1, 3, 7, 1, 2, 6, 0, 1])
peaks = find_peaks(a)
print("Peaks indices:", peaks)
print("Peaks values:", a[peaks])
