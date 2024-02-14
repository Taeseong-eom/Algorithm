N = int(input())  # 피연산자 개수
word = input()
numlist = [0]*N
stack = []

for i in range(N):
    numlist[i] = int(input())

for i in word:
    if 'A' <= i <= 'Z':
        stack.append(numlist[ord(i) - ord('A')])
    else:
        str2 = stack.pop() 
        str1 = stack.pop()
        if i == '+':
            stack.append(str1+str2)
        elif i == '-':
            stack.append(str1-str2)
        elif i == '/':
            stack.append(str1/str2)
        elif i == '*':
            stack.append(str1*str2)

print('%.2f' %stack[0])

