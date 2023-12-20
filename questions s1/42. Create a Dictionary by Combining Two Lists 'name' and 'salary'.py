"""
	Write a program to create a dictionary by combining two lists 'name' for employee name and 'salary' for employee salary. Use the list 'name' as the key and 'salary' as the value of dictionary elements. 
"""

employee_names = input("Enter employee names separated by spaces: ").split()
employee_salaries = input("Enter corresponding salaries separated by spaces: ")
employee_salaries = [float(salary) for salary in employee_salaries.split()]

employee_dict = dict(zip(employee_names, employee_salaries))
print("Employee dictionary:", employee_dict)
    
"""
	------- output 1 --------
    Enter employee names separated by spaces: ram sam
    Enter corresponding salaries separated by spaces: 90000 60000
    Employee dictionary: {'ram': 90000.0, 'sam': 60000.0}

	------- output 2 --------
    Enter employee names separated by spaces: lucky rov sara
    Enter corresponding salaries separated by spaces: 70000 120000 85000
    Employee dictionary: {'lucky': 70000.0, 'rov': 120000.0, 'sara': 85000.0}
"""