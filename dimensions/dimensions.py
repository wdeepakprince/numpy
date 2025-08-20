import numpy as np

arr_0d = np.array(42)
arr_1d = np.array([1, 2, 3, 4, 5])
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
arr_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print("NumPy Array : ",arr_1d)
print("NumPy Array Type : ",type(arr_1d))
print("NumPy Version : ", np.__version__)
print("NumPy ",arr_0d.ndim,"-D : ", arr_0d)
print("NumPy ",arr_1d.ndim,"-D : ", arr_1d)
print("NumPy ",arr_2d.ndim,"-D : ", arr_2d)
print("NumPy ",arr_3d.ndim,"-D : ", arr_3d)
