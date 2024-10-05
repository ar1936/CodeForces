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
    n, t, a, b = read_ints()  # Corrected: added whitespace after ','

    cities = []
    for i in range(n):
        x, y = read_ints()  # Corrected: added whitespace after ','
        cities.append((x, y))  # Corrected: added whitespace after ','

    ans = (abs(cities[a - 1][0] - cities[b - 1][0]) + 
           abs(cities[a - 1][1] - cities[b - 1][1]))  # Line split to meet 79 character limit

    # Uncomment for debugging:
    # print(n, t, a, b)  # Corrected: block comment with space after '#'

    mn1 = 1e18
    mn2 = 1e18

    for i in range(t):
        mn1 = min(mn1, (abs(cities[a - 1][0] - cities[i][0]) + 
                        abs(cities[a - 1][1] - cities[i][1])))  # Line split to meet 79 character limit
        mn2 = min(mn2, (abs(cities[b - 1][0] - cities[i][0]) + 
                        abs(cities[b - 1][1] - cities[i][1])))  # Line split to meet 79 character limit

    # Uncomment for debugging:
    # print("min_value =>", mn1, mn2)  # Corrected: block comment with space after '#'

    print(min(mn1 + mn2, ans))  # Corrected: removed trailing whitespace



# To run the main function automatically
if __name__ == "__main__":
    main()


