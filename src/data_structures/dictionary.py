from collections import defaultdict, OrderedDict, Counter
from operator import itemgetter

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)
print(d.items())

s = 'mississippi'
d = defaultdict(int)    # defaults factory to int which is zero
for k in s:
    d[k] += 1
print(d.items())

s = 'mississippi'
d = defaultdict(lambda: 10)    # defaults factory to int with default value 10
for k in s:
    d[k] += 1
print(d.items())

s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
d = defaultdict(set)    # defaults factory to set distinct
for k, v in s:
    d[k].add(v)
print(d.items())


# regular unsorted dictionary
d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}

#  remember the order that items were inserted
# dictionary sorted by key
print(OrderedDict(sorted(d.items(), key=lambda t: t[0])))
# OrderedDict([('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1)])

# dictionary sorted by key itemgetter
print(OrderedDict(sorted(d.items(), key=itemgetter(0))))

# dictionary sorted by value
print(OrderedDict(sorted(d.items(), key=lambda t: t[1])))
#OrderedDict([('pear', 1), ('orange', 2), ('banana', 3), ('apple', 4)])

# dictionary sorted by value itemgetter
print(OrderedDict(sorted(d.items(), key=itemgetter(1))))

# dictionary sorted by length of the key string
print(OrderedDict(sorted(d.items(), key=lambda t: len(t[0]))))
#OrderedDict([('pear', 1), ('apple', 4), ('orange', 2), ('banana', 3)])

class LastUpdatedOrderedDict(OrderedDict):
    """Store items in the order the keys were last added
        remembers the order the keys were last inserted.
        If a new entry overwrites an existing entry,
        the original insertion position is changed and moved to the end:
    """
    def __setitem__(self, key, value):
        if key in self:
            del self[key]
        OrderedDict.__setitem__(self, key, value)

luod = LastUpdatedOrderedDict(d.items())
print(luod)
luod['banana'] = 5
luod['blueberry'] = 10
print(luod)

class OrderedCounter(Counter, OrderedDict):
    """Counter that remembers the order elements are first encountered
        """
    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, OrderedDict(self))

    def __reduce__(self):
        return self.__class__, (OrderedDict(self),)

oc = OrderedCounter(d.items())
print(oc)
oc[('banana', 5)] = 1
oc[('blueberry', 10)] = 1
oc[('blueberry', 10)] = 2
print(oc)



