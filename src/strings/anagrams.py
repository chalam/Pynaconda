import itertools


def anagrams1(elements):
    return [''.join(perm) for perm in itertools.permutations(elements)]

def anagrams2(elements):
    if len(elements) <= 1:
        return elements
    else:
        tmp = []
        substr = anagrams2(elements[1:])
        print('substr', substr)
        for perm in substr:
        # for perm in anagrams2(elements[1:]):
            for i in range(len(elements)):
                tmp.append(perm[:i] + elements[0:1] + perm[i:])
            print(perm, tmp)
        return tmp

def anagrams3(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in anagrams3(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]

def anagrams4(elements):
    for i in range(1, len(elements)):
        for j in range(len(elements)):
            print(elements[j:j+i])

if __name__ == '__main__':
    print(anagrams1('abc'))
    print(anagrams2('abc'))
    print(list(anagrams3('abc')))
    print(anagrams4('abba'))
