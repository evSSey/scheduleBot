import tkinter as tk

ROOT = tk.Tk()

def delete_widgets() -> None:
    for widget in root.winfo_children():
        widget.destroy()


def make_new_schedule() -> None:
    delete_widgets()

    sign = tk.Label(text="Окно создания нового расписания")
    sign.pack(expand=True, fill="none")

    btn_back = tk.Button(text="Назад", command=hello_window)
    btn_back.pack(expand=True, fill="none")


def edit_schedule() -> None:
    delete_widgets()
    sign = tk.Label(text="Окно изменения расписания")
    sign.pack(expand=True, fill="none")

    btn_back = tk.Button(text="Назад", command=hello_window)
    btn_back.pack(expand=True, fill="none")


def hello_window() -> None:
    delete_widgets()

    hello_text = tk.Label(text="Составитель Расписаний", font=("Arial", 45))
    hello_text.pack(expand=True, fill="none")

    btn_new_schedule = tk.Button(text="Создать новое расписание", command=make_new_schedule)
    btn_new_schedule.pack(expand=True, fill="none")

    btn_edit_schedule = tk.Button(text="Изменить текущее расписание", command=edit_schedule)
    btn_edit_schedule.pack(expand=True, fill="none")


if __name__ == "__main__":
    root = tk.Tk()
    root.wm_geometry("1500x850")
    root.title("Составитель Расписаний")
    hello_window()
    root.mainloop()
