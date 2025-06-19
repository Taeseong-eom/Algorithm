def 재귀함수(number):
    if number == M:
        print(*arr)
        return
    for i in range(1, N+1):
        if i in arr:
            continue
        if arr and arr[-1] > i:
            continue
        arr.append(i)
        재귀함수(number+1)
        arr.pop()


N, M = map(int, input().split()) # 입력 자연수 N, M
arr = []

재귀함수(0)