from datetime import datetime

def display_current_datetime():
  # Save the current date
  current_date = datetime.datetime.now()
  formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
  print(f"Current date and time: {formatted_datetime}")


def calculate_future_date():
  #Get current date
  current_date = datetime.datetime.now()
  #Get user input for number of days to add
  number_of_days = int(input("Enter the number of days to add to the current date:"))

  #Convert days to be added to date format and assign to variable
  time_to_add = datetime.timedelta(days=number_of_days)
#   Calculate future date
  future_date = current_date + time_to_add
  formatted_future_date = future_date.strftime("%Y-%m-%d")
  print(f"Future date: {formatted_future_date}")

if __name__ == "__main__":
  display_current_datetime()
  calculate_future_date()