"""
TASK
Given an array of N integers, can you find the sum of its elements?
INPUT
The first line contains an integer, N, denoting the size of the array.
The second line contains N space-separated integers representing the array's elements
OUTPUT
Print the sum of the array's element as a single integer.
SAMPLE INPUT
6
1 2 3 4 10 11
SAMPLE OUTPUT
31
"""

import sys

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
# nums = list(map(int, input().split()))
# list = [int(x) for x in raw_input().split(' ')]
print(sum(arr))
