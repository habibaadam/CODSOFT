#!/usr/bin/env python3
"""CodeBase for To-Do-App(GUI)"""
import tkinter as kint
import tkinter.messagebox

class To_Do:
    """Defining Class For To-Do-App"""
    def __init__(self, window):
        self.window = window
        self.window.title("To-Do-List")
        self.window.geometry("650x410+300+150")
        self.window.resizable(True, False)

        self.label = kint.Label(
            self.window, text="To-Do-List",
            font=("Helvetica", 25, "bold"),
            fg="white", bg="blue", width=10, bd=5)
        self.label.pack(side="top", fill=kint.BOTH)

        self.label2 = kint.Label(
            self.window, text="Add Task",
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


        """Creating Buttons"""
        self.add_button = kint.Button(text="Tap To Add", font="Helvetica 25 bold",
                                      command=self.add_task, width=9,bd=5,
                                      fg="blue", bg="black")
        self.add_button.place(x=20, y=140)

        self.delete_button = kint.Button(text="Delete Task", font="Helvetica 25 bold",
                                      command=self.delete_task, width=9,bd=5,
                                      fg="blue", bg="black")
        self.delete_button.place(x=20, y=180)


    def add_task(self):
        """Adding Tasks For To-Do-List, and saving it to a file"""
        data = self.text.get(1.0, kint.END)
        self.all_tasks.insert(kint.END, data)
        with open("data.txt", "a") as file:
            file.write(data)
            file.seek()
            file.close()
        self.text.delete(1.0, kint.END)

    def delete_task(self):
        """Deleting Tasks From To-Do-List"""
        task_selected = self.all_tasks.curselection()
        check = self.all_tasks.get(task_selected)
        with open("data.txt", "r") as file:
            new_file = file.readlines()
            file.seek(0)
            for line in new_file:
                if line != check:
                    file.write(line)
            file.truncate()
        self.all_tasks.delete(task_selected)

        """Reading Tasks From File to ALL_TASKS FIELD"""
        with open("data.txt", "r") as file:
            each_line = file.readlines()
            for h in each_line:
                read_lines = h.split()
            self.all_tasks.insert(kint.END, read_lines)
            file.close()



"""Creating my window"""
def interface():
    window = kint.Tk()

    todo_app = To_Do(window)
    window.mainloop()


if __name__ == "__main__":
    interface()