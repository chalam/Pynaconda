def is_subsequence(pattern, text):
    i = j = 0
    while i < len(text):
        print(pattern[j], text[i])
        if pattern[j] == text[i]:
            if j == len(pattern) - 1:
                return True
            else:
                j += 1
        i += 1

    return False


assert is_subsequence('nano', 'nematode knowledge')
assert not is_subsequence('empty bottle', 'nematode knowledge')
assert is_subsequence('empty bottle', 'nemaptody kbnotwtledge')