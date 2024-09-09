import sys
import math

input = sys.stdin.read

def sieve_of_eratosthenes(max_n):
    # 에라토스테네스의 체를 이용해 max_n까지의 소수를 구함
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
    # n = a + b 형태의 a, b 찾기
    for a in odd_primes:
        if a >= n:  # a가 n보다 크면 더 이상 볼 필요 없음
            break
        b = n - a
        if is_prime[b]:  # b가 소수이면 조건 만족
            return a, b
    return None  # 찾을 수 없는 경우

# 입력 처리
numbers = list(map(int, input().split()))

# 입력 중 가장 큰 수 찾기
max_number = max(numbers)

# 소수 리스트 생성 (입력의 최대값까지)
is_prime, odd_primes = sieve_of_eratosthenes(max_number)

# 출력 처리
for n in numbers:
    if n == 0:
        break
    result = find_goldbach_pair(n, is_prime, odd_primes)
    if result:
        a, b = result
        print(f"{n} = {a} + {b}")
    else:
        print("Goldbach's conjecture is wrong.")
