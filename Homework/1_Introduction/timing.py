import time

from matplotlib import pyplot as plt


def timed(f, *args, n_iter=10):
    acc = float("inf")
    for i in range(n_iter):
        t0 = time.perf_counter()
        f(*args)
        acc = min(acc, time.perf_counter() - t0)

    return acc


def compare(fs, args, isOneArgs = True):
    xs = list(range(len(args)))
    for f in fs:
        if isOneArgs == True:
            plt.plot(xs, [timed(f, chunk) for chunk in args],label=f.__name__)
        else:
            plt.plot(xs, [timed(f, *chunk) for chunk in args],label=f.__name__)
    plt.legend()
    plt.grid(True)