#txt data reading
def read__logins():
    with open('log_in.txt','r')as f:
        contents = f.readlines()

        new_contents = []

        for line in contents:
            fields = line.split(',')
            fields [1] = fields [1].rstrip()
            new_contents.append(fields)

        return(new_contents)

#compare un and pw 
def login(logins):
    name = ''
    ask_username = str(input('Username: '))
    ask_password = str(input('Password: '))

    logged_in = False

    for line in logins:
        if line [0] == ask_username and line[1] == ask_password:
            logged_in = True
            name = line[2].strip()
            break

    if logged_in == True:
        print('Login was Successful')
        print(f"Hello {name} Enjoy your Session :)")

    else:
        print('Username or Password are incorrect')
    
    return logged_in

#Merge functions
def main():
    print('Welcome to DnD. Please Login with your Username and Password')
    logins = read__logins()
    return login(logins)

#loop till login was successful
while main() == False:
    pass