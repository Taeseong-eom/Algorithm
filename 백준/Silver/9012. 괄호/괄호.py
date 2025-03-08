import sys

data = sys.stdin.readlines()

num = int(data[0])

result = []

for i in data[1:]:
    stack = []
    YN = True

    for j in i.strip():
        if j == '(':
            stack.append(j)
        else:
            if stack:
                stack.pop()
            else:
                YN = False
                break
    if YN and not stack:
        result.append("YES")
    else:
        result.append("NO")
    
sys.stdout.write('\n'.join(result)+'\n')