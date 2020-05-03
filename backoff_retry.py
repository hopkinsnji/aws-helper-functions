# Implement backoff/retry logic with a fibunacci backoff timer.

import time
def fib(n):
    # return the n-th number in the Fibonacci sequence
    if n == 0: return 0
    elif n == 1: return 1
    else: return fib(n-1)+fib(n-2)
for retries in range(10):
    try:
        print('do your thing')
        break
    except Exception as e:
        time.sleep(retries)
