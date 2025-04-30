from collections import deque
import sys
input = sys.stdin.readline

chk_left = ['[', '(']
chk_right = [']', ')']

while(True):
    tmp = input().rstrip()
    if tmp == ".":
        break
    
    s = deque()
    is_balanced = True
    
    for letter in tmp:
        if letter in chk_left:
            s.append(letter)
        elif letter in chk_right:
            if not s:
                is_balanced = False
                break
            top = s.pop()
            if (letter == ']' and top != '[') or (letter == ')' and top != '('):
                is_balanced = False
                break
    
    if is_balanced and not s:
        print("yes")
    else:
        print("no")