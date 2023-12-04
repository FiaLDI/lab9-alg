#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import bisect


def main():
    """
    Главная функция программы.
    """
    for size_of_list in range(100, 10000, 100):
        list_of_nums = [j for j in range(size_of_list)]
        time_full = 0

        for desired_element in range(len(list_of_nums) - 1, 1, -1):
            time_start = time.perf_counter()
            bisect.bisect_left(list_of_nums, desired_element)
            time_end = time.perf_counter()
            time_full += time_end - time_start
        
        print(f"{time_full/(size_of_list - 3):.10f}")
        
if __name__ == '__main__':
    main()