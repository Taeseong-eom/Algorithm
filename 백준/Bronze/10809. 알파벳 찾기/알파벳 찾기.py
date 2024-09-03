word = list(input())  # 사용자로부터 문자열 입력 받음
result = [-1] * 26 
for i in range(len(word)):
    j = ord(word[i]) - 97
    if result[j] == -1:
        result[j] = i
print(*result)
