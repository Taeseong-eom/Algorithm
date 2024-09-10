import sys

def count_prime_factor(x, p):
    count = 0
    while x >= p:
        x //= p
        count += x
    return count

n, m = map(int, sys.stdin.readline().split())

count_twos = count_prime_factor(n, 2) - count_prime_factor(m, 2) - count_prime_factor(n - m, 2)
count_fives = count_prime_factor(n, 5) - count_prime_factor(m, 5) - count_prime_factor(n - m, 5)

print(min(count_twos, count_fives))
