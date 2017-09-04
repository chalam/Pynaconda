#! /usr/bin/env python
#
# Adapted from: http://clouddbs.blogspot.ch/2010/10/googles-mapreduce-in-98-lines-of-python.html
#

import threading
from queue import Queue
import operator


class MapReduce(object):
    ''' MapReduce - to use, subclass by defining these functions,
                    then call self.map_reduce():
        split_fn(self, data) => [(k, v), ...]
        map_fn(self, k, v) => [(k, v1), (k, v2), ...]
        reduce_fn(self, k, [v1, v2, ...]) => [(k, v)]
        output_fn(self, [(k, v), ...])
    '''
    def __init__(self):
        self.data = None
        self.num_worker_threads = 5
        self.min_count = 1

    class SynchronizedDict(dict): # we need this for merging
        def __new__(cls, initializer=[]):
            new = dict.__new__(cls, initializer)
            new.lock = threading.Lock()
            return new
        def __contains__(self, k):
            with self.lock:
                return dict.__contains__(self, k)
        def __getitem__(self, k):
            with self.lock:
                return dict.__getitem__(self, k)
        def __setitem__(self, k, v):
            with self.lock:
                dict.__setitem__(self, k, v)
        def append(self, k, v): # for thread-safe list append
            with self.lock:
                dict.__getitem__(self, k).append(v)
        def items(self):
            with self.lock:
                return dict.items(self)

    def create_queue(self, input_list): # helper fn for queues
        output_queue = Queue()
        for value in input_list:
            output_queue.put(value)
        return output_queue

    def create_list(self, input_queue): # helper fn for queues
        output_list = []
        while not input_queue.empty():
            item = input_queue.get()
            output_list.append(item)
            input_queue.task_done()
        return output_list

    def merge_fn(self, k, v, merge_dict): # helper fn for merge
        if k in merge_dict:
            merge_dict.append(k, v)
        else:
            merge_dict[k] = [v]

    def process_queue(self, input_queue, fn_selector): # helper fn
        output_queue = Queue()
        if fn_selector == 'merge':
            merge_dict = self.SynchronizedDict()
        def worker():
            while not input_queue.empty():
                (k, v) = input_queue.get()
                if fn_selector in ['map', 'reduce']:
                    if fn_selector == 'map':
                        result_list = list(self.map_fn(k, v))
                    elif fn_selector == 'reduce':
                        result_list = list(self.reduce_fn(k, v))
                    for result_tuple in result_list: # flatten
                        output_queue.put(result_tuple)
                elif fn_selector == 'merge': # merge v to same k
                    self.merge_fn(k, v, merge_dict)
                else:
                    raise Exception("Bad fn_selector="+fn_selector)
                input_queue.task_done()
        for i in range(self.num_worker_threads): # start threads
            worker_thread = threading.Thread(target=worker)
            worker_thread.daemon = True
            worker_thread.start()
        input_queue.join() # wait for worker threads to finish
        if fn_selector == 'merge':
            output_list = sorted(merge_dict.items(), key=operator.itemgetter(0))
            output_queue = self.create_queue(output_list)
        return output_queue

    # def output_fn(self, output_list): # just print the resulting list
    #     print("Word".ljust(15), "Count".rjust(5))
    #     print("______________".ljust(15), "_____".rjust(5))
    #     sorted_list = sorted(output_list, key=operator.itemgetter(1), reverse=True)
    #     for (word, count) in sorted_list:
    #         if int(count, 10) > self.min_count:
    #             print(word.ljust(15), repr(count).rjust(5))
    #     print('')

    def map_reduce(self): # the actual map-reduce algoritm
        data_list = self.split_fn(self.data)
        data_queue = self.create_queue(data_list) # enqueue the data so we can multi-process
        map_queue = self.process_queue(data_queue, 'map') # [(k,v),...] => [(k,v1),(k,v2),...]
        merge_queue = self.process_queue(map_queue, 'merge') # [(k,v1),(k,v2),...] => [(k,[v1,v2,...]),...]
        reduce_queue = self.process_queue(merge_queue, 'reduce') # [(k,[v1,v2,...]),...] => [(k,v),...]
        output_list = self.create_list(reduce_queue) # deque into list for output handling
        return output_list