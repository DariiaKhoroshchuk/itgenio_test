def show_all():
    for name, subjects in students_subjects.items():
        print(name, subjects, sep=": ")


def student_for_sub(name):
    print(students_subjects.get(name, 'There are no students with this name.'))


def sub_for_students(subject):
    sub_for_student = list()
    for name, subjects in students_subjects.items():
        if subject in subjects:
            sub_for_student.append(name)
    if len(sub_for_student) == 0:
        print("The are no matching students.")
    else:
        print(sub_for_student)


students_subjects = {}
num_of_students = int(input("Write number of students: "))
for i in range(num_of_students):
    student = input(f"Name of {i+1} student: ")
    students_subjects[student] = input(f"Subjects of {i+1} student: ").split()
