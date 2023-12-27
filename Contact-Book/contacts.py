#!/usr/bin/python3
"""CodeBase for Contact-Book(GUI)"""
import tkinter as kint
from tkinter import ttk
import tkinter.messagebox

class ContactBook:
    """Defining Class and Labels For Contact-Book"""
    def __init__(self, window):
        self.window = window
        self.window.title("Contact-Book")
        self.window.geometry("1000x410+300+150")
        self.window.resizable(False, False)
        self.window.config(bg="black")

#Frame For Asking Details
        self.label_frame = kint.LabelFrame(
            window, text="Enter Contact Details", padx=15, pady=15)
        self.label_frame.grid(padx=15, pady=15)

        self.label_2 = kint.Label(self.label_frame, text="First Name:")
        self.label_2.grid(row=0, column=0, padx=5, pady=5, sticky="ne")

        first_name_var = kint.StringVar()
        self.first_name = kint.Entry(
            self.label_frame, textvariable=first_name_var, width=20)
        self.first_name.grid(row=0, column=1, padx=5, pady=5)

        self.label_2  = kint.Label(self.label_frame, text="Last Name:")
        self.label_2.grid(row=1, column=0, padx=5, pady=5)

        second_name_var = kint.StringVar()
        self.second_name = kint.Entry(
            self.label_frame, textvariable=second_name_var, width=20)
        self.second_name.grid(row=1, column=1, padx=5, pady=5)

        self.label_3 = kint.Label(self.label_frame, text="Phone:")
        self.label_3.grid(row=2, column=0, padx=5, pady=5)

        phone_var = kint.StringVar()
        self.phone = kint.Entry(
            self.label_frame, textvariable=phone_var, width=20)
        self.phone.grid(row=2, column=1, padx=5, pady=5)

        self.label_4 = kint.Label(self.label_frame, text="Email:")
        self.label_4.grid(row=3, column=0, padx=5, pady=5)

        email_var = kint.StringVar()
        self.email = kint.Entry(
            self.label_frame, textvariable=email_var, width=20)
        self.email.grid(row=3, column=1, padx=5, pady=5)

#Frame For Listbox
       # Treeview to display contacts
        self.contacts_tree = ttk.Treeview(self.window, columns=("First Name", "Last Name", "Phone", "Email"))
        self.contacts_tree.heading("#0", text=" Names")
        self.contacts_tree.heading("First Name", text="First Name")
        self.contacts_tree.heading("Last Name", text="Last Name")
        self.contacts_tree.heading("Phone", text="Phone")
        self.contacts_tree.heading("Email", text="Email")

        self.contacts_tree.column("#0", width=120)
        self.contacts_tree.column("First Name", width=100)
        self.contacts_tree.column("Last Name", width=100)
        self.contacts_tree.column("Phone", width=150)
        self.contacts_tree.column("Email", width=150)
        self.contacts_tree["displaycolumns"] = (
            "First Name", "Last Name", "Phone", "Email")
        self.contacts_tree.place(x=370, y=20)


        style = ttk.Style()
        style.configure("Treeview",
                        background="grey",
                        fieldbackground="brown",
                        foreground="white",
                        bordercolor="grey")

        # Scrollbar
        y_scrollbar = ttk.Scrollbar(
            self.window, orient="vertical", command=self.contacts_tree.yview)
        self.contacts_tree.configure(yscroll=y_scrollbar.set)

        # Pack the Treeview and Scrollbar
        self.contacts_tree.grid(row=0, column=1, sticky="nsew")
        y_scrollbar.grid(row=0, column=2, sticky="ns")



#Frame For Buttons
        self.button_frame = kint.Frame(window, bg="grey")
        self.button_frame.grid(row=1, column=0, padx=15, pady=15, sticky="sw")

        self.add_button = kint.Button(
            self.button_frame, text="Save Contact", width=13, bd=5, bg="#00FF00", fg="#00FF00")
        self.add_button.grid(row=0, column=0, padx=5, pady=5, sticky="sw")

        self.update_button = kint.Button(
            self.button_frame, text="Update Contact", width=13, bd=5, fg="blue")
        self.update_button.grid(row=0, column=1, padx=5, pady=5, sticky="sw")

        self.delete_button = kint.Button(
            self.button_frame, text="Delete Contact", width=13, bd=5, fg="red",bg="black"
        )
        self.delete_button.grid(row=1, column=0, padx=5, pady=5, sticky="sw")

        self.exit_button = kint.Button(
            self.button_frame, text="Exit", width=13, bd=5, fg="#FF4500", command=self.window.destroy)
        self.exit_button.grid(row=1, column=1, padx=5, pady=5, sticky="sw")



"""Creating my window"""
def interface():
    window = kint.Tk()
    contact_book = ContactBook(window)
    window.mainloop()


if __name__ == "__main__":
    interface()