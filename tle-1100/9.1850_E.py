import sys
from collections import defaultdict, deque
import itertools
from heapq import heappush, heappop
from math import gcd, sqrt


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
def solve(a,b,c,mid):
    return a*mid*mid + b*mid + c 

# Example problem solving function
def solve_problem():
    n, m = read_ints()
    arr = read_ints()
    sq_sum = 0
    su = sum(arr)
    for val in arr:
        sq_sum+=val**2
    a = 4*n 
    b = 4*su
    c = sq_sum 
    left = 0
    right = 1e9
    while left<=right:
        mid = left + (right-left)//2
        val = solve(a,b,c,mid)
        if(val>m):
            right = mid -1 
        else:
            left = mid + 1

  
   

    #print(left, right)
    if(solve(a,b,c,int(left))-m<1):
        print(int(left))
    else:
        print(int(right))
# To run the main function automatically
if __name__ == "__main__":
    main()


