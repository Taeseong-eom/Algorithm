import sys
li = list(map(int, sys.stdin.readline().split()))

print((li[0]+li[1])%li[2])
print(((li[0]%li[2]) + (li[1]%li[2]))%li[2])
print((li[0]*li[1])%li[2])
print(((li[0]%li[2]) * (li[1]%li[2]))%li[2])