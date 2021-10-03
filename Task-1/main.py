import menu_actions as ma
import inputs

while True:
    print("**********************MENU**********************")
    print("1.Add a new Student into Database")
    print("2.Display a Student Details")
    print("3.Get all students Details")
    print("4.Update Student Details")
    print("5.Delete a Student from Database")
    print("6.EXIT")
    user_choice = int(input("Enter your choice\n"))
    if user_choice == 1:
        student_data = inputs.get_input()
        ma.insert_student_details(student_data)
    elif user_choice == 2:
        print("Enter Student ID")
        id_no = int(input())
        ma.display_Student_details(id_no)
    elif user_choice == 3:
        ma.display_all_Students_details()
    elif user_choice == 4:
        print("Enter Student ID")
        id_no = int(input())
        student_data = inputs.get_input()
        ma.update_student_details(student_data, id_no)
    elif user_choice == 5:
        print("Enter Student ID")
        id_no = int(input())
        ma.delete_Student_details(id_no)
    elif user_choice == 6:
        ma.close_connection()
        print("Thank you, See you again")
        quit()
    else:
        print("Enter  a Valid integer")
