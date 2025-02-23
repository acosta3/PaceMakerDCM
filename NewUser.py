from tkinter import *
from tkinter import messagebox
from SqlConnection import create_db_connection
import mysql
background = "#06283D"
framebg = "#EDEDED"

root = Tk()
root.title("Add User")
root.geometry("360x360")  # size of the screen
root.config(bg=background)
root.resizable(False, False)


# Background Image
frame = Frame(root, bg="red")
frame.pack(fill=Y)

backgroundimage = PhotoImage(file="Images/LOGIN.png")
Label(frame, image=backgroundimage).pack()



def login():
    root.destroy() # closing this window
    import Login


#####User entry
def user_enter(e):
    user.delete(0,'end');
def user_leave(e):
    name=user.get();
    if name =='':
        user.insert(0,'User')


###




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

# Create a label widget to display text
text = "ADD NEW USER"
adduser_label = Label(root, text=text, fg="#fff", bg="#375174", font=('Arial', 12))

# Pack the label widget to add it to the window
adduser_label.pack()
adduser_label.place(x=110, y=70)

# Start the Tkinter main loop

#password textbox
# Have to fix match the color of the textbox
password = Entry(frame,width=18,fg="#fff",border=0, bg="#375174",font=('Arial Bold',12))
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


def AddUser():
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
    # command to check if the user exists
    sqlcommand="select * from login where username=%s "
    mycursor.execute(sqlcommand,(usernameEntry,))
    myresult=mycursor.fetchone()
    print(myresult)
    #to check how many number of users
    sqlCount = "SELECT COUNT(*) FROM login WHERE username = %s"
    mycursor.execute(sqlCount, (usernameEntry,))
    print(mycursor)
    # convert to integer list
    numberofuser = mycursor.fetchone()
    print(numberofuser)
    if numberofuser != None:
        numberofuser = int(numberofuser[0])
    else:
        numberofuser = 0  # Set to 0 if no result was found

    # add the user if its unique and if the number of user count is less than 10
    if (myresult) == None and (numberofuser < 10):
        sqlInsert = "INSERT INTO login (username, password) VALUES (%s, %s)"
        insert_values = (usernameEntry, passwordEntry)
        try:

            mycursor.execute(sqlInsert, insert_values)
            db_connection.commit()
            messagebox.showinfo("New User added", "User: " + usernameEntry + " is now added")
        except mysql.connector.Error as err:
            # If an error occurs, you can handle it as needed (e.g., username already exists, database connection issue)
            messagebox.showerror("Error", "Failed to add user: " + str(err))

    elif  myresult != None :
        # Username doesn't exist, but the number of users has reached the limit
        messagebox.showinfo("Error", "User :" + usernameEntry + " already exists" )

    elif  numberofuser >= 10 :
        # Username doesn't exist, but the number of users has reached the limit
        messagebox.showinfo("Error", "Max number of users reached")

    else:
        messagebox.showinfo("login", "User Already Exist please Try Again")


openeye=PhotoImage(file="Images/openeye.png")
closeeye=PhotoImage(file="Images/close eye.png")
openeye = openeye.subsample(2, 2) ## resize to a factor of 3
closeeye = closeeye.subsample(2, 2) # resize to a factor of 2
eyeButton=Button(frame,image=openeye,bg="#375174",bd=0, command=hide)
eyeButton.place(x=40,y=180)


###########
NewUserButton=Button(root,text="ADD USER",bg="white", fg="black",width=18,height=1,font=("arial",12,'bold'),bd=0, command=AddUser)
NewUserButton.place(x=80,y=250)

BackButton=Button(root,text="Back",bg="white", fg="black",width=15,height=1,font=("arial",8,'bold'),bd=0, command=login)
BackButton.place(x=120,y=300)




root.mainloop()