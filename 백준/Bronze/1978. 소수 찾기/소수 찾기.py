import sys
import math

def is_prime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    
N = int(input())  # 데이터 수
numbers = list(map(int, input().split())) 

result = 0

for i in numbers:    
    if is_prime(i):
        result += 1

print(result)
