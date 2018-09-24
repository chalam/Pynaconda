import bisect
import numpy as np
import scipy.interpolate


def interpolate(n, quantity, price):
    found_index = None
    try:
        found_index = quantity.index(n)
    except:
        pass
    if found_index is not None:
        print(found_index)
        return price[found_index]

    # sorted(quantity)
    # sorted(price)

    intervals = zip(quantity, quantity[1:], price, price[1:])
    slopes = [(y2 - y1) / (x2 - x1) for x1, x2, y1, y2 in intervals]

    if n <= quantity[0]:
        return price[0]
    elif n >= quantity[-1]:
        # return price[-1] # default max idx for extraplotation
        # https://en.wikipedia.org/wiki/Extrapolation
        i = bisect.bisect_left(quantity, n)
        if i == len(quantity):
            i -= 1
        # diff_price = price[i - 1] - price[i - 2]
        # diff_qty   = quantity[i] - quantity[i - 1]
        # jump = n / diff_qty
        # new_price = (price[i - 1] - diff_price) * jump
        new_price = price[i-1] +  \
            ((n - quantity[i])/(quantity[i] - quantity[i-1])) * \
            (price[i]-price[i-1])
    else:
        i = bisect.bisect_left(quantity, n) - 1
        new_price = price[i] + slopes[i] * (n - quantity[i])
    # print(new_price, new_price1)

    return new_price

def lerp(x0, y0, x1, y1, x):
    """linear interpolation"""
    return y0 + (x - x0)*((y1 - y0)/(x1 - x0))

print('lerp', lerp(10, 27.32, 25, 23.13, 20))   # 24.526666666666667
print('lerp', lerp(100, 18.00, 500, 15.50, 200))    # 17.375

for n in [20, 125, 200, 300, 700, 2000]:
    quantity = [10, 25, 50, 100, 500]
    price    = [27.32, 23.13, 21.25, 18.00, 15.50]

    print('n: ', n)
    try:
        print('interpolate', interpolate(n, quantity, price))
    except:
        print('Error')

    try:
        y_interp = scipy.interpolate.interp1d(quantity, price, bounds_error=False, fill_value='extrapolate') # lerp outside
        # y_interp = scipy.interpolate.interp1d(quantity, price)  # lerp inside
        print('scipy', y_interp(n))
    except:
        print('Error')

    print('numpy', np.interp(n, quantity, price))
