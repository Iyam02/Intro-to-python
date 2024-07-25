print("Hello WOrld!")

#Data Types
# Integer
a = 10
print(a)

# Float
b = 10.5
print(b)

# String
c = "Hello"
print(c)

# Boolean
d = True
print(d)

# List
e = [1, 2, 3]
print(e)

# Tuple
f = (1, 2, 3)
print(f)

# Dictionary
g = {"name": "Kinuthia", "age": 25}
print(g)

#Control Structures
#if-else statements

x = 4
if x < 10 :
    print(x, " is less than 10")
else:
    print(x, " is larger than 10")

# for-loop

students = ['Bob', 'Mike', 'Lesly', 'Kim', 'Sean', 'Njoroge']
for student in students:
    print(student)

# Functions
def sum(a, b):
    return a + b

#calling the function
print(sum(10, 67))
print(sum(90, 34))

#List and Dictionaries
#List
nums = [1,4,5,6,7,89,98]
print(nums[4]) #Accessing the fourth element
print(nums[6]) #Accessing the last element

#Dictionary
personas = {"Uno": "Juan", "Dos": "Jose", "Tres": "Maria", "Cuatro": "Miguel"}
print(personas["Tres"]) # Accessing values by key
personas["cinco"] = "Ariella" #Adding a key-value pair
print(personas)

#Exception Handling
try:
    input = input('Enter a number: ')
    input = float(input) #Converts the str into float
    result = 10 / input
    
    print("Result: ", result)

# Handles case where the user enters zero
except ZeroDivisionError:
    print("Cannot divide by zero. Please enter a non-zero number.")

# Handles case where user enters a non-integer value
except ValueError:
    print("Invalid input. Please enter a valid number")

# This block executes whether or not an exception occurred
finally:
    print("Execution finished")


# Modules and Packages
# Using math modules
import math

print(math.sqrt(25)) #Using sqrt, square root, function from module
