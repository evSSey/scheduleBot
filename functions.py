from test import *
import pandas as pd

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
    return {"Расписание": grades_schedule, "Расписание для учителей": teachers_schedule}


def df_to_excel(name, schedule):
    # Данные для пятницы
    for d in DAYS:
        day = pd.DataFrame.from_dict(schedule[d])

        # Создаем ExcelWriter с движком xlsxwriter
        with pd.ExcelWriter(f"C:\\Users\\Evsey\\PycharmProjects\\scheduleBot\\Excel Schedule\\{name} {d}.xlsx", engine="xlsxwriter") as writer:
            # Записываем датафрейм в Excel с индексом и без замены пропусков
            day.to_excel(writer, sheet_name=f"{d}", index=True, na_rep="")

            # Получаем доступ к листу
            worksheet = writer.sheets[f"{d}"]

            # Настраиваем ширину колонок
            for i, column in enumerate(day.columns.insert(0, day.index.name or "Index")):
                # Определяем максимальную ширину данных в колонке
                max_width = max(
                    day[column].astype(str).map(len).max() if column in day.columns else day.index.astype(str).map(
                        len).max(),
                    len(column)
                )
                # Устанавливаем ширину колонки
                worksheet.set_column(i, i, max_width + 2)  # +2 для небольшого отступа
