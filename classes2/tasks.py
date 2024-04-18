import sqlite3

# Task 1: Working with a Database

# Connect to the database
conn = sqlite3.connect('census.sqlite')
cursor = conn.cursor()

# 1. States present in the database
cursor.execute("SELECT DISTINCT state FROM census")
states = cursor.fetchall()
print("States in the database:")
for state in states:
    print(state[0])

# 2. Count population in Alaska and New York in 2000 and 2008
def count_population(state, year):
    cursor.execute("SELECT SUM(population) FROM census WHERE state=? AND year=?", (state, year))
    population = cursor.fetchone()[0]
    return population

alaska_2000 = count_population('Alaska', 2000)
alaska_2008 = count_population('Alaska', 2008)
new_york_2000 = count_population('New York', 2000)
new_york_2008 = count_population('New York', 2008)

print("\nPopulation in Alaska in 2000:", alaska_2000)
print("Population in Alaska in 2008:", alaska_2008)
print("Population in New York in 2000:", new_york_2000)
print("Population in New York in 2008:", new_york_2008)

# 3. Count number of males and females in New York in 2008
cursor.execute("SELECT SUM(male_population), SUM(female_population) FROM census WHERE state=? AND year=?", ('New York', 2008))
male_population, female_population = cursor.fetchone()
print("\nNumber of males in New York in 2008:", male_population)
print("Number of females in New York in 2008:", female_population)

# Task 2: Basics of Database Creation

# Create a table named 'students'
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER,
                grade REAL)''')

# Add students to the table
students_data = [
    ('John', 20, 3.5),
    ('Emma', 21, 4.0),
    ('Michael', 19, 3.2)
]

cursor.executemany("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", students_data)
conn.commit()

# Select and display all students
cursor.execute("SELECT * FROM students")
all_students = cursor.fetchall()
print("\nAll students:")
for student in all_students:
    print(student)

# Task 3: CRUD Operations

# Function to add a new student
def add_student(name, age, grade):
    cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", (name, age, grade))
    conn.commit()

# Function to get student data by ID
def get_student_by_id(student_id):
    cursor.execute("SELECT * FROM students WHERE id=?", (student_id,))
    student = cursor.fetchone()
    return student

# Function to update student data by ID
def update_student_by_id(student_id, name, age, grade):
    cursor.execute("UPDATE students SET name=?, age=?, grade=? WHERE id=?", (name, age, grade, student_id))
    conn.commit()

# Function to delete a student by ID
def delete_student_by_id(student_id):
    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()

# Sample usage of CRUD functions
add_student('Sarah', 22, 3.7)
print("\nAdded a new student:", get_student_by_id(4))

update_student_by_id(4, 'Sarah Smith', 23, 3.8)
print("Updated student data:", get_student_by_id(4))

delete_student_by_id(4)
print("Deleted student with ID=4")

# Close the connection
conn.close()
