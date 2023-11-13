#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import time

def binary_poisk(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

def main():
    for i in range(1000000, 10000000, 1000000):
        a = [j for j in range(i)]
        b = 0
        for o in range(len(a) - 1, 1, -1):
            start = time.perf_counter()
            r = binary_poisk(a, o)
            end = time.perf_counter()
            b += end-start
        print(f"{b/(i - 3):.10f}")

        
if __name__ == '__main__':
    main()