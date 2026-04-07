def calculate_rpn(expression):
	stack = []

	operations = {
		'+': lambda x, y: x + y,
		'*': lambda x, y: x * y,
		'-': lambda x, y: x - y,
		'/': lambda x, y: x // y,
		'%': lambda x,y : x % y
	}

	for token in expression.split():
		if token in operations:
			b = stack.pop()
			a = stack.pop()

			result = operations[token](a, b)
			stack.append(result)
		else:
			stack.append(int(token))
	return stack[0]

exp = input()
print(calculate_rpn(exp))