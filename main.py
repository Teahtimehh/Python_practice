def calculate_average(grades):
    if len(grades) > 0:
        return sum(grades) / len(grades)
    else:
        return 0


def update_group_average(students):
    all_grades = []
    for student in students:
        all_grades.extend(student["grades"])

    if all_grades:
        group_average = calculate_average(all_grades)
        print(f"\nОбщий средний балл группы: {group_average:.2f}\n")
    else:
        print("\nНет студентов в группе.\n")


def display_students(students):
    for student in students:
        avg = calculate_average(student["grades"])
        status = "Успешен" if avg >= 75 else "Отстающий"
        print(f"""
Студент: {student['name']}
Средний балл: {avg:.2f}
Статус: {status}
""")


def add_student(students, name, grades):
    new_student = {"name": name, "grades": grades}
    students.append(new_student)
    print(f'\nСтудент "{name}" успешно добавлен!\n')


def remove_lowest_performers(students):
    if not students:
        return

    min_avg = float('inf')
    lowest_performers = []
    for student in students:
        avg = calculate_average(student["grades"])
        if avg <= min_avg:
            if avg < min_avg:
                lowest_performers.clear()
                min_avg = avg
            lowest_performers.append(student)

    removed_count = 0
    for lp in lowest_performers:
        students.remove(lp)
        removed_count += 1

    if removed_count > 0:
        print(f'\nСтуденты с низкими результатами ({removed_count}) были исключены.\n')
    else:
        print('\nНет отстающих студентов.\n')


if __name__ == "__main__":
    students = [
        {"name": "Harry", "grades": [85, 90, 80, 95]},
        {"name": "Hermione", "grades": [95, 90, 92, 98]},
        {"name": "Ron", "grades": [70, 65, 75, 72]}
    ]

    update_group_average(students)
    display_students(students)

    add_student(students, "Draco", [75, 78, 80, 82])
    update_group_average(students)
    display_students(students)

    remove_lowest_performers(students)
    update_group_average(students)
    display_students(students)
