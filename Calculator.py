
# Print possible commands and examples
print('Examples of possible operations')
print('-'*31)
print('Multiplication\t: 2x2')
print('Division\t\t: 2/2')
print('Addition\t\t: 2+2')
print('Subtraction\t\t: 2-2')
print('Exponetial\t\t: 2^2')
print('Square Root\t\t: 2^^2')
print('Cube Root\t\t: 2^^3')
print('Nth Root\t\t: 2^^N')
print('Quit\t\t\t: q\n')

user_input = ''
while user_input not in ['q', 'quit', 'exit']:

    # User is given prompt to enter formula
    user_input = input('Enter an equation: ')

    # Break the formula up, eg. 2x3, [2, 3]

    solution = ''
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
    elif '^^' in user_input:
        parts = user_input.split('^^')
        solution = float(parts[0]) ** (1 / float(parts[1]))
    elif '^' in user_input:
        parts = user_input.split('^')
        solution = float(parts[0]) ** float(parts[1])
    elif user_input in ['q', 'quit', 'exit']:
        print('Quitting...')
    else:
        print('Invalid Response!')

    print(solution)
