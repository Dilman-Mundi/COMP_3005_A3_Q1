import psycopg

def createTable(conn):
    cursor = conn.cursor()

    cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS students (
            student_id SERIAL PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            enrollment_date DATE
        )""")

    conn.commit()
    cursor.close()

#Outputs all the data from the students table
def getAllStudents(conn):
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")

    for row in cursor.fetchall():
        print(row)

    cursor.close()

#Adds a student with the given info
def addStudent(conn, first_name, last_name, email, enrollment_date):
    cursor = conn.cursor()
    
    cursor.execute("""INSERT INTO students 
                    (first_name, last_name, email, enrollment_date) 
                    VALUES (%s,%s,%s,%s)""", 
                    (first_name, last_name, email, enrollment_date))

    conn.commit()
    cursor.close()

#Updates the students email using their id
def updateStudentEmail(conn, student_id, new_email):
    cursor = conn.cursor()

    cursor.execute("UPDATE students SET email=%s WHERE student_id=%s", (new_email, student_id))

    conn.commit()
    cursor.close()

#Deletes a student using their id
def deleteStudent(conn, student_id):
    cursor=conn.cursor()

    cursor.execute("DELETE FROM students WHERE student_id=%s", (student_id,))

    conn.commit()
    cursor.close()

def main():
    conn = psycopg.connect(
        host="localhost",
        port=5433,
        dbname="postgres",                
        user="postgres",
        password="comp3005!"
    )

    createTable(conn)

    print("Current table")
    getAllStudents(conn)

    addStudent(conn, "Dilman", "Mundi", "dilmanmundi@cmail.carleton.ca", "2025-01-01")
    print("Adding a student")
    getAllStudents(conn)

    updateStudentEmail(conn, 2, "jane2023@example.com")
    print("Updating Jane's email")
    getAllStudents(conn)

    deleteStudent(conn, 3)
    print("deleting student Jim")
    getAllStudents(conn)

    conn.close()

main()