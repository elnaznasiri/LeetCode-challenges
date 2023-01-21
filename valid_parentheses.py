def isValid(s):
    stack = []
    lookup={")":"(",
        "}":"{",
        "]":"["
        }
    for i in s:
        if i in lookup.values():
            stack.append(i)
        elif stack and lookup[i] == stack[-1]:
            stack.pop()
        else:
            return False
    return stack == []

print(isValid("()"))