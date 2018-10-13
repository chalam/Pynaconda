
def get_all_substrings(s):
    l = []
    n = len(s)
    for i in range(1, n+1):  # length of substr
        for start in range(n) : # start idx
            end = start + i
            if end <= n:
                print(start, end, s[start:end])
                l.append(s[start:end])
    print('len', len(l))
    return l

def get_all_substrings2(input_string):
  length = len(input_string)
  return [input_string[i:j+1] for i in range(length) for j in range(i,length)]

s = 'abcde'
print(get_all_substrings(s))
print(get_all_substrings2(s))