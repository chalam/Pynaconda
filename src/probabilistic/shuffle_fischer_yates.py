import random

def shuffle(a):
    for i in range(len(a)-1, -1, -1):
        j = random.randint(0, i)
        a[i], a[j] = a[j], a[i]
    return a

if __name__ == '__main__':
    a = [i+100 for i in range(10)]
    print(a)
    print(shuffle(a))