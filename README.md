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