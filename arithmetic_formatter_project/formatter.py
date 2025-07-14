def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    top_line = []
    bottom_line = []
    dash_line = []
    answer_line = []

    for problem in problems:
        parts = problem.split()
        left = parts[0]
        operator = parts[1]
        right = parts[2]

        if operator not in ['+', '-']:
            return 'Error: Operator must be \'+\' or \'-\'.'
        elif not left.isdigit() or not right.isdigit():
            return 'Error: Numbers must only contain digits.'
        elif len(left) > 4 or len(right) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        width = max(len(left), len(right)) + 2
        top_line.append(left.rjust(width))
        bottom_line.append(operator + right.rjust(width - 1))
        dash_line.append('-' * width)

        if show_answers:
            if operator == '+':
                result = int(left) + int(right)
            else:
                result = int(left) - int(right)
            answer_line.append(str(result).rjust(width))

    arranged_result = '    '.join(top_line) + '\n' + \
                      '    '.join(bottom_line) + '\n' + \
                      '    '.join(dash_line)

    if show_answers:
        arranged_result += '\n' + '    '.join(answer_line)

    return arranged_result
