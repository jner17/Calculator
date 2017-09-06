import re

# Sample equation: ((4^2+1)*6)/(1-6^(3-2)/125^^3+10-6+4/2+2*2+2*2/2)*(((((2.0/4^3/6+1-2^1.0/56)*5)-1)^1.2)/6.7)


def run():
    # Print possible commands and examples
    print('Examples of possible operations')
    print('-' * 31)
    print('Multiplication\t: 2x2')
    print('Division\t\t: 2/2')
    print('Addition\t\t: 2+2')
    print('Subtraction\t\t: 2-2')
    print('Exponetial\t\t: 2^2')
    print('Square Root\t\t: 2^^2')
    print('Cube Root\t\t: 2^^3')
    print('Nth Root\t\t: 2^^N')
    print('Previous Value\t: _ (underscore, e.g. _/5)')
    print('Quit\t\t\t: q\n')

    user_input = ''
    old_value = None
    while user_input not in ['q', 'quit', 'exit', 'close', 'end']:

        # User is given prompt to enter formula
        user_input = input('Enter an equation: ')
        if user_input == '':
            continue

        # Remove whitespace
        user_input = user_input.replace(' ', '')

        # Identify the type of operation and calculate the solution
        solution = ''

        # Add in previous value if needed
        if '_' in user_input:
            if old_value is None:
                print('There is no previous value')
                continue
            else:
                user_input = user_input.replace('_', str(old_value))

        # Check if the user requested to quit
        if user_input in ['q', 'quit', 'exit', 'close', 'end']:
            print('Quitting...')
        else:
            solution = complex_math(user_input)

        old_value = solution
        print('{:.4f}'.format(float(solution)))


def complex_math(complex_equation: str) -> float:
    """
    Takes a chained and or hierarchical equation and computes the answer.\n
    **Examples of Possible Operations**\n
    **====================**\n
    Multiplication: 2x2\n
    Division: 2/2\n
    Addition: 2+2\n
    Subtraction: 2-2\n
    Exponetial: 2^2\n
    Square Root: 2^^2\n
    Cube Root: 2^^3\n
    Nth Root: 2^^N\n

    :param complex_equation: str, e.g. '((4.5-2.3)^2 + 5*6.80) / 10.12'
    :return: solution
    :rtype: float
    """

    # Otherwise begin processing equation
    solved = False
    equation = complex_equation
    while not solved:

        # Search for and remove serperfullis parenthesis, e.g. (4.0) -> 4.0
        result = re.search(r'\(-?[\d.]+\)', equation)
        if result is not None:
            i1, i2 = result.span(0)[:2]
            # sub_str = re.sub(r'[()]', '', equation[i1: i2])
            equation = equation[: i1] + equation[i1 + 1: i2 - 1] + equation[i2:]
            continue

        # Search for simple operations within parenthesis, e.g. (-3/4), (3-4)
        result = re.search(r'\((-?[\d.]+)([+x*/-])(-?[\d.])\)', equation)
        if result is not None:
            i1, i2 = result.span(0)[:2]
            equation = equation[: i1] + simple_math(equation[i1 + 1: i2 - 1]) + equation[i2:]
            continue

        # Search for exponent operations, e.g. 2^2, 27^^3
        result = re.search(r'-?[\d.]+([\^]|\^\^)-?[\d.]+', equation)
        if result is not None:
            i1, i2 = result.span(0)[:2]
            equation = equation[: i1] + simple_math(equation[i1: i2]) + equation[i2:]
            continue

        # Search for multiplication and division operations, e.g. 2x2, 2/3
        result = re.search(r'(-?[\d.]+)([/*x])(-?[\d.]+(?!\^))', equation)
        if result is not None:
            i1, i2 = result.span(0)[:2]
            equation = equation[: i1] + simple_math(equation[i1: i2]) + equation[i2:]
            continue

        # Search for addition and subtraction operations, e.g. 2-1, -4+5
        result = re.search(r'(-?[\d.]+)([+-])(-?[\d.]+(?![*x/^]))', equation)
        if result is not None:
            i1, i2 = result.span(0)[:2]
            equation = equation[: i1] + simple_math(equation[i1: i2]) + equation[i2:]
            continue

        # If there are no more operations break from loop
        solved = True
        solution = float(equation)
        return solution


def simple_math(equation):
    # todo: add docstrings

    # Identify the type of operation and calculate the solution
    answer = ''
    if 'x' in equation:
        parts = equation.split('x')
        answer = float(parts[0]) * float(parts[1])
    elif '*' in equation:
        parts = equation.split('*')
        answer = float(parts[0]) * float(parts[1])
    elif '/' in equation:
        parts = equation.split('/')
        answer = float(parts[0]) / float(parts[1])
    elif '+' in equation:
        parts = equation.split('+')
        answer = float(parts[0]) + float(parts[1])
    elif '^^' in equation:
        parts = equation.split('^^')
        answer = float(parts[0]) ** (1 / float(parts[1]))
    elif '^' in equation:
        parts = equation.split('^')
        answer = float(parts[0]) ** float(parts[1])
    elif '-' in equation:
        parts = re.search(r'(-?[\d.]+)([+-])(-?[\d.]+)', equation)
        answer = float(parts.group(1)) - float(parts.group(3))
        # parts = equation.split('-')
        # answer = float(parts[0]) - float(parts[1])

    return str(answer)

if __name__ == '__main__':
    run()
    print('Finished')
