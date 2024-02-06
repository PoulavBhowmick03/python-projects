def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("Username: ", user , " , Password: ", passw)


def add():
    name = input("What is your name?").lower()
    password = input("What is your password?").lower()
    
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + password + "\n" )






while True:
    mode = input("Would you like to add a new password or view an old one, or quit? Press add or view or q").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")
        continue
