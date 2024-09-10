import math

num = int(input())
facto = list(str(math.factorial(num)))

count = 0
for i in range(len(facto)):
    if int(facto[len(facto)-1-i]) == 0:
        count += 1
    else:
        break

print(count)