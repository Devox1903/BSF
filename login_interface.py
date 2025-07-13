import tkinter as tk
from tkinter import ttk

#window
window = tk.Tk()
window.title("Blacksmithfraction")
window.geometry("600x400")

#widgtes
dnd_lable = ttk.Label(window, text = "Welcome to DnD")
response = ttk.Label(window, text = " ")
username = ttk.Label(window, text ="Username:")
password = ttk.Label(window, text = "Password:")
login_button = ttk.Button(text = "Log in")
e_user = ttk.Entry()
e_password = ttk.Entry()

#define a grid
for i in range(0,10):
    window.columnconfigure(i,weight = 1)
    window.rowconfigure(i, weight = 1)

#place widget
dnd_lable.grid(row = 0, column = 5, sticky = "nwes")
username.grid(row = 4, column = 4)
password.grid(row = 5, column = 4)
e_user.grid(row = 4, column = 5)
e_password.grid(row = 5, column = 5)
login_button.grid(row = 6, column = 4, columnspan = 2,ipadx = 50, ipady = 10)
response.grid(row = 7, column = 4, columnspan = 2)


#Text datei auslesen und UN und PW erkennen
def read_logins():
    with open('log_in.txt','r')as f:
        contents = f.readlines()

        new_contents = []

        for line in contents:
            fields = line.split(',')
            fields [1] = fields [1].rstrip()
            new_contents.append(fields)

    return(new_contents)
              
#UN und PW vergleichen
def login(logins):
    global response
    name =''
    ask_username = e_user.get().strip()
    ask_password = e_password.get().strip()
    logged_in = False
    for line in logins:
        if line[0] == ask_username and line[1] == ask_password:
            logged_in = True
            name = line[2].strip()
            break
    if logged_in == True:
        response.config(text=f"Hello {name}, you are logged in. Enjoy your Session")
    else:
        response.config(text="Username/Password incorrect")
    return logged_in
def check_login():
    logins = read_logins()
    return login(logins)
login_button.config(command=check_login)

window.mainloop()
print(read_logins())