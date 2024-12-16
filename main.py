from data import *


def make_schedule():
    grades_schedule = {
        day: {grade_dict["grade"] + grade_dict["letter"]: {i: None for i in range(1, 8)} for grade_dict in classes} for
        day in DAYS}
    teachers_schedule = {day: {teacher: {i: None for i in range(1, 8)} for teacher in teachers if
                               day in teachers[teacher]["available_days"]} for day in DAYS}

    for teacher_name in teachers:
        for subject in teachers[teacher_name]["subjects"]:
            for grade in teachers[teacher_name]["subjects"][subject]:
                count_of_lessons = subjects[subject][grade]
                for i in range(1, 8):
                    if count_of_lessons == 0:
                        break
                    for day in teachers[teacher_name]["available_days"]:
                        if (grades_schedule[day][grade][i] is None
                                and teachers_schedule[day][teacher_name][i] is None):
                            grades_schedule[day][grade][i] = subject
                            teachers_schedule[day][teacher_name][i] = grade
                            count_of_lessons -= 1
                        if count_of_lessons == 0:
                            break
    return grades_schedule, teachers_schedule

grades_schedule, teachers_schedule = make_schedule()
