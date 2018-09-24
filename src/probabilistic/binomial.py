# import numpy as np
from scipy.stats import binom

# When flipped a biased coin has a probability of 0.9 for heads.
# You get $1 for heads and loose $10 for tails, what is your expected wealth after 10 tosses?
k, n, p = 1, 10, 0.9
s = binom.pmf(k, n, p)
print(s)