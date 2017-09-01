import re


# todo: consider adding ability to perform operations on previous answer
def main():
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
    print('Quit\t\t\t: q\n')

    user_input = ''
    while user_input not in ['q', 'quit', 'exit', 'close', 'end']:

        # User is given prompt to enter formula
        user_input = input('Enter an equation: ')

        # Remove whitespace
        user_input = user_input.replace(' ', '')

        # Identify the type of operation and calculate the solution
        solution = ''

        # Check if the user requested to quit
        if user_input in ['q', 'quit', 'exit', 'close', 'end']:
            print('Quitting...')
        else:
            # Otherwise begin processing equation
            solved = False
            equation = user_input
            # equation = '((4^2+1)*6)/(1-6^(3-2)/125^^3+10-6+4/2+2*2+2*2/2)*(((((2.0/4^3/6+1-2^1.0/56)*5)-1)^1.2)/6.7)'
            while not solved:

                # Search for and remove serperfullis parenthesis, e.g. (4.0) -> 4.0
                result = re.search(r'\(-?[\d.]+\)', equation)
                if result is not None:
                    i1, i2 = result.span(0)[:2]
                    # sub_str = re.sub(r'[()]', '', equation[i1: i2])
                    equation = equation[: i1] + equation[i1 + 1: i2 - 1] + equation[i2:]
                    continue

                # Search for simple operations within parenthesis, e.g. (3/4), (3-4)
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
                solution = equation

        print('{:.4f}'.format(float(solution)))


def simple_math(equation):

    # Identify the type of operation and calculate the solution
    answer = ''
    if 'x' in equation:
        parts = equation.split('x')
        answer = float(parts[0]) * float(parts[1])
    if '*' in equation:
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
    main()
    print('Finished')
