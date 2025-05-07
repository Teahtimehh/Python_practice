students = [
    {"name": "Harry", "grades": [85, 90, 80, 95]},
    {"name": "Hermione", "grades": [95, 90, 92, 98]},
    {"name": "Ron", "grades": [70, 65, 75, 72]}
]


def calculate_average(grades):
    return sum(grades) / len(grades)


def add_student(name, grades):
    new_student = {"name": name, "grades": grades}
    students.append(new_student)
    update_and_display()


def remove_lowest_performer():
    if not students:
        return

    min_avg = float("inf")
    worst_student = None
    for student in students:
        avg = calculate_average(student["grades"])
        if avg < min_avg:
            min_avg = avg
            worst_student = student

    if worst_student:
        students.remove(worst_student)
        update_and_display()


def update_and_display():
    update_group_average()
    display_students()


def update_group_average():
    all_grades = []
    for student in students:
        all_grades.extend(student["grades"])
    if all_grades:
        group_average = calculate_average(all_grades)
        print(f"\nОбщий средний балл группы: {group_average:.2f}\n")
    else:
        print("\nНет студентов в группе.\n")


def display_students():
    for student in students:
        avg = calculate_average(student["grades"])
        status = "Успешен" if avg >= 75 else "Отстающий"
        print(f"""
Студент: {student['name']}
Средний балл: {avg:.2f}
Статус: {status}
""")


update_and_display()

add_student("Draco", [75, 78, 80, 82])

remove_lowest_performer()