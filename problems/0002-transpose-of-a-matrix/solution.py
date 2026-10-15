def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    ls1 = []
    for i in range(len(a[0])):
        ls2 = []
        for j in range(len(a)):
            ls2.append(a[j][i])
        ls1.append(ls2)

    return ls1
