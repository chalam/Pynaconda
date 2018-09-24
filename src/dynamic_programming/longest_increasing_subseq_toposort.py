# model the sequence as graph for  bellman ford i
# The first step is to turn the bidirectional edges into directional edges,
# only going from the smaller to the larger numbered node for each one.
# Note that the resulting graph will be a directed acyclic graph (DAG),
# since we can't go from a small-high-small number in a path.
# From here on we can ignore the node numbering.
# use topological sort
# find the longest path
# https://en.wikipedia.org/wiki/Longest_increasing_subsequence
# http://www.stoimen.com/blog/2012/12/03/computer-algorithms-longest-increasing-subsequence/