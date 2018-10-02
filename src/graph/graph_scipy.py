import numpy as np

#       G
#
#      (0)
#     /   \
#    1     2
#   /       \
# (2)       (1)


# A graph with N nodes can be represented by an (N x N) adjacency matrix G.If there is a connection
# from node i to node j, then G[i, j] = w, where w is the weight of the connection.For nodes i and j
# which are not connected, the value depends on the representation:
# for dense array representations, non-edges are represented by G[i, j] = 0, infinity, or NaN.

G_dense = np.array([[0, 2, 1],  # Node 0 has edges with weight  (0,1)=2 and (0,2)=1
                    [2, 0, 0],  # Node 1,2 has edges to 0, since undirected graph
                    [1, 0, 0]])
print('G_dense', G_dense.data)
# for dense masked representations (of type np.ma.MaskedArray), non-edges are represented by masked values.
# This can be useful when graphs with zero-weight edges are desired.
G_masked = np.ma.masked_values(G_dense, 0)
print('G_masked', G_masked.data)
# for sparse array representations, non-edges are represented by non-entries in the matrix.
# This sort of sparse representation also allows for edges with zero weights.

from scipy.sparse import csr_matrix

G_sparse = csr_matrix(G_dense)
print('G_sparse', G_sparse.data)

#      G2
#
#      (0)
#     /   \
#    0     2
#   /       \
# (2)       (1)
# when zero edges are significant
G2_data = np.array([[np.inf, 2, 0],
                    [2, np.inf, np.inf],
                    [0, np.inf, np.inf]])
print('G2_data', G2_data.data)
G2_masked = np.ma.masked_invalid(G2_data)
print('G_dense', G2_masked.data)

from scipy.sparse.csgraph import csgraph_from_dense

# G2_sparse = csr_matrix(G2_data) would give the wrong result
G2_sparse = csgraph_from_dense(G2_data, null_value=np.inf)
print('G2_sparse', G2_sparse.data)
# [2. 0. 2. 0.]

# Dijkstra bellman_ford, johnson, floyd_warshall
genes = ['g0', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'g9', 'g10', 'g11']

# create a list containing 12 lists initialised to 0
Matrix = [[0 for x in range(12)] for x in range(12)]
Matrix[0][1] = -105
Matrix[0][2] = -110
Matrix[1][3] = -132
Matrix[1][4] = -126
Matrix[3][5] = -150
Matrix[4][6] = -128
Matrix[4][7] = -166
Matrix[4][8] = -132
Matrix[4][9] = -118
Matrix[5][6] = -128
Matrix[5][7] = -166
Matrix[5][8] = -132
Matrix[5][9] = -118
Matrix[6][10] = -196
Matrix[7][8] = -132
Matrix[8][9] = -118
Matrix[9][10] = -196
Matrix[2][4] = -126
Matrix[2][5] = -150
Matrix[10][11] = -100

# make a sparse matrix
from scipy.sparse import csr_matrix

Matrix_sparse = csr_matrix(Matrix)

# run Dijkstra's algorithm, starting at index 0
from scipy.sparse.csgraph import dijkstra, bellman_ford, johnson, floyd_warshall

distances, predecessors = dijkstra(Matrix_sparse, indices=0, return_predecessors=True, directed=True)

# print out the distance to g11
print("dijkstra distance to g11=", distances[11])

# print out the path
path = []
i = 11
while i != 0:
    path.append(genes[i])
    i = predecessors[i]
path.append(genes[0])
print("dijkstra path=", path[::-1])

# Bellman-Ford
distances, predecessors = bellman_ford(Matrix_sparse, indices=0, return_predecessors=True, directed=True)

# print out the distance to g11
print("Bellman-Ford distance to g11=", distances[11])

# print out the path
path = []
i = 11
while i != 0:
    path.append(genes[i])
    i = predecessors[i]
path.append(genes[0])
print("Bellman-Ford path=", path[::-1])

# floyd_warshall(
distances, predecessors = floyd_warshall(Matrix_sparse, return_predecessors=True, directed=True)

# print out the distance to g11
print("floyd_warshall distance to g11=", distances[11])

# print out the path
# path = []
# i = 11
# while i != 0:
#     path.append(genes[i])
#     i = predecessors[i]
# path.append(genes[0])
# print("floyd_warshall path=", path[::-1])

# johnson
distances, predecessors = johnson(Matrix_sparse, indices=0, return_predecessors=True, directed=True)

# print out the distance to g11
print("johnson distance to g11=", distances[11])

# print out the path
path = []
i = 11
while i != 0:
    path.append(genes[i])
    i = predecessors[i]
path.append(genes[0])
print("johnson path=", path[::-1])