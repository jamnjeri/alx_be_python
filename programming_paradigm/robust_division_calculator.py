def safe_divide(numerator,denominator):  
  try:
    number1 = float(numerator)
    number2 = float(denominator)
    
    result = number1 / number2
    return f"The result of the division is {result}"
  except ValueError:
    return("Error: Please enter numeric values only.")
  except ZeroDivisionError:
    return("Error: Cannot divide by zero.")
    
