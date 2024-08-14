#Task 1: Identify the Greatest Write a Python program that asks the user to enter three numbers. Your code should then identify and print out the largest number among the three.
#named two variables for later assignment and use in print()
largest = 0
smallest = 0

#added an opening line for flavor
print ("This program will take three numbers and output the highest and lowest of those entered by the user.")
#opted to convert input to a float in case the user inputs a number with a decimal
number1 = float(input("Please enter your first number: "))
number2 = float(input("Please enter your second number: "))
number3 = float(input("Please enter your third number: "))

if number1 >= number2 and number1 >= number3:
    largest = number1
elif number2 >= number1 and number2 >= number3:
    largest = number2
else:
    largest = number3

#removed print() after testing first block since final print results in both largest and smallest being displayed

#Task 2: Identify the Smallest Improve upon your code from Task 1 to also determine the smallest number among the three and print it out.

#copied previous block and edited conditional statements to assign the lowest value to "smallest variable"
if number1 <= number2 and number1 <= number3:
    smallest = number1
elif number2 <= number1 and number2 <= number3:
    smallest = number2
else:
    smallest = number3
#printed final results as f statement to use variables in the text of the print
print (f"The smallest number is {smallest}. The largest number is {largest}.")