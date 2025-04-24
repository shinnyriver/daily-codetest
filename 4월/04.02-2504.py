s = input()
stack = []

for char in s:
    if char == '(' or char == '[':
        stack.append(char)
    else:
        if not stack:
            print(0)
            exit()
            
        if char == ')':
            if stack[-1] == '(':    #직전이 괄호를 완성할경우
                stack.pop()
                stack.append(2)     #값을 추가
            elif isinstance(stack[-1], int):    #직전이 숫자일 경우
                temp = 0
                while stack and isinstance(stack[-1], int):
                    temp += stack.pop()
                if stack and stack[-1] == '(':
                    stack.pop()
                    stack.append(temp * 2)
                else:
                    print(0)
                    exit()
            else:
                print(0)
                exit()
        else:  # char == ']'
            if stack[-1] == '[':
                stack.pop()
                stack.append(3)
            elif isinstance(stack[-1], int):
                temp = 0
                while stack and isinstance(stack[-1], int):
                    temp += stack.pop()
                if stack and stack[-1] == '[':
                    stack.pop()
                    stack.append(temp * 3)
                else:
                    print(0)
                    exit()
            else:
                print(0)
                exit()

result = 0
for num in stack:   #마지막 체크, 스택에 숫자만 있다면 정상 문자열
    if isinstance(num, int):
        result += num
    else:   #스택에 괄호가 있다면 잘못된 문자열
        print(0)
        exit()

print(result)