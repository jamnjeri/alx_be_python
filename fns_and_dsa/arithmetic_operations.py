def perform_operation(num1, num2, operation):
  match (operation):
   case "add":
     sum = num1 + num2
     return sum
   case "subtract":
     difference = num1 - num2
     return difference
   case "multiply":
     product = num1 * num2
     return product
   case "divide":
     if(num2 == 0):
       return "Sorry, no number is divisible by 0"
     else:
       result = num1 / num2
       return result