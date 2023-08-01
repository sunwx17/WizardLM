import numpy as np

def partial_trace(matrix, subsystems):
    """
    Computes the partial trace of a matrix over the specified subsystems.

    Args:
        matrix (numpy.ndarray): The matrix to compute the partial trace of.
        subsystems (list): A list of subsystems to trace out.

    Returns:
        numpy.ndarray: The partial trace of the matrix over the specified subsystems.
    """
    # Get the dimensions of the matrix
    n_rows, n_cols = matrix.shape

    # Compute the trace out subsystems
    #trace_out = np.trace(matrix, axis1=subsystems[0], axis2=subsystems[1])

    # Compute the dimensions of the resulting matrix
    n_subsystems = len(subsystems[0])
    n_rows_new = n_rows - n_subsystems
    n_cols_new = n_cols - n_subsystems

    # Compute the new matrix by summing over the trace out subsystems
    new_matrix = np.zeros((n_rows_new, n_cols_new))
    for i in range(n_rows_new):
        for j in range(n_cols_new):
            new_matrix[i, j] = np.trace(matrix[np.ix_(range(i, i+n_subsystems), range(j, j+n_subsystems))])

    # Return the new matrix
    return new_matrix

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
subsystems = ([0, 1], [0, 1])
print(partial_trace(matrix, subsystems))