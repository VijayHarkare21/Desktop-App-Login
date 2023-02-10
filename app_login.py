from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root2 = Tk()

valid_email = "xyz.abc@gmail.com"
valid_password = "XYZ@123"

valid_creds = [(valid_email, valid_password)]

wwidth1 = 1000 # root.winfo_reqwidth()
wheight1 = 700 # root.winfo_reqheight()
wwidth2 = 530
wheight2 = 390
blue = "#e3ebff"
gray = "#606163"
copyright = u"\u00A9"
green = "#00a757"

def root_win():
    root.title("My Desktop Application")
    root.configure(bg=blue)
    root.resizable(False, False)
    root.columnconfigure(0, weight=1)
    root.title("My Desktop Application")
    centering(root, wwidth1, wheight1)
    root.bind_all('<Configure>', holdon1)
    footer = copyright + " 2022 | Vijay Harkare All Right Reserved."
    foot = Label(root, text=footer, bg=blue, fg=gray, pady=20, font=("Calibri", 12))
    foot.grid(row=3, column=0, sticky='s')
    root.grid_rowconfigure(0, weight=1)

def centering(root, wwidth, wheight):
    windowheight = wheight
    windowwidth = wwidth

    right = int(root.winfo_screenwidth() / 2 - windowwidth / 2)
    down = int(root.winfo_screenheight() / 2 - windowheight / 2)

    root.geometry("{}x{}+{}+{}".format(wwidth, wheight, right, down))

def holdon1(event):
    right = int(root.winfo_screenwidth() / 2 - wwidth1 / 2)
    down = int(root.winfo_screenheight() / 2 - wheight1 / 2)

    root.geometry("+{}+{}".format(right, down))

def holdon2(event):
    right = int(root2.winfo_screenwidth() / 2 - wwidth2 / 2)
    down = int(root2.winfo_screenheight() / 2 - wheight2 / 2)

    root2.geometry("+{}+{}".format(right, down))

def restore():
    for widget in root2.winfo_children():
        widget.destroy()
    root2_win()

def root2_win():
    root_win()
    root2.title("Login Page")
    root2.columnconfigure(0, weight=1)
    root2.configure(bg=green)
    centering(root2, wwidth2, wheight2)
    root2.attributes("-topmost", True)
    root2.resizable(False, False)
    root2.bind_all('<Configure>', holdon2)

    head = Label(root2, text="App Login", bg=green, fg="white", font=("Calibri", 20, "bold"))
    head.grid(row=0, column=0, columnspan=2, sticky='ew', padx=40, pady=20)

    email_frame = Frame(root2, bg="white")
    pass_frame = Frame(root2, bg="white")

    email = Entry(email_frame, fg="gray", width=30, font=("Calibri", 18), bd=0)
    password = Entry(pass_frame, fg="gray", width=30, font=("Calibri", 18), bd=0)

    email.pack(padx=10, pady=5)
    password.pack(padx=10, pady=5)

    email.insert(0, "Enter Email...")
    email_frame.grid(row=1, column=0, columnspan=2, pady=(0, 30))
    password.insert(0, "Enter Password...")
    pass_frame.grid(row=2, column=0, columnspan=2, pady=(0, 30))

    response = Label(root2, bg=green, fg="red", font=("Calibri", 12))

    def login_check():
        response.config(text="")
        email_content = email.get()
        password_content = password.get()
        if email_content == "" or email_content == "Enter Email..." or password_content == "" or password_content == "Enter Password...":
            response.config(text="Email and/or Password not entered!\nPlease enter Email and Password")
            email.delete(0, END)
            email.insert(0, "Enter Email...")
            password.delete(0, END)
            password.insert(0, "Enter Password...")
        elif (email_content, password_content) in valid_creds:
            root2.destroy()
            root.attributes("-topmost", True)
            success = Label(root, bg=blue, fg="green", font=("Calibri", 16), text="Login Successful!")
            welcome = Label(root, bg=blue, fg="black", font=("Calibri", 32, "bold"), text="Welcome to My Desktop Application!")
            success.grid(row=0, column=0, pady=50, sticky=N)
            welcome.place(relx=0.5, rely=0.5, anchor=CENTER)
        else:
            response.config(text="Invalid Email and/or Password!\nPlease re-enter Email and Password")
            email.delete(0, END)
            email.insert(0, "Enter Email...")
            password.delete(0, END)
            password.insert(0, "Enter Password...")
        return

    def register_acc():
        email_content = email.get()
        password_content = password.get()
        if email_content == "" or email_content == "Enter Email..." or password_content == "" or password_content == "Enter Password...":
            response.config(text="Email and/or Password not entered!\nPlease enter Email and Password")
            email.delete(0, END)
            email.insert(0, "Enter Email...")
            password.delete(0, END)
            password.insert(0, "Enter Password...")
        elif (email_content, password_content) not in valid_creds:
            valid_creds.append((email_content, password_content))
            restore()
        return

    def register_now():
        response.config(text="")
        root2.title("Register Account")
        head.config(text="Register Account")
        login.config(text="Back", command=restore)
        register.config(command=register_acc)
        forgot.destroy()
        return

    def reset():
        email_content = email.get()
        password_content = password.get()
        emails = list(map(lambda x: x[0], valid_creds))
        if email_content == "" or email_content == "Enter Email..." or password_content == "" or password_content == "Enter New Password...":
            response.config(text="Email and/or New Password not entered!\nPlease enter Email and New Password")
            email.delete(0, END)
            email.insert(0, "Enter Email...")
            password.delete(0, END)
            password.insert(0, "Enter New Password...")
        elif email_content in emails:
            valid_creds.pop(emails.index(email_content))
            valid_creds.append((email_content, password_content))
            restore()
        else:
            response.config(text="Invalid Email!\nPlease re-enter Email and New Password")
            email.delete(0, END)
            email.insert(0, "Enter Email...")
            password.delete(0, END)
            password.insert(0, "Enter New Password...")
        return

    def forgot_pass():
        response.config(text="")
        root2.title("Reset Password")
        head.config(text="Reset Password")
        register.config(text="Reset Password")
        password.delete(0, END)
        password.insert(0, "Enter New Password...")
        login.config(text="Back", command=restore)
        register.config(command=reset)
        forgot.destroy()
        return

    empty = Label(root2, bg=green)
    empty.grid(row=3, column=0, columnspan=2, pady=(0, 30))

    register_frame = Frame(root2, bg="black")
    login_frame = Frame(root2, bg="black")
    forgot_frame = Frame(root2, bg=green)

    register = Button(register_frame, text="Register Account", fg="white", font=("Calibri", 18), bd=0, bg="black", width=17, command=register_now)
    login = Button(login_frame, text="Login", fg="white", font=("Calibri", 18), bd=0, bg="black", width=9, command=login_check)
    forgot = Button(forgot_frame, text="Forgot Password?", fg="white", font=("Calibri", 16), bd=0, bg=green, command=forgot_pass)

    register.pack(padx=10, pady=0)
    login.pack(padx=10, pady=0)
    forgot.pack(padx=10, pady=0)

    register_frame.place(x=74, y=220)
    login_frame.place(x=322, y=220)
    forgot_frame.grid(row=4, column=0, columnspan=2, pady=(15, 0))
    response.grid(row=5, column=0, columnspan=2)
    return

if __name__ == "__main__":
    root_win()
    root2_win()

    root.mainloop()