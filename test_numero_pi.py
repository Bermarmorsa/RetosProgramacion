
import decimal

def calculate_pi(precision):
  """Calculates Pi to the specified precision using the Chudnovsky formula.

  Args:
    precision: The desired number of decimal places for the result.

  Returns:
    A decimal object representing the calculated value of Pi with the given precision.
  """

  # Initialize the calculation result and accuracy flag
  result = decimal.Decimal(0)
  accuracy_flag = True

  # Chudnovsky formula for pi approximation
  for n in range(precision + 1):
    result += (decimal.Decimal(-1)**n * decimal.Decimal(2*n+1) / decimal.Decimal(2**n))
    if accuracy_flag:
      print(f"Iteration {n+1}: result = {result}")

  return result

# Get user input for desired precision
precision = int(input("Enter the number of decimal places you need: "))

# Calculate Pi and print the result with the specified precision
pi_value = calculate_pi(precision)
print(f"Pi calculated to {precision} decimal places is: {pi_value}")

