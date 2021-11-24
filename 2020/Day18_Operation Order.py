import LoadInput

debug = False

if debug:
    lines = LoadInput.LoadLines('d18ex.txt')
else:
    lines = LoadInput.LoadLines('d18input.txt')

def parseInput(lines):

    eqs = []
    for line in lines:
        line = line.strip()

        eqs.append(parsEq(line))
    
    return eqs

'''
while there are tokens to be read:
    read a token.
    if the token is a number, then:
        push it to the output queue.
    else if the token is a function then:
        push it onto the operator stack 
    else if the token is an operator then:
        while ((there is an operator at the top of the operator stack)
              and ((the operator at the top of the operator stack has greater precedence)
                  or (the operator at the top of the operator stack has equal precedence and the token is left associative))
              and (the operator at the top of the operator stack is not a left parenthesis)):
            pop operators from the operator stack onto the output queue.
        push it onto the operator stack.
    else if the token is a left parenthesis (i.e. "("), then:
        push it onto the operator stack.
    else if the token is a right parenthesis (i.e. ")"), then:
        while the operator at the top of the operator stack is not a left parenthesis:
            pop the operator from the operator stack onto the output queue.
        /* If the stack runs out without finding a left parenthesis, then there are mismatched parentheses. */
        if there is a left parenthesis at the top of the operator stack, then:
            pop the operator from the operator stack and discard it
        if there is a function token at the top of the operator stack, then:
            pop the function from the operator stack onto the output queue.
/* After while loop, if operator stack not null, pop everything to output queue */
if there are no more tokens to read then:
    while there are still operator tokens on the stack:
        /* If the operator token on the top of the stack is a parenthesis, then there are mismatched parentheses. */
        pop the operator from the operator stack onto the output queue.
exit.
'''
def parsEq(line):

    line = line.replace(' ', '')

    output = []
    operator = []

    for i, c in enumerate(line):
        if c.isnumeric():
            output.append(int(c))
        elif c == '*':
            while len(operator) > 0 and operator[-1] == '+' and operator[-1] != '(':
                output.append(operator.pop())
            operator.append(c)
        elif c == "+":
            while len(operator) > 0 and operator[-1] != '*' and operator[-1] != '(':
                output.append(operator.pop())
            operator.append(c)
        elif c == "(":
            operator.append(c)
        elif c == ")":
            while len(operator) > 0 and operator[-1] != '(':
                output.append(operator.pop())
            
            if len(operator) > 0 and operator[-1] == '(':
                operator.pop()
    
    while operator:
        output.append(operator.pop())
    
    return output

def evalEq(queue):

    stack = []
    for token in queue:

        if token == '+':
            b = stack.pop()
            a = stack.pop()
            stack.append(a+b)
        elif token == '*':
            b = stack.pop()
            a = stack.pop()
            stack.append(a*b)
        else:
            stack.append(token)
    
    ans = stack.pop()
    return ans

eqs = parseInput(lines)

ans = 0
for eq in eqs:
    ans += evalEq(eq)

print(ans)