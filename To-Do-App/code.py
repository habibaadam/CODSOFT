#!/usr/bin/env python3
"""CodeBase for To-Do-App(GUI)"""
import tkinter as kint
import tkinter.messagebox
from tkinter import ttk
import sys

class To_Do:
    """Defining Class For To-Do-App"""
    def __init__(self, window):
        self.window = window
        self.window.title("To-Do-App")
        self.window.geometry("650x410+300+150")
        self.window.resizable(False, False)
        self.window.config(bg="black")

        self.label = kint.Label(
            self.window, text="To-Do-List",
            font=("Helvetica", 25, "bold"),
            fg="white", bg="blue", width=10, bd=5)
        self.label.pack(side="top", fill=kint.BOTH)

        self.label2 = kint.Label(
            self.window, text="Type To-Dos",
            font=("Helvetica", 15, "bold"),
            fg="white", bg="blue", width=10, bd=5)
        self.label2.place(x=40, y=54)

        self.label3 = kint.Label(
            self.window, text="All Tasks",
            font=("Helvetica", 15, "bold"),
            fg="white", bg="blue", width=10, bd=5)
        self.label3.place(x=440, y=54)

        self.all_tasks = kint.Listbox(self.window,
                                        font=("Helvetica", 20, "bold"),
                                        bd=5, height=15, width=24)
        self.all_tasks.place(x=350, y=100)

        self.text = kint.Text(self.window, bd=5, height=1,
                              width=20, font=("Helvetica", 15, "bold"))
        self.text.place(x=10, y=100)

        self.label_feelings = kint.Label(
            self.window, text="How are you feeling?",
            font=("Helvetica", 15, "bold"),
            fg="white", bg="blue", width=38, height="3", bd=4
        )
        self.label_feelings.place(x=2, y=270)

        self.selected_feeling = kint.StringVar()

        # dropdown menu for feelings
        self.feelings_menu = ttk.Combobox(
            self.window, textvariable=self.selected_feeling,
            values=["Normal😊", "Sad😢", "Annoyed😠", "Cool😎", "Sleepy😴", "Hyped😜"],
            font=("Helvetica", 15, "bold"), width=20
        )
        self.feelings_menu.place(x=1, y=350)
        self.feelings_menu.set("Normal😊" )

        """Creating Buttons
        1. Add Task Button
        2. Delete Task Button
        3. Mark Task Button

        """
        self.add_button = kint.Button(text="Tap To Add", font="Helvetica 25 bold",
                                      command=self.add_task, width=9,bd=5,
                                      fg="blue", bg="black")
        self.add_button.place(x=20, y=140)

        self.delete_button = kint.Button(text="Delete Task", font="Helvetica 25 bold",
                                      command=self.delete_task, width=9,bd=5,
                                      fg="blue", bg="black")
        self.delete_button.place(x=20, y=180)

        self.mark_button = kint.Button(text="Mark Task", font="Helvetica 25 bold",
                                        command=self.mark_completed, width=9,bd=5,
                                        fg="blue", bg="black")
        self.mark_button.place(x=20, y=220)

        self.exit_button = kint.Button(text="Exit", font="Helvetica 25 bold",
                                       command=self.exit_app, width=3,bd=5,
                                       fg="blue", bg="white")
        self.exit_button.place(x=275, y=370)


    def add_task(self):
        """Adding Tasks For To-Do-List, and saving it to a file"""
        data = self.text.get(1.0, kint.END)
        """Adding bullet points to the tasks"""
        formatted_data = f"• {data.strip()}\n"
        self.all_tasks.insert(kint.END,formatted_data)
        with open("data.txt", "a") as file:
            file.write(formatted_data)
            file.seek(0)
        self.text.delete(1.0, kint.END)

    def delete_task(self):
        """Deleting Tasks From To-Do-List"""
        task_selected = self.all_tasks.curselection()
        check = self.all_tasks.get(task_selected)
        with open("data.txt", "r+") as file:
            new_file = file.readlines()
            file.seek(0)
            file.truncate()

            for line in new_file:
                if check.strip() != line.strip():
                    file.write(line)
        self.all_tasks.delete(task_selected)


        """Reading Tasks From File to ALL_TASKS FIELD"""
        self.all_tasks.delete(0, kint.END)
        with open("data.txt", "r") as file:
            each_line = file.readlines()
            for h in each_line:
                read_lines = h.strip()
                self.all_tasks.insert(kint.END, read_lines)

    def mark_completed(self):
        """Marking Tasks Completed"""
        select = self.all_tasks.curselection()
        if select:
            text_of_task = self.all_tasks.get(select)
            completed_task = f"✅ {text_of_task}"
            self.all_tasks.delete(select)
            self.all_tasks.insert(select, completed_task)

            with open("data.txt", "r+") as file:
                new_file = file.readlines()
                file.seek(0)
                file.truncate()

                for line in new_file:
                    if text_of_task.strip() != line.strip():
                        file.write(line)
                file.write(completed_task)

    def exit_app(self):
            """Method to exit the app"""
            sys.exit(0)


"""Creating my window"""
def interface():
    window = kint.Tk()

    todo_app = To_Do(window)
    window.mainloop()


if __name__ == "__main__":
    interface()