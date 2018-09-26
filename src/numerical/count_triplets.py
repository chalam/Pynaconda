from collections import defaultdict

# https://www.hackerrank.com/challenges/count-triplets-1/forum
# As a base consider a triplet made up of numbers A,B and C (where B = A* r and C = A* r * r = B* r).
#
# For each value (say X) in the array, you have to consider that X may be an A, B and/or C in some triplet.
#
# When can X be a middle of a triplet (that is case X = B in the triplet)? -> when I already have had one or more
# previous values which will fulfill the requirements of A for this B. So we need to check if there are any
# previous A's "waiting" for this B. Here we just check the map mentioned in the previous comment.
# If there's any that means that we need to consider how many A's are "waiting" to know how many 2/3 complete
# triplets we'd now have with this X.
#
# Similarly to the previous comment we will then let future Cs know that we have these extra 2/3 triplets ready.
# So store in map of almost complete triplets (ensuring that we add to any previous ones already stored).
# This is the second part of the loop.

#
# Final case, when X completes one or more previously 2/3 complete triplets. Simply check how many
# (if any incomplete triplets) are "waiting" for this value to become complete. So check the map of 2/3 triplets and
# accumulate the result.
#
# In any case X can be an A of a future triplet so add it to the map2 so future B's know of this A's existence ->
# Final part of the loop.

def countTriplets(arr, r):
    v2 = defaultdict(int)
    v3 = defaultdict(int)
    count = 0
    for k in arr:
        count += v3[k]
        v3[k*r] += v2[k]
        v2[k*r] += 1

    return count

assert countTriplets([1, 3, 9, 9, 27, 81], 3)