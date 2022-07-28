from array_stack import ArrayStack


def check_parentheses(expr):
    match = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    stack = ArrayStack()

    for c in expr:
        if c in '({[':
            stack.push(c)
        elif c in match:
            if stack.is_empty():
                return False
            else:
                t = stack.pop()
                if t != match[c]:
                    return False

    return stack.is_empty()
