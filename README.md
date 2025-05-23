# Student Management System

## Project Description  
This project is a Python-based Student Management System designed to manage student, user, grades, and extracurricular activity data stored in CSV files. It features modular code using Object-Oriented Programming (OOP) principles and handles data input/output efficiently with proper file and error handling. The system provides separate dashboards for Admins and Students, allowing user authentication and role-based access to functionalities.

## Design Overview  
The system is architected with emphasis on:

- **Modularity:** Each functionality is separated into modules/classes for better maintainability and clarity.
- **Object-Oriented Programming:** Classes represent entities such as Users, Students, and Grades, encapsulating data and behaviors.
- **File Handling:** Robust reading/writing from CSV files ensures persistent data storage.
- **Error Handling:** Validations and exception handling provide smooth operation and meaningful feedback on errors.
- **Role-Based Dashboards:** Separate interfaces for Admin and Student roles provide tailored access and operations.

## Core Functionalities

- **User Authentication:** Secure login system validating user credentials and role.
- **Admin Dashboard:** Manage student records, view grades, assign extracurricular activities, and update user info.
- **Student Dashboard:** View personal grades, profile, and assigned extracurricular activities.
- **Data Management:** Load, update, and save data for users, students, grades, and extracurricular activities via CSV.
- **Error Validation:** Detects and handles invalid inputs, missing files, or corrupted data gracefully.
- **Modular Code Structure:** Easily extensible and maintainable for future enhancements.

## File Management

- **CSV Data Storage:**  
  - `users.csv` stores user information including emails and roles.  
  - `students.csv` contains detailed student info like name, age, and gender.  
  - `grades.csv` holds student marks across subjects.  
  - `eca.csv` tracks extracurricular activities assigned to students.

- **Data Persistence:** All updates are saved back to respective CSV files, ensuring data consistency across sessions.
