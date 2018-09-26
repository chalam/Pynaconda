# import urllib.parse
# import urllib.request

# def isPowerOfTwo_wolfram(n):
#     params = urllib.parse.urlencode({"i": "log2(" + str(n) + ")"})
#     url = "https://www.wolframalpha.com/input/?" + params
#     page = urllib.request.urlopen(url).read().decode('utf-8')
#     return page.find('More digits') == -1   ## Need JS browser

# assert isPowerOfTwo_wolfram(8)
# assert not isPowerOfTwo_wolfram(6)
# assert isPowerOfTwo_wolfram(16)
from math import ceil, floor, log2

def isPowerOfTwo_bit(n):
    return n != 0 and (n & (n - 1) == 0)

def isPowerOfTwo_log(n):
    # python log is not accurate, use log2
    log_val = log2(n)
    return ceil(log_val) == floor(log_val)

def isPowerOfTwo_div(n):
    if n == 0:
        return False
    while n > 0 and n % 2 == 0:
        n /= 2
    return n == 1

doPass = True
powersOf10 = [1, 2, 4, 8, 16 ,32, 64, 128]
notPowersOf10 = [5, 390, 12, 144, 12, 50, 17]

for n in powersOf10:
    if not isPowerOfTwo_bit(n):
        print("Failed for " + str(n) + "\n")
        doPass = False
    if not isPowerOfTwo_log(n):
        print("Failed for " + str(n) + "\n")
        doPass = False
    if not isPowerOfTwo_div(n):
        print("Failed for " + str(n) + "\n")
        doPass = False


for n in notPowersOf10:
    if isPowerOfTwo_bit(n):
        print("Failed for " + str(n) + "\n")
        doPass = False
    if isPowerOfTwo_log(n):
        print("Failed for " + str(n) + "\n")
        doPass = False
    if isPowerOfTwo_div(n):
        print("Failed for " + str(n) + "\n")
        doPass = False

if doPass:
    print("All tests pass\n")
