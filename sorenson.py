import numpy as np


def sorensen_index(adj_matrix):
    n = adj_matrix.shape[0]

    sorensen_matrix = np.zeros((n, n))

    degrees = np.sum(adj_matrix, axis=1)

    for i in range(n):
        for j in range(i, n):
            if i != j:
                # Common neighbors
                common_neighbors = np.sum(np.logical_and(adj_matrix[i], adj_matrix[j]))
                if degrees[i] + degrees[j] > 0:
                    sorensen_matrix[i, j] = (2 * common_neighbors) / (degrees[i] + degrees[j])
                    sorensen_matrix[j, i] = sorensen_matrix[i, j]  # Symmetric matrix
    return sorensen_matrix


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

sorensen_idx_matrix = sorensen_index(adj_matrix)
print("Sørensen Index Matrix:")
print(sorensen_idx_matrix)
