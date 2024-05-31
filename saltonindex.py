import numpy as np


def salton_index(adj_matrix):
    n = adj_matrix.shape[0]

    salton_matrix = np.zeros((n, n))

    degrees = np.sum(adj_matrix, axis=1)

    for i in range(n):
        for j in range(i, n):
            if i != j:
                # Common neighbors
                common_neighbors = np.sum(np.logical_and(adj_matrix[i], adj_matrix[j]))
                if degrees[i] != 0 and degrees[j] != 0:
                    salton_matrix[i, j] = common_neighbors / np.sqrt(degrees[i] * degrees[j])
                    salton_matrix[j, i] = salton_matrix[i, j]  # Symmetric matrix
    return salton_matrix


adj_matrix = np.array([
        [0, 1, 1, 0, 0, 0, 1, 0, 0, 0],
        [1, 0, 1, 1, 0, 0, 0, 1, 0, 0],
        [1, 1, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 1, 1, 0, 0, 1],
        [0, 0, 0, 1, 1, 0, 1, 1, 0, 0],
        [1, 0, 0, 0, 1, 1, 0, 1, 1, 0],
        [0, 1, 0, 0, 0, 1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 1, 1, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 1, 1, 0]
    ])

salton_idx_matrix = salton_index(adj_matrix)
print("Salton Index Matrix:")
print(salton_idx_matrix)
