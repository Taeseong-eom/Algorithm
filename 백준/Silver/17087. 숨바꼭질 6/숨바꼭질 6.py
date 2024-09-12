import math
from functools import reduce

def find_max_d(N, S, A):
    diff = [abs(a - S) for a in A]
    
    max_d = reduce(math.gcd, diff)
    
    return max_d

N, S = map(int, input().split())
A = list(map(int, input().split()))

result = find_max_d(N, S, A)

print(result)
