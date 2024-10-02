import sys                           # For fast input/output handling
import itertools                     # For efficient looping and combinatorial functions
import bisect                        # For binary search and sorted insertions
from collections import defaultdict, deque  # For efficient dictionaries and double-ended queues
from heapq import heappush, heappop   # For priority queues (min-heaps)
from math import gcd, sqrt, factorial, log, ceil, floor  # For various mathematical functions
from functools import lru_cache  

# Fast input setup
# input = sys.stdin.read
input = sys.stdin.readline  # if you want to read input line by line
sys.setrecursionlimit(10**6)

# Constants
INF = float('inf')
MOD = 10**9 + 7

# Utility function to read space-separated integers
def read_ints():
    return list(map(int, input().split()))

# To read a single integer
def read_int():
    return int(input().strip())

# To read a string
def read_string():
    return input().strip()

# To read a list of space-separated strings
def read_strings():
    return input().split()

# To read a list of characters from a single string
def read_chars():
    return list(input().strip())

# To read a grid of integers
def read_int_grid(n):
    return [list(map(int, input().split())) for _ in range(n)]

# To read a grid of characters
def read_char_grid(n):
    return [list(input().strip()) for _ in range(n)]

# Main function template for competitive programming
def main():
    # Example: Number of test cases
    t = int(input().strip())
    for _ in range(t):
        solve_problem()

# Example problem solving function
def solve_problem():
    n = read_int()
    arr = read_ints()
    ans = [0] * n
    sorted_arr = sorted(arr)
    pre_sum_arr = list(sorted_arr)
    for i in range(1,n):
        pre_sum_arr[i]+=pre_sum_arr[i-1]
    
    ind = 0
    s = 0 
    for i in range(n):
        ind = bisect.bisect_right(sorted_arr,arr[i]) -1 
        j = ind
        s = pre_sum_arr[ind]
        while ind<n:
            prev_ind = ind
            ind = bisect.bisect_right(sorted_arr,s)-1
            s = pre_sum_arr[ind]
            if ind == prev_ind:
                break
        ans[i] = ind
    
    print(' '.join(map(str, ans)))

# To run the main function automatically
if __name__ == "__main__":
    main()


