import cProfile

def my_model():
    sum = 0
    for i in range(100):
        sum += i
    return sum

cProfile.run('my_model()', 'prof')

import pstats
p = pstats.Stats('prof')
p.strip_dirs().sort_stats('cumulative').print_stats()