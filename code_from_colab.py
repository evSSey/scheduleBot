import pandas as pd
from main import *

schedule = {day: {grade_dict["grade"] + grade_dict["letter"]: {i: None for i in range(1, 8)} for grade_dict in classes}
            for day in DAYS}

grades_schedule, teachers_schedule = make_schedule()

friday = pd.DataFrame.from_dict(grades_schedule["Пятница"])

friday.to_excel("name.xlsx")