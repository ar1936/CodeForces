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
    n = read_int()
    arr = read_ints()
    possible_ans = []
    i = 0
    j = n-1
    while i<=j:
        if arr[i] != arr[j]:
            possible_ans.append(abs(arr[i]-arr[j]))
        i+=1
        j-=1
        
    possible_ans = set(possible_ans)
    possible_ans = sorted(possible_ans)
    possible_ans = possible_ans[::-1]
    if(len(possible_ans)==0):
        print(0)
        return 
    #print("possible => ", possible_ans)
    ans = 0
    for possible in possible_ans:
        ans = gcd(ans,possible)
    print(ans)



# To run the main function automatically
if __name__ == "__main__":
    main()


