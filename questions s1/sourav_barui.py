my_list_of_file_names = [
    # "Rotate Values of x, y, and z",
    # "Display Specific Numbers from a Given Number",
    # "Add Two Complex Numbers",
    # "Calculate Interest Amount and Total Amount",
    # "Sort Three Numbers using if-elif-else",
    # "Print Patterns",
    # "Calculate Simple Interest with Conditions",
    # "Print Patterns" "Print Odd Numbers in a Range using While Loop",
    # "Compute GCD of Two Numbers",
    # "Decimal Equivalents using For Loop",
    # "Check Prime Number",
    # "Check Armstrong Number",
    # "Get LCM of Two Numbers",
    # "Sum of Prime Numbers in a Range",
    # "Count of Prime and Composite Numbers",
    # "Find the Sum of Even-Valued Terms of the Fibonacci Series up to 100",
    # "Count the Number of Each Vowel in a Sentence",
    # "Check Palindrome String",
    # "Replace Occurrences of the Last Character in a String",
    # "Count Occurrences of a Word in a Sentence",
    # "Generate All Substrings of a Given String",
    # "Detect Whether Two Strings are Anagrams or Not",
    # "Find Maximum and Minimum of a List of Numbers without Using Built-in Functions",
    # "Multiply Two Matrices as Nested Lists",
    # "Find the Union of Two Lists",
    # "Concatenate Two Lists using List Comprehension",
    # "Create a List from Two Given Lists",
    # "Find Distinct Pair of Numbers Whose Product is Odd from a List",
    # "Generate a Tuple from Comma-Separated Numbers",
    # "Add Elements in a Tuple without Using Built-in Functions",
    # "Calculate the Mean of Elements in a Tuple of Integers",
    # "Display Unique and Duplicate Elements of a Tuple",
    # "Count the Frequency of Elements in a Tuple",
    # "Find Distinct Pair of Numbers Whose Product is Even from a Tuple",
    # "Create a Dictionary with (i, i^i) for Integral Numbers between 1 and n",
    # "Count the Number of Characters in a String and Store in a Dictionary",
    # "Create a Dictionary by Combining Two Lists 'name' and 'salary'",
    # "Input and Display Cricket Player's Details using a Dictionary",
    # "Sort a Dictionary by Value in Ascending Order",
    # "Merge Two Dictionaries",
    # "Find GCD and LCM of Two Numbers using a Function",
    # "Count Uppercase and Lowercase Letters in a String using a Function",
    # "Find Unique Elements of a List using a Function",
    # "Find Numbers Divisible by 5 and 7 in a Range using a Lambda Function",
    # "Print Even Numbers from a List using a Lambda Function",
    # "Find Maximum Value from a List using a Lambda Function",
    "Palindrome Checking Module",
    "Prime Checking Module",
    "Factorial Module",
    "Calculate Mean, Median, and Standard Deviation of a List of Random Numbers",
    "Shuffle Elements of a List of Random Numbers",
    "Create a List of Random Numbers using List Comprehension",
    "Read a Number, Print if Positive or Zero, Otherwise Raise an Exception",
    "Read Two Numbers, Perform Basic Mathematical Operations, Handle Exceptions",
    "Read a Number, Print its Square, Generate KeyboardInterrupt",
    "Print Random Numbers Infinitely, Raise StopIteration Exception after 10 Numbers",
    "Generate a Random Number, Raise a User-Defined Exception if Below 0.5",
    "Read the Age of a Person, Raise Exceptions if Negative",
    "Count Words in a File",
    "Print Each Line of a File in Reverse Order",
    "Reverse the Content of a File and Store in Another File",
    "Copy First 100 Characters of a Binary File to Another",
    "Convert Text File to Uppercase",
    "Copy Python Script Skipping Comment Lines",
    "Class for Storing Student Information",
    "Derived Class Employee with Multiple Inheritance",
    "Class Inheritance Example - Person, Faculty, and Publication",
    "Abstract Class Polygon and Derived Classes Rectangle and Triangle",
]
question_names = [
    # "Write a program to rotate the values of x, y, and z such that x has the value of y, y has the value of z, and z has the value of x.",
    # "Write a program to display the following numbers: 5678, 678, 78, 8, where the given number is 5678.",
    # "Write a program to add two complex numbers by reading the numbers from the user.",
    # "Write a program to accept the principal amount, rate of interest, and duration from the user. Calculate the interest amount and the total amount (principal + interest).",
    # "Write a program to sort three numbers using if-elif-else.",
    # "Write a program to calculate simple interest with the following conditions: If the principal amount is less than 2,00,000, the interest rate is 10%. If the principal amount is 2,00,000 - 10,00,000, the interest rate is 12%. If the principal amount is greater than 10,00,000, the interest rate is 15%.",
    # "Write a program to print the following patterns:\n  a)\n     1\n     2, 3\n     4, 5, 6\n     7, 8, 9, 10\n     11, 12, 13, 14, 15\n  b)\n     * * * * * * * * *\n     * * * * * * *\n     * * * * *",
    # "Write a program using a while loop to print all the odd numbers within a given range.",
    # "Write a program to compute the GCD of two integer numbers.",
    # "Write a program to print the decimal equivalents of 1/2, 1/3, 1/4,..., 1/10 using a for loop.",
    # "Write a program to check whether a given number is a prime number or not.",
    # "Write a program to check whether a given number is an Armstrong number or not.",
    # "Write a program to get the LCM of two positive integers.",
    # "Write a program to find the sum of all prime numbers within a given range.",
    # "Write a program that prompts users to enter numbers. This process repeats until the user enters -1. Finally, the program prints the count of prime and composite numbers entered.",
    # "Write a program to find the sum of the even-valued terms of the Fibonacci series up to 100.",
    # "Write a program to count the number of each vowel in a sentence.",
    # "Write a program to read a string and check whether the string is a palindrome or not.",
    # "Write a program to get a string from a given string where all occurrences of the last character have been changed to '*' except the last character.",
    # "Write a program to count the occurrences of a word in a given sentence.",
    # "Write a program to get all substrings of a given string.",
    # "Write a program to detect whether two strings are anagrams or not.",
    # "Write a program to find the maximum and minimum of a list of numbers without using built-in functions.",
    # "Write a program to multiply two matrices as nested lists.",
    # "Write a program to find the union of two lists.",
    # "Write a program to concatenate two lists using list comprehension.",
    # "Write a program to create a list from two given lists 'list1' and 'list2' of numbers such that it contains numbers that are present in 'list2' but not in 'list1'.",
    # "Write a program to find the distinct pair of numbers whose product is odd from a list of integers.",
    # "Write a program to accept a sequence of comma-separated numbers from the user and generate a tuple with those numbers.",
    # "Write a program to add elements in a tuple without using built-in functions.",
    # "Write a program to calculate the mean of elements in a tuple of integers.",
    # "Write a program to display unique and duplicate elements of a tuple.",
    # "Write a program to count the frequency of all the elements in a tuple.",
    # "Write a program to find the distinct pair of numbers whose product is even from a tuple of integers.",
    # "Write a program to create a dictionary that contains (i, i^2) such that i is an integral number between 1 and n (both included).",
    # "Write a program to count the numbers of characters in a string and store them in a dictionary.",
    # "Write a program to create a dictionary by combining two lists 'name' for employee name and 'salary' for employee salary. Use the list 'name' as the key and 'salary' as the value of dictionary elements.",
    # "Write a program to input a player's name (string) and runs (integer) scored for n number of players where n should be input from the keyboard. Store the player’s details in a dictionary called 'cricket'. After preparing the dictionary, input the player's name and print the runs scored by the player, otherwise return '-1' if the player's name is not found.",
    # "Write a program to sort (ascending order) a dictionary by value.",
    # "Write a program to merge two dictionaries.",
    # "Write a program to find GCD and LCM of two numbers by defining a function to compute GCD and LCM.",
    # "Write a program to define a function that accepts a string and calculates the number of uppercase letters and lowercase letters.",
    # "Write a program to find all the unique elements of a list by defining a function.",
    # "Write a program to find all the numbers divisible by 5 and 7 between the given range using the lambda function.",
    # "Write a program to print the even numbers from a given list using the lambda function.",
    # "Write a program to find the maximum value from a list using the lambda function.",
    "Create a module to check if a passed string is a palindrome or not. Write a program to find whether a string is a palindrome or not using this module.",
    "Create a module to check whether a number is a prime or not. Write a program to find the prime number between two limits using this module.",
    "Create a module to find the factorial of a number and import the module from the main program to find the factorial of a given number.",
    "Write a program to find the mean, median, and standard deviation of a list of random numbers between 1 and 10.",
    "Write a program to shuffle elements of a list of random numbers between given ranges.",
    "Write a program to create a list of random numbers using list comprehension.",
    "Write a program to read a number from the user. If the number is positive or zero, print it; otherwise, raise an exception.",
    "Write a program to read two numbers from the user and perform basic mathematical operations (addition, multiplication, subtraction, division) by handling all possible exceptions.",
    "Write a program to read a number from the user and print its square. Generate KeyboardInterrupt exception if Ctrl + C is pressed instead of a number.",
    "Write a program to print random numbers infinitely. Raise the StopIteration exception after displaying 10 numbers to exit from the program.",
    "Write a program to generate a random number. Raise a user-defined exception if the number is below 0.5.",
    "Write a program to read the age of a person and raise exceptions if age is negative.",
    "Write a program to accept a filename from the user and count the number of words present in the file.",
    "Write a program to print each line of a file in reverse order.",
    "Write a program to reverse the content of a file and store it in another file.",
    "Write a program to copy the first 100 characters of a binary file into another.",
    "Write a program to copy the content of the text file to another file by converting all lowercase characters to uppercase.",
    "Write a program to copy one Python script into another in such a way that all comment lines are skipped and not copied to the destination file.",
    "Write a program that has a class Student for storing roll number, name, and marks in five subjects of a student. Display the information stored about the student.",
    "Write a program to create a derived class employee derived from the class basicinformation (member variables are name, empid, and age) and departmentinformation (member variables are dept name, assigned work, and time to complete) using multiple inheritances. Create two objects of the employee class and print the details of individual objects.",
    "Write a program that has a class Person. Inherit a class Faculty from Person which also has a class Publication.",
    "Write a program that has an abstract class Polygon. Derive two classes Rectangle and Triangle from Polygon and write methods to get the details of their dimensions and hence calculate the area.",
    "Write a program to create a GUI to add two numbers from different two checkboxes.",
    "Write a program to create a GUI that has an entry box in which the message entered by the user is printed on the screen.",
    "Write a program to create a GUI to convert any number (Binary, Decimal, Hexadecimal, Octal) to the number of all other bases.",
]

programs = [
    # 52. Palindrome Module and Program
    """
def is_palindrome(s):
    return s == s[::-1]

input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
    """,

    # 53. Prime Number Module and Program
    """
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

lower_limit = int(input("Enter lower limit: "))
upper_limit = int(input("Enter upper limit: "))

print(f"Prime numbers between {lower_limit} and {upper_limit}:")
for num in range(lower_limit, upper_limit + 1):
    if is_prime(num):
        print(num)
    """,

    # 54. Factorial Module and Program
    """
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

number = int(input("Enter a number: "))
result = factorial(number)
print(f"The factorial of {number} is: {result}")
    """,

    # 55. Mean, Median, and Standard Deviation Program
    """
import statistics
import random

random_numbers = [random.randint(1, 10) for _ in range(10)]

mean = statistics.mean(random_numbers)
median = statistics.median(random_numbers)
std_dev = statistics.stdev(random_numbers)

print(f"List of random numbers: {random_numbers}")
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Standard Deviation: {std_dev}")
    """,

    # 56. Shuffle List Program
    """
import random

random_numbers = list(range(1, 11))
random.shuffle(random_numbers)

print(f"Shuffled list: {random_numbers}")
    """,

    # 57. List Comprehension Program
    """
import random

random_numbers = [random.randint(1, 10) for _ in range(10)]

print(f"List of random numbers using list comprehension: {random_numbers}")
    """,

    # 58. Exception Handling Program
    """
try:
    number = float(input("Enter a number: "))
    if number >= 0:
        print(f"The number is: {number}")
    else:
        raise ValueError("Number should be positive or zero.")
except ValueError as ve:
    print(f"Error: {ve}")
    """,

    # 59. Exception Handling for Basic Mathematical Operations
    """
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    result_addition = num1 + num2
    result_subtraction = num1 - num2
    result_multiplication = num1 * num2
    result_division = num1 / num2

    print(f"Addition: {result_addition}")
    print(f"Subtraction: {result_subtraction}")
    print(f"Multiplication: {result_multiplication}")
    print(f"Division: {result_division}")

except Exception as e:
    print(f"Error: {e}")
    """,

    # 60. KeyboardInterrupt Exception Program
    """
try:
    number = float(input("Enter a number: "))
    square = number ** 2
    print(f"The square of {number} is: {square}")
except KeyboardInterrupt:
    print("Ctrl + C detected. Exiting the program.")
    """,

    # 61. StopIteration Exception Program
    """
import random

class RandomNumberGenerator:
    def __iter__(self):
        return self

    def __next__(self):
        if random.randint(0, 1):
            return random.randint(1, 100)
        else:
            raise StopIteration

rng = RandomNumberGenerator()

for _ in range(10):
    try:
        print(next(rng))
    except StopIteration:
        print("StopIteration exception. Exiting the program.")
        break
    """,

    # 62. User-Defined Exception Program
    """
class BelowThresholdError(Exception):
    pass

try:
    random_number = random.random()
    if random_number < 0.5:
        raise BelowThresholdError("Number is below 0.5.")
    else:
        print(f"Random number: {random_number}")

except BelowThresholdError as e:
    print(f"Error: {e}")
    """,

    # 63. Age Exception Program
    """
class NegativeAgeError(Exception):
    pass

try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise NegativeAgeError("Age cannot be negative.")
    else:
        print(f"Your age is: {age}")

except NegativeAgeError as e:
    print(f"Error: {e}")
    """,

    # 64. File Word Count Program
    """
file_name = input("Enter the file name: ")

try:
    with open(file_name, 'r') as file:
        content = file.read()
        word_count = len(content.split())
        print(f"Number of words in the file: {word_count}")

except FileNotFoundError:
    print(f"Error: File '{file_name}' not found.")
    """,

    # 65. Print Each Line in Reverse Order Program
    """
file_name = input("Enter the file name: ")

try:
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in reversed(lines):
            print(line.strip())

except FileNotFoundError:
    print(f"Error: File '{file_name}' not found.")
    """,

    # 66. Reverse Content and Store in Another File Program
    """
input_file = input("Enter the input file name: ")
output_file = input("Enter the output file name: ")

try:
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        content = infile.read()
        reversed_content = content[::-1]
        outfile.write(reversed_content)

except FileNotFoundError:
    print(f"Error: One or both files not found.")
    """,

    # 67. Copy First 100 Characters of a Binary File Program
    """
input_file = input("Enter the input binary file name: ")
output_file = input("Enter the output binary file name: ")

try:
    with open(input_file, 'rb') as infile, open(output_file, 'wb') as outfile:
        data = infile.read(100)
        outfile.write(data)

except FileNotFoundError:
    print(f"Error: One or both files not found.")
    """,

    # 68. Convert Lowercase to Uppercase in File Program
    """
input_file = input("Enter the input file name: ")
output_file = input("Enter the output file name: ")

try:
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        content = infile.read()
        uppercase_content = content.upper()
        outfile.write(uppercase_content)

except FileNotFoundError:
    print(f"Error: One or both files not found.")
    """,

    # 69. Copy Python Script Skipping Comment Lines Program
    """
input_file = input("Enter the input Python script file name: ")
output_file = input("Enter the output Python script file name: ")

try:
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if not line.strip().startswith('#'):
                outfile.write(line)

except FileNotFoundError:
    print(f"Error: One or both files not found.")
    """,

    # 70. Student Class Program
    """
class Student:
    def __init__(self, roll_number, name, marks):
        self.roll_number = roll_number
        self.name = name
        self.marks = marks

    def display_info(self):
        print(f"Roll Number: {self.roll_number}")
        print(f"Name: {self.name}")
        print(f"Marks: {', '.join(map(str, self.marks))}")

# Example usage:
student1 = Student(1, "John", [80, 75, 90, 85, 88])
student1.display_info()
    """,

    # 71. Employee Class with Multiple Inheritance Program
    """
class BasicInformation:
    def __init__(self, name, empid, age):
        self.name = name
        self.empid = empid
        self.age = age

class DepartmentInformation:
    def __init__(self, dept_name, assigned_work, time_to_complete):
        self.dept_name = dept_name
        self.assigned_work = assigned_work
        self.time_to_complete = time_to_complete

class Employee(BasicInformation, DepartmentInformation):
    def __init__(self, name, empid, age, dept_name, assigned_work, time_to_complete):
        BasicInformation.__init__(self, name, empid, age)
        DepartmentInformation.__init__(self, dept_name, assigned_work, time_to_complete)

# Example usage:
employee1 = Employee("Alice", 101, 28, "HR", "Recruitment", 10)
employee2 = Employee("Bob", 102, 35, "IT", "Programming", 20)

print("Employee 1 details:")
print(f"Name: {employee1.name}, Age: {employee1.age}, Dept: {employee1.dept_name}")

print("\\nEmployee 2 details:")
print(f"Name: {employee2.name}, Age: {employee2.age}, Dept: {employee2.dept_name}")
    """,

    # 72. Person, Faculty, and Publication Classes Program
    """
class Person:
    def __init__(self, name):
        self.name = name

class Publication:
    def __init__(self, title):
        self.title = title

class Faculty(Person, Publication):
    def __init__(self, name, title):
        Person.__init__(self, name)
        Publication.__init__(self, title)

# Example usage:
faculty_member = Faculty("Dr. Smith", "Research Paper")
print(f"Faculty Name: {faculty_member.name}")
print(f"Publication Title: {faculty_member.title}")
    """,

    # 73. Abstract Polygon, Rectangle, and Triangle Classes Program
    """
from abc import ABC, abstractmethod

class Polygon(ABC):
    @abstractmethod
    def get_dimensions(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Polygon):
    def get_dimensions(self):
        self.length = float(input("Enter the length of the rectangle: "))
        self.width = float(input("Enter the width of the rectangle: "))

    def calculate_area(self):
        return self.length * self.width

class Triangle(Polygon):
    def get_dimensions(self):
        self.base = float(input("Enter the base of the triangle: "))
        self.height = float(input("Enter the height of the triangle: "))

    def calculate_area(self):
        return 0.5 * self.base * self.height

# Example usage:
rectangle = Rectangle()
rectangle.get_dimensions()
print(f"Area of the rectangle: {rectangle.calculate_area()}")

triangle = Triangle()
triangle.get_dimensions()
print(f"Area of the triangle: {triangle.calculate_area()}")
    """
]

# Execute the programs one by one
for i, program in enumerate(programs, start=52):
    print(f"\nProgram {i}:\n{program}\n")

for i, item in enumerate(my_list_of_file_names):
    fname = f"{i + 52}. {item}.py"
    fformated = question_names[i].replace("\n", "\n\t")
    p = programs[i].replace('"""', "")
    fl = f'"""\n\t{fformated} \n"""\n\n{p}\n"""\n\t------- output 1 --------\n\n\n\t------- output 2 --------\n\n"""'
    with open(fname, "w") as file:
        file.write(fl)
