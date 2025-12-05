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

# --- Оцінка словника студентом №2 ---
# Автор коментаря: Головчук Н.
# Коментар: Структура словника цілком зрозуміла і зручна для роботи з невеликою групою студентів.
#! --- Функція сортування студентів за середнім балом ---
#! Код написала: Головчук Н.


#? Обчисленя середнього балу
def get_average(student_info):
    return sum(student_info["subjects"].values()) / len(student_info["subjects"])

#? Сортування
def sort_students_by_average(students_dict, reverse=True):
    return sorted(
        students_dict.items(),
        key=lambda item: get_average(item[1]),
        reverse=reverse
    )

print("\nСортування студентів за середнім балом (від найвищого):")
sorted_students = sort_students_by_average(students)

for student_id, info in sorted_students:
    avg = get_average(info)
    print(f"ID: {student_id} | {info['name']} | Середній бал: {avg:.2f}")


#! Завдання для студента №3:

# Реалізувати функцію пошуку студента за ПІБ (повністю або частково).


# --- Оцінка коду студентом №3 ---
# Автор коментаря: Швачко Єгор
# Коментар: Функція сортування реалізована професійно. Структура словника залишається зручною, змін не потребує.

# --- Виконання завдання: Пошук студента за ПІБ ---
# Автор функції: Швачко Єгор

def find_student_by_name(students_dict, search_query):

    print(f"\n--- Результати пошуку за запитом: '{search_query}' ---")
    
    found_count = 0
    search_query = search_query.lower()

    for s_id, info in students_dict.items():
        student_name = info['name']
        
        if search_query in student_name.lower():
            avg = sum(info['subjects'].values()) / len(info['subjects'])
            
            print(f"ID: {s_id} | {student_name} | Група: {info['group']} | Середній бал: {avg:.2f}")
            
            found_count += 1

    if found_count == 0:
        print("На жаль, студентів не знайдено.")
    else:
        print(f"Знайдено студентів: {found_count}")


# --- Перевірка роботи пошуку ---
find_student_by_name(students, "Петренко")  
find_student_by_name(students, "ольга")     
find_student_by_name(students, "Сидоренко") 

# Завдання для студента №4:
# Реалізувати функцію видалення студента зі словника за його ID.
# Перед видаленням питати підтвердження (Так/Ні).

# --- Оцінка коду студентом №4 ---
# Автор коментаря: Строгий Д.Р.
# Коментар: Функція пошуку реалізована коректно (реалізовано частковий та повний пошук, нечутливість до регістру, зрозумілий неймінг) та працює без помилок.
# Внесені зміни: замінив розрахунок середніх оцінок на створену раніше студентом №2 функцію get_average(), щоб уникнути дублювання коду

# --- Виконання завдання: Видалення студента зі словника за його ID ---
# Автор коду: Строгий Д.Р.

def remove_student_by_id(students_dict, student_id):
    if student_id in students_dict:
        while True:
            confirmation = input(f"Ви впевнені, що хочете видалити студента {students_dict[student_id]['name']}? \nТак/Ні: ").strip().lower()
            if confirmation == "так":
                del students_dict[student_id]
                print("Успішно!")
                return
            elif confirmation == "ні":
                return
            else:
                print("Помилка. Введіть коректну відповідь")
                continue
    else:
        print("Помилка. Студента з заданим ID не існує")
remove_student_by_id(students, 1)

# Завдання для студента №5: 
# Реалізувати функцію редагування даних студента за його ID. Користувач має мати можливість обрати, що саме редагувати

