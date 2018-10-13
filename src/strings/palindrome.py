def is_palindrome(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

def is_palindrome_recur(s):
    if len(s) <= 1: # single or no char
        return True
    else:
        return s[0] == s[-1] and is_palindrome_recur(s[1:-1])

print('', is_palindrome(''))
print('abc', is_palindrome('abc'))
print('civic', is_palindrome('civic'))
print('racecar', is_palindrome('racecar'))
print('aibohphobia', is_palindrome('aibohphobia')) # fear of palindromes
print('caustrophobia', is_palindrome('caustrophobia'))

print('', is_palindrome_recur(''))
print('abc', is_palindrome_recur('abc'))
print('civic', is_palindrome_recur('civic'))
print('racecar', is_palindrome_recur('racecar'))
print('aibohphobia', is_palindrome_recur('aibohphobia')) # fear of palindromes
print('caustrophobia', is_palindrome_recur('caustrophobia'))
