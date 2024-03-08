import sqlite3

ID = "20230178"  # The manager's ID
Password = "333221"  # The manager's password

my_data = sqlite3.connect("student.db")  # create the Data base of student and connect
cr = my_data.cursor()  # setting up the cursor

# Create the tables
cr.execute(
    "CREATE TABLE IF NOT EXISTS student (ID TEXT ,Name TEXT , Level INT , Password TEXT,GPA FlOAT, Group_ TEXT)")
cr.execute("CREATE TABLE IF NOT EXISTS courses (course text, Code text)")
cr.execute("CREATE TABLE IF NOT EXISTS news (News text)")

def add_student():  # Add a new student to my database
    cr.execute("SELECT * FROM student")
    x = cr.fetchall()
    lis = len(cr.fetchall())

    if x == []:
        id = "20240001"              # ID first student
        password = "Std20174"        # Password first student
    else:
        # ID is a function in x
        id = str(20240001 + x[lis-1][0]-20240000)
        # Password is a function in x
        password = "Std2" + str(1000 + (x[lis-1][0]-20240000)*2 + 2*(x[lis-1][0]-20240000))

    name = input("\nEnter the name student: ").capitalize()
    if name == 'Back': manager()

    while True:
        level = input("Enter the level student (1, 2, 3 or 4): ").capitalize()
        if level == 'Back': manager()
        if level in ['1', '2', '3', '4']:
            break

    while True:
        try:
            gpa = float(input("Enter the GPA student: ").capitalize())
            if gpa == 'Back':
                manager()
            if 4 >= gpa >= 0:
                break
            else:
                print("Invalid GPA")
        except:
            print("Invalid GPA")

    # check if he wants to save changes or continue
    print("\nA) Save\nB) Add another student\nC) Cancel")
    while True:
        choice = input("Enter your choice (A/B/C): ").capitalize()

        if choice == "A":
            cr.execute("INSERT INTO student(ID,Name,Level,Password,GPA) values (?,?,?,?,?)",
                       (id, name, level, password, float(gpa)))
            cr.execute(f"CREATE TABLE IF NOT EXISTS '{id}' (Courses text, Code text)")
            my_data.commit()
            print("\n** A new student has been added successfully **\n")
            while True :
                back = input("Enter 'Back' to go back to menu 2: ").capitalize()
                if back == "Back": manager()

        elif choice not in ['A', 'B', 'C', 'Back']:
            print("Invalid choice")

        elif choice == "B":
            cr.execute("INSERT INTO student(ID,Name,Level,Password,GPA) values (?,?,?,?,?)",
                       (id, name, level, password, float(gpa)))
            cr.execute(f"CREATE TABLE IF NOT EXISTS '{id}' (Courses text, Code text)")
            add_student()

        else: manager()
def delete_student():
    while True:
        id_student = input("\nEnter the student's ID: ").capitalize()
        if id_student == "Back": manager()

        # check if ID is valid or not
        cr.execute("SELECT * FROM student where ID = ?", (id_student,))
        check = cr.fetchall()
        if len(check) == 0:
             print("\nThis ID is not found")
        else: break

    # check if he wants to save changes or continue
    print("A) Save\nB) Delete another student\nC) Cancel")
    while True:
        confirm = input("Enter your choice (A/B/C) : ").capitalize()

        if confirm not in ["A", "B", "C", "Back"]:
            print("Invalid choice")

        elif confirm == "A":
            cr.execute("DELETE FROM student WHERE ID = ?", (id_student,))
            cr.execute(f"DROP TABLE IF EXISTS '{id_student}' ")
            my_data.commit()
            print("\n** Deleted successfully **\n")
            while True:
                back = input("Enter 'Back' to go back to menu 2: ").capitalize()
                if back == 'Back': manager()

        elif confirm == 'B':
            cr.execute("DELETE FROM student WHERE ID = ?", (id_student,))
            cr.execute(f"DROP TABLE IF EXISTS '{id_student}' ")
            delete_student()

        else: manager()
def edit_student(id):
    print("\nEdit: ")
    print("A)Name\nB)Level\nC)Password\nD)GPA\nE)Group\nF)Go back to menu 2")
    while True:
        choose = input("Enter your choice (A/B/C/D/E/F): ").capitalize()

        if choose not in ['A', 'B', 'C', 'D','E', 'F', 'Back']:
            print("Invalid choice")

        elif choose == 'A':
            name = input("Enter new name: ").capitalize()
            if name == 'Back': manager()

            # check if he wants to save changes or not
            print("A) Save\nB) Edit something else\nC) Cancel")
            while True:
                confirm = input("Enter your choice (A/B/C) : ").capitalize()

                if confirm not in ['A', 'B', 'C', 'Back']:
                    print("Invalid choice")

                if confirm == 'A':
                    cr.execute("UPDATE student SET Name = ? where ID = ?", (name, id))
                    my_data.commit()
                    print("\n ** Modified successfully **\n")
                    while True:
                        back = input("Enter 'Back' to go back to menu 2: ").capitalize()
                        if back == 'Back': manager()

                elif confirm == 'B':
                    cr.execute("UPDATE student SET Name = ? where ID = ?", (name, id))
                    edit_student(id)

                else: manager()

        elif choose == 'B':
            level = input("Enter new level: ").capitalize()
            if level == 'Back': manager()

            # check if he wants to save changes or not
            print("A) Save\nB) Edit something else\nC) Cancel")
            confirm = input("Enter your choice (A/B) : ").capitalize()

            while True:
                if confirm not in ['A', 'B', 'C', 'Back']:
                    print("Invalid choice")

                if confirm == 'A':
                    cr.execute("UPDATE student SET Level = ? where ID = ?", (level, id))
                    my_data.commit()
                    print("\n** Modified successfully **\n")
                    while True:
                        back = input("Enter 'Back' to go back to menu 2: ").capitalize()
                        if back == 'Back': manager()

                elif confirm == 'B':
                    cr.execute("UPDATE student SET Level = ? where ID = ?", (level, id))
                    edit_student(id)

                else : manager()

        elif choose == 'C':
            password = input("Enter new password: ").capitalize()
            if password == 'Back': manager()

            # check if he wants to save changes or not
            print("A) Save\nB) Edit something else\nC) Cancel")
            confirm = input("Enter your choice (A/B) : ").capitalize()

            while True:
                if confirm not in ['A', 'B', 'C', 'Back']:
                    print("Invalid choice")

                elif confirm == 'A':
                    cr.execute("UPDATE student SET Password = ? where ID = ?", (password, id))
                    my_data.commit()
                    print("\n** Modified successfully **\n")
                    while True:
                        back = input("Enter 'Back' to go back to menu 2: ").capitalize()
                        if back == 'Back': manager()

                elif confirm == 'B':
                    cr.execute("UPDATE student SET Password = ? where ID = ?", (password, id))
                    edit_student(id)

                else: manager()

        elif choose == 'D':

            # To ensure whether GPA is a valid value or not
            while True:
                gpa = input("Enter the GPA student: ").capitalize()
                if gpa == 'Back': manager()

                try:
                    gpa = float(gpa)
                    break
                except:
                    print("Invalid GPA")

            # check if he wants to save changes or not
            print("A) Save\nB) Edit something else\nC) Cancel")
            confirm = input("Enter your choice (A/B) : ").capitalize()

            while True:
                if confirm not in ['A', 'B', 'C', 'Back']:
                    print("Invalid choice")

                elif confirm == 'A':
                    cr.execute("UPDATE student SET GPA = ? where ID = ?", (gpa, id))
                    my_data.commit()
                    print("\n** Modified successfully **\n")
                    while True:
                        back = input("Enter 'Back' to go back to menu 2: ").capitalize()
                        if back == 'Back': manager()

                elif confirm == 'B':
                    cr.execute("UPDATE student SET GPA = ? where ID = ?", (gpa, id))
                    edit_student(id)

                else: manager()

        elif choose == 'E':
            print("A) Group A\nB) Group B")
            while True:
                group = input("Enter your choice (A/B) : ").capitalize()
                if group == 'Back': manager()
                elif group not in ['A', 'B']: print("Invalid choice")
                else: break

            # check if he wants to save changes or not
            print("A) Save\nB) Edit something else\nC) Cancel")
            confirm = input("Enter your choice (A/B) : ").capitalize()
            while True:
                if confirm not in ['A', 'B', 'C', 'Back']:
                    print("Invalid choice")

                elif confirm == 'A':
                    cr.execute("UPDATE student SET Group_ = ? where ID = ?", (group, id))
                    my_data.commit()
                    print("\n** Modified successfully **\n")
                    while True:
                        back = input("Enter 'Back' to go back to menu 2: ").capitalize()
                        if back == 'Back': manager()

                elif confirm == 'B':
                    cr.execute("UPDATE student SET Group_ = ? where ID = ?", (group, id))
                    edit_student(id)

                else: manager()

        else:
            manager()

def add_course():
    course = input("\nAdd the name of course: ").capitalize()
    if course == 'Back': manager()

    # while loop to ensure if course code is already found or not
    while True:
        code = input("Add the code of course: ").upper()
        if code == 'BACK': manager()
        cr.execute("SELECT * FROM courses WHERE Code = ?", (code,))
        check =cr.fetchall()
        if check != []:
            print("This code is already in use. Please choose another")
        else: break

    # check if he wants to save changes or continue
    print("A) Save\nB) Add another course\nC) Cancel")
    while True:
        confirm = input("Enter your choice (A/B/C) : ").capitalize()

        if confirm not in ['A', 'B', 'C', 'Back']:
            print("Invalid choice")

        elif confirm == 'A':
            cr.execute(" INSERT INTO courses(Course, Code) VALUES (?,?)", (course, code))
            my_data.commit()
            print("\n** added successfully **\n")
            while True :
                back = input("Enter 'Back' to go back to menu 2: ").capitalize()
                if back == 'Back': manager()

        elif confirm == 'B':
            cr.execute(" INSERT INTO courses(Course, Code) VALUES (?,?)", (course, code))
            add_course()

        else: manager()
def delete_course():
    while True:
        code = input("\nEnter the course's code: ").upper()
        if code == 'BACK': manager()

        # check if course code is valid or not
        cr.execute("SELECT * FROM courses WHERE Code = ?", (code,))
        check = cr.fetchall()
        if check == [] : print("\n* This course does not exist")
        else : break

    # check if he wants to save changes or continue
    print("A)Save\nB)Delete another course\nC) Cancel")
    while True:
        confirm = input("Enter your choice (A/B) : ").capitalize()

        if confirm not in ['A', 'B', 'C', 'Back']:
            print("Invalid choice")

        elif confirm == 'A':
            cr.execute("DELETE FROM courses WHERE Code = ?", (code,))
            my_data.commit()
            print("\n** The course has been successfully deleted **\n")
            while True :
                back = input("Enter 'Back' to go back to menu 2: ").capitalize()
                if back == 'Back': manager()

        elif confirm == 'B':
            cr.execute("DELETE FROM courses WHERE Code = ?", (code,))
            delete_course()

        else: manager()
def student_data():
    print("\n      -- Students data --")
    while True :
        id = input("\nEnter the student ID: ").capitalize()
        if id == 'Back' : manager()

        # chick if id is not existing(wrong), else it is existing
        cr.execute("select * from student where ID = ?",(id,))
        lis = cr.fetchall()
        if len(lis) != 0:
            cr.execute("select * from student where ID = ?", (id,))

            # print student data
            for row in lis:
                print()
                print("-" * 100)
                print(f"ID: {row[0]}\nName: {row[1]}\nLevel: {row[2]}\nPassword: {row[3]}\nGPA: {row[4]}\nGroup: {row[5]}")
                print("-" * 100)
                while True:
                    back = input("\nEnter 'Back' to go back to menu 2: ").capitalize()
                    if back == 'Back': manager()

        else: print("Invalid ID, Please try again")
def post_news():
    print("\n     -- News --\n")
    print("You can write here")
    news = input("=> ").capitalize()
    if news == 'Back': manager()

    # check if he wants to save changes or not
    print("A)Save\nB)Cancel)")
    while True:
        confirm = input("Enter your choice (A/B)").capitalize()

        if confirm not in ['A', 'B', 'C', 'Back']:
            print("Invalid choice")

        if confirm == 'A':
            cr.execute(f"INSERT INTO news VALUES ('{news}')")
            my_data.commit()
            print("\n** Your post has shared successfully. **\n")
            while True:
                back = input("Enter 'Back' to go back to menu 2: ").capitalize()
                if back == 'Back': manager()

        else: manager()
def login():
    print("         -- Login --\n")
    while True :
        id = input("Enter your ID : ").capitalize()
        if id == 'Back': main()
        password = input("Enter your password : ").capitalize()
        if password == 'Back': main()

        # chick if id is not existing(wrong), else it is existing
        cr.execute("SELECT * FROM student WHERE id = ? AND password = ?", (id, password))
        check = cr.fetchall()
        if check == []:
            print("\n* ID or password is wrong.\n")

        # print student data
        else:
            cr.execute(f"select * from student where ID = {id}")
            for row in check:

                print()
                print("-" * 30)
                print(f"ID: {row[0]}\nName: {row[1]}\nLevel: {row[2]}\nPassword: {row[3]}\nGPA: {row[4]}\nGroup: {row[5]}")
                print("-" * 30)
            student(id)
def register(id_student, test):
    # print courses table
    if test == 1:
        cr.execute("select * from courses ")
        lis = cr.fetchall()
        print("\n     ** The table of courses **")
        for key,row in enumerate(lis):
            if key == 0: print("-" * 50)
            print(f"course: {row[0]}, Code: {row[1]}")
            print("-" * 50)

    # loop to ensure if course code is valid or not
    while True:
        code = input("\nEnter the code of course: ").upper()
        if code == 'BACK': student(id)

        cr.execute("select * from courses where Code = ?", (code,))
        check1 = cr.fetchall()
        if check1 == []:
            print("Invalid code")

        else:       # To ensure if the course is already exist or not
            cr.execute(f"select * from '{id_student}' where Code = ?", (code,))
            check2 = cr.fetchall()
            if check2 != [] :
                print("\n* This course is already registered.")
            else: break

    # check if he wants to save changes,continue or cancel
    print("A) Save\nB) Register another course\nC) Cancel")
    while True:
        confirm = input("Enter your choice (A/B/C) : ").capitalize()

        if confirm not in ['A', 'B', 'C', 'Back']:
            print("Invalid choice")

        elif confirm == 'A':
            name_course = check1[0][0]
            cr.execute(f"insert into '{id_student}' values (?,?)", (name_course,code))
            my_data.commit()
            print("\n** successfully registered **\n")
            while True:
                back = input("Enter 'Back' to go back to menu 2: ").capitalize()
                if back == 'Back': student(id_student)

        elif confirm == 'B':
            name_course = check1[0][0]
            cr.execute(f"insert into '{id_student}' values (?,?)", (name_course, code))
            register(id_student,2)

        else: student(id_student)
def edit_course(id,test):
    # check if course is registered or not
    cr.execute(f"select * from '{id}'")
    check = cr.fetchall()
    if len(check) == 0:
        print("\n     ** No registered courses **")
        while True:
            back = input("Enter 'Back' to go back to menu 2: ").capitalize()
            if back == 'Back': student(id)

    # to print registered courses once
    if test == 1:
        print("\n    ** The table of registered courses **")
        for key, row in enumerate(check):
            if key == 0: print("-"*50)
            print(f"Course: {row[0]} , Code: {row[1]}")
        print("-"*50)

    # check if course code is valid or not
    while True:
        code = input("Enter the code of course: ").upper()
        if code == "BACK": student(id)
        cr.execute(f"select * from '{id}' where Code = ?", (code,))
        check = cr.fetchall()
        if check != []:
            break
        print("Invalid code")

    # check if he wants to save changes,continue or cancel
    print ("A) Save\nB) Delete another course\nC) Cancel")
    while True :
        confirm = input("Enter your choice (A\B\C) : ").capitalize()

        if confirm not in ['A', 'B', 'C', 'Back']:
            print("Invalid choice")

        elif confirm == "A":
            cr.execute(f"DELETE from '{id}' where Code = ?", (code,))
            my_data.commit()
            print("\n ** Done successfully **\n")
            while True:
                back = input("Enter 'Back' to go back to menu 2: ").capitalize()
                if back == "Back": student(id)

        elif confirm == "B":
            cr.execute(f"DELETE from '{id}' where Code = ?", (code,))
            edit_course(id, 2)

        else: student(id)
def Group(id):
    # to ensure whether the student is in a group or not
    cr.execute("select * from student where ID = ?", (id,))
    check = cr.fetchall()

    if check[0][5] != None :
        print(f"\n   You are in group {check[0][5]}.")
        while True:
            back = input("\nEnter 'Back' to go back to menu 2: ").capitalize()
            if back == "Back": student(id)

    # check if he wants to save changes,continue or cancel
    print("\nWhich group would you like to register with ?")
    print("A) Group A\nB) Group B")
    while True :
        group = input("Enter your choice (A\B) : ").capitalize()
        if group == "Back": student(id)

        if group not in ['A', 'B']:
            print("Invalid choice")

        else : break

    print("\nA) Save\nB) Cancel")
    while True:
        choice = input("Enter your choice (A\B) : ").capitalize()

        if choice not in ['A', 'B', 'Back']:
            print("Invalid choice")

        elif choice == "A":
            cr.execute("UPDATE student SET Group_ = ? where ID = ?",(group, id))
            my_data.commit()
            print("\n** Done successfully **\n")
            while True :
                back = input("Enter 'Back' to go back to menu 2: ").capitalize()
                if back == "Back": student(id)

        else : student(id)
def see_news(id):
    print("\n                        ** News **\n")
    cr.execute("SELECT * FROM news")
    News = reversed(cr.fetchall())
    for key, news in enumerate(News):
        if key == 0: print("-"*101)
        if len(news[0]) > 100:
            start = 0
            end = 101
            while end <= len(news[0]) :
                while news[0][end - 1] != " ":
                    end -= 1
                print(news[0][start:end])
                end += 100
                start += end-100
            end -= 100
            if end != len(news[0]) :
                print(news[0][end:])
        else : print(news[0])
        print("-" * 101)
    while True:
        back = input("\nEnter 'Back' to go back to menu 2: ").capitalize()
        if back == 'Back': student(id)

# main function which contains menus and inputs
def manager():
    print("\n     Welcome to control")
    print("        ----------")
    print("""
Menu 2
A) Add student
B) Delete student.
C) Edit student information.
D) Student information.
E) Add courses.
F) Delete courses.
G) Post news
H) Go back to menu 1""")

    while True:
        Choice = input("Enter your choice (A/B/C/D/E/F/G/H) : ").capitalize()

        if Choice not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'Back']:
            print("Invalid choice.")

        elif Choice == "A":
            print("\n     __ add students __")
            add_student()

        elif Choice == "B":
            print("\n     __ delete students __")
            delete_student()

        elif Choice == "C":
            print("\n     __ edit student data __\n")
            while True:
                id = input("Enter the student ID to edit : ").capitalize()
                if id == "Back": manager()

                # chick if id is not existing(wrong), else it is existing
                cr.execute("SELECT * FROM student WHERE ID = ?", (id,))
                lis = cr.fetchall()
                if len(lis) == 0:
                    print("\nInvalid ID")

                # print student data
                else:
                    cr.execute("SELECT * FROM student WHERE ID = ?", (id,))
                    for row in lis:
                        print("-" * 30)
                        print(f"ID: {row[0]}\nName: {row[1]}\nLevel: {row[2]}\nPassword: {row[3]}\nGPA: {row[4]}\nGroup: {row[5]}")
                        print("-" * 30)
                    edit_student(id)

        elif Choice == "D":
            student_data()

        elif Choice == "E":
            print("\n     __ Add Courses __")
            add_course()

        elif Choice == "F":
            print("\n     __ Delete courses __")
            delete_course()

        elif Choice == "G":
            post_news()

        else:
            main()
def student(id):
    print("""
Menu 2
A) Register courses.
B) Edit courses.
C) Choose his group.
D) See news
E) Back to menu 1""")
    while True :
        choice = input("Enter your choice (A/B/C/D/E): ").capitalize()

        if choice not in ['A', 'B', 'C', 'D', 'E', 'Back']:
            print("Invalid choice")
            continue

        if choice == 'A':
            print("\n     __ Courses registration __")
            register(id,1)

        elif choice == 'B':
            print("\n      Edit courses")
            print("        --------")
            edit_course(id, 1)

        elif choice == 'C':
            Group(id)

        elif choice == 'D':
            see_news(id)

        else:
            main()

def main():
    print("Menu 1\nA) Manager\nB) student\nC) Exit")
    while True:
        choice = input("Enter your choice (A/B/C) : ").upper()

        if choice == "A":
            print("*" * 29)
            print("*  Enter 'back' to go back  *")
            print("*" * 29)

            while True:
                id = input("\nEnter your ID : ").capitalize()
                if id == 'Back':  main()
                password = input("Enter your password : ").capitalize()
                if password == 'Back': main()
                if password == Password and id == ID:
                    manager()
                else:
                    print("\n* The ID or password is incorrect")

        elif choice == "B":
            print("*" * 29)
            print("*  Enter 'back' to go back  *")
            print("*" * 29)
            login()

        elif choice == "C":
            my_data.close()
            exit()

        else:
            print("Invalid choice.")


main()