user_input = ''
while user_input not in ['q', 'quit', 'exit']:
    # User is given prompt to enter formula
    user_input = input('Enter a formula: ')

    # Break the formula up, eg. 2x3, [2, 3]
    if 'x' in user_input:
        parts = user_input.split('x')
        solution = float(parts[0]) * float(parts[1])
    elif '/' in user_input:
        parts = user_input.split('/')
        solution = float(parts[0]) / float(parts[1])
    elif '+' in user_input:
        parts = user_input.split('+')
        solution = float(parts[0]) + float(parts[1])
    elif '-' in user_input:
        parts = user_input.split('-')
        solution = float(parts[0]) - float(parts[1])
    elif '^' in user_input:
        parts = user_input.split('^')
        solution = float(parts[0]) ** float(parts[1])

    print(solution)
