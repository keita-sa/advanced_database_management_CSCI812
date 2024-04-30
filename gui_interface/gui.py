import tkinter as tk
from tkinter import ttk, messagebox
from data_manipulation.data_operations import DataOperations
from mongodb_connection.db_connection import MongoDBConnection

class GUI:
    def __init__(self, db_connection):
        self.connection = db_connection
        self.data_ops = DataOperations(self.connection)

        self.root = tk.Tk()
        self.root.title("MongoDB CRUD GUI")

        self.create_tabs()

    def create_tabs(self):
        tabs = ttk.Notebook(self.root)

        # Create tabs for each collection
        collections = [
            "students",
            "schools_for_further_study",
            "companies_of_employment",
            "courses",
            "course_grades",
            "ones_specialty"
        ]

        for collection in collections:
            tab = ttk.Frame(tabs)
            tabs.add(tab, text=collection)
            self.create_collection_widgets(tab, collection)

        tabs.pack(expand=1, fill="both")

    def create_collection_widgets(self, tab, collection):
        # Create widgets for CRUD operations
        label = tk.Label(tab, text=f"Manage {collection}")
        label.grid(row=0, column=0, columnspan=2)

        # Example: Entry fields for student data
        if collection == "students":
            tk.Label(tab, text="ID:").grid(row=1, column=0)
            self.entry_id = tk.Entry(tab)
            self.entry_id.grid(row=1, column=1)

            tk.Label(tab, text="First Name:").grid(row=2, column=0)
            self.entry_fname = tk.Entry(tab)
            self.entry_fname.grid(row=2, column=1)

            tk.Label(tab, text="Last Name:").grid(row=3, column=0)
            self.entry_lname = tk.Entry(tab)
            self.entry_lname.grid(row=3, column=1)

            tk.Label(tab, text="Department:").grid(row=4, column=0)
            self.entry_department = tk.Entry(tab)
            self.entry_department.grid(row=4, column=1)

            tk.Label(tab, text="Dno:").grid(row=5, column=0)
            self.entry_dno = tk.Entry(tab)
            self.entry_dno.grid(row=5, column=1)

            tk.Label(tab, text="Major:").grid(row=6, column=0)
            self.entry_major = tk.Entry(tab)
            self.entry_major.grid(row=6, column=1)

            # Buttons for CRUD operations
            insert_button = tk.Button(tab, text="Insert", command=self.insert_student)
            insert_button.grid(row=7, column=0)

            fetch_button = tk.Button(tab, text="Fetch", command=self.fetch_student)
            fetch_button.grid(row=7, column=1)

            # Additional buttons for Update and Delete can be added

    def insert_student(self):
        # Retrieve data from entry fields
        student_data = {
            "ID": int(self.entry_id.get()),
            "Fname": self.entry_fname.get(),
            "Lname": self.entry_lname.get(),
            "Department": self.entry_department.get(),
            "Dno": int(self.entry_dno.get()),
            "Major": self.entry_major.get()
        }

        # Insert data into MongoDB
        self.data_ops.insert_document("students", student_data)

        # Clear entry fields after insertion
        self.clear_entry_fields()

    def fetch_student(self):
        # Retrieve student ID from entry field
        student_id = int(self.entry_id.get())

        # Fetch student data from MongoDB
        query_result = self.data_ops.find_document("students", {"ID": student_id})

        # Display fetched data
        if query_result:
            messagebox.showinfo("Student Data", f"ID: {query_result['ID']}\nFirst Name: {query_result['Fname']}\nLast Name: {query_result['Lname']}\nDepartment: {query_result['Department']}\nDno: {query_result['Dno']}\nMajor: {query_result['Major']}")
        else:
            messagebox.showinfo("Error", "No student found with the provided ID.")

    def clear_entry_fields(self):
        # Clear entry fields after insertion
        self.entry_id.delete(0, tk.END)
        self.entry_fname.delete(0, tk.END)
        self.entry_lname.delete(0, tk.END)
        self.entry_department.delete(0, tk.END)
        self.entry_dno.delete(0, tk.END)
        self.entry_major.delete(0, tk.END)

if __name__ == "__main__":
    # Connect to MongoDB
    mongo_connection = MongoDBConnection(host='localhost', port=27017, db_name='your_database')

    # Initialize GUI
    app = GUI(mongo_connection)

    app.root.mainloop()
