#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import time

def binary_poisk(array, target):
    """
    Функция бинароного поиска.
    """
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
    """
    Главная функция программы.
    """
    for size_of_list in range(100, 1000, 100):
        list_of_nums = [j for j in range(size_of_list)]
        time_full = 0

        for desired_element in range(len(list_of_nums) - 1, 1, -1):
            time_start = time.perf_counter()
            find_element = binary_poisk(list_of_nums, desired_element)
            time_end = time.perf_counter()
            time_full += time_end-time_start

        print(f"{time_full/(size_of_list - 3):.10f}")
 
if __name__ == '__main__':
    main()