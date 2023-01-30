from tkinter import * 
#defining login function
def login(): 
    uname=username.get() 
    pwd=password.get() 
    if uname=='' or pwd=='': 
        message.set("fill the empty field!!!") 
    else: 
        if uname=="a" and pwd=="a": 
            message.set("Login success") 
            import main
        else: 
            message.set("Wrong username and password!!!") 
#defining loginform function
def Loginform():
    global login_screen 
    login_screen = Tk() 
    login_screen.title("Login Form") 
    login_screen.geometry("500x500") 
    global message; 
    global username 
    global password 
    username = StringVar() 
    password = StringVar() 
    message=StringVar() 
    Label(login_screen,width="300", text="Please enter details below", 
bg="orange",fg="white").pack() 
    Label(login_screen, text="").pack() 
    Label(login_screen, text="Enter Username * ").pack() 
    Entry(login_screen, textvariable=username).pack() 
    Label(login_screen, text="Enter password * ").pack() 
    Entry(login_screen, textvariable=password ,show="*").pack() 
    Label(login_screen, text="",textvariable=message).pack() 
    Button(login_screen, text="Login", width=10, height=1, bg="orange",
command=login).pack() 
    login_screen.mainloop() 
#calling function Loginform
Loginform() 