# https://docs.scipy.org/doc/scipy/reference/tutorial/csgraph.html

# link “ape” and “man” in the following way:
# ape -> apt -> ait -> bit -> big -> bag -> mag -> man
# ['ape', 'ope', 'opt', 'oat', 'mat', 'man']

file = '../../data/words.txt'
word_list = open(file).readlines()
print('full', len(word_list))
word_list = map(str.strip, word_list)

word_list = [word for word in word_list if len(word) == 3]
word_list = [word for word in word_list if word[0].islower()]
word_list = [word for word in word_list if word.isalpha()]
word_list = list(map(str.lower, word_list))
print('subset', len(word_list))

# ach of these words will become a node in our graph,
# and we will create edges connecting the nodes associated
# with each pair of words which differs by only one letter.

import numpy as np
word_list = np.asarray(word_list)
print('dtype', word_list.dtype) # unicode
word_list.sort()

# We have an array where each entry is three unicode characters long.
# We’d like to find all pairs where exactly one character is different.
# We’ll start by converting each word to a three-dimensional vector:

word_bytes = np.ndarray((word_list.size, word_list.itemsize),
            dtype='uint8',
            buffer=word_list.data)
# each unicode character is four bytes long. We only need first byte
# we know that there are three characters in each word
word_bytes = word_bytes[:, ::word_list.itemsize//3]
print(word_bytes.shape)

# Now we’ll use the Hamming distance between each point to determine
# which pairs of words are connected. The Hamming distance measures the fraction of
# entries between two vectors which differ: any two words with a
# hamming distance equal to , where  is the number of letters, are connected in the word ladder

from scipy.spatial.distance import pdist, squareform
from scipy.sparse import csr_matrix
hamming_dist = pdist(word_bytes, metric='hamming')  #pair-wise distance
# there are three characters in each word
graph = csr_matrix(squareform(hamming_dist < 1.5 / 3))  #sparse square matrix

# When comparing the distances, we don’t use an equality because this can be unstable
# for floating point values. The inequality produces the desired result as long as
# no two entries of the word list are identical. Now that our graph is set up,
# we’ll use a shortest path search to find the path between any two words in the grap

i1 = word_list.searchsorted('ape')
print(word_list[i1])
i2 = word_list.searchsorted('man')
print(word_list[i2])

from scipy.sparse.csgraph import dijkstra
distances, predecessors = dijkstra(graph,
                                   indices=i1,
                                   return_predecessors=True)
print('distances from %s to %s = %s' % (i1, i2, distances[i2]))
path = []
i = i2
while i != i1:
    path.append(word_list[i])
    i = predecessors[i]
path.append(word_list[i1])
print('path', path[::-1])