from data import *


def make_schedule():
    schedule = {grade_data["grade"] + grade_data["letter"]: {day: {i: None for i in range(1, 8)} for day in DAYS} for
                grade_data in classes}

    for teacher_name in teachers:
        teacher_schedule = {day: {i: None for i in range(1, 8)} for day in teachers[teacher_name]["available_days"]}

        for subject in teachers[teacher_name]["subjects"]:

            for grade in teachers[teacher_name]["subjects"][subject]:
                count_of_lessons = subjects[subject][grade]

                for i in range(1, 8):
                    if count_of_lessons == 0:
                        break
                    for day in teachers[teacher_name]["available_days"]:
                        if schedule[grade][day][i] is None and teacher_schedule[day][i] is None:
                            schedule[grade][day][i] = subject
                            teacher_schedule[day][i] = grade
                            count_of_lessons -= 1
                        if count_of_lessons == 0:
                            break
    return schedule


def show_schedule(schedule):
    for g in schedule:
        print(g)
        for d in schedule[g]:
            print(d)
            for l in schedule[g][d]:
                print(l, schedule[g][d][l])
        print()


schedule = make_schedule()
print(schedule)
