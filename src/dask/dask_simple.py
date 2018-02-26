from dask import delayed
import time
from dask.distributed import Client


@delayed
def inc(x):
    time.sleep(5)
    return x + 1

@delayed
def dec(x):
    time.sleep(3)
    return x - 1

@delayed
def add(x, y):
    time.sleep(7)
    return x + y

# https://github.com/dask/dask-tutorial
if __name__ == '__main__':

    #distribute ?
    client = Client('192.168.1.152:8786')

    # this looks like ordinary code
    x = inc(30)
    y = dec(15)
    total = add(x, y)
    # incx, incy and total are all delayed objects.
    # They contain a prescription of how to execute

    total.visualize()

    # execute all tasks
    a = total.compute()

    print(a)