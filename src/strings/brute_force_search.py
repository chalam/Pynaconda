def search(text, pattern):
    n = len(text)
    m = len(pattern)

    for i in range(n - m + 1):
        j = 0
        print(text[i+j], pattern[j])
        while j < m and text[i+j] == pattern[j]:
            print(text[i + j], pattern[j])
            j += 1
        if j == m:
            return i
    return -1


if __name__ == '__main__':
    idx = search('sadasda', 'sda')
    print('search: ', idx)
    assert idx == 4
    assert search('sadasda', 'sde') == -1