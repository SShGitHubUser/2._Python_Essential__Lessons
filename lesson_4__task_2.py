""" Урок 4, завдання 2
Напишіть програму-калькулятор, яка підтримує такі операції: додавання, віднімання, множення, ділення
та піднесення до ступеня. Програма має видавати повідомлення про помилку та продовжувати роботу
під час введення некоректних даних, діленні на нуль та зведенні нуля в негативний степінь.
"""

while True:
    print("""Select operation:
     1. Add
     2. Subtract
     3. Multiply
     4. Divide
     5. Power
     6. Exit""")
    operation = input('Enter operation number: ')
    if operation == '6':
        break
    arg_1 = arg_2 = result = None
    try:
        arg_1 = float(input('Enter first argument: '))
    except ValueError:
        print('   Wrong first argument input')
        continue
    try:
        arg_2 = float(input('Enter second argument: '))
    except ValueError:
        print('   Wrong second argument input')
        continue
    if arg_1 is not None and arg_2 is not None:
        if operation == '1':
            result = arg_1 + arg_2
        elif operation == '2':
            result = arg_1 - arg_2
        elif operation == '3':
            result = arg_1 * arg_2
        elif operation == '4':
            try:
                result = arg_1 / arg_2
            except ZeroDivisionError:
                print('   Cannot divide by zero')
                continue
        elif operation == '5':
            try:
                result = arg_1 ** arg_2
            except ZeroDivisionError:
                print('   0 cannot be raised to a negative power')
                continue
        else:
            print('Wrong operation')
        if result:
            print('Result =', result)
