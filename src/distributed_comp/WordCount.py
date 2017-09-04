#! /usr/bin/env python
#
# Adapted from: http://clouddbs.blogspot.ch/2010/10/googles-mapreduce-in-98-lines-of-python.html
#

import re
import operator
import urllib.request

from src.distributed_comp.MapReduce import MapReduce

class WordCount(MapReduce):

    def __init__(self, data):
        MapReduce.__init__(self)
        self.min_count = 1
        self.data = data

    def split_fn(self, data):
        """Break string into [(k, v), ...] tuples for each line."""
        def line_to_tuple(line):
            return (None, line)
        data_list = [ line_to_tuple(line) for line in  data.splitlines() ]
        return data_list

    def map_fn(self, key, value):
        """Return (word, 1) tuples for each word, ignore key."""
        for word in re.split(r'\W+', value.lower()):
            bare_word = re.sub(r"[^A-Za-z0-9]*", r"", word);
            if len(bare_word) > 0:
                yield (bare_word, 1)

    def reduce_fn(self, word, count_list):
        """Sum the counts."""
        return [(word, sum(count_list))]

    def output_fn(self, output_list): # just print the resulting list
        print("Word".ljust(15), "Count".rjust(5))
        print("______________".ljust(15), "_____".rjust(5))
        sorted_list = sorted(output_list, key=operator.itemgetter(1), reverse=True)
        for (word, count) in sorted_list:
            if count > self.min_count:
                print(word.ljust(15), repr(count).rjust(5))
        print()

## tests
def test_wordcount_with_monty():
    wc = WordCount("""The Meaning of Life is:
        try and be nice to people,
        avoid eating fat,
        read a good book every now and then,
        get some walking in,
        and try and live together in peace and harmony
        with people of all creeds and nations.""")
    wc.map_reduce()

## tests
def test_wordcount_with_shakespeare():
    f = urllib.request.urlopen("http://www.fullbooks.com/The-Complete-Works-of-William-Shakespeare-A.html")
    wc = WordCount(f.read().decode('utf-8'))
    wc.min_count = 200
    f.close()
    wc.map_reduce()


## main
if __name__ == "__main__":
    # demo
    test_wordcount_with_monty()
    test_wordcount_with_shakespeare()