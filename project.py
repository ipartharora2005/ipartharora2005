import tkinter as tk
from tkinter import ttk
import mysql.connector

# Function to create the employee table in the MySQL database
def create_employee_table():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="partharora",
        database="employee"
    )
    cursor = conn.cursor()
    
    # Check if the table already exists
    cursor.execute("SHOW TABLES LIKE 'EMPLOYEES'")
    if not cursor.fetchone():
        sql = '''CREATE TABLE EMPLOYEES (
            EMPLOYEE_ID INT PRIMARY KEY,
            NAME VARCHAR(50),
            SALARY FLOAT
        )'''
        cursor.execute(sql)
    
    cursor.close()
    conn.close()

# Function to add an employee to the MySQL database
def add_employee():
    name = name_entry.get()
    employee_id = emp_id_entry.get()
    salary = salary_entry.get()

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="partharora",
        database="employee"
    )
    cursor = conn.cursor()

    insert_query = "INSERT INTO EMPLOYEES (EMPLOYEE_ID, NAME, SALARY) VALUES (%s, %s, %s)"
    data = (employee_id, name, salary)
    cursor.execute(insert_query, data)
    conn.commit()

    cursor.close()
    conn.close()

    # Clear the input fields
    name_entry.delete(0, 'end')
    emp_id_entry.delete(0, 'end')
    salary_entry.delete(0, 'end')

# Function to view employee details
def view_employees():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="partharora",
        database="employee"
    )
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM EMPLOYEES")
    data = cursor.fetchall()

    # Display employee details in the listbox
    for item in employee_listbox.get_children():
        employee_listbox.delete(item)
    for employee in data:
        employee_listbox.insert('', 'end', values=employee)

    cursor.close()
    conn.close()

# Create the main application window
app = tk.Tk()
app.title("Employee Management System")

# Create and configure labels and entry fields
name_label = tk.Label(app, text="Name:")
name_entry = tk.Entry(app)

emp_id_label = tk.Label(app, text="Employee ID:")
emp_id_entry = tk.Entry(app)

salary_label = tk.Label(app, text="Salary:")
salary_entry = tk.Entry(app)

# Create buttons
add_button = tk.Button(app, text="Add Employee", command=add_employee, bg="green", fg="white")
view_button = tk.Button(app, text="View Employees", command=view_employees, bg="blue", fg="white")

# Create a listbox to display employees
employee_listbox = ttk.Treeview(app, columns=("Employee ID", "Name", "Salary"), show="headings")
employee_listbox.heading("Employee ID", text="Employee ID")
employee_listbox.heading("Name", text="Name")
employee_listbox.heading("Salary", text="Salary")

# Grid layout for widgets
name_label.grid(row=0, column=0, padx=10, pady=5)
name_entry.grid(row=0, column=1, padx=10, pady=5)
emp_id_label.grid(row=1, column=0, padx=10, pady=5)
emp_id_entry.grid(row=1, column=1, padx=10, pady=5)
salary_label.grid(row=2, column=0, padx=10, pady=5)
salary_entry.grid(row=2, column=1, padx=10, pady=5)
add_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5)
view_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5)
employee_listbox.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

# Create the employee table
create_employee_table()

app.mainloop()
