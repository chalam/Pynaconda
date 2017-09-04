#! /usr/bin/env python
#
# Adapted from: http://clouddbs.blogspot.ch/2010/10/googles-mapreduce-in-98-lines-of-python.html
#

import re
import operator
import urllib.request

from src.distributed_comp.MapReduce import MapReduce

class DistributedGrep(MapReduce):

    def __init__(self, regexp, data):
        MapReduce.__init__(self)
        self.matcher = re.compile(regexp)
        self.data = data

    def split_fn(self, data): # one list item per line with line number
        data_list = []
        line_num = 1
        for line in data.splitlines():
            data_list.append((line_num, line))
            line_num = line_num + 1
        return data_list

    def map_fn(self, line_num, line): # return line if matches, include line num
        matcher = self.matcher
        matched_line = []
        if matcher.search(line):
            matched_line = [(line_num, line)]
        return matched_line

    def reduce_fn(self, line_num, line_list): # identity reducer
        return [(line_num, line_list[0])] # we only ever have one line in the list

    def collect_fn(self, output_list): # just print the resulting list
        return list(sorted(output_list, key=operator.itemgetter(0)))


## demo
def prettyprint(result):
    print("LineNum".rjust(8), "Line".ljust(70))
    print("_______".rjust(8), "_"*70)
    for (line_num, line) in result:
        print(str(line_num).rjust(8), line.ljust(70))
    print()

def demo_mrgrep_with_shakespeare():
    f = urllib.request.urlopen("http://www.fullbooks.com/The-Complete-Works-of-William-Shakespeare-A.html")
    page = f.read().decode('utf-8')
    dgrep = DistributedGrep(r"Puck", page)
    f.close()
    result = dgrep.map_reduce()
    prettyprint(result)


## main
if __name__ == "__main__":
    # demo
    demo_mrgrep_with_shakespeare()