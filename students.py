students = [
    {"name": "Harry", "grades": [80, 90, 85]},
    {"name": "Ron", "grades": [60, 70, 65]},
    {"name": "Hermione", "grades": [95, 90, 92]}
]

def calculate_average(grades):
    return sum(grades) / len(grades)

def update_overall_average(students):
    total_sum = 0
    grade_count = 0
    for student in students:
        total_sum += sum(student['grades'])
        grade_count += len(student['grades'])
    return round(total_sum / grade_count, 2) if grade_count > 0 else None

def display_students(students):
    for student in students:
        name = student["name"]
        grades = student["grades"]
        avg_grade = round(calculate_average(grades), 2)

        if avg_grade >= 75:
            status = "Успешен"
        else:
            status = "Отстающий"

        print(f'\nИмя: {name} \nСредний балл: {avg_grade:.2f} \nСтатус: {status}')
    print("\n-------------------------\n")

def add_student(name, grades):
    global students
    new_student = {
        "name": name,
        "grades": grades
    }
    students.append(new_student)
    print(f"Старшекурсник '{name}' добавлен.")

def remove_failing_students():
    global students
    initial_length = len(students)
    students[:] = [student for student in students if calculate_average(student['grades']) >= 75]
    removed_count = initial_length - len(students)
    print(f"Количество удаленных студентов: {removed_count}\n")

display_students(students)
overall_avg = update_overall_average(students)
print(f"Начальный общий средний балл: {overall_avg:.2f}\n")

add_student('Draco', [70, 66, 95])
updated_avg = update_overall_average(students)
print(f"Новый общий средний балл после добавления: {updated_avg:.2f}\n")

remove_failing_students()
final_avg = update_overall_average(students)
print(f"Финальный общий средний балл после очистки списка: {final_avg:.2f}\n")

display_students(students)
