__author__ = 'lamuel'

import urllib

def isPowerOfTwo(n):
    params = urllib.urlencode({"i": "log2(" + str(n) + ")"})
    url = "https://www.wolframalpha.com/input/?" + params
    page = urllib.urlopen(url).read()
    return page.find('More digits') == -1

print isPowerOfTwo(8)
print isPowerOfTwo(6)
print isPowerOfTwo(16)