#!/usr/bin/python3
"""CodeBase for Contact-Book(GUI)"""
import tkinter as kint
from tkinter import ttk
import tkinter.messagebox
import csv

class ContactBook:
    """Reading From CSV File"""
    def read_from_csv(self):
        try:
            with open("contacts.csv", "r", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.contacts_tree.insert(parent="", index="end", values=(
                        row["First Name"], row["Last Name"], row["Phone"], row["Email"]))
        except FileNotFoundError:
            pass

    def save_contacts(self):
        with open("contacts.csv", "w", newline="") as file:
            column_names = ["First Name", "Last Name", "Phone", "Email"]
            writer = csv.DictWriter(file, fieldnames=column_names)

            # Write header
            writer.writeheader()

            # Write contacts
            for c_id in self.contacts_tree.get_children():
                contact = self.contacts_tree.item(c_id)["values"]
                writer.writerow({column_names[h]: contact[h] for h in range(len(column_names))})

    """Defining Class and Labels For Contact-Book"""
    def __init__(self, window):
        self.window = window
        self.window.title("Contact-Book")
        self.window.geometry("1000x410+300+150")
        self.window.resizable(False, False)
        self.window.config(bg="black")


# Frame For Asking Details
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

        self.read_from_csv()

#Defining Functions for buttons
        def add_contact():
            """Adding Contacts"""
            first_name = self.first_name.get()
            last_name = self.second_name.get()
            phone = self.phone.get()
            email = self.email.get()

            if first_name == "" or last_name == "" or phone == "" or email == "":
                tkinter.messagebox.showerror(
                    "Error", "Please Fill All The Fields")
            else:
                self.contacts_tree.insert(
                    parent="", index="end",text="1", values=(first_name, last_name, phone, email))
                tkinter.messagebox.showinfo(
                    "Success", "Contact Has Been Added Successfully")
                self.save_contacts()


        def delete_contact():
            """Deleting Contacts"""
            selected_contact = self.contacts_tree.selection()[0]
            if not selected_contact:
                tkinter.messagebox.showerror(
                    "Please Select A Contact To Delete"
                    )
            else:
                self.contacts_tree.delete(selected_contact)
                tkinter.messagebox.showinfo(
                    "Success", "Contact Has Been Deleted Successfully")
                self.save_contacts()

        def update_contact():
            """Update selected contact"""
            selected_contact = self.contacts_tree.selection()
            if not selected_contact:
                tkinter.messagebox.showerror("Error", "Please select a contact to update")
            else:
                """Delete existing details of contact"""
                contact_details = self.contacts_tree.item(selected_contact)["values"]
                self.first_name.delete(0, 'end')
                self.second_name.delete(0, 'end')
                self.phone.delete(0, 'end')
                self.email.delete(0, 'end')

                """Updating new contact details"""
                self.first_name.insert(0, contact_details[0])
                self.second_name.insert(0, contact_details[1])
                self.phone.insert(0, contact_details[2])
                self.email.insert(0, contact_details[3])
                self.save_contacts()

        def clear_fields():
            """Clears the entry fields"""
            self.first_name.delete(0, 'end')
            self.second_name.delete(0, 'end')
            self.phone.delete(0, 'end')
            self.email.delete(0, 'end')

# Frame For Buttons
        self.button_frame = kint.Frame(window, bg="grey")
        self.button_frame.grid(row=1, column=0, padx=15, pady=15, sticky="sw")

        self.add_button = kint.Button(
            self.button_frame, text="Save Contact",command=add_contact, width=13, bd=5, bg="#00FF00", fg="#00FF00")
        self.add_button.grid(row=0, column=0, padx=5, pady=5, sticky="sw")

        self.update_button = kint.Button(
            self.button_frame, text="Update Contact", command=update_contact, width=13, bd=5, fg="blue")
        self.update_button.grid(row=0, column=1, padx=5, pady=5, sticky="sw")

        self.delete_button = kint.Button(
            self.button_frame, text="Delete Contact", command=delete_contact, width=13, bd=5, fg="red",bg="black"
        )
        self.delete_button.grid(row=1, column=0, padx=5, pady=5, sticky="sw")

        self.exit_button = kint.Button(
            self.button_frame, text="Exit", width=13, bd=5, fg="#FF4500", command=self.window.destroy)
        self.exit_button.grid(row=1, column=1, padx=5, pady=5, sticky="sw")

        self.clear_button = kint.Button(
            self.button_frame, text="Clear", width=13, bd=5, fg="black", command=clear_fields)
        self.clear_button.grid(row=2, column=0, padx=5, pady=5, sticky="sw")

"""Creating my window"""
def interface():
    window = kint.Tk()
    contact_book = ContactBook(window)
    window.mainloop()


if __name__ == "__main__":
    interface()