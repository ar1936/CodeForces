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

def solve(mid, arr):
    s = 0
    for val in arr:
        if val>=mid:
            break
        s += mid - val
    return s

# Example problem solving function
def solve_problem():
    # Example: Return sum of the array and the length of the string
    n, t = read_ints()
    arr = read_ints()
    arr = sorted(arr)
    ans = [] 
    low , high = 0, 1e10
    while low<=high:
        mid = low + (high-low)//2
        s = solve(mid, arr)
        if t>=s:
            ans.append((s, mid))
        if(s<=t):
            low = mid + 1
        else:
            high = mid - 1
    ans = sorted(ans)
    #print(ans)
    print(int(ans[-1][1]))    

# To run the main function automatically
if __name__ == "__main__":
    main()


