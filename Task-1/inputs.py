import calculate


def get_input():
    name = input("Enter Name :\n")
    college = input("Enter College Name : \n")
    depart = input("Enter Department Name : \n")
    c_marks = int(input("Enter C Marks : \n"))
    dse_marks = int(input("Enter dse Marks : \n"))
    python_marks = int(input("Enter python Marks : \n"))
    java_marks = int(input("Enter java Marks : \n"))
    php_marks = int(input("Enter php Marks : \n"))
    total = calculate.calculate_total([c_marks, dse_marks, python_marks, java_marks, php_marks])
    average = calculate.calculate_average([c_marks, dse_marks, python_marks, java_marks, php_marks])
    grade = calculate.calculate_grade(average)
    temp = (name, college, depart, c_marks, dse_marks, python_marks, java_marks, php_marks, total, average, grade)
    return temp
