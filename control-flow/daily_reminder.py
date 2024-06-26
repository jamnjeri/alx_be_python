task = input("Enter your task:")

priority = input("Priority (high/medium/low):").lower()

time_sensitivity =input("Is it time-bound? (yes/no):").lower()

match priority:
  case "high":
    result = f"'{task}' is a high priority task"
  case "medium":
    result = f"'{task}' is a medium priority task"
  case "low":
    result = f"'{task}' is a low priority task"
  case _:
    result = f"'{task}' has an unspecified priority"

if time_sensitivity == "yes":
  result += " that requires immediate attention today!"
  print("Reminder:", result)
elif time_sensitivity == 'no':
  result += ". Consider completing it when you have free time."
  print("Note:", result)
else:
  result += ". (Time-bound status unspecified)"
  print("Note:", result)