import sys
import math

input = sys.stdin.read

def sieve_of_eratosthenes(max_n):
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False  # 0과 1은 소수가 아님

    for i in range(2, int(math.sqrt(max_n)) + 1):
        if is_prime[i]:
            for j in range(i * i, max_n + 1, i):
                is_prime[j] = False
    
    # 홀수 소수만 리스트로 반환
    odd_primes = [i for i in range(3, max_n + 1, 2) if is_prime[i]]
    return is_prime, odd_primes

def find_goldbach_pair(n, is_prime, odd_primes):
    for a in odd_primes:
        if a >= n:  
            break
        b = n - a
        if is_prime[b]: 
            return a, b
    return None

numbers = list(map(int, input().split()))

max_number = max(numbers)

is_prime, odd_primes = sieve_of_eratosthenes(max_number)

for n in numbers:
    if n == 0:
        break
    result = find_goldbach_pair(n, is_prime, odd_primes)
    if result:
        a, b = result
        print(f"{n} = {a} + {b}")
    else:
        print("Goldbach's conjecture is wrong.")
