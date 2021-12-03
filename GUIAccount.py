import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
#import MySQLdb
import GUIActivity

def frame():
    global root
    root = tk.Tk()
    root.geometry("600x450+374+182")
    root.title("WALLET")

    #balance in the account
    accountBalance = tk.Label(root, text="Balance")
    accountBalance.grid(row=0,column=0)

    #statement check by month
    activity = tk.Label(root, text="Month Statement")
    activity.grid(row=2,column=0)
    comvalue1 = tk.StringVar()
    year = ttk.Combobox(root, textvariable=comvalue1,height=10,width=10)
    year.grid(row=2,column=1)
    year['values']=('2022','2021','2020','2019')
    year.current(0)

    comvalue2 = tk.StringVar()
    month = ttk.Combobox(root, textvariable=comvalue2,height=10,width=10)
    month.grid(row=2,column=2)
    month['values']=('Januarary','Feburary','March','April','May','June',
                     'July','August','Sepetember','October','November','December')
    month.current(0)



    # Button
    UserAccount = tk.Button(root, text="My Account Information", command=informationPage)
    UserAccount.grid(row=1,column=0)
    requestMoney = tk.Button(root, text="Request Money",command=GUIActivity.requestPage)
    requestMoney.grid(row=5,column=1)
    sendMoney = tk.Button(root, text="Send Money",command=GUIActivity.sendPage)
    sendMoney.grid(row=5,column=2)
    viewStatment = tk.Button(root, text="View", command=MonthlyStatementPage)
    viewStatment.grid(row=2,column=3)


    root.mainloop()

def informationPage():
    # root = tk.Tk()
    # root.geometry("600x450+374+182")
    # root.title("WALLET")

    # Label
    userName = tk.Label(root, text="Name")
    userName.grid(row=0, column=0)
    userSSN = tk.Label(root, text="SSN")
    userSSN.grid(row=1, column=0)
    userPhoneNum = tk.Label(root, text="Phone Number")
    userPhoneNum.grid(row=2, column=0)
    userEmail = tk.Label(root, text="Email Address")
    userEmail.grid(row=3, column=0)
    userBankAcc = tk.Label(root, text="Bank Account")
    userBankAcc.grid(row=4, column=0)

    # Button
    addEmail = tk.Button(root, text="Add Email Address", command=None)
    addEmail.grid(row=3, column=2)
    addBank = tk.Button(root, text="Add Bank Account", command=None)
    addBank.grid(row=4, column=2)

def MonthlyStatementPage():
    root = tk.Tk()
    root.geometry("600x450+374+182")
    root.title("WALLET")