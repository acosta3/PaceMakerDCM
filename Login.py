from tkinter import *
from tkinter import messagebox
from SqlConnection import create_db_connection
import shelve
import subprocess

USERDATA = "" # GLOBAL variable

background = "#06283D"
framebg = "#EDEDED"
root = Tk()
root.title("Login User")
root.geometry("360x360")  # size of the screen
root.config(bg=background)
root.resizable(False, False)


# Background Image
frame = Frame(root, bg="red")
frame.pack(fill=Y)

backgroundimage = PhotoImage(file="Images/LOGIN.png")
Label(frame, image=backgroundimage).pack()




#####User entry
def user_enter(e):
    user.delete(0,'end');
def user_leave(e):
    name=user.get();
    if name =='':
        user.insert(0,'User')



#username textbox
# Have to fix match the color of the textbox
user= Entry(frame,width=16,fg="#fff",border=0, bg="#375174",font=('Arial Bold',12))
user.insert(0, 'UserID')
user.bind("<FocusIn>", user_enter)
user.bind("<FocusOut>", user_leave)
user.place(x=107, y=120)


#####pasword_entry
def pass_enter(e):
    password.delete(0,'end')
def pass_leave(e):

    if password.get() =='':
        password.insert(0,'Password')



#password textbox
# Have to fix match the color of the textbox
password= Entry(frame,width=18,fg="#fff",border=0, bg="#375174",font=('Arial Bold',12))
password.insert(0, 'Password')
password.bind("<FocusIn>", pass_enter)
password.bind("<FocusOut>", pass_leave)
password.place(x=73, y=180)

##hide and show button
button_mode = True

def hide():
    global button_mode
    if button_mode:
        eyeButton.config(image=closeeye,activebackground="white")
        password.config(show="*")
        button_mode= False
    else:
        eyeButton.config(image=openeye, activebackground="white")
        password.config(show="")
        button_mode = True


def loginUser():
    usernameEntry = user.get()
    passwordEntry = password.get()
    print(usernameEntry, passwordEntry)
    if (usernameEntry == "" or usernameEntry == "UserID") or (passwordEntry == "" or password == "Password"):
        messagebox.showerror("Invalid Entry", "Please Enter a username or a password")
    else:
        try:
            db_connection = create_db_connection()
            mycursor=db_connection.cursor()
            print("connected to database")

        except:
            messagebox.showerror("Connection Failed", "Database fail to connect")

    sqlcommand="use pacemaker"
    mycursor.execute(sqlcommand)
    sqlcommand="select * from login where username=%s and password=%s"
    mycursor.execute(sqlcommand,(usernameEntry,passwordEntry))
    userData=mycursor.fetchone()

    with shelve.open('mydata') as db:
        db['fetched_userdata'] = userData


    if(userData)== None :
        messagebox.showinfo("Invalid", "Wrong Username or Password")

    else:
        messagebox.showinfo("Login", "Sucessfully Login!")
        root.destroy()
        import HomeInterface





def OpenNewUser():
    root.destroy() # close this page
    import NewUser

openeye=PhotoImage(file="Images/openeye.png")
closeeye=PhotoImage(file="Images/close eye.png")
openeye = openeye.subsample(2, 2) ## resize to a factor of 3
closeeye = closeeye.subsample(2, 2) # resize to a factor of 2
eyeButton=Button(frame,image=openeye,bg="#375174",bd=0, command=hide)
eyeButton.place(x=40,y=180)


###########
loginButton = Button(root,text="LOGIN",bg="white", fg="black",width=18,height=1,font=("arial",12,'bold'),bd=0, command=loginUser)
loginButton.place(x=80,y=250)

RegisterButton = Button(root,width=10,text="New User", border=0, bg="#00264d", cursor='hand2', fg="white", command=OpenNewUser)
RegisterButton.place(x=140,y=300)

root.mainloop()
