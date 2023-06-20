import mysql.connector

# GLOBAL VALUES
mydb = ""
mycursor = ""


# SETTING UP CONNECTION
def myconnection():
    global mydb
    global mycursor
    UserName = input("\n ENTER MYSQL SERVER'S USERNAME : ")
    password = input("ENTER MYSQL SERVER'S PASSWORD : ")
    mydb = mysql.connector.connect(host="localhost", user=UserName, passwd=password)
    if mydb:
        print("\n         CONNECTED          \n")
        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE TIMETABLE")
        print("\n CREATING DATABASE..............................\n")
        print("Database TIMETABLE Created\n")
        mycursor.execute("USE TIMETABLE")
        return mydb
    else:
        print("ERROR ESTABLISHING MYSQL CONNECTION CHECK USERNAME AND PASSWORD !\n")


    from TIMETABLE1 import mydb, mycursor


# MAKING TEACHER'S TIMETABLE
def Add_Teacher_Data():
    global mydb
    global mycursor

    if mydb:
        mycursor = mydb.cursor()
        Table1 = "CREATE TABLE IF NOT EXISTS TEACHER (TNO INT(4), NAMEOFTEACHER VARCHAR(30), TEACHERTIME VARCHAR(100))"
        mycursor.execute(Table1)
        print("\n               TEACHER TIMETABLE               ")
        print('\nEnter Teacher Data..........\n')
        A = input("Enter Sno.: ")
        B = input("Enter Name: ")
        print("\n     Enter Time Table     \n")
        Tt1 = input("Time Occupied: ")
        TEACHER = Tt1.split(",")
        TEACHER1.extend(TEACHER)
        SQL1 = "INSERT INTO TEACHER VALUES (" + A + ",'" + B + "','" + Tt1 + "')"
        mycursor.execute(SQL1)
        mydb.commit()
        print("\n TEACHER TABLE CREATED\n")
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION !")


# MAKING STUDENT'S TIMETABLE
def Add_Student_Data():
    global mydb
    global mycursor

    if mydb:
        mycursor = mydb.cursor()
        Table1 = "CREATE TABLE IF NOT EXISTS STUDENT (SNO INT(4), NAMEOFSTUDENT VARCHAR(30), STUDENTTIME VARCHAR(100))"
        mycursor.execute(Table1)
        print("\n               STUDENT TIMETABLE               ")
        print('\nEnter Student Data..........\n')
        C = input("Enter Sno.: ")
        D = input("Enter Name: ")
        print("\n     Enter Time Table     \n")
        Tt2 = input("Time Occupied: ")
        STUDENT = Tt2.split(",")
        STUDENT1.extend(STUDENT)
        SQL2 = "INSERT INTO STUDENT VALUES (" + C + ",'" + D + "','" + Tt2 + "')"
        mycursor.execute(SQL2)
        mydb.commit()
        print("\nSTUDENT TABLE CREATED\n")


# DISPLAYING OF TEACHER'S TIMETABLE IN PYTHON
def Display_Teacher():
    global mydb
    global mycursor
    SQL3 = "SELECT*FROM TEACHER"
    mycursor.execute(SQL3)
    R = mycursor.fetchall()
    i=0
    while True:
      print("S.no: ",R[i][0])
      print("Name: ",R[i][1])
      print("Time Occupied: ",R[i][2])
      print()
      i+=1
      if i == (len(R)):
        break


# DISPLAYING OF STUDENT'S TIMETABLE IN PYTHON
def Display_Student():
    global mydb
    global mycursor
    SQL4 = "SELECT*FROM STUDENT"
    mycursor.execute(SQL4)
    P = mycursor.fetchall()
    i=0
    while True:
      print("S.no: ",P[i][0])
      print("Name: ",P[i][1])
      print("Time Occupied: ",P[i][2])
      print()
      i+=1
      if i == (len(P)):
        break

# FINDING THE COMMON FREE TIME BETWEEN TEACHER AND STUDENT
def get_times(a, b):
    p = []
    q = []
    min1 = []
    min2 = []
    process = []
    output = []
    d1 = {}
    d2 = {}
    delivery = []
    final_delivery = []
    for i in a:
        p.extend(i.split("-"))
    for i in b:
        q.extend(i.split("-"))
    for i in p:
        st = i.split(":")
        hour1 = int(st[0]) * 60 + int(st[1])
        min1.append(hour1)
    for j in q:
        sn = j.split(":")
        hour2 = int(sn[0]) * 60 + int(sn[1])
        min2.append(hour2)
    for k in range(0, len(min1), 2):
        process.append(min1[k])
        process.append(min1[k + 1])
        process.append(min2[k])
        process.append(min2[k + 1])
        output.append(min(process))
        output.append(max(process))
        del process[::]
    for n in range(len(p)):
        d1[min1[n]] = p[n]
        d2[min2[n]] = q[n]
    d1.update(d2)
    for l in output:
        delivery.append(d1[l])
    for a in range(0, len(delivery), 2):
        final_delivery.append(delivery[a] + "-" + delivery[a + 1])

    def free_times(a):
        free = []
        al = []
        pt = []
        for i in a:
            lisst = i.split("-")
            al.extend(lisst)
        for i in range(1, len(al) - 1):
            free.append(al[i])
        for i in range(0, len(free), 2):
            pt.append(free[i] + "-" + free[i + 1])
        return (pt)

    print("The both of you are free from: ",free_times(final_delivery))


TEACHER1 = []
STUDENT1 = []

# INTRO
print('\n                    WELCOME TO SCHEDULE IT                    \n')
print("INPUT TIME FROM TEACHER AND STUDENT AND DISPLAY THE COMMON TIME FOR BOTH\n\n")

# MAIN MENU
while (True):

    CH = input("\nC:Setup Connection  \nT:Teacher Data   \nS:Student Data   \nTD:Display Teacher Table  \nSD:Display Student Table  \nG:Get free Time   \nQ:Quit     \nEnter Option: ")
    print("\n")
    
    if CH.upper() == 'C':
        myconnection()
    elif CH.upper() == 'T':
        Add_Teacher_Data()
    elif CH.upper() == 'S':
        Add_Student_Data()
    elif CH.upper() == 'TD':
        Display_Teacher()
    elif CH.upper() == 'SD':
        Display_Student()
    elif CH.upper() == 'G':
        get_times(TEACHER1, STUDENT1)
        TEACHER1.clear()
        STUDENT1.clear()
    elif CH.upper() == 'Q':#DATABASE WILL BE DELETED ONCE QUIT COMMAND IS GIVEN
        print("DELETING DATABASE..................")
        print("DATABASE DELETED")
        print("-" * 6)
        print(" Thank you for using SCHEDULE IT")
        print("-" * 6)
        SQLN = "DROP DATABASE TIMETABLE"
        mycursor.execute(SQLN)
        break
    else:
        print("Invalid Input! ")
        break
