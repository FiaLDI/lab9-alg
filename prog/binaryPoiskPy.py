#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import time
import bisect
        
if __name__ == '__main__':
    for i in range(100, 10000, 100):
        a = [j for j in range(i)]
        b = 0
        for o in range(len(a) - 1, 1, -1):
            start = time.perf_counter()
            bisect.bisect_left(a, o)
            end = time.perf_counter()
            b += end-start
        print(f"{b/(i - 3):.10f}")