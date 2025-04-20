import tkinter as tk
from tkinter import ttk
import json
import os

TEACHERS_FILE = "json objects/teachers.json"
SUBJECTS_FILE = "json objects/subjects.json"
CLASSES_FILE = "json objects/classes.json"



class SchoolScheduleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Автоматическое расписание")
        icon = tk.PhotoImage(file="icon.png")
        self.root.iconphoto(False, icon)
        # Размеры окна
        window_width = 600
        window_height = 400

        # Получаем размеры экрана
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Вычисляем координаты для центра
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # Устанавливаем геометрию окна
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Интерфейс
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

        # Класс (1-11)
        ttk.Label(frame, text="Класс:").grid(row=0, column=0)
        self.grade_var = tk.StringVar()
        self.grade_combobox = ttk.Combobox(frame, textvariable=self.grade_var, width=5, state="readonly")
        self.grade_combobox["values"] = [str(i) for i in range(1, 12)]
        self.grade_combobox.grid(row=0, column=1)

        # Буква (А-Я)
        ttk.Label(frame, text="Буква:").grid(row=0, column=2)
        self.letter_var = tk.StringVar()
        self.letter_combobox = ttk.Combobox(frame, textvariable=self.letter_var, width=5, state="readonly")
        self.letter_combobox["values"] = [chr(i) for i in range(ord("А"), ord("Я") + 1)]
        self.letter_combobox.grid(row=0, column=3)

        self.add_class_button = ttk.Button(frame, text="Добавить", command=self.add_class)
        self.add_class_button.grid(row=0, column=4, padx=5)

        self.classes_listbox = tk.Listbox(self.classes_tab, width=50, height=10)
        self.classes_listbox.pack()

        buttons_frame = ttk.Frame(self.classes_tab)
        buttons_frame.pack(pady=5)

        ttk.Button(buttons_frame, text="Удалить", command=self.delete_class).grid(row=0, column=0, padx=5)
        ttk.Button(buttons_frame, text="Изменить", command=self.edit_class).grid(row=0, column=1, padx=5)

        self.update_classes_listbox()

    def add_class(self):
        grade = self.grade_var.get().strip()
        letter = self.letter_var.get().strip()

        if grade:
            new_class = {"grade": grade, "letter": letter}

            if new_class not in self.classes:
                self.classes.append(new_class)
                self.save_data(CLASSES_FILE, self.classes)
                self.update_classes_listbox()

    def delete_class(self):
        selection = self.classes_listbox.curselection()
        if selection:
            index = selection[0]
            del self.classes[index]
            self.save_data(CLASSES_FILE, self.classes)
            self.update_classes_listbox()

    def edit_class(self):
        selection = self.classes_listbox.curselection()
        if selection:
            index = selection[0]
            grade = self.grade_var.get().strip()
            letter = self.letter_var.get().strip()
            if grade:
                self.classes[index] = {"grade": grade, "letter": letter}
                self.save_data(CLASSES_FILE, self.classes)
                self.update_classes_listbox()

    def update_classes_listbox(self):
        self.classes_listbox.delete(0, tk.END)
        for class_info in self.classes:
            class_display = f"{class_info['grade']}{class_info['letter']}"
            self.classes_listbox.insert(tk.END, class_display)

    def update_subject_hours(self):
        subject = self.subject_combobox.get().strip()
        class_name = self.class_combobox.get().strip()
        hours = self.hours_combobox.get().strip()  # Получаем значение из выпадающего списка

        if subject and class_name and hours.isdigit():
            hours = int(hours)

            if subject not in self.subjects:
                self.subjects[subject] = {}

            self.subjects[subject][class_name] = hours
            self.save_data(SUBJECTS_FILE, self.subjects)
            self.update_subjects_listbox()

    def create_subjects_tab(self):
        self.subjects_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.subjects_tab, text="Предметы")

        ttk.Label(self.subjects_tab, text="Изменить предметы").pack()
        frame = ttk.Frame(self.subjects_tab)
        frame.pack(pady=10)

        # Список всех предметов
        subjects = [
            'Алгебра', 'Биология', 'География', 'Геометрия', 'ИЗО',
            'Иностранный язык', 'Информатика', 'История', 'Индивидуальный проект',
            'Литература', 'Математика', 'Музыка', 'ОБЗР', 'ОДНКНР',
            'Обществознание', 'Русский язык', 'Технология', 'Физика',
            'Физическая культура', 'Вероятность и статистика'
        ]

        ttk.Label(frame, text="Предмет:").grid(row=0, column=0)
        self.subject_combobox = ttk.Combobox(frame, width=25, state="readonly")
        self.subject_combobox["values"] = subjects
        self.subject_combobox.grid(row=0, column=1)

        # Список классов
        class_names = [f"{cls['grade']}{cls['letter']}" for cls in self.classes]
        ttk.Label(frame, text="Класс:").grid(row=0, column=2)
        self.class_combobox = ttk.Combobox(frame, width=7, state="readonly")
        self.class_combobox["values"] = class_names
        self.class_combobox.grid(row=0, column=3)

        ttk.Label(frame, text="Часы:").grid(row=0, column=4)
        self.hours_combobox = ttk.Combobox(frame, width=5, state="readonly")
        self.hours_combobox["values"] = [str(i) for i in range(1, 8)]  # Выпадающий список от 1 до 7
        self.hours_combobox.grid(row=0, column=5)

        self.update_button = ttk.Button(frame, text="Изменить", command=self.update_subject_hours)
        self.update_button.grid(row=0, column=6, padx=5)

        self.subjects_listbox = tk.Listbox(self.subjects_tab, width=50, height=10)
        self.subjects_listbox.pack()

        buttons_frame = ttk.Frame(self.subjects_tab)
        buttons_frame.pack(pady=5)

        ttk.Button(buttons_frame, text="Удалить", command=self.delete_subject).grid(row=0, column=0, padx=5)

        self.update_subjects_listbox()

    def delete_subject(self):
        selection = self.subjects_listbox.curselection()
        if selection:
            item = self.subjects_listbox.get(selection[0])
            subject, class_info = item.split(" (")
            class_name = class_info.split("):")[0]
            if subject in self.subjects and class_name in self.subjects[subject]:
                del self.subjects[subject][class_name]
                if not self.subjects[subject]:
                    del self.subjects[subject]
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

        # Предмет и класс: объединяем предмет и класс в одну строку
        self.teacher_combobox = ttk.Combobox(frame, width=20, state="readonly")
        self.update_teacher_combobox()  # Обновляем комбобокс с объединёнными предметами и классами
        ttk.Label(frame, text="Предмет и класс:").grid(row=0, column=2)
        self.teacher_combobox.grid(row=0, column=3)

        # Дни: можно выбрать несколько дней
        ttk.Label(frame, text="Дни:").grid(row=1, column=0)

        # Список дней недели
        self.teacher_days_listbox = tk.Listbox(frame, selectmode=tk.MULTIPLE, height=5, exportselection=False)
        self.teacher_days_listbox.grid(row=1, column=1)
        days_of_week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"]
        for day in days_of_week:
            self.teacher_days_listbox.insert(tk.END, day)

        self.add_teacher_button = ttk.Button(frame, text="Добавить", command=self.add_teacher)
        self.add_teacher_button.grid(row=1, column=2, padx=5)

        self.teachers_listbox = tk.Listbox(self.teachers_tab, width=70, height=10)
        self.teachers_listbox.pack()

        buttons_frame = ttk.Frame(self.teachers_tab)
        buttons_frame.pack(pady=5)

        ttk.Button(buttons_frame, text="Удалить", command=self.delete_teacher).grid(row=0, column=0, padx=5)

        self.update_teachers_listbox()

    def add_teacher(self):
        name = self.teacher_name_entry.get().strip()
        teacher_class = self.teacher_combobox.get().strip()  # Получаем объединённый предмет и класс

        # Получаем выбранные дни из Listbox
        selected_days_indices = self.teacher_days_listbox.curselection()  # Получаем индексы выбранных дней
        days = [self.teacher_days_listbox.get(i) for i in selected_days_indices]  # Извлекаем сами дни

        if name and teacher_class and days:
            if name not in self.teachers:
                self.teachers[name] = {"subjects": {}, "available_days": days}

            # Разделяем предмет и класс
            subject, class_name = teacher_class.split(" (")
            class_name = class_name[:-1]  # Убираем закрывающую скобку

            if subject not in self.teachers[name]["subjects"]:
                self.teachers[name]["subjects"][subject] = []

            self.teachers[name]["subjects"][subject].append(class_name)
            self.teachers[name]["subjects"][subject] = list(
                set(self.teachers[name]["subjects"][subject]))  # Убираем дубли

            self.save_data(TEACHERS_FILE, self.teachers)
            self.update_teachers_listbox()

    def update_teacher_combobox(self):
        # Создаём комбинированный список предметов и классов
        combined_list = []
        for subject in self.subjects:
            for cls in self.classes:
                combined_list.append(f"{subject} ({cls['grade']}{cls['letter']})")
        self.teacher_combobox["values"] = combined_list

    def delete_teacher(self):
        selection = self.teachers_listbox.curselection()
        if selection:
            name = list(self.teachers.keys())[selection[0]]
            del self.teachers[name]
            self.save_data(TEACHERS_FILE, self.teachers)
            self.update_teachers_listbox()

    def update_teachers_listbox(self):
        self.teachers_listbox.delete(0, tk.END)
        for name, data in self.teachers.items():
            subjects_info = ", ".join(
                [f"{subject} ({', '.join(classes)})" for subject, classes in data["subjects"].items()]
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

        # Кнопка "Сгенерировать расписание"
        generate_button = ttk.Button(self.schedule_tab, text="Сгенерировать расписание", command=self.generate_schedule)
        generate_button.pack(pady=20)

        # Список или текстовое поле для отображения расписания (можно изменить по необходимости)
        self.schedule_output = tk.Text(self.schedule_tab, width=70, height=15, state="disabled")
        self.schedule_output.pack()

    def generate_schedule(self):
        # Здесь будет логика генерации расписания
        self.schedule_output.configure(state="normal")
        self.schedule_output.delete("1.0", tk.END)
        self.schedule_output.insert(tk.END, "Генерация расписания...\n(логика ещё не реализована)")
        self.schedule_output.configure(state="disabled")


if __name__ == "__main__":
    root = tk.Tk()
    app = SchoolScheduleApp(root)
    root.mainloop()
