# Студент 1
# Автор: Маліяд.Р.О.
# Завдання: створити словник для зберігання інформації про успішність студентів
# та реалізувати функцію додавання нового студента
# Наступне завдання для студента №2:
#   – реалізувати функцію сортування студентів за середнім балом

# Словник, де ключ — це номер залікової книжки (ID студента),
# а значення — вкладений словник з усіма даними студента

students = {
    1: {
        "group": "КН-21",
        "name": "Петренко Андрій Сергійович",
        "course": 2,
        "subjects": {
            "Математика": 85,
            "Програмування": 92,
            "Фізика": 78
        }
    },
    2: {
        "group": "КН-21",
        "name": "Іваненко Ольга Михайлівна",
        "course": 2,
        "subjects": {
            "Математика": 90,
            "Програмування": 88,
            "Фізика": 82
        }
    },
    3: {
        "group": "КН-21",
        "name": "Коваленко Дмитро Олександрович",
        "course": 2,
        "subjects": {
            "Математика": 70,
            "Програмування": 75,
            "Фізика": 68
        }
    }
}

# --- Функція для додавання нового студента ---
def add_student(students_dict, student_id, group, name, course, subjects):
    """
    Додає нового студента до словника.
    :param students_dict: головний словник зі студентами
    :param student_id: унікальний ID студента
    :param group: номер групи
    :param name: ПІБ студента
    :param course: курс навчання
    :param subjects: словник з предметами та оцінками
    """
    students_dict[student_id] = {
        "group": group,
        "name": name,
        "course": course,
        "subjects": subjects
    }
    print(f" Студента '{name}' успішно додано до бази.")

# --- Перевірка роботи функції ---
new_subjects = {
    "Математика": 88,
    "Програмування": 91,
    "Фізика": 79
}

add_student(students, 4, "КН-21", "Козленко Богдан Віталійович", 2, new_subjects)

# --- Вивід усіх студентів ---
print("\nПоточний список студентів:")
for student_id, info in students.items():
    print(f"ID: {student_id} | {info['name']} | Курс: {info['course']} | "
          f"Середній бал: {sum(info['subjects'].values()) / len(info['subjects'])}")


# --- Функція сортування студентів за середнім балом ---
# Код написала: Головчук Н.

def sort_students_by_average(students_dict, reverse=True):
    return sorted(
        students_dict.items(),
        key=lambda item: sum(item[1]["subjects"].values()) / len(item[1]["subjects"]),
        reverse=reverse
    )

print("\nСортування студентів за середнім балом (від найвищого):")
sorted_students = sort_students_by_average(students)

for student_id, info in sorted_students:
    avg = sum(info["subjects"].values()) / len(info["subjects"])
    print(f"ID: {student_id} | {info['name']} | Середній бал: {avg:.2f}")
