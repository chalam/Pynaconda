from collections import namedtuple, defaultdict
from functools import cmp_to_key
from itertools import groupby
from operator import itemgetter, attrgetter

Student = namedtuple('Student', ['name', 'grade', 'age'])

student_objects = [
    Student('Bravo', 'C', 10),
    Student('Delta', 'B', 12),
    Student('Charlie', 'A', 15),
    Student('Alpha', 'B', 12),
    Student('Echo', 'C', 9),
    Student('Foxtrot', 'A', 19),
    Student('Foxtrot', 'A', 20),
]
print(student_objects)

print(sorted(student_objects, key=lambda s: s.name))
print(sorted(student_objects, key=itemgetter(0)))

print(sorted(student_objects, key=lambda s: s[1]))   # grade
print(sorted(student_objects, key=itemgetter(1)))

print(sorted(student_objects, key=lambda s: s.age))
print(sorted(student_objects, key=attrgetter('age')))
print(sorted(student_objects, key=attrgetter('age'), reverse=True))


def comparator(a, b):
    """
        return a negative value for less-than,
        return zero if they are equal, or
        return a positive value for greater-than
    :param a:
    :param b:
    :return:
    """
    if a.grade < b.grade:   # Grade: A >  B > C
        return -1
    if a.grade > b.grade:
        return 1
    if a.name < b.name:     # Name: Lexi
        return -1
    if a.name > b.name:
        return 1
    if a.age < b.age:     # Age: Reverse Numeric for seniority
        return 1
    if a.age > b.age:
        return -1
    return 0
print(sorted(student_objects, key=cmp_to_key(comparator)))


groups = defaultdict(list)
uniquekeys = []
# data = sorted(student_objects, key=itemgetter(1))
data = sorted(student_objects, key=cmp_to_key(comparator))
for k, g in groupby(data, itemgetter(1)):
    indexes = list(g)
    groups[k] += indexes  # Store group iterator as a list
    uniquekeys.append(k)
print(groups)
print(uniquekeys)
