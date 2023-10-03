from tkinter import *
from mydb import * 
from PIL import ImageTk
from tkinter import messagebox
from login import data1

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()


def checkrecord():
    if usernameEntry.get=='' or passwordEntry.get()=='':
        messagebox.showerror('ERROR','All Fields Are Required')
    else:
            row=data1.cur.execute(" SELECT COUNT(*) FROM users WHERE username = ?  AND password = ? ",(usernameEntry.get(),passwordEntry.get())).fetchone()[0]
            if row==0:
                messagebox.showerror('Error','Invalid username or password') 
                
            else:
                login_window.destroy()
                import main
                   
            

def signup_page():
    login_window.destroy()
    import login


def on_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)

def pass_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)


login_window=Tk()
bgImage=ImageTk.PhotoImage(file='bg.jpg')
login_window.title('Login Page')

bgLabel=Label(login_window,image=bgImage)
bgLabel.grid(row=0,column=0)

heading=Label(login_window,text='USER LOGIN',font=('Microsoft Yahei UT Light',23,'bold'),bg='white',fg='firebrick1')
heading.place(x=605,y=120)

usernameEntry=Entry(login_window,width=25,font=('Microsoft Yahei UT Light',11,'bold'),bd=0,fg='firebrick1')
usernameEntry.place(x=580,y=200)
usernameEntry.insert(0,'Username')

usernameEntry.bind('<FocusIn>',on_enter)

Frame(login_window,width=250,height=2,bg='firebrick1').place(x=588,y=222)


passwordEntry=Entry(login_window,width=25,font=('Microsoft Yahei UT Light',11,'bold'),bd=0,fg='firebrick1')
passwordEntry.place(x=580,y=260)
passwordEntry.insert(0,'Password')

passwordEntry.bind('<FocusIn>',pass_enter)
Frame(login_window,width=250,height=2,bg='firebrick1').place(x=588,y=282)

loginButton=Button(login_window,text='Login',font=('Open Sans',16,'bold'),fg='white',bg='firebrick1',activeforeground='white',activebackground='firebrick1',cursor='hand2',bd=0,width=19,command=checkrecord)
loginButton.place(x=578,y=350)

newAccButton=Button(login_window,text='Create New Account',font=('Open Sans',9,'bold underline'),fg='blue',bg='white',activeforeground='blue',activebackground='white',cursor='hand2',bd=0,command=signup_page)
newAccButton.place(x=650,y=450)

login_window.mainloop()