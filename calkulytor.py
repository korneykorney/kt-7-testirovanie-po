def calculate(first, operation, second):
    if operation == '+':
        result = float(first) + float(second)
    elif operation == '-':
        result = float(first) - float(second)
    elif operation == '*':
        result = float(first) * float(second)
    elif operation == '/':
        result = float(first) / float(second)
    elif operation == '^':
        result = float(first) ** float(second)
    else:
        return '\nНекорректный знак операции'
    return f'\nРезультат операции: {int(result)}'

try:
    first = input('Введите первое число: ')
    operation = input('Введите операцию (/, *, +, -, ^): ')
    second = input('Введите второе число: ')
    print(calculate( float(first), operation, float(second) ))
except ZeroDivisionError:
    print('\nНа ноль делить нельзя!')
except ValueError:
    print('\nОшибка ввода числа!')
except KeyboardInterrupt:
    print('\n\nВы вышли из системы')
