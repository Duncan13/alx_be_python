def perform_operation(num1, num2, operation):
    if operation == 'add':
        print(num1 + num2)
    elif operation == 'subtract':
        print(num1 - num2)
    elif operation == 'multiply':
        print(num1 * num2)
    elif operation == 'divide':
        if num1 == 0 or num2 == 0:
            try:
                return num1 / num2
            except ZeroDivisionError:
                print(0)
        else:
            print(num1/num2)
