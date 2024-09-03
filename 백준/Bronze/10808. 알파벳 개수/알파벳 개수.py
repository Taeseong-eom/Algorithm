word = list(input())  # 사용자로부터 문자열 입력 받음
result = [0] * 26 
for i in word:
    j = ord(i) - 97
    result[j] += 1
print(*result)
