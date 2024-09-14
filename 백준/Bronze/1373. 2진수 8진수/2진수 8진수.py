ejin = input().strip()

# 이진수를 십진수로 변환
sibjin = int(ejin, 2)

result = oct(sibjin)[2:]

print(result)