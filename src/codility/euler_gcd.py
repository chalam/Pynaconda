def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def gcd2(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def gcd3(a, b):

    return
if __name__ == '__main__':
    print(gcd(30, 18))
    print(gcd2(30, 18))
    print(gcd(18, 30))
    import math
    print(math.gcd(18, 30))