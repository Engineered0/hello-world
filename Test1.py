def factorial(n):
    """Calculate the factorial of a number."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Get number from user
number = int(input("Enter a number to calculate its factorial: "))

# Calculate and display the factorial
result = factorial(number)
print(f"The factorial of {number} is {result}")
