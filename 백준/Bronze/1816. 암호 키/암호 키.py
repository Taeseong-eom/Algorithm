import sys

data = sys.stdin.readlines()

number = int(data[0].strip())

result = []
limit_num = 10**6

for i in data[1:]:
    state = True
    for j in range(2, limit_num + 1):
        if int(i.strip()) % j == 0:
            state = False
            break

    if state:
        result.append("YES")
    else:
        result.append("NO")
    


pr = '\n'.join(result) + '\n'

sys.stdout.write(pr)