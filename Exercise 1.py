# Question 1: Variable Assignment and String Manipulation

# TODO: Ask the user for their name and store it in a variable

print("Hello user, what is your name?")
while True:
    user_name = input("Enter your name: ")
    if user_name.isalpha(): 
        break
    else:
        print("Please enter a valid name (letters only).")


# TODO: Ask the user for their age and store it in a variable

while True:
    age = input("Enter your age: ")
    if age.isdigit():  
        user_age = int(age)  
        break
    else:
        print("Please enter a valid age (numbers only).")


# TODO: Print a greeting using the name and age variables

print(f"Welcome {user_name}, you are {user_age} years old")

#------------------------------------------------------------------------------------
# Question 2: Integer Operations

# TODO: Ask the user for the length of a rectangle and store it as an integer

print("What is the length of a rectangle   ?")
length = int(input("Enter the length of the rectangle: "))

# TODO: Ask the user for the width of a rectangle and store it as an integer

width = int(input("Enter the width of the rectangle: "))
print(f"The width of the rectangle is {width}")

# TODO: Calculate the area of the rectangle

area = length * width

# TODO: Print the result
print(f"The area is: {area}")

#------------------------------------------------------------------------------------
# Question 3: Working with Floats

# TODO: Ask the user for a temperature in Celsius and store it as a float

celsius = float(input("Enter the temperature in Celsius: "))
print(f"The temperature you entered is {celsius}°C")

# TODO: Convert the temperature to Fahrenheit using the formula: (C * 9/5) + 32

fahrenheit = (celsius * 9/5) + 32

# TODO: Print the result rounded to two decimal places

print(f"The temperature in Fahrenheit is {round(fahrenheit, 2)}")