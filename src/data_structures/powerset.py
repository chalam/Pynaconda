import pprint as pp
import itertools as iter


# for each element in the set:
# 	for each subset constructed so far:
# 		new subset = (subset + element)
def powerset(s):
    result = [[]]
    for x in s:
        # for every additional element in our set
        # the power set consists of the subsets that don't
        # contain this element (just take the previous power set)
        # plus the subsets that do contain the element (use list
        # comprehension to add [x] onto everything in the
        # previous power set)
        result.extend([subset + [x] for subset in result])


def powerset_iter(s):
    s = list(s)
    # create r-length tuples for string and chain them
    return set(iter.chain.from_iterable(iter.combinations(s, r) for r in range(len(s)+1)))


pp.pprint(powerset('1234'))
pp.pprint(powerset_iter('1234'))