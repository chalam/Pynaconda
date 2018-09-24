# Python implementation of Binary Indexed Tree BIT

# Returns sum of arr[0..index]. This function assumes
# that the array is preprocessed and partial sums of
# array elements are stored in BITree[].
def getsum(BIT, i):
    s = 0  # initialize result

    # index in BITree[] is 1 more than the index in arr[]
    i = i + 1

    # Traverse ancestors of BITree[index]
    while i > 0:
        # Add current element of BITree to sum
        s += BIT[i]

        # Move index to parent node in getSum View
        i -= i & (-i)
    return s


# Updates a node in Binary Index Tree (BITree) at given index
# in BITree.  The given value 'val' is added to BITree[i] and
# all of its ancestors in tree.
def updatebit(BIT, n, i, v):
    # index in BITree[] is 1 more than the index in arr[]
    i += 1

    # Traverse all ancestors and add 'val'
    while i <= n:
        # Add 'val' to current node of BI Tree
        BIT[i] += v

        # Update index to that of parent in update View
        i += i & (-i)   #LSB


# Constructs and returns a Binary Indexed Tree for given
# array of size n.
def construct(arr, n):
    # Create and initialize BITree[] as 0
    BIT = [0] * (n + 1)

    # Store the actual values in BITree[] using update()
    for i in range(n):
        updatebit(BIT, n, i, arr[i])

    # Uncomment below lines to see contents of BITree[]
    # for i in range(1,n+1):
    #      print BIT[i],
    return BIT


# Driver code to test above methods
freq = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
BIT = construct(freq, len(freq))
print("Sum of elements in arr[0..5] is " + str(getsum(BIT, 5)))
freq[3] += 6
updatebit(BIT, len(freq), 3, 6)
print("Sum of elements in arr[0..5] is " + str(getsum(BIT, 5)))
