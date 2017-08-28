from pybloom import BloomFilter
from data import jabber_words, parker_words

bf = BloomFilter(capacity=1000, error_rate=0.001)

for word in parker_words:
    bf.add(word)

intersect = set([])

for word in jabber_words:
    if word in bf:
        intersect.add(word)

print('intersect', intersect)