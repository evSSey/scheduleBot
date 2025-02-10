import tkinter as tk
from tkinter import ttk
import json
import os

TEACHERS_FILE = "teachers.json"
SUBJECTS_FILE = "subjects.json"
CLASSES_FILE = "classes.json"


class SchoolScheduleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Автоматическое расписание")
        self.root.geometry("600x400")

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill="both", expand=True)

        self.teachers = self.load_data(TEACHERS_FILE)
        self.subjects = self.load_data(SUBJECTS_FILE)
        self.classes = self.load_data(CLASSES_FILE)

        self.create_classes_tab()
        self.create_subjects_tab()
        self.create_teachers_tab()
        self.create_settings_tab()
        self.create_schedule_tab()

    def create_classes_tab(self):
        self.classes_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.classes_tab, text="Классы")

        ttk.Label(self.classes_tab, text="Добавить класс").pack()
        frame = ttk.Frame(self.classes_tab)
        frame.pack(pady=10)

        ttk.Label(frame, text="Класс:").grid(row=0, column=0)
        self.grade_entry = ttk.Entry(frame, width=5)
        self.grade_entry.grid(row=0, column=1)

        ttk.Label(frame, text="Буква:").grid(row=0, column=2)
        self.letter_entry = ttk.Entry(frame, width=5)
        self.letter_entry.grid(row=0, column=3)

        self.add_class_button = ttk.Button(frame, text="Добавить", command=self.add_class)
        self.add_class_button.grid(row=0, column=4, padx=5)

        self.classes_listbox = tk.Listbox(self.classes_tab, width=50, height=10)
        self.classes_listbox.pack()

        self.update_classes_listbox()

    def add_class(self):
        grade = self.grade_entry.get().strip()
        letter = self.letter_entry.get().strip()

        if grade:
            new_class = {"grade": grade, "letter": letter}

            if new_class not in self.classes:
                self.classes.append(new_class)
                self.save_data(CLASSES_FILE, self.classes)
                self.update_classes_listbox()

    def update_classes_listbox(self):
        self.classes_listbox.delete(0, tk.END)
        for class_info in self.classes:
            class_display = f"{class_info['grade']}{class_info['letter']}"
            self.classes_listbox.insert(tk.END, class_display)

    def create_subjects_tab(self):
        self.subjects_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.subjects_tab, text="Предметы")

        ttk.Label(self.subjects_tab, text="Добавить предмет").pack()
        frame = ttk.Frame(self.subjects_tab)
        frame.pack(pady=10)

        ttk.Label(frame, text="Название:").grid(row=0, column=0)
        self.subject_entry = ttk.Entry(frame, width=20)
        self.subject_entry.grid(row=0, column=1)

        ttk.Label(frame, text="Класс:").grid(row=0, column=2)
        self.class_entry = ttk.Entry(frame, width=5)
        self.class_entry.grid(row=0, column=3)

        ttk.Label(frame, text="Часы:").grid(row=0, column=4)
        self.hours_entry = ttk.Entry(frame, width=5)
        self.hours_entry.grid(row=0, column=5)

        self.add_subject_button = ttk.Button(frame, text="Добавить", command=self.add_subject)
        self.add_subject_button.grid(row=0, column=6, padx=5)

        self.subjects_listbox = tk.Listbox(self.subjects_tab, width=50, height=10)
        self.subjects_listbox.pack()

        self.update_subjects_listbox()

    def add_subject(self):
        subject = self.subject_entry.get().strip()
        class_name = self.class_entry.get().strip()
        hours = self.hours_entry.get().strip()

        if subject and class_name and hours.isdigit():
            hours = int(hours)

            if subject not in self.subjects:
                self.subjects[subject] = {}

            self.subjects[subject][class_name] = hours
            self.save_data(SUBJECTS_FILE, self.subjects)
            self.update_subjects_listbox()

    def update_subjects_listbox(self):
        self.subjects_listbox.delete(0, tk.END)
        for subject, classes in self.subjects.items():
            for class_name, hours in classes.items():
                self.subjects_listbox.insert(tk.END, f"{subject} ({class_name}): {hours} ч.")

    def create_teachers_tab(self):
        self.teachers_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.teachers_tab, text="Учителя")

        ttk.Label(self.teachers_tab, text="Добавить учителя").pack()
        frame = ttk.Frame(self.teachers_tab)
        frame.pack(pady=10)

        ttk.Label(frame, text="ФИО:").grid(row=0, column=0)
        self.teacher_name_entry = ttk.Entry(frame, width=20)
        self.teacher_name_entry.grid(row=0, column=1)

        ttk.Label(frame, text="Предмет:").grid(row=0, column=2)
        self.teacher_subject_entry = ttk.Entry(frame, width=15)
        self.teacher_subject_entry.grid(row=0, column=3)

        ttk.Label(frame, text="Классы (через запятую):").grid(row=1, column=0)
        self.teacher_classes_entry = ttk.Entry(frame, width=20)
        self.teacher_classes_entry.grid(row=1, column=1)

        ttk.Label(frame, text="Дни (через запятую):").grid(row=1, column=2)
        self.teacher_days_entry = ttk.Entry(frame, width=20)
        self.teacher_days_entry.grid(row=1, column=3)

        self.add_teacher_button = ttk.Button(frame, text="Добавить", command=self.add_teacher)
        self.add_teacher_button.grid(row=1, column=4, padx=5)

        self.teachers_listbox = tk.Listbox(self.teachers_tab, width=70, height=10)
        self.teachers_listbox.pack()

        self.update_teachers_listbox()

    def add_teacher(self):
        name = self.teacher_name_entry.get().strip()
        subject = self.teacher_subject_entry.get().strip()
        classes = self.teacher_classes_entry.get().strip().split(",")
        days = self.teacher_days_entry.get().strip().split(",")

        classes = [c.strip() for c in classes if c.strip()]
        days = [d.strip() for d in days if d.strip()]

        if name and subject and classes and days:
            if name not in self.teachers:
                self.teachers[name] = {"subjects": {}, "available_days": days}

            if subject not in self.teachers[name]["subjects"]:
                self.teachers[name]["subjects"][subject] = []

            self.teachers[name]["subjects"][subject].extend(classes)
            self.teachers[name]["subjects"][subject] = list(set(self.teachers[name]["subjects"][subject]))

            self.save_data(TEACHERS_FILE, self.teachers)
            self.update_teachers_listbox()

    def update_teachers_listbox(self):
        self.teachers_listbox.delete(0, tk.END)
        for name, data in self.teachers.items():
            subjects_info = ", ".join(
                [f"{subject}: {', '.join(classes)}" for subject, classes in data["subjects"].items()]
            )
            days_info = ", ".join(data["available_days"])
            self.teachers_listbox.insert(tk.END, f"{name} | {subjects_info} | Дни: {days_info}")

    def save_data(self, file_path, data):
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def load_data(self, file_path):
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        return [] if file_path == CLASSES_FILE else {}

    def create_settings_tab(self):
        self.settings_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.settings_tab, text="Настройки")
        ttk.Label(self.settings_tab, text="Раздел в разработке").pack()

    def create_schedule_tab(self):
        self.schedule_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.schedule_tab, text="Расписание")


if __name__ == "__main__":
    root = tk.Tk()
    app = SchoolScheduleApp(root)
    root.mainloop()
