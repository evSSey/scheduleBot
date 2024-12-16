from pprint import pprint

from data import *

grades_schedule = {
    day: {grade_dict["grade"] + grade_dict["letter"]: {i: None for i in range(1, 8)} for grade_dict in classes} for
    day in DAYS}
teachers_schedule = {day: {teacher: {i: None for i in range(1, 8)} for teacher in teachers if day in teachers[teacher]["available_days"]} for day in DAYS}
pprint(teachers_schedule)




# from data import *
#
#
# def make_schedule_without_subjects():
#     schedule = {}
#     for grade_data in academic_load_per_week:
#         grade = grade_data["grade"]
#         lessons_per_week = grade_data["lessons_per_week"]
#
#         min_lessons_per_day = lessons_per_week // COUNT_DAYS
#         remain_of_lessons = lessons_per_week - (min_lessons_per_day * COUNT_DAYS)
#         lessons = {}
#
#         for i in range(COUNT_DAYS):
#             lessons_per_day = min_lessons_per_day + (1 if remain_of_lessons - 1 >= i else 0)
#             lessons[DAYS[i]] = {i: None for i in range(1, lessons_per_day + 1)}
#
#         schedule[grade] = lessons
#     return schedule
#
# schedule_without_subjects = make_schedule_without_subjects()
#
# print(schedule_without_subjects)
#
# # def main():
# #     root = tk.Tk()
# #     root.wm_geometry("1500x850")
# #     root.title("Составитель Расписаний")
# #     hello_window()
# #     root.mainloop()
# #
# # if __name__ == "__main__":
# #     main()
