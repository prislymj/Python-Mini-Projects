master_pwd = input("What is the master password?")

def view():
    pass

def add():
    name = input("Account name: ")
    password = input("Password: ")

    with open("passwords.txt", 'a') as f: # 'with keyword automatically close file after use
        f.write(name+"|"+password)

while True:
    mode = input("Would you like to add a new password or view existing ones? (add/view)\n Type Q to quit").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode =="add":
        add()
    else:
        print("Invalid mode")
        continue