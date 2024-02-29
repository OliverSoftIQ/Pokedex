'''
import tkinter as tk
from tkinter import messagebox

# Function to validate the login
def validate_login():
    userid = username_entry.get()
    password = password_entry.get()

    # You can add your own validation logic here
    if userid == "Ash" and password == "Pikachu1987":
        messagebox.showinfo("Login Successful", "Welcome, Ash")
    if userid == "Misty" and password == "StaryuTears":
        messagebox.showinfo("Login Successful", "Welcome, Misty")
    if userid == "Brock" and password == "Olivia":
        messagebox.showinfo("Login Successful", "Welcome, Brock")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create the main window
parent = tk.Tk()
parent.title("Login Form")

# Create and place the username label and entry
username_label = tk.Label(parent, text="Userid:")
username_label.pack()

username_entry = tk.Entry(parent)
username_entry.pack()

# Create and place the password label and entry
password_label = tk.Label(parent, text="Password:")
password_label.pack()

password_entry = tk.Entry(parent, show="*")  # Show asterisks for password
password_entry.pack()

# Create and place the login button
login_button = tk.Button(parent, text="Login", command=validate_login)
login_button.pack()

# Start the Tkinter event loop
parent.mainloop()
'''





custom_list = [0,4,21,5,2,78,2,5,52,5,3,1,9]
unique_list = sorted(set(custom_list))
print(unique_list)