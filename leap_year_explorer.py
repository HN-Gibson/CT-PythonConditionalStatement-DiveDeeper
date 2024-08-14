#Task 1: Leap Year Checker Write a Python program that prompts the user to input a year. The program should determine if the given year is a leap year or not and then display an appropriate message. Please note that this is the definition of a leap year: Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100, but these centurial years are leap years if they are exactly divisible by 400.

#identify a variable for leap year being a literal type variable
leap_year = False

#call for input from user in an int type variable so that it can be run through arithmetic functions
year = int(input ('''Is a year a leap year?
    Enter it and find out: '''))

#utilize %, modulus, to determine the remainder from dividing and comparing results to determine if it is a leap year while passing year divisible by 100 to the elif to divide by 400 and to else line if neither conditions are met
if year % 4 == 0 and not year % 100 == 0:
    leap_year = True
elif year % 400 == 0:
    leap_year = True
else:
    leap_year = False

#used if/else statement to print a fun line depending on literal value of leap_year variable
if leap_year:
    print (f"February 29th exists in {year}! It is a leap year!")
else:
    print (f"{year} is not a leap year...")