# student_profile_system.py

import pandas as pd
import os

# --- File paths for storing data ---
USERS_FILE = "users.csv"
PASSWORDS_FILE = "passwords.csv"
GRADES_FILE = "grades.csv"
ECA_FILE = "eca.csv"

# --- Load CSV files if they exist; otherwise, initialize empty DataFrames ---
df = pd.read_csv(USERS_FILE) if os.path.exists(USERS_FILE) else pd.DataFrame(columns=['id', 'first_name', 'email', 'age', 'gender', 'role'])
passdf = pd.read_csv(PASSWORDS_FILE) if os.path.exists(PASSWORDS_FILE) else pd.DataFrame(columns=['email', 'password'])
gradedf = pd.read_csv(GRADES_FILE) if os.path.exists(GRADES_FILE) else pd.DataFrame(columns=['id', 'first_name', 'email', 'physics', 'chemistry', 'maths'])
ecadf = pd.read_csv(ECA_FILE) if os.path.exists(ECA_FILE) else pd.DataFrame(columns=['id', 'first_name', 'email', 'eca'])

# --- Function to save all data back to CSV files ---
def save_data():
    df.to_csv(USERS_FILE, index=False)
    passdf.to_csv(PASSWORDS_FILE, index=False)
    gradedf.to_csv(GRADES_FILE, index=False)
    ecadf.to_csv(ECA_FILE, index=False)

# --- User login functionality ---
def login():
    while True:
        userID = input("Enter your email: ")
        password = input("Enter your password: ")

        # Check if email and password match
        if userID in df['email'].values and password in passdf[passdf['email'] == userID]['password'].values:
            role = df[df['email'] == userID]['role'].values[0]
            # Redirect based on role
            if role.lower() == 'admin':
                admin_dashboard(userID)
            else:
                student_dashboard(userID)
            break
        else:
            print("Invalid username or password. Try again.\n")

# --- Admin dashboard options ---
def admin_dashboard(userID):
    while True:
        print("\n--- Admin Dashboard ---")
        print("1. Add User\n2. Access User Data\n3. Delete User\n4. Logout")
        choice = input("Enter your choice: ")

        if choice == '1':
            register_user()
        elif choice == '2':
            print(df)
        elif choice == '3':
            delete_user()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Try again.")

# --- Delete a user and their associated data ---
def delete_user():
    email = input("Enter the email of the user to delete: ")
    global df, gradedf, ecadf, passdf

    if email in df['email'].values:
        # Delete from all DataFrames
        df = df[df['email'] != email]
        gradedf = gradedf[gradedf['email'] != email]
        ecadf = ecadf[ecadf['email'] != email]
        passdf = passdf[passdf['email'] != email]
        save_data()
        print("User deleted successfully.")
    else:
        print("User not found.")

# --- Register a new student or admin user ---
def register_user():
    global df, passdf, gradedf, ecadf

    # Basic user details
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    age = input("Enter Age: ")
    gender = input("Enter Gender: ")
    role = input("Enter Role (admin/student): ").lower()
    password = input("Set a Password: ")

    # Check for existing email
    if email in df['email'].values:
        print("Email already registered.")
        return

    # Assign a new ID
    new_id = len(df) + 1

    # Add to users and passwords
    df.loc[len(df)] = [new_id, name, email, age, gender, role]
    passdf.loc[len(passdf)] = [email, password]

    # If the user is a student, collect academic and ECA info
    if role == 'student':
        physics = input("Physics Marks: ")
        chemistry = input("Chemistry Marks: ")
        maths = input("Maths Marks: ")
        eca = input("ECA Activities: ")

        gradedf.loc[len(gradedf)] = [new_id, name, email, physics, chemistry, maths]
        ecadf.loc[len(ecadf)] = [new_id, name, email, eca]

    save_data()
    print("User registered successfully.")

# --- Student dashboard with options to update profile, view ECA, or view grades ---
def student_dashboard(userID):
    while True:
        print("\n--- Student Dashboard ---")
        print("1. Update Profile\n2. View ECA\n3. View Grades\n4. Logout")
        choice = input("Enter your choice: ")

        if choice == '1':
            update_profile(userID)
        elif choice == '2':
            view_eca(userID)
        elif choice == '3':
            view_grades(userID)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Try again.")

# --- Update student profile details (name, age, gender) ---
def update_profile(email):
    name = input("Updated Name: ")
    age = input("Updated Age: ")
    gender = input("Updated Gender: ")

    df.loc[df['email'] == email, ['first_name', 'age', 'gender']] = [name, age, gender]

    # Sync changes in other files too
    if email in ecadf['email'].values:
        ecadf.loc[ecadf['email'] == email, 'first_name'] = name
    if email in gradedf['email'].values:
        gradedf.loc[gradedf['email'] == email, 'first_name'] = name

    save_data()
    print("Profile updated.")

# --- View ECA activities for the logged-in student ---
def view_eca(email):
    eca_data = ecadf[ecadf['email'] == email]
    print("\n--- ECA Details ---")
    print(eca_data if not eca_data.empty else "No ECA data available.")

# --- View grades for the logged-in student ---
def view_grades(email):
    grade_data = gradedf[gradedf['email'] == email]
    print("\n--- Grades ---")
    print(grade_data if not grade_data.empty else "No grades available.")

# --- Start the program by asking for login ---
if __name__ == "__main__":
    login()
