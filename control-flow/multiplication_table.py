X = int(input("Enter a number to see its multiplication table:"))

for Y in range(0,10):
  print(f"{X} * {Y+1} = {X * (Y+1)}")