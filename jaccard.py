import numpy as np


def jaccard_index(adj_matrix):
    n = adj_matrix.shape[0]

    jaccard_matrix = np.zeros((n, n))

    for i in range(n):
        for j in range(i, n):
            if i != j:
                neighbors_i = set(np.where(adj_matrix[i])[0])
                neighbors_j = set(np.where(adj_matrix[j])[0])

                intersection = len(neighbors_i.intersection(neighbors_j))
                union = len(neighbors_i.union(neighbors_j))

                if union > 0:
                    jaccard_matrix[i, j] = intersection / union
                    jaccard_matrix[j, i] = jaccard_matrix[i, j]

    return jaccard_matrix


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

jaccard_idx_matrix = jaccard_index(adj_matrix)
print("Jaccard Index Matrix:")
print(jaccard_idx_matrix)
