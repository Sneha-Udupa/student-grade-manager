```
1. Project Title
Student Grade Manager

2. Description
A command-line Python application for managing student records. Users can add students, calculate average marks, assign grades, view a list of all students, identify the class topper.

3. Features
- Add new students
- Store marks for multiple subjects
- Calculate average marks
- Assign grades based on averages
- Display all students
- Find the topper
- Handle invalid mark input
- Save student records to a JSON file
- Load previously saved student records

4. Technologies
- Python 3
- Dictionaries
- Lists
- Functions
- Loops
- Exception Handling
- JSON

5. How to Run
python student_grade_project.py

6. Sample Input/Output

----- Student Grade Manager -----
Do you want to load previous student records? Type Y (YES) or N (NO): Y
{'Alice': [88, 89, 90], 'Bob': [90, 87, 89]}
Enter number of records: 1
Enter student name: cara
Enter student marks: 89 87 80
{'Alice': [88, 89, 90], 'Bob': [90, 87, 89], 'Cara': [89, 87, 80]}

----- MENU -----
----- 1. Add Students -----
----- 2. Find Average -----
----- 3. Assess Grade -----
----- 4. View all Students -----
----- 5. Topper with Average marks -----
----- 6. Exit -----
Select action number: 4

---- List of students ---- 
['Alice', 'Bob', 'Cara']



----- MENU -----
----- 1. Add Students -----
----- 2. Find Average -----
----- 3. Assess Grade -----
----- 4. View all Students -----
----- 5. Topper with Average marks -----
----- 6. Exit -----
Select action number: 6

== Thanks for using student manager! ==


7. Future Improvements
- Search for a student
- Update marks
- Delete students
- Sort students by average
- Handle an empty or corrupted JSON file
- Prompt the user before overwriting existing student records
```