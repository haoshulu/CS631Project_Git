import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
#import MySQLdb


def sendPage():
    root = Tk()
    root.geometry("600x450+374+182")
    root.title("WALLET")

    # Label
    recipientPhone = tk.Label(root, text="Recipient's Phone Number")
    recipientPhone.grid(row=0, column=0)
    orLabel = tk.Label(root, text="OR")
    orLabel.grid(row=1,column=0)
    recipentEmail = tk.Label(root, text="Recipient's Email Address")
    recipentEmail.grid(row=2,column=0)
    sendAmount = tk.Label(root, text="Amount")
    sendAmount.grid(row=3,column=0)
    memo = tk.Label(root,text="Memo")
    memo.grid(row=4,column=0)


    # Entry
    recipientPhoneEntry = tk.Entry(root)
    recipientPhoneEntry.grid(row=0, column=1)
    recipentEmailEntry = tk.Entry(root)
    recipentEmailEntry.grid(row=2, column=1)
    sendAmountEntry = tk.Entry(root)
    sendAmountEntry.grid(row=3, column=1)
    memoEntry = tk.Entry(root)
    memoEntry.grid(row=4, column=1)
    memoEntry.insert(0,"Optional")


    # Button
    send = tk.Button(root, text="Send", command=None)
    send.grid(row=5, column=1)


def requestPage():
    root = tk.Tk()
    root.geometry("600x450+374+182")
    root.title("WALLET")

#
#
#
#
#
#