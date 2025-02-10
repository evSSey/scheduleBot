from functions import *

data = make_schedule()

df_to_excel("Расписание", data["Расписание"])
df_to_excel("Учителям", data["Расписание для учителей"])