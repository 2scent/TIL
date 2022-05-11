from array_stack import ArrayStack


def split_tokens(expr):
    tokens = []
    val = 0
    val_processing = False
    for c in expr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            val_processing = True
        else:
            if val_processing:
                tokens.append(val)
                val = 0
            val_processing = False
            tokens.append(c)
    if val_processing:
        tokens.append(val)

    return tokens


def infix_to_postfix(token_list):
    precedences = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    op_stack = ArrayStack()
    postfix_list = []

    for token in token_list:
        if type(token) is int:
            postfix_list.append(token)
            continue

        if token == '(':
            op_stack.push(token)
            continue

        if token == ')':
            t = op_stack.pop()
            while t != '(':
                postfix_list.append(t)
                t = op_stack.pop()
            continue

        while not op_stack.is_empty() and precedences[op_stack.peek()] >= precedences[token]:
            postfix_list.append(op_stack.pop())

        op_stack.push(token)

    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())

    return postfix_list


def postfix_eval(token_list):
    val_stack = ArrayStack()

    for token in token_list:
        if type(token) is int:
            val_stack.push(token)
            continue

        val1 = val_stack.pop()
        val2 = val_stack.pop()

        if token == '*':
            val_stack.push(val2 * val1)
            continue

        if token == '/':
            val_stack.push(val2 / val1)
            continue

        if token == '+':
            val_stack.push(val2 + val1)
            continue

        if token == '-':
            val_stack.push(val2 - val1)
            continue

    return val_stack.pop()


def calculate_postfix(expr):
    tokens = split_tokens(expr)
    postfix = infix_to_postfix(tokens)
    val = postfix_eval(postfix)
    return val
