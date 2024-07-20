# Intro to Python Tasks

## Task 0. Basic Arithmetic Exercise
#### Objective: To practice basic arithmetic operations in Python by performing predefined calculations.

#### Task Description:

You are required to complete a Python script that performs basic arithmetic operations with two predefined numbers. The script should do the following:

1. Assign specific values to two variables, number1 and number2.
2. Perform addition, subtraction, and multiplication on these numbers.
3. Print the results of these operations in a human-readable format.

#### Instructions:
- Create a file named basic_operations.py.
- In this file, you will define two variables: number1 and number2, with the values 10 and 5, respectively.
- You do not need to write any functions or import any modules.
- Calculate the sum, difference (by subtracting number2 from number1), and product of number1 and number2.
- Print the results of each operation in the format: [operation] of [number1] and [number2] is [result].

#### Expected Output:
When executed, your script should print the following (assuming number1 = 10 and number2 = 5):

How to execute
`python3 basic_operations.py`
Here is the outcome
```
Addition of 10 and 5 is 15
Subtraction of 10 and 5 is 5
Multiplication of 10 and 5 is 50
```

## Task 1. Simple Interest Calculator 
#### Objective: Apply basic Python arithmetic operations and variable assignments to calculate the simple interest on a given principal amount, rate of interest, and time.

#### Task Description:

Your task is to complete a Python script that calculates the simple interest earned on an investment over a period of time. The formula for simple interest is (I = P * R * T), where:
- ( I ) is the interest earned,
- ( P ) is the principal amount (initial investment),
- ( R ) is the annual interest rate (as a decimal),
- ( T ) is the time the money is invested for in years.

#### Instructions:
- Create a file named simple_interest.py.
- Define three variables in this file:
- principal with a value of 1000 (representing $1000),
- rate with a value of 0.05 (representing 5% annual interest rate),
- time with a value of 3 (representing 3 years).
- Calculate the simple interest using the formula provided and store the result in a variable named interest.
- Print the calculated interest in a format: The simple interest is: [interest].

#### Expected Output:
When executed, your script should print the simple interest calculated with the provided values. For principal = 1000, rate = 0.05, and time = 3, the output should be:
```
The simple interest is: 150.0
```


## Task 2. Calculate the Area of a Rectangle
#### Objective: Use basic Python arithmetic operations and variable assignments to calculate the area of a rectangle using its length and width.

#### Task Description:
For this task, you are to write a Python script that calculates the area of a rectangle. The area of a rectangle is found by multiplying its length by its width.

#### Instructions:
- Create a file named rectangle_area.py.
- Define two variables in this file:
- - length with a value representing the length of the rectangle.
- - width with a value representing the width of the rectangle.
- For simplicity, let’s use length = 10 and width = 5.
- Calculate the area of the rectangle using the formula (Area = length × width) and store the result in a variable named area.
- Print the calculated area in a format: The area of the rectangle is: [area].

#### Expected Output:
When executed, your script, with the provided values (length = 10 and width = 5), should print the area of the rectangle:
```
The area of the rectangle is: 50
```


## Task 3. Convert Hours to Seconds
#### Objective: Demonstrate understanding of variable assignments and arithmetic operations by converting a given number of hours into seconds.

#### Task Description:
For this task, write a Python script that converts a specific number of hours into seconds. This task reinforces the concept of arithmetic operations within a practical context.

#### Instructions:
- Create a file named hours_to_seconds.py.
- Define a variable named hours and assign it a value representing the number of hours you want to convert to seconds. Use hours = 2.
- Calculate the number of seconds in the given hours. Remember, there are 3600 seconds in an hour (since there are 60 minutes in an hour and 60 seconds in a minute, thus 60 x 60 = 3600).
- Store the result of the conversion in a variable named seconds.
- Print the result in the format: [hours] hour(s) is [seconds] seconds.

#### Expected Output:
Given the value hours = 2, your script should output:
```
2 hour(s) is 7200 seconds.
```


## Task 4. User Input Age Calculator
#### Objective: Practice receiving user input in Python and perform a simple arithmetic operation to calculate the user’s age in a future year.

#### Task Description:
Create a Python script that asks the user for their current age and then calculates how old they will be in a specific future year. This task introduces handling user input and reinforces arithmetic operations.

#### Instructions:
- Create a file named future_age_calculator.py.
- Prompt the user to input their current age with the question: “How old are you? ”.
- Assume the user will input a valid integer value.
- Calculate how old the user will be in the year 2050. To keep calculations simple, assume the current year is 2023. Therefore, you need to add 27 years to the user’s current age.
- Print the user’s age in 2050 in the format: In 2050, you will be [age] years old.

#### Expected Script Flow:
1. The script prompts the user for their current age.
2. The user enters their age.
3. The script calculates and prints how old the user will be in 2050.

#### Example Interaction:
If the user inputs 30 when prompted for their current age, the output should be:
```
In 2050, you will be 57 years old.
```


## Task 5. Personal Finance Calculator

#### Objective: Use user input, variables, and arithmetic operations to calculate and provide feedback on a user’s monthly savings and potential future savings without applying conditional statements.

#### Task Description:
You will create a script named finance_calculator.py. This script will calculate the user’s monthly savings based on inputted monthly income and expenses. It will then project these savings over a year, assuming a fixed interest rate, to demonstrate compound interest’s effect on savings.

#### Instructions:
###### 1. User Input for Financial Details:
- - Prompt the user for their monthly income: “Enter your monthly income: ”.
- - Ask for their total monthly expenses: “Enter your total monthly expenses: ”.
###### 2.  Calculate Monthly Savings:
- - Calculate the monthly savings by subtracting monthly expenses from the monthly income.
###### 3. Project Annual Savings:
- - Assume a simple annual interest rate of 5%.
- - Calculate the projected savings after one year, incorporating the interest. Use the simplified formula for annual savings projection: (Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05)).

###### 4. Output Results:
- - Display the user’s monthly savings.
- - Display the projected annual savings after including interest.

#### Example Interaction:
```
Enter your monthly income: 5000
Enter your total monthly expenses: 4000
Your monthly savings are $1000.
Projected savings after one year, with interest, is: $12600.
```


# Introducing Logic into programming (Control flow and loops)

## Task 0. Weather Recommendation Program

#### Objective: Utilize conditional statements to guide program execution based on user input regarding weather conditions.

#### Task Description:

Create a Python script named [weather_advice.py]. This script will ask the user about the current weather conditions and provide clothing recommendations based on the input. This task aims to demonstrate the use of [if], [elif], and [else] statements to make decisions in a program.

#### Instructions:

1. Prompt User for Weather Input:
- Ask the user to input the current weather from a predefined set of conditions: [sunny], [rainy], or [cold].
Use the prompt: [What's the weather like today? (sunny/rainy/cold):].

2. Provide Clothing Recommendations:
- Based on the user’s input, your program will recommend different types of clothing:
- - If the weather is “sunny”, recommend: Wear a t-shirt and sunglasses.
- - If the weather is “rainy”, recommend: Don't forget your umbrella and a raincoat.
- - If the weather is “cold”, recommend: Make sure to wear a warm coat and a scarf.
- Include an else statement that handles unexpected input by printing: Sorry, I don't have recommendations for this weather.

3. Output the Recommendation:
- Print the clothing recommendation based on the weather condition provided by the user.

#### Example Interaction:
```
What's the weather like today? (sunny/rainy/cold): sunny
Wear a t-shirt and sunglasses.
```
Or, for an unexpected input scenario:
```
What's the weather like today? (sunny/rainy/cold): windy
Sorry, I don't have recommendations for this weather.
Repo:
```


## Task 1. Simple Calculator with Match Case
#### Objective: Learn to use Match Case statements for handling multiple operations in a simple calculator program.

#### Task Description:
- Develop a Python script named [match_case_calculator.py]. This calculator will prompt the user to enter two numbers and select an operation (addition, subtraction, multiplication, or division). The script will then perform the selected operation using a Match Case statement and display the result.

#### Instructions:
1. Prompt for User Input:
- Ask the user to input two numbers (one at a time) using: [Enter the first number]: and [Enter the second number]:
- Make sure you use num1 and num2 for first and second numbers
- Ask for the type of operation they’d like to perform: [Choose the operation (+, -, *, /):].

2. Perform the Calculation Using Match Case:
- Implement a Match Case statement that executes the chosen operation based on the user’s input.
- - For addition (+), subtract (-), multiply (*), and divide (/).
- Ensure to handle the division by zero case gracefully, displaying a message if the user tries to divide by zero.

3. Output the Result:
- Display the result of the operation in a user-friendly message, e.g., [The result is [result]].

#### Example Interaction:
```
Enter the first number: 10
Enter the second number: 5
Choose the operation (+, -, *, /): *
The result is 50.
```
Or, for a division by zero scenario:
```
Enter the first number: 10
Enter the second number: 0
Choose the operation (+, -, *, /): /
Cannot divide by zero.
```


## Task 2. Multiplication Table Generator
#### Objective: Use a for loop to generate and print the multiplication table for a given number.

#### Task Description:
- Create a Python script named [multiplication_table.py]. This script will ask the user to enter a number, then use a for loop to print the multiplication table for that number from 1 to 10.

#### Instructions:
1. Prompt User for a Number:
- Ask the user to input a number for which they want to see the multiplication table: [Enter a number to see its multiplication table:].
- Save it in a variable name [number]

2. Generate and Print the Multiplication Table:
- Use a [for] loop to iterate through the numbers 1 to 10.
- For each iteration, calculate the product of the user’s number and the iterator (the current number in the loop from 1 to 10).
- Print each line of the multiplication table in the format: “X * Y = Z”, where X is the user’s number, Y is the current number in the loop, and Z is the product.

#### Example Interaction:
If the user inputs 5, the output should be:
```
Enter a number to see its multiplication table: 5
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
5 * 10 = 50
```
This task is designed to reinforce the concept of for loops by applying them in a practical scenario that generates a multiplication table. Through this exercise, students will learn how loops can significantly simplify the process of performing repetitive tasks, enhancing their understanding of looping constructs in Python.


## Task 3. Drawing Patterns with Nested Loops
#### Objective: Utilize while loops and nested for loops to draw a simple text-based pattern.

#### Task Description:
Develop a Python script named [pattern_drawing.py]. This script will prompt the user to enter a positive integer, then use nested loops to print a square pattern of that size made of asterisks (*).

#### Instructions:
1. Prompt User for Pattern Size:
- Ask the user to input a positive integer that represents the size of the pattern (i.e., the length of each side of the square): [Enter the size of the pattern:].

2. Draw the Pattern:
- First, use a while loop to iterate through each row of the pattern.
- Inside the while loop, use a for loop to print asterisks (*) side by side without advancing to a new line (you can use [print("*", end="")] for this).
- After completing each row, print a newline character to move to the next row.
- Continue until the pattern forms a square of the inputted size.

#### Example Interaction:
If the user inputs [4], the output should be:
```
Enter the size of the pattern: 4
****
****
****
****
```


## Task 4. Personal Daily Reminder
#### Objective: 
Create a simplified Python script that uses conditional statements, Match Case, and loops to remind the user about a single, priority task for the day based on time sensitivity.

#### Task Description:
Develop a script named [daily_reminder.py]. This script will ask the user for a single task, its priority level, and if it is time-sensitive. The program will then provide a customized reminder for that task, demonstrating control flow and loops without relying on data structures to store multiple tasks.

#### Instructions:
1. Prompt for a Single Task:
- Ask the user to input a task description and save it into a task variable
- Prompt for the task’s priority (high, medium, low) and save it into a priority variable
- In a time_bound variable, Ask if the task is time-bound (yes or no)

2. Process the Task Based on Priority and Time Sensitivity:
- Use a Match Case statement to react differently based on the task’s priority.
- Within the Match Case or after, use an if statement to modify the reminder if the task is time-bound.

3. Provide a Customized Reminder:
- Print a reminder about the task that includes its priority level and whether immediate action is required based on time sensitivity.
- A message should be ‘that requires immediate attention today!’

#### Example Interaction and Output:
```
Enter your task: Finish project report
Priority (high/medium/low): high
Is it time-bound? (yes/no): yes

Reminder: 'Finish project report' is a high priority task that requires immediate attention today!
```
Or, for a non-time-bound task:
```
Enter your task: Read a book
Priority (high/medium/low): low
Is it time-bound? (yes/no): no

Note: 'Read a book' is a low priority task. Consider completing it when you have free time.
```

# Programming Paradigms & Exception handling

## Task 0. Create a Simple Bank Account Class

#### Objective: 
Understand the fundamentals of OOP in Python by implementing a BankAccount class that encapsulates banking operations. Use command line arguments to interact with instances of this class.

#### Task Description:
You will create two Python scripts: [bank_account.py], which contains the BankAccount class, and [main-0.py], which interfaces with the class through command line arguments to perform banking operations.

[bank_account.py]:
1. Class Definition:
- Define a class named BankAccount.
- Use the __init__ method to initialize an account_balance attribute. Optionally, accept an initial balance parameter, defaulting to zero.

2. Encapsulation and Behaviors:
- Implement [deposit(amount)], [withdraw(amount)], and [display_balance()] methods.
- [deposit] should add the specified amount to account_balance.
- [withdraw] should deduct the amount from account_balance if funds are sufficient, returning True; otherwise, return False and do not alter the balance.
- [display_balance] should print the current balance in a user-friendly format.

[main-0.py] for Command Line Interaction:
- This script utilizes BankAccount through command line arguments for banking operations.
```
import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Example starting balance
    if len(sys.argv) < 2:
        print("Usage: python main.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
```

#### Sample Command Line Usage and Expected Outputs:
1. Deposit:
```
   python main-0.py deposit:50
```
Expected Output: Deposited: $50

2. Withdraw with Sufficient Funds:
```
   python main-0.py withdraw:20
```
Expected Output: Withdrew: $20

3. Withdraw with Insufficient Funds:
```
   python main-0.py withdraw:150
```
Expected Output: Insufficient funds.

4. Display Balance:
```
   python main-0.py display
```
Expected Output: Current Balance: $[amount]

#### Implementation Notes for you:
- Ensure your [BankAccount] class in [bank_account.py] correctly implements the specified functionalities and adheres to the principles of encapsulation.
- Use [main.py] to test your [BankAccount] class by performing various operations. Adjust the initial balance as needed for testing different scenarios.
- This task combines learning OOP concepts with practical command line interaction, enhancing your understanding of Python programming.


## Task 1. Robust Division Calculator with Command Line Arguments

#### Objective:
Implement a division calculator that robustly handles errors like division by zero and non-numeric inputs using command line arguments.

#### Task Description:
Create two Python scripts: [robust_division_calculator.py], which contains the division logic including error handling, and [main.py], which interfaces with the user through the command line.

[robust_division_calculator.py]:
1. Define a function safe_divide(numerator, denominator) that performs division, handling potential errors:
- Division by Zero: Use a try-except block to catch ZeroDivisionError.
- Non-numeric Input: Attempt to convert arguments to floats. Use a try-except block to catch ValueError for non-numeric inputs.
- Return appropriate messages for errors or the result for successful division.

[main.py] for Command Line Interaction:
This script will import safe_divide from robust_division_calculator.py and use it to divide numbers provided as command line arguments.
```
import sys
from robust_division_calculator import safe_divide

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()
```

#### Expected Behavior:
The script is executed from the command line with two additional arguments representing the numerator and denominator. Here are sample commands and the expected outputs:

1. Normal Division:
```
  python main.py 10 5
```
Expected Output: The result of the division is 2.0

2. Division by Zero:
```
  python main.py 10 0
```
Expected Output: Error: Cannot divide by zero.

3. Invalid Input (Non-numeric):
```
  python main.py ten 5
```
Expected Output: Error: Please enter numeric values only.

#### Implementation Notes for you:
- Focus on error handling within [safe_divide] in [robust_division_calculator.py]. Ensure you cover the scenarios detailed above.
- Test your function using [main.py] by passing different types of inputs via command line arguments. This method allows you to quickly assess how well your error handling works in various situations.
- This task helps you practice writing error-resistant code, a crucial skill in software development.


# More about OOP
## Task 0. Dive into Python Magic Methods

#### Objective:
Master Python magic methods by implementing a Book class that incorporates constructors (__init__), destructors (__del__), and the representation methods (__str__ and __repr__).

#### Task Description:
Create a Python script named [book_class.py]. In this script, define a Book class that uses specific magic methods to enhance its functionality. This class will model a book with attributes for the title, author, and publication year.

#### Requirements for Book Class in book_class.py:
1. Attributes:
- title (str): The title of the book.
- author (str): The author of the book.
- year (int): The publication year of the book.

2. Magic Methods:
- Constructor (__init__): Initializes a Book instance with title, author, and year.
- Destructor (__del__): Prints "Deleting (title of the book)" upon object deletion.
- String Representation (__str__): Returns a string in the format "(title) by (author), published in (year)".
- Official Representation (__repr__): Returns a string that would recreate the Book instance: f"Book('{self.title}', '{self.author}', {self.year})".

#### Provided for Testing: main.py
To test your Book class, use the following main.py script, which demonstrates creating a Book instance and utilizing the implemented magic methods:
```
from book_class import Book

def main():
    # Creating an instance of Book
    my_book = Book("1984", "George Orwell", 1949)

    # Demonstrating the __str__ method
    print(my_book)  # Expected to use __str__

    # Demonstrating the __repr__ method
    print(repr(my_book))  # Expected to use __repr__

    # Deleting a book instance to trigger __del__
    del my_book

if __name__ == "__main__":
    main()
```

#### Expected Output:
```
1984 by George Orwell, published in 1949
Book('1984', 'George Orwell', 1949)
Deleting 1984
```

## Task 1. Mastering Inheritance and Composition in Python

#### Objective:
Deepen your understanding of inheritance and composition in Python by creating a system that models a library with different types of books.

#### Task Description:
Develop two Python scripts: library_system.py and main.py. In library_system.py, you’ll define a base class Book and two derived classes, EBook and PrintBook, showcasing inheritance. Additionally, implement a Library class demonstrating composition by managing a collection of books.

#### library_system.py:
1. Base Class - Book:
 - Attributes: title (str) and author (str).
 - Method: __init__(self, title, author) for initializing book attributes.
2. Derived Classes - EBook and PrintBook:
 - Both classes inherit from Book.
 - EBook additional attribute: file_size (int).
 - PrintBook additional attribute: page_count (int).
 - Each derived class should have its own __init__ method that properly calls the base class __init__ while also initializing its unique attribute.
3. Composition - Library:
 - Attributes: books (a list to store instances of Book, EBook, and PrintBook).
 - Methods:
 - - add_book(self, book): Adds a Book, EBook, or PrintBook instance to the library.
 - - list_books(self): Prints details of each book in the library.

#### main.py (Provided for Testing):
This script tests the functionality of your classes in library_system.py by adding different types of books to a Library instance and listing them.
```
from library_system import Book, EBook, PrintBook, Library

def main():
    # Create a Library instance
    my_library = Library()

    # Create instances of each type of book
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    # Add books to the library
    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    # List all books in the library
    my_library.list_books()

if __name__ == "__main__":
    main()
```
#### Expected Output:
Your output should list the details of each book added to the library, reflecting the specific attributes of EBook and PrintBook, as well as the common attributes inherited from Book.
```
Book: Pride and Prejudice by Jane Austen
EBook: Snow Crash by Neal Stephenson, File Size: 500KB
PrintBook: The Catcher in the Rye by J.D. Salinger, Page Count: 234
```

