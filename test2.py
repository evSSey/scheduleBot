import tkinter as tk
from tkinter import ttk, messagebox


class SchoolScheduleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Автоматическое расписание")
        self.root.geometry("700x500")

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True)

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

        self.classes = []

    def add_class(self):
        grade = self.grade_entry.get()
        letter = self.letter_entry.get()
        if grade and letter:
            class_name = f"{grade}{letter}"
            self.classes.append({"grade": grade, "letter": letter})
            self.classes_listbox.insert(tk.END, class_name)

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

        self.subjects = {}

    def add_subject(self):
        subject = self.subject_entry.get()
        class_name = self.class_entry.get()
        hours = self.hours_entry.get()

        if subject and class_name and hours.isdigit():
            if subject not in self.subjects:
                self.subjects[subject] = {}
            self.subjects[subject][class_name] = int(hours)
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
        self.teacher_subject_entry = ttk.Entry(frame, width=20)
        self.teacher_subject_entry.grid(row=0, column=3)

        ttk.Label(frame, text="Классы (через запятую):").grid(row=1, column=0)
        self.teacher_classes_entry = ttk.Entry(frame, width=20)
        self.teacher_classes_entry.grid(row=1, column=1)

        ttk.Label(frame, text="Доступные дни (через запятую):").grid(row=1, column=2)
        self.teacher_days_entry = ttk.Entry(frame, width=20)
        self.teacher_days_entry.grid(row=1, column=3)

        self.add_teacher_button = ttk.Button(frame, text="Добавить", command=self.add_teacher)
        self.add_teacher_button.grid(row=1, column=4, padx=5)

        self.teachers_listbox = tk.Listbox(self.teachers_tab, width=70, height=10)
        self.teachers_listbox.pack()

        self.teachers = {}

    def add_teacher(self):
        name = self.teacher_name_entry.get()
        subject = self.teacher_subject_entry.get()
        classes = self.teacher_classes_entry.get().split(",")
        available_days = self.teacher_days_entry.get().split(",")

        if name and subject and classes and available_days:
            classes = [cls.strip() for cls in classes]
            available_days = [day.strip() for day in available_days]

            if name not in self.teachers:
                self.teachers[name] = {"subjects": {}, "available_days": available_days}
            if subject not in self.teachers[name]["subjects"]:
                self.teachers[name]["subjects"][subject] = classes

            self.teachers_listbox.insert(tk.END,
                                         f"{name}: {subject} ({', '.join(classes)}) - {', '.join(available_days)}")

    def create_settings_tab(self):
        self.settings_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.settings_tab, text="Настройки")
        ttk.Label(self.settings_tab, text="Раздел в разработке").pack()

    def create_schedule_tab(self):
        self.schedule_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.schedule_tab, text="Расписание")

        self.generate_schedule_button = ttk.Button(self.schedule_tab, text="Сгенерировать расписание")
        self.generate_schedule_button.pack(pady=20)


if __name__ == "__main__":
    root = tk.Tk()
    app = SchoolScheduleApp(root)
    root.mainloop()
