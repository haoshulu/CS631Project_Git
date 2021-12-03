import tkinter as tk
from tkinter import messagebox
#import MySQLdb


def frame():
    root = tk.Tk()
    root.geometry("600x450+374+182")
    root.title("WALLET")

    # Label
    userName = tk.Label(root, text="Name")
    userName.grid()
    userSSN = tk.Label(root, text="SSN")
    userSSN.grid()
    phoneNumber = tk.Label(root, text="Phone Number")
    phoneNumber.grid()
    emailAddress = tk.Label(root, text="Email Address")
    emailAddress.grid()

    # Entry
    userNameEntry = tk.Entry(root)
    userNameEntry.grid(row=0, column=1)
    userSSNEntry = tk.Entry(root)
    userSSNEntry.grid(row=1, column=1)
    phoneNumEntry = tk.Entry(root)
    phoneNumEntry.grid(row=2,column=1)
    emailEntry = tk.Entry(root)
    emailEntry.grid(row=3,column=1)

    # Button
    SignUpButton = tk.Button(root, text="Sign Up", command=None)
    SignUpButton.grid(row=4, column=1)
    phoneVerified = tk.Button(root, text="Verified",command=None)
    phoneVerified.grid(row=2,column=2)
    emailVerified = tk.Button(root, text="Verified",command=None)
    emailVerified.grid(row=3,column=2)

    root.mainloop()