from tkinter import * 
from PIL import ImageTk
from mydb import * 
from tkinter import messagebox

data1 = Database(db='mydatabase.db')

def saveRecord():
    global data1
    if emailEntry.get()=='' or usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','All fields Are Required')
    else:
        data1.insertRecord(username=usernameEntry.get(),password=passwordEntry.get(),email=emailEntry.get())
        signup_window.destroy()
        import signin


def login_page():
    signup_window.destroy()
    import signin


signup_window=Tk()
signup_window.title('Signup Page')
signup_window.resizable(False,False)
background=ImageTk.PhotoImage(file='bg.jpg')

bgLabel=Label (signup_window, image=background) 
bgLabel.grid()

frame=Frame (signup_window, bg='white')
frame.place (x=554,y=100)

heading=Label (frame, text='CREATE AN ACCOUNT', font=('Microsoft Yahei UI Light', 18, 'bold')
,bg='white', fg='firebrick1')
heading.grid(row=0, column=0, padx=10,pady=10)

emailLabel=Label (frame, text='Email', font=('Microsoft Yahei UI Light',10, 'bold'), bg='white' ,fg='firebrick1')
emailLabel.grid(row=1, column=0, sticky='w', padx=25,pady=(10,0))

emailEntry=Entry (frame, width=25, font=('Microsoft Yahei UI Light', 10, 'bold'),
fg='white', bg='firebrick1')
emailEntry.grid(row=2, column=0, sticky='w',padx=25)

usernameLabel=Label (frame, text='Username', font=('Microsoft Yahei UI Light',10, 'bold'), bg='white' ,fg='firebrick1')
usernameLabel.grid(row=3, column=0, sticky='w', padx=25,pady=(10,0))

usernameEntry=Entry (frame, width=25, font=('Microsoft Yahei UI Light', 10, 'bold'),
                      fg='white', bg='firebrick1')
usernameEntry.grid(row=4, column=0, sticky='w',padx=25)

passwordLabel=Label (frame, text='Password', font=('Microsoft Yahei UI Light',10, 'bold'), bg='white' ,fg='firebrick1')
passwordLabel.grid(row=5, column=0, sticky='w', padx=25,pady=(10,0))

passwordEntry=Entry (frame, width=25, font=('Microsoft Yahei UI Light', 10, 'bold'),
                      fg='white', bg='firebrick1')
passwordEntry.grid(row=6, column=0, sticky='w',padx=25)


signupButton=Button(frame,text='Signup',font=('Open Sans', 16, 'bold'),bd=0,bg='firebrick1',fg='white',activeforeground='white',activebackground='firebrick1',width=17,command=saveRecord)
signupButton.grid(row=7,column=0,pady=(70,0))


alreadyaccount=Label(frame,text="Don't have an account?",font=('Open Sans','9','bold'),bg='white',fg='firebrick1')
alreadyaccount.grid(row=8,column=0,padx=25)

loginButton=Button(frame, text='Log in', font=('Open Sans', 9, 'bold underline'),bg='white', fg='blue', bd=0, cursor='hand2', activebackground='white' , activeforeground='blue',
                     command=login_page)
loginButton.place(x=220,y=340)

signup_window.mainloop()