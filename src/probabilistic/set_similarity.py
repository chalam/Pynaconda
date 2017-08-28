from hashlib import sha1
from datasketch import MinHash
from data import jabber_words, parker_words


def mh_digest (data):
    """estimate Jaccard similarity resemblance
    plagiarize or not"""
    m = MinHash(num_perm=512)

    for d in data:
        sha = sha1(d.encode('utf8'))
        # print('sha', sha.digest(), 'd', d)
        m.update(sha.digest())

    return m

m1 = mh_digest(set(jabber_words))
m2 = mh_digest(set(parker_words))

print("Jaccard simularity %f" % m1.jaccard(m2), "estimated")
print("Jaccard cardinality %f, %f" % (m1.count(), m2.count()), "estimated")

s1 = set(jabber_words)
s2 = set(parker_words)
actual_jaccard = float(len(s1.intersection(s2)))/float(len(s1.union(s2)))

print( "Jaccard simularity %f" % actual_jaccard, "actual")
print("Jaccard cardinality %f, %f" % (len(s1), len(s2)), "actual")
