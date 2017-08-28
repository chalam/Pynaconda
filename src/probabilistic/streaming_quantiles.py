from tdigest import TDigest
import random

'''
streaming count
'''
td = TDigest()

# stream some rand number
for x in range(0, 1000):
    td.update(random.random(), 1)

# get their quantile, should be clse to uniform distribution due to PRNG random
for q in [0.05, 0.5, 0.95]:
    print("%f @ %f" % (q, td.quantile(q)))