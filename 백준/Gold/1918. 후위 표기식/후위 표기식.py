instr = list(input())  # 사용자로부터 문자열 입력 받음
stack = []
outstr = ""

for i in instr:
    if i.isalpha():  # 알파벳인 경우 바로 결과 문자열에 추가
        outstr += i
    else:
        if i == '(':  # 여는 괄호는 스택에 push
            stack.append(i)
        elif i == '*' or i == '/':  # 곱셈, 나눗셈 연산자 처리
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                outstr += stack.pop()
            stack.append(i)
        elif i == '+' or i == '-':  # 덧셈, 뺄셈 연산자 처리
            while stack and stack[-1] != '(':
                outstr += stack.pop()
            stack.append(i)
        else:  # 닫는 괄호인 경우
            while stack and stack[-1] != '(':
                outstr += stack.pop()
            stack.pop()  # 여는 괄호 제거
while stack:  # 스택에 남은 연산자를 모두 결과 문자열에 추가
    outstr += stack.pop()

print(outstr)  # 변환된 후위 표기법 출력
