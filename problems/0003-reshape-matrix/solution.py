import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	matrix = np.array(a)
	old_shape = matrix.shape
	if old_shape[0]*old_shape[1] != new_shape[0]*new_shape[1]:
		return []
	reshaped_matrix = np.reshape(matrix,new_shape)
	return reshaped_matrix