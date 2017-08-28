import hyperloglog
from data import jabber_words, jabber_uniq

# accept 1% counting error
hll = hyperloglog.HyperLogLog(0.01)

for word in jabber_words:
    print(word)
    hll.add(word)

print("prob count %d, true count %d" % (len(hll), len(jabber_uniq)))
print("observed error rate %0.2f" % (abs(len(hll) - len(jabber_uniq)) / float(len(jabber_uniq))))
