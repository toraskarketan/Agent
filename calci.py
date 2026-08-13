import sys
import math

def get_number(prompt):
    """Prompts the user for a number and validates the input."""
    while True:
        try:
            user_input = input(prompt).strip()
            if user_input.lower() == 'exit':
                print("Exiting the calculator. Goodbye!")
                sys.exit(0)
            return float(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid numerical value (or type 'exit' to quit).")

def get_operator():
    """Prompts the user for an operator and validates it."""
    valid_operators = ['+', '-', '*', '/', '^']
    while True:
        operator = input("Enter an operator (+, -, *, /, ^) or 'exit': ").strip()
        if operator.lower() == 'exit':
            print("Exiting the calculator. Goodbye!")
            sys.exit(0)
        if operator in valid_operators:
            return operator
        print(f"Invalid operator. Please choose from: {', '.join(valid_operators)}")

def calculate(num1, operator, num2):
    """Performs the calculation based on the operator and operands."""
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            raise ZeroDivisionError("Error: Division by zero is undefined.")
        return num1 / num2
    elif operator == '^':
        # Handle potential math domain errors (e.g., negative base with fractional exponent)
        try:
            return math.pow(num1, num2)
        except ValueError:
            raise ValueError("Error: Math domain error (e.g., negative base with fractional exponent).")
        except OverflowError:
            raise OverflowError("Error: Result is too large (overflow).")

def main():
    print("========================================")
    print("       Command-Line Calculator          ")
    print("========================================")
    print("Type 'exit' at any prompt to quit.\n")

    while True:
        try:
            num1 = get_number("Enter the first number: ")
            operator = get_operator()
            num2 = get_number("Enter the second number: ")

            result = calculate(num1, operator, num2)

            # Format result to avoid trailing zeros for integers
            if result.is_integer():
                formatted_result = int(result)
            else:
                formatted_result = result

            print(f"\nResult: {num1} {operator} {num2} = {formatted_result}\n")
            print("-" * 40)

        except (ZeroDivisionError, ValueError, OverflowError) as e:
            print(f"\n{e}\n")
            print("-" * 40)
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Exiting. Goodbye!")
            sys.exit(0)
