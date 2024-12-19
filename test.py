import random
from pprint import pprint
from random import randint

# grade = random.randint(5, 11)
# letter = random.choice(["А", "Б", "В", "Г"])

DAYS = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"]
COUNT_DAYS = 5

classes = [{"grade": "10", "letter": "А"}]

subjects = {
    "Русский язык": {"10А": 3},
    "Английский язык": {"10А": 3},
    "Физкультура": {"10А": 3},
    "История": {"10А": 3},
    "География": {"10А": 3},
    "Химия": {"10А": 3},
    "Физика": {"10А": 3},
    "Информатика": {"10А": 2},
    "Литература": {"10А": 2},
    "Алгебра": {"10А": 2},
    "Геометрия": {"10А": 2},
    "Обществознание": {"10А": 2},
    "Биология": {"10А": 2},
    "ОБЗР": {"10А": 2}
}

academic_load_per_week = {
    "5": 30,
    "6": 30,
    "7": 32,
    "8": 33,
    "9": 33,
    "10": 34,
    "11": 35
}

with open("male_names_rus.txt", "r", encoding="utf-8") as file: names = file.readlines()
with open("male_surnames_rus.txt", "r", encoding="utf-8") as file: surnames = file.readlines()
names = [names[randint(0, 734)].rstrip() for _ in range(14)]
surnames = [surnames[randint(0, 14650)].rstrip() for _ in range(14)]

teachers = {f"{names[i]} {surnames[i]}": {"subjects": {list(subjects.keys())[i]: ["10А"]}, "available_days": DAYS} for i in range(14)}
