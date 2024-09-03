import sys

while True:
    text = sys.stdin.readline().rstrip("\n")

    if not text: # 입력된 라인이 없으면 루트 탈출
        break

    low, up, digi, space = 0, 0, 0, 0

    for i in text:
        if i.islower():
            low += 1
        elif i.isupper():
            up += 1
        elif i.isdigit():
            digi += 1
        elif i.isspace():
            space += 1
    print(low,  up, digi, space)