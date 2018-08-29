def power(x, n):
    product = 1
    powerseq = x
    while (n > 0):
        if n % 2 == 1:
            product = product * powerseq
        n = n / 2
        powerseq = powerseq * powerseq
    return power

if __name__ == '__main__':
    print(power(6, 10))
    import math
    print(math.pow(6, 10))