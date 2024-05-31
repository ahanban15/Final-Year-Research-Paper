import numpy as np


def common_neighbors(adj_matrix):
    num_nodes = len(adj_matrix)
    similarity_matrix = np.zeros((num_nodes, num_nodes))

    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            neighbors_i = set(np.where(adj_matrix[i] == 1)[0])
            neighbors_j = set(np.where(adj_matrix[j] == 1)[0])
            common_neighbors_count = len(neighbors_i & neighbors_j)
            similarity_matrix[i, j] = similarity_matrix[j, i] = common_neighbors_count

    return similarity_matrix


def main():
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

    similarity_matrix = common_neighbors(adj_matrix)

    print("Adjacency Matrix:")
    print(adj_matrix)
    print("\nCommon Neighbors Similarity Matrix:")
    print(similarity_matrix)


if __name__ == "__main__":
    main()
