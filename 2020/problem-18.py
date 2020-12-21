def ex(op, a, b):
    if op == '+':
        return a + b
    elif op == '*':
        return a * b
    return NotImplementedError

def eval(expr, prec):
    literals = []
    operators = []
    expr = expr.replace('(', '( ').replace(')', ' )')
    for token in expr.split():
        if str.isdigit(token):
            literals.append(int(token))
            continue
        if token == '(' or len(operators) == 0:
            operators.append(token)
            continue
        while len(operators) > 0 and prec[token] <= prec[operators[-1]]:
            if operators[-1] == '(':
                break
            op = operators.pop()
            a = literals.pop()
            b = literals.pop()
            literals.append(ex(op, a, b))
        if token == ')':
            if len(operators) == 0 or operators[-1] != '(':
                raise ValueError
            operators.pop()
        else:
            operators.append(token)
    while len(operators) > 0:
        literals.append(ex(operators.pop(), literals.pop(), literals.pop()))
    assert len(literals) == 1 and len(operators) == 0
    return literals.pop()

p1 = p2 = 0
with open('input/input-18.txt') as f:
    for expr in f:
        p1 += eval(expr, {'+': 1, '*': 1, '(': 0, ')': 0})
        p2 += eval(expr, {'+': 2, '*': 1, '(': 0, ')': 0})
print("part 1:", p1)
print("part 2:", p2)
