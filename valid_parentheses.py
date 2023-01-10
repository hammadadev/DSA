def is_valid(s: str) -> bool:
    stack = []
    match_case = {')': '(', '}': '{', ']': '['}
    for character in s:
        if character in match_case:
            top = stack.pop() if stack else '$'
            if match_case[character] != top:
                return False
        else:
            stack.append(character)
    return not stack  

print(is_valid("{[]}"))    