__author__ = 'lamuel'

import urllib.request
import urllib.parse

def isPowerOfTwo(n):
    params = urllib.parse.urlencode({"i": "log2(" + str(n) + ")"})
    url = "https://www.wolframalpha.com/input/?" + params
    page = urllib.request.urlopen(url).read().decode('utf-8')
    return page.find('More digits') == -1

print(isPowerOfTwo(8))
print(isPowerOfTwo(6))
print(isPowerOfTwo(16))