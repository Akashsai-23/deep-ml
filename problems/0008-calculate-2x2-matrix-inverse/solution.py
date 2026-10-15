import numpy as np
def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """
    # Your code here
    array = np.array(matrix)
    det = array[0][0]*array[1][1] - array[0][1]*array[1][0]
    if (det == 0):
        return None
    else:
        return [[array[1,1],-array[0,1]],[-array[1,0],array[0,0]]]/det
    