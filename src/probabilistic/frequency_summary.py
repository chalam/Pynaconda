from collections import Counter
# from yacms import CountMinSketch
from count_min_sketch import CountMinSketch
from data import jabber_words


counts = Counter()

'''
count–min sketch is to consume a stream of events, one at a time, and count the frequency of the different types of events in the stream
'''
# table size=1000, hash functions=10
cms = CountMinSketch(200, 3)

for word in jabber_words:
    counts[word] += 1
    cms.update(word, 1)


for word in ["the", "and", "he", "that"]:
    print("instances of the word `%s` %d" % (word, cms.estimate(word)))

for e in counts:
    if counts[e] != cms.estimate(e):
        print("missed '%s' counter: %d, sketch: %d" % (e, counts[e], cms.estimate(e)))