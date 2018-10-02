# https://careercup.com/question?id=5647083983863808
# Two sigma
import itertools

# make Union-Find datastructure
import random
import time

from src.data_structures.union_find_disjoint_set import UnionFind

def friendCircles_uf(friends):
    # print(friends)
    n = len(friends)
    uf = UnionFind(range(n))

    for i in range(n):
        j = 0
        for c in friends[i]:
            if c == 'Y':
                uf.union(uf[i], uf[j])
                uf.union(uf[j], uf[i])
            j += 1

    uniqKeys = []
    for k, grp in itertools.groupby(uf.disjoint_set()):
        uniqKeys.append(k)
        # for g in grp:
        #     print(g)
    return len(set(uniqKeys))

def friendCircles(friends):
    """
        Keep two sets for friend and contact.
    :param friends:
    :return:
    """
    n = len(friends)
    ret = []
    for friend in range(n):
        contacts = friends[friend]
        for contact in range(n):
            s1 = s2 = None
            if contacts[contact] == 'Y':
                for s in ret:
                    if friend in s:
                        s1 = s
                    if contact in s:
                        s2 = s
                if s1 is None and s2 is None:
                    newS = {friend, contact}
                    ret.append(newS)
                elif s1 is None and s2 is not None:
                    s2.add(friend)
                elif s1 is not None and s2 is None:
                    s1.add(contact)
                else:
                    if s1 != s2:
                        for i in s2:
                            s1.add(i)
                        ret.remove(s2)
    return len(ret)




# friends = ['YYNN', 'YYYN', 'NYYN', 'NNNY']
# print(friendCircles_uf(friends))
# print(friendCircles(friends))
# friends = ['YNNNN', 'NYNNN', 'NNYNN', 'NNNYN', 'NNNNY']
# print(friendCircles_uf(friends))
# print(friendCircles(friends))

n = 100
ll=[]
for i in range(n):
    l = []
    for j in range(n):
        if i == j:
            l.append('Y')
        elif random.random() > 0.40:
            l.append('Y')
        else:
            l.append('N')
    ll.append(''.join(l))
# print(ll)
st = time.clock()
print(friendCircles_uf(ll))
print(time.clock()-st)
st = time.clock()
print(friendCircles(ll))
print(time.clock()-st)

# ['YNNNNNYNNN', 'NYNNNNNNYN', 'NNYNYNNNNN', 'NNNYNNNNNN', 'NNNNYNNNNN', 'YNNYNYNNNN', 'NNNNNNYNNN', 'NNNNNNNYNN', 'NNNNNNNNYY', 'NNNNNNNNNY']
# 8
# 4
friends = ['YNNNNNYNNN', 'NYNNNNNNYN', 'NNYNYNNNNN', 'NNNYNNNNNN', 'NNNNYNNNNN', 'YNNYNYNNNN', 'NNNNNNYNNN', 'NNNNNNNYNN', 'NNNNNNNNYY', 'NNNNNNNNNY']
print(friendCircles_uf(friends))
print(friendCircles(friends)) # [{0, 3, 5, 6}, {8, 1, 9}, {2, 4}, {7}]
# YNNNNNYNNN
# NNNYNNNNNN
# YNNYNYNNNN
# NNYNYNNNNN
# 0123456789