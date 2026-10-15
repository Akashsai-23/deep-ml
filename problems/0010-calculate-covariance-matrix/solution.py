import numpy as np
def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	# Your code here
	array = np.array(vectors)
	M,N = array.shape
	means = np.mean(array,axis = 1)
	res = np.zeros((M,M))
	for i in range(M):
		for j in range(M):
			if res[j][i] != 0:
				res[i][j] = res[j][i]
				continue
			res[i][j] = np.sum((array[i] - means[i])*(array[j] - means[j]))/(N-1)
	return res