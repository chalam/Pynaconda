import math

# https://leetcode.com/articles/maximmum-product-of-three-numbers/


def productTriplets(a):
    """
        Time: O(n^3), Space: O(1)
    :param a:
    :return:
    """
    res = -math.inf
    n = len(a)
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                print(i, j, k, a[i], a[j], a[k])
                if a[i] * a[j] * a[k] > res:
                    res = a[i] * a[j] * a[k]
    return res


def productTriplets2(a):
    """
        Time: O(nlogn), Space: O(nlogn)
        1. All positive;
        2. all negative;
        3. includes positive and negative.
    :param a:
    :return:
    """
    a = sorted(a)
    n = len(a)
    (min1, min2, max3, max2, max1) = (a[0], a[1], a[n-3], a[n-2], a[n-1])
    print(min1, min2, max3, max2, max1)
    return max(max3 * max2 * max1,
               min1 * min2 * max1) # two negatives make a positive  edge case


def productTriplets3(a):
    """
        Time: O(n), Space: O(1)
        scan and keep max 3 and the fist min two negatives.. Same as above. No sort
    :param a:
    :return:
    """
    n = len(a)
    max1 = max2 = max3 = -math.inf
    min1 = min2 = math.inf
    for i in range(n):
        # Invariant: max3 <= max2 <= max1
        if a[i] >= max1:
            # push back max
            max3 = max2
            max2 = max1
            max1 = a[i]
        elif a[i] >= max2:
            max3 = max2
            max2 = a[i]
        elif a[i] >= max3:
            max3 = a[i]

        # Invariant: min1 <= min2
        if a[i] <= min1:
            # push back min
            min2 = min1
            min1 = a[i]
        elif a[i] <= min2:
            min2 = a[i]
    print(min1, min2, max3, max2, max1)
    return max(max3 * max2 * max1,
               min1 * min2 * max1)

if __name__ == '__main__':
    assert productTriplets([10, 3, 5, 6, 20]) == 1200
    assert productTriplets([-10, -3, -5, -6, -20]) == -90
    assert productTriplets([1, -4, 3, -6, 7, 0]) == 168
    assert productTriplets2([10, 3, 5, 6, 20]) == 1200
    assert productTriplets2([-10, -3, -5, -6, -20]) == -90
    assert productTriplets2([1, -4, 3, -6, 7, 0]) == 168
    assert productTriplets3([10, 3, 5, 6, 20]) == 1200
    assert productTriplets3([-10, -3, -5, -6, -20]) == -90
    assert productTriplets3([1, -4, 3, -6, 7, 0]) == 168
