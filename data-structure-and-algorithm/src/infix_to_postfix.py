from array_stack import ArrayStack

precedences = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}


def infix_to_postfix(expr):
    op_stack = ArrayStack()

    result = ''

    for c in expr:
        if c not in '*/+-()':
            result += c
            continue

        if c == '(':
            op_stack.push(c)
            continue

        if c == ')':
            t = op_stack.pop()
            while t != '(':
                result += t
                t = op_stack.pop()
            continue

        while not op_stack.is_empty() and precedences[op_stack.peek()] >= precedences[c]:
            result += op_stack.pop()

        op_stack.push(c)

    while not op_stack.is_empty():
        result += op_stack.pop()

    return result
