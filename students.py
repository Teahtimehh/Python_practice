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
        average_grade = round(calculate_average(grades), 2)

        if average_grade >= 75:
            status = "Успешен"
        else:
            status = "Отстающий"

        print(f"\nСтудент: {name} \nСредний балл: {average_grade:.2f} \nСтатус: {status}")
        print("--------------------")


display_students(students)

initial_average = update_overall_average(students)
print(f'\nНачальный общий средний балл всех студентов: {initial_average}')

new_student = {'name': 'Draco', 'grades': [70, 66, 95]}
students.append(new_student)

after_addition_average = update_overall_average(students)
print(f'\nСредний балл после добавления нового студента: {after_addition_average}')

del students[1]

final_average = update_overall_average(students)
print(f'\nСредний балл после удаления студента: {final_average}')

display_students(students)