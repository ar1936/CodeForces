import sys
from collections import defaultdict, deque
import itertools
from heapq import heappush, heappop
from math import gcd

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
    # Example: Return sum of the array and the length of the string
    n, m = read_ints()
    arr = read_ints()
    arr = sorted(arr)
    pre_sum = [0]*(n+1)
    for i in range(1, n+1):
        pre_sum[i] = pre_sum[i-1] + arr[i-1]
    
    ans = 0 
    for i in range(0, m+1):
        ans = max(ans , pre_sum[-1-m+i] - pre_sum[2*i])
    print(ans)

# To run the main function automatically
if __name__ == "__main__":
    main()


