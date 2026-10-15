import numpy as np
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means = np.mean(matrix,axis = 0 if mode == "column" else 1, dtype = float)
	return means