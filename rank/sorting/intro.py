"""
TASK
Given a sorted array (ar) and a number (V), can you print the index location
of V in the array
INPUT
There will be three lines of input:
V - the value that has to be searched.
n - the size of the array
ar - n numbers that make up the array
CONSTANTS
1 <= n <= 1000
-1000 <= V <= 1000
Its guaranteed that V will occur in ar exactly once.
OUTPUT
Output the index V in the array
SAMPLE INPUT
4
6
1 4 5 7 9 12
SAMPLE OUTPUT
1
EXPLANATION
V = 4. The  value 4 is the 2nd element in the array, but its index is 1 since array indices start from 0, so the
answer is 1.
"""
V = int(input().strip())
N = int(input().strip())
nums = list(map(int, input().split()))
print(nums.index(V))









