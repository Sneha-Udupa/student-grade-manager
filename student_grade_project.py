
def add_student(details):
    """
        Add new student records 

        Arguements : 
            details (dict) : Dictionary containing student names and marks

        Returns:
            details (dict) : Updated dictionary with new records
    """
    m = int(input("Enter number of new records: "))
    for new_rec in range(m):
        student_name = input("Enter student name: ")
        student_marks = input("Enter student marks: ").split()
    new_list = []
    for str_num in student_marks:
        try:
            new_list.append(int(str_num))
        except ValueError:
            exit()
            print("Invalid marks!")
    details.update({student_name.title() : new_list})
    return details

def average_of_marks(details):
    """
        Calculate avg marks for each student 
    
        Arguements : 
            details (dict) : Dictionary containing student names and marks
    
        Returns:
            avg_dict (dict) : Dictionary mapping student names with their avg marks
    """
    avg_dict = {}
    for name in details:
        total = 0
        for num in details[name]:
            total += num
        avg = total/len(details[name])
        avg_dict.update({name : round(avg, 2)})
    return avg_dict

def grade(avg_dict):
    """
        Assess grades for each student
    
        Arguements : 
            avg_dict : Dictionary mapping student names with their avg marks
    
        Returns:
            grade_dict (dict) : Dictionary mapping student names with their grade
    """
    grade_dict = {}
    for name in avg_dict:
        if avg_dict[name] >= 90 and avg_dict[name] <= 100:
            grade = 'A+'
        elif avg_dict[name] >= 80 and avg_dict[name] < 90:
            grade = 'A'
        elif avg_dict[name]>= 70 and avg_dict[name] < 80:
            grade = 'B'
        elif avg_dict[name] >= 60 and avg_dict[name] < 70:
            grade = 'C'
        elif avg_dict[name] >= 50 and avg_dict[name] < 60:
            grade = 'D'
        else:
            grade = "FAIL"
        grade_dict.update({name : grade})
    return grade_dict

def view_students(details):
    """
        List all students
    
        Arguements : 
            details (dict) : Dictionary containing student names and marks
    
        Returns:
            student_list (list) : List containing student names
    """
    student_list = []
    for student in details:
        student_list.append(student)
    return student_list

def topper(details):
    """
        Identify topper based on average marks 
    
        Arguements : 
            details (dict) : Dictionary containing student names and marks
    
        Returns:
            name (key) of details (dict) corresponding to the highest average marks
    """
    avg_list = []
    avg_info = average_of_marks(details)
    for value in avg_info.values():
        avg_list.append(value)
    highest_avg = max(avg_list)

    for name, avg in avg_info.items():
        if avg == highest_avg:
            return name

print("----- Student Grade Manager -----")
n = int(input("Enter number of records: "))
details = {}
for record in range(n):
    student_name = input("Enter student name: ")
    student_marks = input("Enter student marks: ").split()
    if student_marks == []:
        print("Empty List!")
        exit()
    details.update({student_name.title() : student_marks})

for name in details:
    new_list = []
    for str_num in details[name]:
        try:
            new_list.append(int(str_num))
        except ValueError:
            print("Invalid marks!")
            exit()
    details[name] = new_list
print(details)

while True:
    print("\n----- MENU -----")
    print("----- 1. Add Students -----")
    print("----- 2. Find Average -----")
    print("----- 3. Assess Grade -----")
    print("----- 4. View all Students -----")
    print("----- 5. Topper with Average marks -----")
    print("----- 6. Exit -----")

    op = int(input("Select action number: "))

    if op == 1:
        print(add_student(details))
        print("\n")

    elif op == 2:
        print("\n---- Average marks of students ---- ")
        print(average_of_marks(details))
        print("\n")

    elif op == 3:
        avg_dict = average_of_marks(details)
        print("\n---- Grades of students based on average marks ---- ")
        print(grade(avg_dict))
        print("\n")

    elif op == 4:
        print("\n---- List of students ---- ")
        print(view_students(details))
        print("\n")

    elif op == 5:
        print("\n---- Topper ---- ")
        print(topper(details))
        print("\n")

    elif op == 6:
        print("\n== Thanks for using student manager! ==")
        break

    else:
        print("\nInvalid choice! Please enter numbers between 1 and 6")