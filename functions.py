import datetime
import sqlite3
import tabulate
import csv
# Users = user_id, first_name, last_name, phone, email, password, active, hire_date, date_created, user_type

#TABLES
def assessment_table():
    print()
    connection = sqlite3.connect('Capstone.db')    
    cursor = connection.cursor()
    cursor.execute ("""
    CREATE TABLE IF NOT EXISTS Assessments(
        assessment_id INTEGER PRIMARY KEY AUTOINCREMENT, 
        competency TEXT,
        assessment TEXT NOT NULL,
        date_created TEXT
        );
            """)    
    connection.commit()
def competencies_table():
    print()
    connection = sqlite3.connect('Capstone.db')    
    cursor = connection.cursor()
    cursor.execute ("""
    CREATE TABLE IF NOT EXISTS Competencies(
        competency_id INTEGER PRIMARY KEY AUTOINCREMENT, 
        competency_name TEXT NOT NULL,
        date_created TEXT
        );
            """)    
    connection.commit()
def user_table():
    print()
    connection = sqlite3.connect('Capstone.db')    
    cursor = connection.cursor()
    cursor.execute ("""
    CREATE TABLE IF NOT EXISTS Users(
        user_id INTEGER PRIMARY KEY AUTOINCREMENT, 
        first_name TEXT NOT NULL,
        last_name TEXT,
        phone TEXT,
        email TEXT  NOT NULL,
        password TEXT NOT NULL,
        active INT ,
        hire_date TEXT,
        date_created TEXT,
        user_type TEXT
        );
            """)    
    connection.commit()
def competency_assessment_results_table():
    print()
    connection = sqlite3.connect('Capstone.db')    
    cursor = connection.cursor()
    cursor.execute ("""
    CREATE TABLE IF NOT EXISTS Competency_Assessment_Results( 
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user TEXT NOT NULL,
        competency Text,
        assessment TEXT NOT NULL,
        score TEXT NOT NULL,
        date_taken TEXT,
        manager TEXT
        );
            """)    
    connection.commit()
def csv_import_assessment_results():
    con = sqlite3.connect("Capstone.db")
    cur = con.cursor()

    a_file = open("initial_assessment_result.csv")
    rows = csv.reader(a_file)
    cur.executemany("INSERT INTO Competency_Assessment_Results(user, competency, assessment, score, date_taken, manager) VALUES (?,?,?,?,?,?)", rows)
    con.commit()    

#DUMMY ACCOUNTS
def csv_import_users():
    con = sqlite3.connect("Capstone.db")
    cur = con.cursor()

    a_file = open("initial_users.csv")
    rows = csv.reader(a_file)
    cur.executemany("INSERT INTO Users(first_name, Last_name, phone, email, password, active, hire_date, user_type) VALUES (?,?,?,?,?,?,?,?)", rows)
    con.commit()
def csv_import_competencies():
    con = sqlite3.connect("Capstone.db")
    cur = con.cursor()

    a_file = open("initial_competencies.csv")
    rows = csv.reader(a_file)
    cur.executemany("INSERT INTO Competencies(competency_name, date_created) VALUES (?, ?)", rows)
    con.commit()
def csv_import_assessments():
    con = sqlite3.connect("Capstone.db")
    cur = con.cursor()

    a_file = open("initial_assessments.csv")
    rows = csv.reader(a_file)
    cur.executemany("INSERT INTO Assessments(competency, assessment, date_created) VALUES (?,?,?)", rows)
    con.commit()
def csv_import_assessment_results():
    con = sqlite3.connect("Capstone.db")
    cur = con.cursor()

    a_file = open("initial_assessment_result.csv")
    rows = csv.reader(a_file)
    cur.executemany("INSERT INTO Competency_Assessment_Results(user, competency, assessment, score, date_taken, manager) VALUES (?,?,?,?,?,?)", rows)
    con.commit()

#MENUS
def manager_menu():
    print()
    print("manager menu")
    print("__________")
    print("[1] Users:")
    print("[2] Competencies:")
    print("[3] Assessments:")
    print("[4] CSV files:")
    print("[0] Log out:")
    print("__________")
    option = int(input("Enter your selection: "))


    while option != 0:
        if option == 1:
            manager_user_menu()
        elif option == 2:
            manager_competency_menu()
        elif option == 3:
            manager_assessment_menu()
        elif option == 4:
            manager_csv_menu()
        else:
            print("Invalid option.")
    print("You are logged out")
    log_in()
def manager_competency_menu():
    print()
    print("competency menu")
    print("__________")
    print("[1] View list competencies:")
    print("[2] View report by user:")
    print("[3] Add a new competency:")
    print("[4] Update compatency:")
    print("[5] View assessment report by competency")
    print("[6] Return to previous menu:")
    print("[0] Log out:")
    print("__________")
    option = int(input("Enter your selection: "))


    while option != 0:
        if option == 1:
            manager_competency_view()
        elif option == 2:
            manager_competency_user()
        elif option == 3:
            manager_competency_add()
        elif option == 4:
            manager_update_competency()
        elif option == 5:
            manager_competency_assessment_view()
        elif option == 6:
            manager_menu()
        else:
            print("Invalid option.")
            break
    print("You are logged out")
    log_in()
def manager_user_menu():
    print()
    print("Users:")
    print("__________")
    print("[1] add")
    print("[2] view")
    print("[3] searchh")
    print("[4] update")
    print("[5] return to previous menu")
    print("[0] Log out:")
    print("__________")
    option = int(input("Enter your selection: ")) 

    while option != 0:
        if option == 1:
            user_add()
        elif option == 2:
            user_view()
        elif option == 3:
            user_search()
        elif option == 4:
            manager_user_update()
        elif option == 5:
            manager_menu ()
        else:
            print("Invalid option.")
    print("You are logged out") 
    log_in()
def manager_assessment_menu ():
    print()
    print("Assessment menu")
    print("__________")
    print("[1] View assesments")
    print("[2] View report by assessment:")
    print("[3] View report by user:")
    print("[4] Add a new assessment:")
    print("[5] Add new assessment score:")
    print("[6] Update assessment:")
    print("[7] Update assessment result:")
    print("[8] Delete assessment result:")
    print("[9] Return to previous menu:")
    print("[0] Log out:")
    print("__________")
    option = int(input("Enter your selection: "))


    while option != 0:
        if option == 1:
            manager_assessment()
        if option == 2:
            manager_assessment_view_assessment()
        elif option == 3:
            manager_assessment_view_user()
        elif option == 4:
            add_assessment()
        elif option == 5:
            add_assessment_result()
        elif option == 6:
            manager_update_Assessments()
        elif option == 7:
            manager_update_assessment_result()
        elif option == 8:
            delete_assessment_result()
        elif option == 9:
            manager_menu()
        else:
            print("Invalid option.")
            break
    print("You are logged out")
    log_in()
def manager_csv_menu ():
    print()
    print("CSV menu")
    print("__________")
    print("[1] Create user csv file:")
    print("[2] Create competency csv file:")
    print("[3] Create assessment csv file:")
    print("[4] Create assessment results csv file:")
    print("[5] create assessment csv file by user:")
    print("[6] Creat assessment csv file by Competency:")
    print("[7] Import assessment result csv file:")
    print("[8] Previous menu:")
    print("[0] Log out:")
    print("__________")
    option = int(input("Enter your selection: "))


    while option != 0:
        if option == 1:
            export_manager_csv_user()
        elif option == 2:
            export_manager_csv_competency()
        elif option == 3:
            export_manager_csv_assessment()
        elif option == 4:
            export_manager_csv_assessment_result()
        elif option == 5:
            export_csv_user_assessment_results()
        elif option == 6:
            export_csv_assessment_results_competency()
        elif option == 7:
            csv_import()
        elif option == 8:
            manager_menu()
        else:
            print("Invalid option.")
            break
    print("You are logged out")
    log_in()

#VIEW
def user_view():
    print()
    connection = sqlite3.connect('capstone.db')    
    cursor = connection.cursor()
    connection.commit()

    customers = cursor.execute("select * from Users ORDER BY last_name")
    customers_data = []
    for row in customers:
        customer= {"User ID":row[0], "First name":row[1], "Last name":row[2], "Phone number":row[3], "Email address":row[4], "Hire date":row[7], "User type":row[9]}
        customers_data.append(customer)
    header = customers_data[0].keys()
    rows =  [x.values() for x in customers_data]
    print(tabulate.tabulate(rows, header))
    manager_user_menu()
def user_search():
    print()
    connection = sqlite3.connect('capstone.db')    
    cursor = connection.cursor()
    connection.commit()

    SQL_SEARCH = ("""SELECT *
                    FROM Users 
                    WHERE first_name = ? OR last_name = ?;
    """)
    f_name = input("Enter first name of the user: ")
    l_name = input("Enter last name of the user: ")
    customers = cursor.execute(SQL_SEARCH, (f_name, l_name))

    customers_data = []
    for row in customers:
        customer= {"User ID":row[0], "First name":row[1], "Last name":row[2], "Phone number":row[3], "Email address":row[4], "Hire date":row[7], "User type":row[9]}
        customers_data.append(customer)
    header = customers_data[0].keys()
    rows =  [x.values() for x in customers_data]
    print(tabulate.tabulate(rows, header))
    manager_user_menu()
def manager_competency_view ():
    print()
    connection = sqlite3.connect('capstone.db')    
    cursor = connection.cursor()
    connection.commit()

    customers = cursor.execute("select * from Competencies")
    customers_data = []
    for row in customers:
        customer= {"Competency ID":row[0], "Competency name":row[1], "Date created":row[2]}
        customers_data.append(customer)
    header = customers_data[0].keys()
    rows =  [x.values() for x in customers_data]
    print(tabulate.tabulate(rows, header))
    manager_competency_menu()
def manager_competency_user():
    print()
    connection = sqlite3.connect('capstone.db')    
    cursor = connection.cursor()
    connection.commit()

    user = input("Enter user: ")
    SQL_VIEW = ("select * from Competency_Assessment_Results WHERE user = ? ORDER BY competency")
    customers = cursor.execute(SQL_VIEW, (user,))
    customers_data = []
    for row in customers:
        customer= {"Assessment ID":row[0], "User":row[1], "Competency":row[2], "Assessment":row[3], "Score":row[4], "Date taken":row[5], "Manager":row[6]}
        customers_data.append(customer)
    header = customers_data[0].keys()
    rows =  [x.values() for x in customers_data]
    print(tabulate.tabulate(rows, header))
    manager_competency_menu()
def manager_assessment_view_assessment():
    print()
    connection = sqlite3.connect('capstone.db')    
    cursor = connection.cursor()
    connection.commit()
    customers = cursor.execute("select * from Competencies")
    customers_data = []
    for row in customers:
        customer= {"ID":row[0], "Competency name":row[1]}
        customers_data.append(customer)
    header = customers_data[0].keys()
    rows =  [x.values() for x in customers_data]
    print(tabulate.tabulate(rows, header))
    print()
    competency = input("competency that assessment measures: ")

    SQL_SEARCH = ("""SELECT * 
                        FROM Assessments
                        WHERE competency = ?
                        ;
        """)  
    cursor = connection.cursor()
    customers = cursor.execute(SQL_SEARCH, (competency,))
    customers_data = []
    for row in customers:
        customer= {"ID":row[0], "competency":row[1], "assessment":row[2], "date created":row[3]}
        customers_data.append(customer)
    header = customers_data[0].keys()
    rows =  [x.values() for x in customers_data]
    print(tabulate.tabulate(rows, header))
    print()
    assessment = input("Pick an assessment: ")

    print()
    connection = sqlite3.connect('capstone.db')    
    cursor = connection.cursor()
    connection.commit()
    SQL_VIEW = ("select * from Competency_Assessment_Results WHERE competency = ? AND assessment = ? ORDER BY competency")
    customers = cursor.execute(SQL_VIEW, (competency, assessment,))
    customers_data = []
    for row in customers:
        customer= {"Assessment ID":row[0], "User":row[1], "Competency":row[2], "Assessment":row[3], "Score":row[4], "Date taken":row[5], "Manager":row[6]}
        customers_data.append(customer)
    header = customers_data[0].keys()
    rows =  [x.values() for x in customers_data]
    print(tabulate.tabulate(rows, header))
    manager_assessment_menu()
def manager_assessment_view_user():
    print()
    connection = sqlite3.connect('capstone.db')    
    cursor = connection.cursor()
    connection.commit()
    customers = cursor.execute("select * from Users")
    customers_data = []
    for row in customers:
        customer= {"ID":row[0], "first name":row[1], "last name":row[2], "email/user name":row[4]}
        customers_data.append(customer)
    header = customers_data[0].keys()
    rows =  [x.values() for x in customers_data]
    print(tabulate.tabulate(rows, header))
    print()
    user = input("Inpute user email: ")
    
    print()
    connection = sqlite3.connect('capstone.db')    
    cursor = connection.cursor()
    connection.commit()
    SQL_VIEW = ("select * from Competency_Assessment_Results WHERE user = ? ORDER BY competency")
    customers = cursor.execute(SQL_VIEW, (user,))
    customers_data = []
    for row in customers:
        customer= {"Assessment ID":row[0], "User":row[1], "Competency":row[2], "Assessment":row[3], "Score":row[4], "Date taken":row[5], "Manager":row[6]}
        customers_data.append(customer)
    header = customers_data[0].keys()
    rows =  [x.values() for x in customers_data]
    print(tabulate.tabulate(rows, header))
    manager_assessment_menu()
def manager_assessment():
    print()
    connection = sqlite3.connect('capstone.db')    
    cursor = connection.cursor()
    connection.commit()

    customers = cursor.execute("select * from Assessments")
    customers_data = []
    for row in customers:
        customer= {"Assessment ID":row[0], "Competency name":row[1], "Assessment name":row[2], "Date created":row[3]}
        customers_data.append(customer)
    header = customers_data[0].keys()
    rows =  [x.values() for x in customers_data]
    print(tabulate.tabulate(rows, header))
    manager_assessment_menu ()
def manager_competency_assessment_view():
    print()
    connection = sqlite3.connect('capstone.db')    
    cursor = connection.cursor()
    connection.commit()
    customers = cursor.execute("select * from Competencies")
    customers_data = []
    for row in customers:
        customer= {"ID":row[0], "Competency name":row[1]}
        customers_data.append(customer)
    header = customers_data[0].keys()
    rows =  [x.values() for x in customers_data]
    print(tabulate.tabulate(rows, header))
    print()
    competency = input("competency that assessment measures: ")

    SQL_SEARCH = ("""SELECT * 
                        FROM Competency_Assessment_results
                        WHERE competency = ?
                        ;
        """)  
    cursor = connection.cursor()
    customers = cursor.execute(SQL_SEARCH, (competency,))
    customers_data = []
    for row in customers:
        customer= {"ID":row[0], "User":row[1], "Competency":row[2], "Assessment":row[3], "Score":row[4], "Date taken":row[5], "Manager":row[6]}
        customers_data.append(customer)
    header = customers_data[0].keys()
    rows =  [x.values() for x in customers_data]
    print(tabulate.tabulate(rows, header))
    manager_competency_menu()


#ADD
def user_add():
    print()
    class User:
        def __init__(self):
            self.first_name = input("Enter first name: ")
            self.last_name = input("Enter last name: ")
            self.phone = input("Enter phone: ")
            self.email  = input("Enter email address: ")
            self.password = input("Enter password: ")
            self.active = 1
            self.hire_date = input("Enter date hired: ")
            self.date_created = datetime.datetime.today()
            self.user_type = "user"

    def add(values):
        SQL_INSERT = ("""INSERT INTO Users(first_name, last_name, phone, email, password, active, hire_date, date_created, user_type) 
                VALUES (?,?,?,?,?,?,?,?,?);
        """)
        connection = sqlite3.connect('Capstone.db')    
        cursor = connection.cursor()
        cursor.execute(SQL_INSERT, values)
        connection.commit()
    u = User()
    add((u.first_name, u.last_name, u.phone, u.email, u.password, u.active, u.hire_date, u.date_created, u.user_type))
    manager_user_menu()
def manager_competency_add():
    print()
    class Comp:
        def __init__(self):
            self.competency_name = input("Enter name of Competency: ")
            self.date_created = datetime.datetime.today()

    def add(values):
        SQL_INSERT = ("""INSERT INTO Competencies(competency_name, date_created) 
                VALUES (?, ?);
        """)
        connection = sqlite3.connect('Capstone.db')    
        cursor = connection.cursor()
        cursor.execute(SQL_INSERT, values)
        connection.commit()
    u = Comp()
    add((u.competency_name, u.date_created))
    manager_competency_menu()
def add_assessment():
    connection = sqlite3.connect('capstone.db')    
    cursor = connection.cursor()
    connection.commit()

    customers = cursor.execute("select * from Competencies")
    customers_data = []
    for row in customers:
        customer= {"ID":row[0], "Competency name":row[1]}
        customers_data.append(customer)
    header = customers_data[0].keys()
    rows =  [x.values() for x in customers_data]
    print(tabulate.tabulate(rows, header))
    print()

    competency = input("competency that assessment measures: ")

    SQL_INSERT = ("""INSERT INTO Assessments(assessment, competency, date_created) 
            VALUES (?,?,?);
    """)
    assess = input("Enter new assessment: ")
    date_created = datetime.datetime.today()
    connection = sqlite3.connect('Capstone.db')    
    cursor = connection.cursor()
    cursor.execute(SQL_INSERT, (competency, assess, date_created))
    connection.commit()
    manager_assessment_menu()
def add_assessment_result():
    connection = sqlite3.connect('capstone.db')    
    cursor = connection.cursor()
    connection.commit()

    users = cursor.execute("select * from Users")
    users_data = []
    for row in users:
        user= {"user ID":row[0], "first name":row[1], "last name":row[2], "email":row[4]}
        users_data.append(user)
    header = users_data[0].keys()
    rows =  [x.values() for x in users_data]
    print(tabulate.tabulate(rows, header))
    print()
    user = input("Enter user email: ")

    customers = cursor.execute("select * from Competencies")
    customers_data = []
    for row in customers:
        customer= {"ID":row[0], "Competency name":row[1]}
        customers_data.append(customer)
    header = customers_data[0].keys()
    rows =  [x.values() for x in customers_data]
    print(tabulate.tabulate(rows, header))
    print()
    competency = input("competency: ")

    SQL_SEARCH = ("""SELECT * 
                        FROM Assessments
                        WHERE competency = ?
                        ;
        """)  
    cursor = connection.cursor()
    customers = cursor.execute(SQL_SEARCH, (competency,)).fetchall() 
    customers_data = []
    for row in customers:
        customer= {"ID":row[0], "competency":row[1], "assessment":row[2], "date created":row[3]}
        customers_data.append(customer)
    header = customers_data[0].keys()
    rows =  [x.values() for x in customers_data]
    print(tabulate.tabulate(rows, header))
    print()
    assess = input("Enter new assessment: ")

    print("Competencies are measured and tracked on a scale from 0-4:")
    print("0 - No competency - Needs Training and Direction")
    print("1 - Basic Competency - Needs Ongoing Support")
    print("2 - Intermediate Competency - Needs Occasional Support")
    print("3 - Advanced Competency - Completes Task Independently")
    print("4 - Expert Competency - Can Effectively pass on this knowledge and can initiate optimizations")
    print()

    SQL_INSERT = ("""INSERT INTO Competency_Assessment_Results(user, competency, assessment, score, date_taken, manager) 
            VALUES (?,?,?,?,?,?);
    """)
    date_taken = datetime.datetime.today()
    score = input("Enter competency score: ")
    manager = input("Enter your (manager) email: ")
    connection = sqlite3.connect('Capstone.db')    
    cursor = connection.cursor()
    cursor.execute(SQL_INSERT, (user, competency, assess, score, date_taken, manager))
    connection.commit()
    manager_assessment_menu()

#EDIT
def user_update():
    print()
    class Table():
        def __init__(self, user_id, first_name, last_name, phone, email, password, active, hire_date, date_created, user_type):
            self.user_id = user_id
            self.first_name = first_name
            self.last_name = last_name
            self.phone = phone
            self.email = email
            self.password = password
            self.active = active
            self.hire_date = hire_date
            self.date_created = date_created
            self.user_type = user_type

        def print_me (self):
            print(f'user ID:       {self.user_id}')
            print(f'first name:    {self.first_name}')
            print(f'last name:     {self.last_name}')
            print(f'phone:         {self.phone}')
            print(f'email:         {self.email}')
            print(f'password:        #########')
            print(f'date hired:     {self.hire_date}')
            print(f'user privlages: {self.user_type}')

    def select():
        print()
        SQL_SEARCH = ("""SELECT * 
                        FROM Users
                        WHERE email = ?
                        ;
        """)
        email = input("Please confirm your email address: ")
        connection = sqlite3.connect('Capstone.db')    
        cursor = connection.cursor()
        rows = cursor.execute(SQL_SEARCH, (email,)).fetchone() 
        while True:
            if rows != None:
                return rows[0],rows[1],rows[2],rows[3],rows[4],rows[5],rows[6],rows[7],rows[8],rows[9]
            else:
                print("Incorect user name")
                user_update()
            break
        
    user_id, first_name, last_name, phone, email, password, active, hire_date, date_created, user_type = select()
    my_user = Table(user_id, first_name, last_name, phone, email, password, active, hire_date, date_created, user_type)
#user_id, first_name, last_name, phone, email, password, active, hire_date, date_created, user_type
    my_user.print_me()
    object = input("Enter the field would you like to update or press 0 to submit: ")
    while object != "0":  
        if object == "user ID":
            print("Can not be updated.")   
        elif object == "first name":
            my_user.first_name = input("Input your updated first name: ")
        elif object == "last name":
            my_user.last_name = input("Input your updated last name: ")
        elif object == "phone":
            my_user.phone = input("Input your updated phone number: ")
        elif object == "email":
            my_user.email = input("Input your updated email: ")
        elif object == "password":
            my_user.password = input("Input your updated password: ")
            print(f'New password {my_user.password}')
        elif object == "date hired":
            print("Can not be updated.") 
        elif object == "user privlages":
            print("Can not be updated.") 
        else:
            print("Invalid entry, try again.")
        my_user.print_me()
        object = input("Enter the field would you like to update or press 0 to submit: ")

    print()
    print("Your information has been updated.")

    SQL_UPDATE = ("""UPDATE Users 
                        SET first_name = ?,
                            last_name = ?,
                            phone = ?,
                            email = ?,
                            password = ?
                        WHERE user_id = ?;
    """)
    connection = sqlite3.connect('Capstone.db')    
    cursor = connection.cursor()
    cursor.execute(SQL_UPDATE, (my_user.first_name, my_user.last_name, my_user.phone, my_user.email, my_user.password, user_id))
    connection.commit()
def manager_user_update():
    print()
    class Table():
        def __init__(self, user_id, first_name, last_name, phone, email, password, active, hire_date, date_created, user_type):
            self.user_id = user_id
            self.first_name = first_name
            self.last_name = last_name
            self.phone = phone
            self.email = email
            self.password = password
            self.active = active
            self.hire_date = hire_date
            self.date_created = date_created
            self.user_type = user_type

        def print_me (self):
            print(f'user ID:       {self.user_id}')
            print(f'first name:    {self.first_name}')
            print(f'last name:     {self.last_name}')
            print(f'phone:         {self.phone}')
            print(f'email:         {self.email}')
            print(f'password:        #########')
            print(f'date hired:     {self.hire_date}')
            print(f'user privlages: {self.user_type}')
            print(f'active:         {self.active}')

    def select():
        SQL_SEARCH = ("""SELECT * 
                        FROM Users
                        WHERE last_name = ? AND 
                        first_name = ?;
        """)
        last = input("Enter user last name: ")
        first = input("Enter user first name: ")
        connection = sqlite3.connect('Capstone.db')    
        cursor = connection.cursor()
        rows = cursor.execute(SQL_SEARCH, (last, first)).fetchone() 
        while True:
            if rows != None:
                return rows[0],rows[1],rows[2],rows[3],rows[4],rows[5],rows[6],rows[7],rows[8],rows[9]
            else:
                print("Incorect user name")
            manager_menu()
        
    user_id, first_name, last_name, phone, email, password, active, hire_date, date_created, user_type = select()
    my_user = Table(user_id, first_name, last_name, phone, email, password, active, hire_date, date_created, user_type)
#user_id, first_name, last_name, phone, email, password, active, hire_date, date_created, user_type
    my_user.print_me()
    object = input("Enter the field would you like to update or press 0 to submit: ")
    while object != "0":  
        if object == "user ID":
            my_user.user_id = input("Input updated user id: ")     
        elif object == "first name":
            my_user.first_name = input("Input updated first name: ")
        elif object == "last name":
            my_user.last_name = input("Input updated last name: ")
        elif object == "phone":
            my_user.phone = input("Input updated phone number: ")
        elif object == "email":
            my_user.email = input("Input updated email: ")
        elif object == "password":
            my_user.password = input("Input updated password: ")
            print(f'New password {my_user.password}')
        elif object == "date hired":
            my_user.hire_date = input("Input updated hire date: ")
        elif object == "user privlages":
            my_user.user_type = input("Enter either manager or user: ")  
        elif object == "active":
            my_user.active = input("Enter 1 for active and 0 for inactive: ") 
        else:
            print("Invalid entry, try again.")
        my_user.print_me()
        object = input("Enter the field would you like to update or press 0 to submit: ")

    print()
    print("Your information has been updated.")

    SQL_UPDATE = ("""UPDATE Users 
                        SET user_id = ?,
                            first_name = ?,
                            last_name = ?,
                            phone = ?,
                            email = ?,
                            password = ?,
                            hire_date = ?,
                            user_type = ?,
                            active = ?
                        WHERE user_id = ?;
    """)
    connection = sqlite3.connect('Capstone.db')    
    cursor = connection.cursor()
    cursor.execute(SQL_UPDATE, (my_user.user_id, my_user.first_name, my_user.last_name, my_user.phone, my_user.email, my_user.password, my_user.hire_date, my_user.user_type, my_user.active, user_id))
    connection.commit()

    SQL_UP = ("""UPDATE Competency_Assessment_Results 
                        SET user = ?
                        WHERE user = ?;
    """)
    connection = sqlite3.connect('Capstone.db')    
    cursor = connection.cursor()
    cursor.execute(SQL_UP, (my_user.email, email))
    connection.commit()
    manager_user_menu()
def manager_update_competency():
    connection = sqlite3.connect('capstone.db')    
    cursor = connection.cursor()
    connection.commit()

    customers = cursor.execute("select * from Competencies")
    customers_data = []
    for row in customers:
        customer= {"ID":row[0], "Competency name":row[1]}
        customers_data.append(customer)
    header = customers_data[0].keys()
    rows =  [x.values() for x in customers_data]
    print(tabulate.tabulate(rows, header))
    print()

    competency = input("Enter competency you wish to edit: ")

    SQL_UPDATE = ("""UPDATE Competencies 
                        SET competency_name = ?
                        WHERE competency_name = ?;
    """)
    new_name = input("enter new competency name: ")
    connection = sqlite3.connect('Capstone.db')    
    cursor = connection.cursor()
    cursor.execute(SQL_UPDATE, (new_name, competency))
    connection.commit()

    upt = input("Do you want to update everywhere? type 1 for yes a 2 for no: ")
    while True:
        if upt == "1":
                SQL_UPDATE = ("""UPDATE Assessments 
                        SET competency = ?
                        WHERE competency = ?;
                """)
                connection = sqlite3.connect('Capstone.db')    
                cursor = connection.cursor()
                cursor.execute(SQL_UPDATE, (new_name, competency))
                connection.commit()

                SQL_UP = ("""UPDATE Competency_Assessment_Results 
                        SET competency = ?
                        WHERE competency = ?;
                """)
                connection = sqlite3.connect('Capstone.db')    
                cursor = connection.cursor()
                cursor.execute(SQL_UP, (new_name, competency))
                connection.commit()
                print("updated")
        elif upt =="2":
            print("Only update in competencies.")
        else:
            print("Invalid option.")    
        break    
    manager_competency_menu()
def manager_update_Assessments():
    connection = sqlite3.connect('capstone.db')    
    cursor = connection.cursor()
    connection.commit()

    customers = cursor.execute("select * from Assessments")
    customers_data = []
    for row in customers:
        customer= {"ID":row[0], "Competency name":row[1], "assessment name":row[2]}
        customers_data.append(customer)
    header = customers_data[0].keys()
    rows =  [x.values() for x in customers_data]
    print(tabulate.tabulate(rows, header))
    print()

    assessment = input("Enter assessment you wish to edit: ")
    competency = input("enter competency this assessment is associated with: ")

    SQL_UPDATE = ("""UPDATE Assessments 
                        SET assessment = ?
                        WHERE assessment = ? AND competency = ?;
    """)
    new_name = input("enter new assessment name: ")
    connection = sqlite3.connect('Capstone.db')    
    cursor = connection.cursor()
    cursor.execute(SQL_UPDATE, (new_name, assessment, competency))
    connection.commit()

    upt = input("Do you want to update everywhere? type 1 for yes a 2 for no: ")
    while True:
        if upt == "1":
                SQL_UPDATE = ("""UPDATE Competency_Assessment_results 
                        SET assessment = ?
                        WHERE assessment = ? AND competency = ?;
                """)
                connection = sqlite3.connect('Capstone.db')    
                cursor = connection.cursor()
                cursor.execute(SQL_UPDATE, (new_name, assessment, competency))
                connection.commit()
                print("updated")
        elif upt =="2":
            print("Only updated in Assessments.")
        else:
            print("Invalid option.")    
        break   
    manager_assessment_menu() 
def manager_update_assessment_result():
    connection = sqlite3.connect('capstone.db')    
    cursor = connection.cursor()
    connection.commit()

    customers = cursor.execute("select * from Competency_Assessment_Results")
    customers_data = []
    for row in customers:
        customer= {"Assessment results ID":row[0], "Competency name":row[1], "Assessment name":row[2], "Score":row[3], "Date taken":row[4], "Manager":row[5]}
        customers_data.append(customer)
    header = customers_data[0].keys()
    rows =  [x.values() for x in customers_data]
    print(tabulate.tabulate(rows, header))
    print()

    score = input("Enter the Assessment results ID that you would like to update the score for: ")
    print()
    print("Competencies are measured and tracked on a scale from 0-4:")
    print("0 - No competency - Needs Training and Direction")
    print("1 - Basic Competency - Needs Ongoing Support")
    print("2 - Intermediate Competency - Needs Occasional Support")
    print("3 - Advanced Competency - Completes Task Independently")
    print("4 - Expert Competency - Can Effectively pass on this knowledge and can initiate optimizations")
    print()

    SQL_UPDATE = ("""UPDATE Competency_Assessment_Results
                        SET score = ?
                        WHERE id = ?;
    """)
    new_score = input("enter new assessment score: ")
    connection = sqlite3.connect('Capstone.db')    
    cursor = connection.cursor()
    cursor.execute(SQL_UPDATE, (new_score, score))
    connection.commit()
    manager_assessment_menu()

#DELETE
def delete_assessment_result():
    connection = sqlite3.connect('capstone.db')    
    cursor = connection.cursor()
    connection.commit()

    customers = cursor.execute("select * from Competency_Assessment_Results")
    customers_data = []
    for row in customers:
        customer= {"Assessment results ID":row[0], "Competency name":row[1], "Assessment name":row[2], "Score":row[3], "Date taken":row[4], "Manager":row[5]}
        customers_data.append(customer)
    header = customers_data[0].keys()
    rows =  [x.values() for x in customers_data]
    print(tabulate.tabulate(rows, header))
    print()

    id = input("Enter the Assessment results ID that you would like to delete(This can not be undone): ")

    SQL_DELETE = ("""DELETE FROM Competency_Assessment_Results WHERE id = ?;
    """)
    connection = sqlite3.connect('Capstone.db')    
    cursor = connection.cursor()
    cursor.execute(SQL_DELETE, (id,))
    connection.commit()
    manager_assessment_menu()

#EXPORT
def export_csv_assessment_results_competency():
    connection = sqlite3.connect('capstone.db')    
    cursor = connection.cursor()
    connection.commit()

    SQL_CSV = ("select * from Competency_Assessment_Results WHERE competency = ? ")
    comp = input("Enter Competency:")
    customers = cursor.execute(SQL_CSV, (comp,))
    customers_data = []
    for row in customers:
        customer= {"User ID":row[1], "competency_id":row[2], "assessment_id":row[3], "score":row[4], "date_taken":row[5]}
        customers_data.append(customer)
    header = customers_data[0].keys()
    rows =  [x.values() for x in customers_data]
    print(tabulate.tabulate(rows, header))

    with open('user_assessment.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(rows)
        manager_csv_menu ()
def export_csv_user_assessment_results():
    connection = sqlite3.connect('capstone.db')    
    cursor = connection.cursor()
    connection.commit()

    SQL_CSV = ("select * from Competency_Assessment_Results WHERE user = ? ")
    user = input("Enter user email:")
    customers = cursor.execute(SQL_CSV, (user,))
    customers_data = []
    for row in customers:
        customer= {"User ID":row[1], "competency_id":row[2], "assessment_id":row[3], "score":row[4], "date_taken":row[5]}
        customers_data.append(customer)
    header = customers_data[0].keys()
    rows =  [x.values() for x in customers_data]
    print(tabulate.tabulate(rows, header))

    with open('user_assessment.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(rows)
        manager_csv_menu ()
def export_manager_csv_user():
    connection = sqlite3.connect('capstone.db')    
    cursor = connection.cursor()
    connection.commit()

    customers = cursor.execute("select * from Users ORDER BY user_id")
    customers_data = []
    for row in customers:
        customer= {"User ID":row[0], "First name":row[1], "Last name":row[2], "Phone":row[3], "Email":row[4], "Password":row[5], "active":row[6], "hire date":row[7], "date created":row[8], "user type":row[9]}
        customers_data.append(customer)
    header = customers_data[0].keys()
    rows =  [x.values() for x in customers_data]
    print(tabulate.tabulate(rows, header))

    with open('manager_csv_user.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(rows)
        manager_csv_menu ()
def export_manager_csv_competency():
    connection = sqlite3.connect('capstone.db')    
    cursor = connection.cursor()
    connection.commit()

    customers = cursor.execute("select * from Competencies ORDER BY competency_id")
    customers_data = []
    for row in customers:
        customer= {"Competency ID":row[0], "Competency name":row[1], "Date created":row[2]}
        customers_data.append(customer)
    header = customers_data[0].keys()
    rows =  [x.values() for x in customers_data]
    print(tabulate.tabulate(rows, header))

    with open('manager_csv_competency.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(rows)
        manager_csv_menu ()
def export_manager_csv_assessment():
    connection = sqlite3.connect('capstone.db')    
    cursor = connection.cursor()
    connection.commit()

    customers = cursor.execute("select * from Assessments ORDER BY assessment_id")
    customers_data = []
    for row in customers:
        customer= {"Assessment ID":row[0], "Competency name":row[1], "Assessment name":row[2], "Date created":row[3]}
        customers_data.append(customer)
    header = customers_data[0].keys()
    rows =  [x.values() for x in customers_data]
    print(tabulate.tabulate(rows, header))

    with open('manager_csv_assessment.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(rows)
        manager_csv_menu ()
def export_manager_csv_assessment_result():
    connection = sqlite3.connect('capstone.db')    
    cursor = connection.cursor()
    connection.commit()

    customers = cursor.execute("select * from Competency_Assessment_Results ORDER BY competency")
    customers_data = []
    for row in customers:
        customer= {"Assessment id":row[0], "User":row[1], "Competency name":row[2], "Assessment name":row[3], "Score":row[4], "Date taken":row[5], "Manager":row[6]}
        customers_data.append(customer)
    header = customers_data[0].keys()
    rows =  [x.values() for x in customers_data]
    print(tabulate.tabulate(rows, header))

    with open('manager_csv_assessment_result.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(rows)
        manager_csv_menu ()
def csv_import():
    con = sqlite3.connect("Capstone.db")
    cur = con.cursor()

    a_file = open("assessment_result.csv")
    rows = csv.reader(a_file)
    cur.executemany("INSERT INTO Competency_Assessment_Results(user, competency, assessment, score, date_taken, manager) VALUES (?,?,?,?,?,?)", rows)
    con.commit()
    customers =cur.execute("SELECT * FROM Competency_Assessment_Results")
    customers_data = []
    for row in customers:
        customer= {"ID":row[0], "User":row[1], "Competency":row[2], "Assessment":row[3], "Score":row[4], "Date taken":row[5], "Manager":row[6]}
        customers_data.append(customer)
    header = customers_data[0].keys()
    rows =  [x.values() for x in customers_data]
    print(tabulate.tabulate(rows, header))

def log_in():
    print()
    print("***Welcomw to your Competency Tracking Tool***")
    print("_______________________________________________")
    print()
    print("Please log in to continue")
    print()

    log_email = input("Enter your user name or email: ")
    log_password = input("Enter your password: ")
    SQL_USER = ("""SELECT user_type 
                    FROM Users
                    WHERE email = ? AND
                    password = ? AND
                    active = 1
                    ; 
                    """)
    connection = sqlite3.connect('Capstone.db')    
    cursor = connection.cursor()
    rows = cursor.execute(SQL_USER, (log_email, log_password)).fetchone()
    print(rows)
    while True:
        if rows == ('user',):
            print()
            print("user menu")
            print("__________")
            print("[1] Update personal info.")
            print("[2] View competency and assessment data.")
            print("[0] Log out.")
            option = int(input("Enter your selection: "))


            while option != 0:
                if option == 1:
                    print()
                    class Table():
                        def __init__(self, user_id, first_name, last_name, phone, email, password, active, hire_date, date_created, user_type):
                            self.user_id = user_id
                            self.first_name = first_name
                            self.last_name = last_name
                            self.phone = phone
                            self.email = email
                            self.password = password
                            self.active = active
                            self.hire_date = hire_date
                            self.date_created = date_created
                            self.user_type = user_type

                        def print_me (self):
                            print(f'user ID:       {self.user_id}')
                            print(f'first name:    {self.first_name}')
                            print(f'last name:     {self.last_name}')
                            print(f'phone:         {self.phone}')
                            print(f'email:         {self.email}')
                            print(f'password:        #########')
                            print(f'date hired:     {self.hire_date}')
                            print(f'user privlages: {self.user_type}')

                    def select():
                        print()
                        SQL_SEARCH = ("""SELECT * 
                                        FROM Users
                                        WHERE email = ?
                                        ;
                        """)
                        connection = sqlite3.connect('Capstone.db')    
                        cursor = connection.cursor()
                        rows = cursor.execute(SQL_SEARCH, (log_email,)).fetchone() 
                        while True:
                            if rows != None:
                                return rows[0],rows[1],rows[2],rows[3],rows[4],rows[5],rows[6],rows[7],rows[8],rows[9]
                            else:
                                print("Incorect user name")
                                user_update()
                            break
                        
                    user_id, first_name, last_name, phone, email, password, active, hire_date, date_created, user_type = select()
                    my_user = Table(user_id, first_name, last_name, phone, email, password, active, hire_date, date_created, user_type)
                #user_id, first_name, last_name, phone, email, password, active, hire_date, date_created, user_type
                    my_user.print_me()
                    object = input("Enter the field would you like to update or press 0 to submit: ")
                    while object != "0":  
                        if object == "user ID":
                            print("Can not be updated.")   
                        elif object == "first name":
                            my_user.first_name = input("Input your updated first name: ")
                        elif object == "last name":
                            my_user.last_name = input("Input your updated last name: ")
                        elif object == "phone":
                            my_user.phone = input("Input your updated phone number: ")
                        elif object == "email":
                            my_user.email = input("Input your updated email: ")
                        elif object == "password":
                            my_user.password = input("Input your updated password: ")
                            print(f'New password {my_user.password}')
                        elif object == "date hired":
                            print("Can not be updated.") 
                        elif object == "user privlages":
                            print("Can not be updated.") 
                        else:
                            print("Invalid entry, try again.")
                        my_user.print_me()
                        object = input("Enter the field would you like to update or press 0 to submit: ")

                    print()
                    print("Your information has been updated.")

                    SQL_UPDATE = ("""UPDATE Users 
                                        SET first_name = ?,
                                            last_name = ?,
                                            phone = ?,
                                            email = ?,
                                            password = ?
                                        WHERE user_id = ?;
                    """)
                    connection = sqlite3.connect('Capstone.db')    
                    cursor = connection.cursor()
                    cursor.execute(SQL_UPDATE, (my_user.first_name, my_user.last_name, my_user.phone, my_user.email, my_user.password, user_id))
                    connection.commit()

                    SQL_UP = ("""UPDATE Competency_Assessment_Results 
                    SET user = ?
                    WHERE user = ?;
                    """)
                    connection = sqlite3.connect('Capstone.db')    
                    cursor = connection.cursor()
                    cursor.execute(SQL_UP, (my_user.email, email))
                    connection.commit()
                    log_in()
                elif option == 2:
                    print()
                    connection = sqlite3.connect('capstone.db')    
                    cursor = connection.cursor()
                    connection.commit()

                    
                    SQL_VIEW = ("select * from Competency_Assessment_Results WHERE user = ? ORDER BY competency")
                    customers = cursor.execute(SQL_VIEW, (log_email,))
                    customers_data = []
                    for row in customers:
                        customer= {"Assessment ID":row[0], "User":row[1], "Competency":row[2], "Assessment":row[3], "Score":row[4], "Date taken":row[5], "Manager":row[6]}
                        customers_data.append(customer)
                    header = customers_data[0].keys()
                    rows =  [x.values() for x in customers_data]
                    print(tabulate.tabulate(rows, header))
                    log_in()
                else:
                    print("Invalid option.")
            print("You are logged out")
        elif rows == ('manager',):
            manager_menu()
        elif rows == None:
            print("Incorect credentials, try aqain: ")
            print()
            log_in()
        break