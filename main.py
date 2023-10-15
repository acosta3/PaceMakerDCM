# Initialize an empty list to store user data
import tkinter as tk
from SqlConnection import create_db_connection
from tkinter import simpledialog
from tkinter import messagebox


userCount = 0
user_list = []

# Get the database connection
db_connection = create_db_connection()

def add_user():
    global userCount
    new_username = simpledialog.askstring("Add User", "Enter a username:")

    if new_username:
        if any(user.get("Username") == new_username for user in user_list):
            messagebox.showerror("Username Exists", "Username already exists. Please choose a different username.")
        else:
            if userCount <= 10:
                new_password = simpledialog.askstring("Add User", "Enter a password:", show="*")
                userCount += 1
                if new_password:
                    user = {"Username": new_username, "Password": new_password}
                    user_list.append(user)
                    user_listbox.insert(tk.END, f"Username: {new_username}, Password: {new_password}")


def login():
    username = simpledialog.askstring("Login", "Enter "
                                               "your username:")
    password = simpledialog.askstring("Login", "Enter your password:", show="*")

    if username and password:
        # Check if the username and password match any user in the user_list
        matching_users = [user for user in user_list if user["Username"] == username and user["Password"] == password]
        if matching_users:
            messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
        else:
            messagebox.showerror("Login Failed", "Incorrect username or password. Please try again.")


# Create the main window
window = tk.Tk()
window.title("User Management Example")

# Create a menu
menu = tk.Menu(window)
window.config(menu=menu)

# Create a "User" submenu with "New User" and "Login" options
user_menu = tk.Menu(menu)
menu.add_cascade(label="User", menu=user_menu)
user_menu.add_command(label="New User", command=add_user)
user_menu.add_command(label="Login", command=login)

# Create a listbox to display user entries
user_listbox = tk.Listbox(window)
user_listbox.pack()

# Start the GUI event loop
window.mainloop()
