#Task 1: Code Correction You are provided with a Python script that uses conditional statements to tell if a number is positive, negative, or zero, but it has some errors. Identify and fix them.

#There appear to be three issues:
    #line 7: calls for input of a number without specifying to turn the response into an int or float so that the functions below can be performed
    #line 11: uses "=" where it should be "==" as this is the correct way to format "equal too" in a conditional statement
    #line 13: uses an "else" with a conditional statement following. this could be fixed by either changing the "else" to an "elif" or removing the conditional statement
number = float(input("Enter a number: ")) #opted to convert the input to a float so that the functions run even if the user uses decimals

if number > 0:
    print("The number is positive.")
elif number == 0: #edited the "=" to "=="
    print("The number is zero.")
else: #opted for the removal of the conditional statement for brevity
    print("The number is negative.")