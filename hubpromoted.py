import numpy as np


def hub_promoted_index(adj_matrix):
    n = adj_matrix.shape[0]

    hub_promoted_matrix = np.zeros((n, n))

    degrees = np.sum(adj_matrix, axis=1)

    for i in range(n):
        for j in range(i, n):
            if i != j:
                common_neighbors = np.sum(np.logical_and(adj_matrix[i], adj_matrix[j]))

                min_degree = min(degrees[i], degrees[j])

                if min_degree > 0:
                    hub_promoted_matrix[i, j] = common_neighbors / min_degree
                    hub_promoted_matrix[j, i] = hub_promoted_matrix[i, j]  # Symmetric matrix
    return hub_promoted_matrix


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

hub_promoted_idx_matrix = hub_promoted_index(adj_matrix)
print("Hub Promoted Index Matrix:")
print(hub_promoted_idx_matrix)
