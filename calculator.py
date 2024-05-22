def calculate(num1, num2, operator):
  """Calculates based on operator (+, -, *, /). Handles division by zero."""
  if operator == "+":
    return num1 + num2
  elif operator == "-":
    return num1 - num2
  elif operator == "*":
    return num1 * num2
  elif operator == "/":
    if num2 == 0:
      return "Error: Cannot divide by zero"
    else:
      return num1 / num2
  else:
    return "Error: Invalid operator"

def get_number(prompt):
  """Gets a valid number from the user."""
  while True:
    try:
      num = float(input(prompt))
      return num
    except ValueError:
      print("Invalid input. Enter a number.")

def get_operation():
  """Gets a valid operation (+, -, *, /) from the user."""
  while True:
    operator = input("Select operation (+, -, *, /): ")
    if operator in "+-*/":
      return operator
    else:
      print("Invalid operator. Enter +, -, *, or /.")

def main():
  """Runs the calculator program."""
  print("Welcome to the calculator!")

  while True:
    # Get numbers and handle invalid input
    num1 = get_number("Enter first number: ")
    if num1 is None:
      continue
    num2 = get_number("Enter second number: ")
    if num2 is None:
      continue

    # Get operation and handle invalid input
    operator = get_operation()
    if operator is None:
      continue

    # Perform calculation and display result
    result = calculate(num1, num2, operator)
    print(f"{num1} {operator} {num2} = {result}")

    # Ask user if they want to continue
    choice = input("Do you want to perform another calculation? (y/n): ")
    if choice.lower() != 'y':
      break

  print("Thank you for using the calculator!")

if __name__ == "__main__":
  main()
