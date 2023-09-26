# Addition operation
def addition(x, y):
    return x + y

# Subtraction operation
def subtraction(x, y):
    return x - y

# Multiplication operation
def multiplication(x, y):
    return x * y

# Division operation
def division(x, y):
    if y == 0:
        return "Division by zero error!"
    return x / y

print("Choose the operation you want to perform.")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:
    choice = input("Enter your choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == '1':
            print("Result:", addition(num1, num2))
        elif choice == '2':
            print("Result:", subtraction(num1, num2))
        elif choice == '3':
            print("Result:", multiplication(num1, num2))
        elif choice == '4':
            print("Result:", division(num1, num2))
        
        continue_calculation = input("Do you want to perform another calculation? (Y/N): ")
        if continue_calculation.upper() != 'Y':
            break
    else:
        print("Invalid input. Please choose 1, 2, 3, or 4.")