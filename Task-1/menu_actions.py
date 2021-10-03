from os import name
import mysql.connector as connection

try:
    con = connection.connect(host="localhost ", user="root", password="", database="practise")
except connection.Error as err:
    if err.errno == connection.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == connection.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)

cursor = con.cursor()


def insert_student_details(data):
    insert_stmt = ("INSERT INTO STUDENT(NAME,COLLEGE,DEPARTMENT,c_marks,dse_marks,python_marks,java_marks,php_marks,"
                   "TOTAL,AVERAGE,GRADE) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    cursor.execute(insert_stmt, data)
    con.commit()
    print("Student record inserted into the database successfully ")


def display_Student_details(idno):
    query = "SELECT * FROM STUDENT WHERE id = %(id_no)s"
    cursor.execute(query, {'id_no': idno})
    data = cursor.fetchone()
    if data is None:
        print("No Student Exists with that ID")
    else:
        for i in data:
            print(i, end="\t")
        print("\n")


def display_all_Students_details():
    cursor.execute("Select * from STUDENT")
    data = cursor.fetchall()
    if data is None:
        print("No records found")
    else:
        for i in data:
            for j in i:
                print(j, end="\t")
            print("\n")


def update_student_details(temp, id_no):
    update_stmt = "UPDATE STUDENT SET NAME=%s,COLLEGE=%s,DEPARTMENT=%s,c_marks=%s,dse_marks=%s,python_marks=%s," \
                  "java_marks=%s,php_marks=%s,TOTAL=%s,AVERAGE=%s,GRADE=%s where id=" + str(
        id_no)
    cursor.execute(update_stmt, temp)
    con.commit()
    print("Student record Updated in the database successfully ")


def delete_Student_details(id_no):
    query = "SELECT * FROM STUDENT WHERE id = %(id_no)s"
    cursor.execute(query, {'id_no': id_no})
    data = cursor.fetchone()
    if data is None:
        print("No Student Exists with that ID")
    else:
        query = "DELETE FROM STUDENT WHERE ID=%(id_no)s"
        cursor.execute(query, {'id_no': id_no})
        con.commit()
        print("Student details are removed from the database")


def close_connection():
    con.close()
