def add_student(details):
    student_add = {}
    for item in details:
        student_add.update({item : details[item]})
    return student_add

def average_of_marks(details):
    avg_dict = {}
    for item in details:
        avg = sum(details[item])/len(details[item]) 
        avg_dict.update({item : avg})
    return avg_dict

def grade(details):
    for item in details:
        for num in details[item]:
            if num >= 90 and num <= 100:
                grade = 'A+'
            elif num >= 80 and num < 90:
                grade = 'A'
            elif num >= 70 and num < 80:
                grade = 'B'
            elif num >= 60 and num < 70:
                grade = 'C'
            elif num >= 50 and num < 60:
                grade = 'D'
            else:
                grade = "FAIL"
    return grade

def view_students(details):
    student_list = []
    for student in details:
        student_list.append(student)
    return student_list

def topper(details):
    topper_dict = {}
    high_avg = average_of_marks(details)
    for item in details:
        topper_dict.update({item : high_avg})
    return topper_dict

n = int(input("Enter number of records: "))
details = {}
for record in range(n):
    student_name = input("Enter student name: ")
    student_marks = input("Enter student marks: ").split()
    details.update({student_name : student_marks})
print(details)
# while True:
#     print("----- Student Grade Manager -----")
#     print("----- MENU -----")
#     print("----- 1. Add Students -----")
#     print("----- 2. Find Average -----")
#     print("----- 3. Assess Grade -----")
#     print("----- 4. View all Students -----")
#     print("----- 5. Topper with Average marks -----")
#     print("----- 6. Exit -----")
#     op = int(input("Select action number: "))

#     if op == 1:
#         print(add_student(details))
#     elif op == 2:
#         print(average_of_marks(details))
#     elif op == 3:
#         print(grade(details))
#     elif op == 4:
#         print(view_students(details))
#     elif op == 5:
#         print(topper(details))
#     elif op == 6:
#         print("== Thanks for using student manager! ==")
#         break