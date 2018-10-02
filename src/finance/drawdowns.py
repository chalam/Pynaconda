import numpy as np
import pandas as pd
from numpy.lib.stride_tricks import as_strided


def gen_series(n):
    return pd.Series(np.random.randn(n)).cumsum()


def dd_1(ser):
    # naively loop over all possible start and end points
    # O(n^2)
    servals = ser.values
    drawdowns = []
    for end in range(len(servals)):
        for start in range(end):
            drawdowns.append(servals[end] - servals[start])
    return min(min(drawdowns), 0)


def dd_2(ser):
    # only compare each point to the previous running peak
    # O(N)
    running_max = pd.expanding_max(ser)
    cur_dd = ser - runnig_max
    return min(0, cur_dd.min())


anomalies = []
for i in range(100):
    ser = gen_series(1000)
    answers = pd.Series([dd_1(ser), dd_2(ser)])
    diffs = answers - answers[0]
    max_abs_diff = diffs.abs().max()
    if max_abs_diff != 0:
        anomalies.append(ser)

len(anomalies)

# ser = gen_series(10)
# print('n = 10')
# % timeit dd_1(ser)
# % timeit dd_2(ser)
#
# ser = gen_series(100)
# print('n = 100')
# % timeit dd_1(ser)
# % timeit dd_2(ser)
#
# ser = gen_series(1000)
# print ('n = 1000')
# % timeit dd_1(ser)
# % timeit dd_2(ser)
#
# ser = gen_series(10000)
# print ('n = 10000')
# % timeit dd_1(ser)
# % timeit dd_2(ser)

# n = 10
# 10000 loops, best of 3: 31.9 µs per loop
# 10000 loops, best of 3: 125 µs per loop
# n = 100
# 100 loops, best of 3: 3.1 ms per loop
# 10000 loops, best of 3: 123 µs per loop
# n = 1000
# 1 loops, best of 3: 290 ms per loop
# 10000 loops, best of 3: 154 µs per loop
# n = 10000
# 1 loops, best of 3: 33 s per loop
# 1000 loops, best of 3: 441 µs per loop

def dd_3(ser):
    if isinstance(ser, pd.Series):
        ser = ser.values
    running_global_peak = ser[0]
    min_since_global_peak = ser[0]
    running_max_dd = 0
    running_global_peak_id = np.nan
    running_max_dd_peak_id = np.nan
    running_max_dd_trough_id = np.nan

    for i, val in enumerate(ser):
        if val >= running_global_peak:
            running_global_peak = val
            running_global_peak_id = i
            min_since_global_peak = val
        if val < min_since_global_peak:
            min_since_global_peak = val
            if val - running_global_peak <= running_max_dd:
                running_max_dd = val - running_global_peak
                running_max_dd_peak_id = running_global_peak_id
                running_max_dd_trough_id = i
    return (running_max_dd, running_max_dd_peak_id, running_max_dd_trough_id, running_global_peak_id)


anomalies = []
for i in range(100):
    ser = gen_series(1000)
    answers = pd.Series([dd_2(ser), dd_3(ser)[0]])
    diffs = answers - answers[0]
    max_abs_diff = diffs.abs().max()
    if max_abs_diff != 0:
        anomalies.append(ser)


# ser = gen_series(10)
# print('n = 10')
# % timeit dd_2(ser)
# % timeit dd_3(ser)
#
# ser = gen_series(100)
# print('n = 100')
# % timeit dd_2(ser)
# % timeit dd_3(ser)
#
# ser = gen_series(1000)
# print ('n = 1000')
# % timeit dd_2(ser)
# % timeit dd_3(ser)
#
# ser = gen_series(10000)
# print ('n = 10000')
# % timeit dd_2(ser)
# % timeit dd_3(ser)

# n = 100
# 10000 loops, best of 3: 118 µs per loop
# 10000 loops, best of 3: 41.3 µs per loop
# n = 1000
# 10000 loops, best of 3: 159 µs per loop
# 1000 loops, best of 3: 351 µs per loop
# n = 10000
# 1000 loops, best of 3: 436 µs per loop
# 100 loops, best of 3: 2.41 ms per loop


def rolling_dd_using_dd1(ser, win):
    return pd.rolling_apply(ser, win, dd_2, min_periods=0)


def rolling_dd_custom(ser, window):
    index = ser.index
    name = ser.name
    ser = ser.values

    n = len(ser)
    result = np.zeros((n, 4))
    running_global_peak = ser[0]
    min_since_global_peak = ser[0]
    running_max_dd = 0
    running_global_peak_id = np.nan
    running_max_dd_peak_id = np.nan
    running_max_dd_trough_id = np.nan
    for i, val in enumerate(ser):
        if i < window:
            if val >= running_global_peak:
                running_global_peak = val
                running_global_peak_id = i
                min_since_global_peak = val
            if val < min_since_global_peak:
                min_since_global_peak = val
                if val - running_global_peak <= running_max_dd:
                    running_max_dd = val - running_global_peak
                    running_max_dd_peak_id = running_global_peak_id
                    running_max_dd_trough_id = i
            result[i, :] = np.array(
                (running_max_dd,
                 running_max_dd_peak_id,
                 running_max_dd_trough_id,
                 running_global_peak_id)
            )
        else:
            # current window max index is i
            # current window min index is i-window+1
            # possible difficult situations
            # 1) previous running_global_peak falls out of early edge of sample
            prob_1 = result[i - 1, 3] <= i - window
            # 2) previous running_max_peak_id falls out of early edge of sample
            prob_2 = result[i - 1, 1] <= i - window
            if prob_1 or prob_2:
                rolling_window = ser[i - window + 1: i + 1]
                intermed = dd_3(rolling_window)
                result[i, :] = np.array((intermed[0],
                                         intermed[1] + i - window + 1,
                                         intermed[2] + i - window + 1,
                                         intermed[3] + i - window + 1))
            else:
                # the new windowed global peak is straightforward:
                result[i, 3] = i if ser[i] >= ser[result[i - 1, 3]] else result[i - 1, 3]
                # one candidate is previous row's drawdown.  other candidate is from previous row's
                # running_global_peak to the newly entered value
                new_candidate_drawdown = val - ser[result[i - 1, 3]]
                if new_candidate_drawdown <= result[i - 1, 0]:
                    result[i, 0] = new_candidate_drawdown
                    result[i, 1] = result[i - 1, 3]
                    result[i, 2] = i
                else:
                    result[i, 0] = result[i - 1, 0]
                    result[i, 1] = result[i - 1, 1]
                    result[i, 2] = result[i - 1, 2]

    result = result[:, 0]
    result = pd.Series(result, name=name, index=index)
    return result


def windowed_view(x, window_size):
    """Creat a 2d windowed view of a 1d array.

    `x` must be a 1d numpy array.

    `numpy.lib.stride_tricks.as_strided` is used to create the view.
    The data is not copied.

    Example:

    >>> x = np.array([1, 2, 3, 4, 5, 6])
    >>> windowed_view(x, 3)
    array([[1, 2, 3],
           [2, 3, 4],
           [3, 4, 5],
           [4, 5, 6]])
    """
    y = as_strided(x, shape=(x.size - window_size + 1, window_size),
                   strides=(x.strides[0], x.strides[0]))
    return y


def rolling_max_dd_so(x, window_size, min_periods=1):
    """Compute the rolling maximum drawdown of `x`.

    `x` must be a 1d numpy array.
    `min_periods` should satisfy `1 <= min_periods <= window_size`.

    Returns an 1d array with length `len(x) - min_periods + 1`.
    """
    if min_periods < window_size:
        pad = np.empty(window_size - min_periods)
        pad.fill(x[0])
        x = np.concatenate((pad, x))
    y = windowed_view(x, window_size)
    running_max_y = np.maximum.accumulate(y, axis=1)
    dd = y - running_max_y
    return dd.min(axis=1)


def rolling_max_dd_so_wrapped(ser, window_size, min_periods=1):
    vals = ser.values
    rmdd = rolling_max_dd_so(vals, window_size, min_periods)
    return pd.Series(data=rmdd, index=ser.index, name=ser.name)


# ser = gen_series(1000)
# print
# 'n=1000, w=10'
# % timeit
# rolling_dd_using_dd1(ser, 10)
# % timeit
# rolling_dd_custom(ser, 10)
# % timeit
# rolling_max_dd_so_wrapped(ser, 10)
#
# ser = gen_series(1000)
# print
# 'n=1000, w=100'
# % timeit
# rolling_dd_using_dd1(ser, 100)
# % timeit
# rolling_dd_custom(ser, 100)
# % timeit
# rolling_max_dd_so_wrapped(ser, 100)
#
# ser = gen_series(10000)
# print
# 'n=10000, w=100'
# % timeit
# rolling_dd_using_dd1(ser, 100)
# % timeit
# rolling_dd_custom(ser, 100)
# % timeit
# rolling_max_dd_so_wrapped(ser, 100)
#
# ser = gen_series(10000)
# print('n=10000, w=1000')
# % timeit
# rolling_dd_using_dd1(ser, 1000)
# % timeit
# rolling_dd_custom(ser, 1000)
# % timeit
# rolling_max_dd_so_wrapped(ser, 1000)

# n=1000, w=10
# 10 loops, best of 3: 27.4 ms per loop
# 100 loops, best of 3: 12.3 ms per loop
# 1000 loops, best of 3: 209 µs per loop
# n=1000, w=100
# 10 loops, best of 3: 30.3 ms per loop
# 100 loops, best of 3: 10.2 ms per loop
# 1000 loops, best of 3: 1.09 ms per loop
# n=10000, w=100
# 1 loops, best of 3: 299 ms per loop
# 10 loops, best of 3: 118 ms per loop
# 100 loops, best of 3: 11.2 ms per loop
# n=10000, w=1000
# 1 loops, best of 3: 421 ms per loop
# 10 loops, best of 3: 130 ms per loop
# 10 loops, best of 3: 152 ms per loop

anomalies = []
for i in range(100):
    ser = gen_series(1000)
    one = rolling_dd_using_dd1(ser, 50)
    two = rolling_dd_custom(ser, 50)
    three = rolling_max_dd_so_wrapped(ser, 50)
    df = pd.concat([one, two, three], axis=1)
    check = df.sub(df.iloc[:, 0], axis=0).abs().sum(1).max()
    if check > 0:
        anomalies.append(ser)

len(anomalies)