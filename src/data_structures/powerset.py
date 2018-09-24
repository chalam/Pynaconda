import pprint as pp
import itertools as iter


# for each element in the set:
# 	for each subset constructed so far:
# 		new subset = (subset + element)
def powerset(s):
    # 2^N subset since we have N char and 2 choices each
    result = [[]]   # empty set
    for x in s:
        # for every additional element in our set
        # the power set consists of the subsets that don't
        # contain this element (just take the previous power set)
        # plus the subsets that do contain the element (use list
        # comprehension to add [x] onto everything in the
        # previous power set)
        result.extend([subset + [x] for subset in result])
    return result


def powerset_iter(s):
    s = list(s)
    # create r-length tuples for string and chain them
    return set(iter.chain.from_iterable(iter.combinations(s, r) for r in range(len(s)+1)))

def contiguous_powerset(s):
    sl = len(s)
    for i in range(sl):
        for j in range(i, sl):
            print(i, j, s[i:j+1])


def noncontiguous_powerset(s):
    sl = len(s)
    for i in range(sl):
        for j in range(i, sl, 2):
            print(j, s[j])

def hop_one_powerset(s):
    sl = len(s)
    for i in range(sl):
        for j in range(i+2, sl):
            print(i, j, s[i], s[j])

def powerset2(seq):
    res = [[]]
    for s in seq:
        subres = []
        for subset in res:
            subres.extend([subset + [s]])
            # print(subres)
        res.extend(subres)
    return res

pp.pprint(powerset('1234'))
pp.pprint(len(powerset2('1234')))
pp.pprint(len(powerset('1234')))
# pp.pprint(powerset_iter('1234'))
# pp.pprint(contiguous_powerset('1234'))
# pp.pprint(noncontiguous_powerset('12345678'))
# pp.pprint(noncontiguous_powerset('123456789'))
# pp.pprint(hop_one_powerset('12345678'))
pp.pprint(powerset('abba'))
