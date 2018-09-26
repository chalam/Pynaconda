from math import ceil, floor, log10

def isPowerOfTen_log(n):
    # python log is not accurate, use log10

    log_val = log10(n)
    return ceil(log_val) == floor(log_val)

def isPowerOfTen_div(n):
    if n == 1:
        return True
    while n > 1 and n % 10 == 0:
        n /= 10
    return n == 1


doPass = True
powersOf10 = [1, 10, 100, 1000, 10000]
notPowersOf10 = [5, 390, 12, 144]

for n in powersOf10:
    if not isPowerOfTen_log(n):
        print("Failed for " + str(n) + "\n")
        doPass = False
    if not isPowerOfTen_div(n):
        print("Failed for " + str(n) + "\n")
        doPass = False


for n in notPowersOf10:
    if isPowerOfTen_log(n):
        print("Failed for " + str(n) + "\n")
        doPass = False
    if isPowerOfTen_div(n):
        print("Failed for " + str(n) + "\n")
        doPass = False

if doPass:
    print("All tests pass\n")
