from functions import *
from pprint import pprint

data = make_schedule()

pprint(data)
df_to_excel("Расписание", data["Расписание"])
df_to_excel("Учителям", data["Расписание для учителей"])