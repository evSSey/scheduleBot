DAYS = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"]

COUNT_DAYS = 5

teachers = {
    "Ольга Иванова": {
        "subjects": {"Русский язык": ['5А', '5Б', '6А', '6Б', '7А', '7Б', '8А', '8Б', '9А', '9Б', '10А', '11А']},
        "available_days": ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"],
    },
    "Анна Смирнова": {
        "subjects": {"Иностранный язык": ['5А', '5Б', '6А', '6Б', '7А', '7Б', '8А', '8Б', '9А', '9Б', '10А', '11А']},
        "available_days": ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"],
    },
    "Сергей Петров": {
        "subjects": {"Литература": ['5А', '5Б', '6А', '6Б', '7А', '7Б', '8А', '8Б', '9А', '9Б', '10А', '11А']},
        "available_days": ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"],
    },
    "Марина Кузнецова": {
        "subjects": {"Алгебра": ['7А', '7Б', '8А', '8Б', '9А', '9Б', '10А', '11А']},
        "available_days": ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"],
    },
    "Алексей Сидоров": {
        "subjects": {"История": ['5А', '5Б', '6А', '6Б', '7А', '7Б', '8А', '8Б', '9А', '9Б', '10А', '11А']},
        "available_days": ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"],
    },
    "Дмитрий Васильев": {
        "subjects": {"Физическая культура": ['5А', '5Б', '6А', '6Б', '7А', '7Б', '8А', '8Б', '9А', '9Б', '10А', '11А']},
        "available_days": ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"],
    },
    "Елена Фёдорова": {
        "subjects": {"Математика": ['5А', '5Б', '6А', '6Б']},
        "available_days": ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"],
    },
    "Олег Никитин": {
        "subjects": {"География": ['5А', '5Б', '6А', '6Б', '7А', '7Б', '8А', '8Б', '9А', '9Б', '10А', '11А']},
        "available_days": ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"],
    },
    "Ирина Павлова": {
        "subjects": {"Геометрия": ['7А', '7Б', '8А', '8Б', '9А', '9Б', '10А', '11А']},
        "available_days": ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"],
    },
    "Николай Беляев": {
        "subjects": {"Физика": ['7А', '7Б', '8А', '8Б', '9А', '9Б', '10А', '11А']},
        "available_days": ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"],
    },
    "Татьяна Орлова": {
        "subjects": {"Биология": ['5А', '5Б', '6А', '6Б', '7А', '7Б', '8А', '8Б', '9А', '9Б', '10А', '11А']},
        "available_days": ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"],
    },
    "Артём Захаров": {
        "subjects": {"Технология": ['5А', '5Б', '6А', '6Б', '7А', '7Б', '8А', '8Б', '9А', '9Б']},
        "available_days": ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"],
    },
    "Виктория Андреева": {
        "subjects": {"Обществознание": ['6А', '6Б', '7А', '7Б', '8А', '8Б', '9А', '9Б', '10А', '11А']},
        "available_days": ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"],
    },
    "Максим Громов": {
        "subjects": {"Химия": ['8А', '8Б', '9А', '9Б', '10А', '11А']},
        "available_days": ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"],
    },
    "Светлана Егорова": {
        "subjects": {"Музыка": ['5А', '5Б', '6А', '6Б', '7А', '7Б', '8А', '8Б']},
        "available_days": ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"],
    },
    "Владимир Тихонов": {
        "subjects": {"Вероятность и статистика": ['7А', '7Б', '8А', '8Б', '9А', '9Б', '10А', '11А']},
        "available_days": ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"],
    },
    "Александра Лебедева": {
        "subjects": {"Информатика": ['7А', '7Б', '8А', '8Б', '9А', '9Б', '10А', '11А']},
        "available_days": ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"],
    },
    "Евгения Волкова": {
        "subjects": {"ИЗО": ['5А', '5Б', '6А', '6Б', '7А', '7Б']},
        "available_days": ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"],
    },
    "Константин Романов": {
        "subjects": {"ОБЗР": ['8А', '8Б', '9А', '9Б', '10А', '11А']},
        "available_days": ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"],
    },
    "Галина Филатова": {
        "subjects": {"ОДНКНР": ['5А', '5Б', '6А', '6Б']},
        "available_days": ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"],
    },
    "Игорь Васильев": {
        "subjects": {"Индивидуальный проект": ['10А']},
        "available_days": ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"],
    }
}

grades = {
    '5А':
        {
            'Биология': 1,
            'География': 1,
            'ИЗО': 1,
            'Иностранный язык': 3,
            'История': 2,
            'Литература': 3,
            'Математика': 5,
            'Музыка': 1,
            'ОДНКНР': 1,
            'Русский язык': 5,
            'Технология': 2,
            'Физическая культура': 2
        },
    '5Б':
        {
            'Биология': 1,
            'География': 1,
            'ИЗО': 1,
            'Иностранный язык': 3,
            'История': 2,
            'Литература': 3,
            'Математика': 5,
            'Музыка': 1,
            'ОДНКНР': 1,
            'Русский язык': 5,
            'Технология': 2,
            'Физическая культура': 2
        },
    '6А':
        {
            'Биология': 1,
            'География': 1,
            'ИЗО': 1,
            'Иностранный язык': 3,
            'История': 2,
            'Литература': 3,
            'Математика': 5,
            'Музыка': 1,
            'Обществознание': 1,
            'ОДНКНР': 1,
            'Русский язык': 6,
            'Технология': 2,
            'Физическая культура': 2
        },
    '6Б':
        {
            'Биология': 1,
            'География': 1,
            'ИЗО': 1,
            'Иностранный язык': 3,
            'История': 2,
            'Литература': 3,
            'Математика': 5,
            'Музыка': 1,
            'Обществознание': 1,
            'ОДНКНР': 1,
            'Русский язык': 6,
            'Технология': 2,
            'Физическая культура': 2
        },
    '7А':
        {
            'Алгебра': 3,
            'Биология': 1,
            'Вероятность и статистика': 1,
            'География': 2,
            'Геометрия': 2,
            'ИЗО': 1,
            'Информатика': 1,
            'Иностранный язык': 3,
            'История': 2,
            'Литература': 2,
            'Музыка': 1,
            'Обществознание': 1,
            'Русский язык': 4,
            'Технология': 2,
            'Физика': 2,
            'Физическая культура': 2
        },
    "7Б":
        {
            'Алгебра': 3,
            'Биология': 1,
            'Вероятность и статистика': 1,
            'География': 2,
            'Геометрия': 2,
            'ИЗО': 1,
            'Информатика': 1,
            'Иностранный язык': 3,
            'История': 2,
            'Литература': 2,
            'Музыка': 1,
            'Обществознание': 1,
            'Русский язык': 4,
            'Технология': 2,
            'Физика': 2,
            'Физическая культура': 2
        },
    '8А':
        {
            'Алгебра': 3,
            'Биология': 2,
            'Вероятность и статистика': 1,
            'География': 2,
            'Геометрия': 2,
            'Информатика': 1,
            'Иностранный язык': 3,
            'История': 2,
            'Литература': 2,
            'Музыка': 1,
            'Обществознание': 1,
            'ОБЗР': 1,
            'Русский язык': 3,
            'Технология': 1,
            'Физика': 2,
            'Физическая культура': 2,
            'Химия': 2
        },
    '8Б':
        {
            'Алгебра': 3,
            'Биология': 2,
            'Вероятность и статистика': 1,
            'География': 2,
            'Геометрия': 2,
            'Информатика': 1,
            'Иностранный язык': 3,
            'История': 2,
            'Литература': 2,
            'Музыка': 1,
            'Обществознание': 1,
            'ОБЗР': 1,
            'Русский язык': 3,
            'Технология': 1,
            'Физика': 2,
            'Физическая культура': 2,
            'Химия': 2
        },
    '9А':
        {
            'Алгебра': 3,
            'Биология': 2,
            'Вероятность и статистика': 1,
            'География': 2,
            'Геометрия': 2,
            'Информатика': 1,
            'Иностранный язык': 3,
            'История': 2,
            'Литература': 3,
            'Обществознание': 1,
            'ОБЗР': 1,
            'Русский язык': 3,
            'Технология': 1,
            'Физика': 3,
            'Физическая культура': 2,
            'Химия': 2
        },
    '9Б':
        {
            'Алгебра': 3,
            'Биология': 2,
            'Вероятность и статистика': 1,
            'География': 2,
            'Геометрия': 2,
            'Информатика': 1,
            'Иностранный язык': 3,
            'История': 2,
            'Литература': 3,
            'Обществознание': 1,
            'ОБЗР': 1,
            'Русский язык': 3,
            'Технология': 1,
            'Физика': 3,
            'Физическая культура': 2,
            'Химия': 2
        },
    '10А':
        {
            'Алгебра': 4,
            'Биология': 1,
            'Вероятность и статистика': 1,
            'География': 1,
            'Геометрия': 3,
            'Индивидуальный проект': 1,
            'Информатика': 1,
            'Иностранный язык': 3,
            'История': 2,
            'Литература': 3,
            'Обществознание': 4,
            'ОБЗР': 1,
            'Русский язык': 2,
            'Физика': 2,
            'Физическая культура': 2,
            'Химия': 1
        },
    '11А':
        {
            'Алгебра': 4,
            'Биология': 1,
            'Вероятность и статистика': 1,
            'География': 1,
            'Геометрия': 3,
            'Информатика': 1,
            'Иностранный язык': 3,
            'История': 2,
            'Литература': 3,
            'Обществознание': 4,
            'ОБЗР': 1,
            'Русский язык': 2,
            'Физика': 2,
            'Физическая культура': 2,
            'Химия': 1
        }
}


# teachers = {
#     "Иван Иванов": {
#         "subjects": {"Математика": ["5А", "5Б", "6А", "6Б", "7А"]},
#         "available_days": ["Понедельник", "Вторник", "Среда", "Четверг"],
#     },
#     "Ольга Петрова": {
#         "subjects": {"Русский язык": ["5А", "6А", "7А"], "Литература": ["5А", "6А"]},
#         "available_days": ["Понедельник", "Вторник", "Пятница"],
#     },
#     "Елена Смирнова": {
#         "subjects": {"Английский язык": ["5Б", "6Б", "7А", "8А"]},
#         "available_days": ["Вторник", "Среда", "Четверг"],
#     },
#     "Дмитрий Павлов": {
#         "subjects": {"Физкультура": ["5А", "5Б", "6А", "7А", "8А", "9А"]},
#         "available_days": ["Понедельник", "Среда", "Пятница"],
#     },
#     "Анна Сидорова": {
#         "subjects": {"История": ["6Б", "7А", "8А"], "География": ["5А", "6А", "7А"]},
#         "available_days": ["Вторник", "Четверг", "Пятница"],
#     },
#     "Виктор Васильев": {
#         "subjects": {"Физика": ["8А", "9А", "10А", "11А"], "Химия": ["8А", "9А", "10А", "11А"]},
#         "available_days": ["Среда", "Четверг", "Пятница"],
#     },
#     "Мария Кузьмина": {
#         "subjects": {"Информатика": ["8А", "9А", "10А", "11А"]},
#         "available_days": ["Понедельник", "Вторник", "Пятница"],
#     },
# }

# academic_load_per_week = {
#     "5": 30,
#     "6": 30,
#     "7": 32,
#     "8": 33,
#     "9": 33,
#     "10": 34,
#     "11": 35
# }
# with open("male_names_rus.txt", "r", encoding="utf-8") as file: names = file.readlines()
# with open("male_surnames_rus.txt", "r", encoding="utf-8") as file: surnames = file.readlines()
# names = [names[randint(0, 734)].rstrip() for _ in range(14)]
# surnames = [surnames[randint(0, 14650)].rstrip() for _ in range(14)]
# teachers = {f"{names[i]} {surnames[i]}": {"subjects": {list(subjects.keys())[i]: ["10А"]}, "available_days": DAYS} for i in range(14)}
# Учителя и их связь с классами и предметами
# grade = random.randint(5, 11)
# letter = random.choice(["А", "Б", "В", "Г"])
# # Классы школы
# classes = [
#     {"grade": "5", "letter": "А"},
#     {"grade": "5", "letter": "Б"},
#     {"grade": "6", "letter": "А"},
#     {"grade": "6", "letter": "Б"},
#     {"grade": "7", "letter": "А"},
#     {"grade": "8", "letter": "А"},
#     {"grade": "9", "letter": "А"},
#     {"grade": "10", "letter": "А"},
#     {"grade": "11", "letter": "А"},
# ]
# subjects = {
#     "Математика": {"5А": 5, "5Б": 5, "6А": 5, "6Б": 5, "7А": 6, "8А": 6, "9А": 6, "10А": 6, "11А": 6},
#     "Русский язык": {"5А": 4, "5Б": 4, "6А": 4, "6Б": 4, "7А": 4, "8А": 4, "9А": 4, "10А": 4, "11А": 4},
#     "Английский язык": {"5А": 3, "5Б": 3, "6А": 3, "6Б": 3, "7А": 3, "8А": 3, "9А": 3, "10А": 3, "11А": 3},
#     "Физкультура": {"5А": 2, "5Б": 2, "6А": 2, "6Б": 2, "7А": 2, "8А": 2, "9А": 2, "10А": 2, "11А": 2},
#     "История": {"5А": 2, "5Б": 2, "6А": 3, "6Б": 3, "7А": 3, "8А": 3, "9А": 3, "10А": 2, "11А": 2},
#     "География": {"5А": 2, "5Б": 2, "6А": 2, "6Б": 2, "7А": 2, "8А": 2, "9А": 2, "10А": 1, "11А": 1},
#     "Химия": {"8А": 2, "9А": 2, "10А": 2, "11А": 2},
#     "Физика": {"7А": 2, "8А": 3, "9А": 3, "10А": 3, "11А": 3},
#     "Информатика": {"8А": 2, "9А": 2, "10А": 2, "11А": 2},
#     "Литература": {"5А": 2, "5Б": 2, "6А": 2, "6Б": 2, "7А": 2, "8А": 2, "9А": 2, "10А": 2, "11А": 2},
# }