import tkinter as tk
from tkinter import messagebox
#import MySQLdb
import GUISignUp, GUIAccount


def frame():

    global root
    #create a GUI
    root = tk.Tk()
    #set GUI size and location
    root.geometry("600x450+374+182")
    #title
    root.title("WALLET")

    #Label
    userName = tk.Label(root,text="User Name (Phone or Email)")
    userName.grid()
    password = tk.Label(root,text="SSN")
    password.grid()
    orLabel = tk.Label(root, text="OR")
    orLabel.grid(row=3,column=1)

    #Entry
    userNameEntry = tk.Entry(root)
    userNameEntry.grid(row=0,column=1)
    SSNEntry = tk.Entry(root)
    SSNEntry.grid(row=1,column=1)
    #if SSN is matched with Phone number or email, then log in

    #Button
    LogInButton = tk.Button(root,text="Log in",command=exit_account)
    LogInButton.grid(row=2,column=1)
    SignUpButton = tk.Button(root,text="Sign up",command=exit_signup)
    SignUpButton.grid(row=4,column=1)

    #display GUI
    root.mainloop()

#switch to account GUI
def exit_account():
    root.destroy()
    GUIAccount.frame()

#switch to Sign up GUI
def exit_signup():
    root.destroy()
    GUISignUp.frame()


if __name__ =='__main__':
    frame()







# start = LogInPage()



