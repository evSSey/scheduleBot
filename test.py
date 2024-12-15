from data import *


def make_schedule_without_subjects():
    schedule = {}
    for grade_data in academic_load_per_week:
        grade = grade_data["grade"]
        lessons_per_week = grade_data["lessons_per_week"]

        min_lessons_per_day = lessons_per_week // COUNT_DAYS
        remain_of_lessons = lessons_per_week - (min_lessons_per_day * COUNT_DAYS)
        lessons = {}

        for i in range(COUNT_DAYS):
            lessons_per_day = min_lessons_per_day + (1 if remain_of_lessons - 1 >= i else 0)
            lessons[DAYS[i]] = {i: None for i in range(1, lessons_per_day + 1)}

        schedule[grade] = lessons
    return schedule

schedule_without_subjects = make_schedule_without_subjects()

print(schedule_without_subjects)

# def main():
#     root = tk.Tk()
#     root.wm_geometry("1500x850")
#     root.title("Составитель Расписаний")
#     hello_window()
#     root.mainloop()
#
# if __name__ == "__main__":
#     main()
