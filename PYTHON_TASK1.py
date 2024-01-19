 
 #Q1 Declare and initialize two variables with integer values
print("Question Number 1 :")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

 # Calculate the sum
sum_result = num1 + num2
 # Print the result
print("THE SUM IS :",sum_result)



 #Q2 # Create a variable and assign it a string value using input function
print("Question Number 2 :")
message = "Hello"

 # Appending another string,
message += " World!"

 # Print the result
print(message)

#Q3 Define a variable, is_python_fun, and assign it a boolean value
print("Question Number 3 :")
is_python_fun = True  # You can set this to False if you want to convey that Python is not considered fun

 # Print a statement based on whether Python is considered fun
if is_python_fun:
     print("Python is fun!")
else:
     print("Python may not be considered fun by everyone.")
    

#Q4 # Create a list, fruits, with three different fruit names
print("Question Number 4 :")
fruits = ["Apple", "Banana", "Orange"]

 # Print the initial list
print("Initial list of fruits:", fruits)

# Add a new fruit to the list
new_fruit = input("ENTER FRUIT NAME : ")
fruits.append(new_fruit)

 # Print the updated list
print("Updated list of fruits:", fruits)


#Q5 Take a floating-point value as input from the user
print("Question Number 5 :")
price = float(input("Enter a floating-point value for the price: "))

# Convert the floating-point value to an integer
converted_price = int(price)

 # Print both the original and converted values
print("Original Price (float):", price)
print("Converted Price (integer):", converted_price)


#Q6 Use input function to take information about a student
print("Question Number 6 :")
name = input("Enter student's name: ")
age = input("Enter student's age: ")
grade = input("Enter student's grade: ")

# Create a dictionary, student_info, with keys for 'name', 'age', and 'grade'
student_info = {
     'name': name,
     'age': age,
     'grade': grade
}

# Print the dictionary
print("Student Information:")
print(student_info)

#Q7 Take user input for age
print("Question Number 7 :")
user_age = int(input("Enter your age: "))

# Determine the age group and print a message
if 13 <= user_age <= 19:
    print("You are a Teenager.")
elif 20 <= user_age <= 64:
    print("You are an Adult.")
elif user_age >= 65:
    print("You are a Senior Citizen.")
else:
    print("You are a Child.")
    

#Q8 Define a complex number variable with a real and imaginary part
print("Question Number 8 :")
comp_num = 3 + 4j  # Example: real part = 3, imaginary part = 4


# Print both the real and imaginary parts separately
print("Real Part:", comp_num.real)
print("Imaginary Part:", comp_num.imag)


# Q9 Two strings to be combined
print("Question Number 9 :")
string1 = "Hello"
string2 = "World"

# string concatenation
combined_string = string1 + string2

# print statement
print("The combined string is: ",combined_string)
print("The length of string is ",len(combined_string))

# Q10 Create a tuple, days_of_week, with the names of the days. Access and print the third day of the week.

print("Question Number 10 :")
# using tuple 
days_of_weeks=("Mon","Tue","Wed","Thurs","Fri")
#printing statement
print("The Third day of the week is: ",days_of_weeks[2])

