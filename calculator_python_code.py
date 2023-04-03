import os


def multiplication():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Multiplication")

    continue_calc = 'y'

    num1 = float(input("Enter a number: "))
    num2 = float(input('Enter a number: '))
    ans = num1 * num2
    input_values = 2
    print(f'results: {ans}')

    while continue_calc.lower() == 'y':
        continue_calc = (input('Add more values (y/n): '))
        while continue_calc.lower() not in ['y', 'n']:
            print("Please enter 'y' or 'n'")
            continue_calc = (input('Add more values (y/n): '))

        if continue_calc.lower() == 'n':
            break

        num = float(input("Input another number: "))
        ans *= num
        input_values += 1
        print(f'results: {ans}')

    return [ans, input_values]


def addition():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Addition")

    continue_calc = 'y'
    ans = 0
    input_values = 0

    while continue_calc.lower() == 'y':
        num = float(input("Enter a number: "))
        ans += num
        input_values += 1
        print(f'results: {ans}')

        continue_calc = (input('Add more values (y/n): '))
        while continue_calc.lower() not in ['y', 'n']:
            print("Please enter 'y' or 'n'")
            continue_calc = (input('Add more values (y/n): '))

    return [ans, input_values]


def division():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Division')

    continue_calc = 'y'

    num1 = float(input('Enter a number: '))
    num2 = float(input('Enter another number: '))
    while num2 == 0.0:  # Remember the rule that a number divided by 0 (zero) process an infinite error
        print("Please enter a second number > 0")
        num2 = float(input('Enter another number: '))
    ans = num1 / num2
    input_values = 2
    print(f'results: {ans}')

    while continue_calc.lower() == 'y':
        continue_calc = (input('Add more values (y/n): '))
        while continue_calc.lower() not in ['y', 'n']:
            print("Please enter 'y' or 'n'")
            continue_calc = (input('Add more values (y/n): '))

        if continue_calc.lower() == 'n':
            break

        num = float(input("Enter another number: "))
        while num == 0.0:
            print("Please enter a valid number > 0")
            num = float(input("Enter another number: "))
        ans /= num
        input_values += 1
        print(f'results: {ans}')

    return [ans, input_values]

def subtraction():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Subtraction')
    
    continue_calc = 'y'
    
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter another number: "))
    ans = num1 - num2
    input_values = 2
    print(f'results: {ans}')
    
    
    while continue_calc.lower() == 'y':
        continue_calc = (input('Add more values (y/n): '))
        while continue_calc.lower() not in ['y', 'n']:
            print("Please enter 'y' or 'n'")
            continue_calc = (input('Add more values (y/n): '))
        if continue_calc.lower() == 'n':
            break
        num = float(input("Enter another number: "))
        ans -= num
        input_values += 1
        print(f'results: {ans}')
    return [ans, input_values]
    
def calc():
    quit = False
    while not quit:
        results = []
        print('Simple Calculator in Python!')
        print("Enter 'a' for addition")
        print("Enter 's' for subtraction")
        print("Enter 'm' for multiplication")
        print("Enter 'd' for division")
        print("Enter 'q' for quit")
        
        choice = input("Selection: ")
        
        if choice == 'q':
            quit = True
            continue # terminate the calculator 
        
        if choice == 'a':
            results = addition()
            print('Ans = ', results[0], ' total inputs: ', results[1])
            
        elif choice == 'd':
            results = division()
            print('Ans = ', results[0], ' total inputs: ', results[1])
        
        elif choice == 'm':
            results = multiplication()
            print('Ans = ', results[0], ' total inputs: ', results[1])
        
        elif choice == 's':
            results = subtraction()
            print('Ans = ', results[0], ' total inputs: ', results[1])

        else:
            print("Sorry, invalid character")
            
if __name__ == '__main__':
    calc() 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
