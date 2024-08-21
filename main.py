def calculator():
    print('Choose the option')
    print('1. Addition')
    print('2. Substraction')
    print('3. Multiplication')
    print('4. Division')

    choice = input("Select an option (1/2/3/4: ")

    num1 = float(input('Enter first number: '))
    num2 = float(input('Enter second number: '))

    if choice == '1':
        print(f'Result: {num1 + num2}')
    elif choice == '2':
        print(f'Result: {num1 - num2}')
    elif choice == '3':
        print(f'Result: {num1 * num2}')
    elif choice == '4':
        if num2 != 0:
            print(f'Result: {num1 / num2}')
        else:
            print('ERROR: You cannot divide by zero!')
    else:
        print('Choose correct option')
calculator()