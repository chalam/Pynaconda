import string

s = 'hello'
print(set(s.lower()))
print(sorted(set(set(string.ascii_lowercase).difference(s.lower()))))
print(''.join(sorted(set(set(string.ascii_lowercase).difference(s.lower())))))
